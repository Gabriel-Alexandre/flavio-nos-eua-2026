"""Conta tudo o que vira número no relatório. Grava resultados/RESUMO.json e as tabelas.

Uso: python ferramentas/analise.py
Nenhum número do relatório é escrito à mão: tudo sai daqui.
"""
import csv
import json
import math
import statistics
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CASOS = RAIZ / "dados" / "casos"
RES = RAIZ / "resultados"

# Adjudicação das divergências da E2, com o motivo. O resto fica como a passada A, porque nos desfechos as duas concordam em tudo.
ADJUDICA = {
    "gonzalez": {"tipo": "derrotado_na_urna"},        # resultado oficial contestado; é candidato, não líder sem candidatura
    "tsikhanouskaya": {"tipo": "derrotado_na_urna", "eua_apoio_declarado": "sim"},
    "fujimori": {"tipo": "processado"},               # renunciou por fax já no Japão, sob escândalo
    "kim-dae-jung": {"tipo": "oposicao", "eua_apoio_declarado": "nao"},
    "sanchez-lozada": {"eua_apoio_declarado": "nao"},  # recusar extradição não é apoio declarado à causa
    "guaido": {"tipo": "oposicao"},
    "aquino": {"tipo": "oposicao"},
    "reza-pahlavi": {"tipo": "oposicao"},
    "sam-rainsy": {"tipo": "oposicao"},
}


def j(nome):
    return json.load(open(CASOS / nome, encoding="utf-8"))


def wilson(k, n, z=1.96):
    if n == 0:
        return (0, 0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (round(max(0, c - m) * 100, 1), round(min(1, c + m) * 100, 1))


def sim(valor):
    return str(valor).lower() in ("sim", "true")


def e2():
    grupo = {l["id"]: l for l in csv.DictReader(open(CASOS / "lista_e2.csv", encoding="utf-8"))}
    linhas = []
    for c in j("e2_passada_a.json"):
        c = {**c, **ADJUDICA.get(c["id"], {})}
        c["grupo"] = grupo[c["id"]]["grupo"]
        c["nome"] = grupo[c["id"]]["nome"]
        c["pais"] = grupo[c["id"]]["pais"]
        linhas.append(c)
    with open(RES / "e2_casos_final.csv", "w", newline="", encoding="utf-8") as f:
        campos = ["id", "nome", "pais", "grupo", "saiu", "anfitriao", "tipo", "regime_casa", "eua_apoio_declarado", "voltou_ao_pais", "anos_ate_voltar", "voltou_ao_poder", "caminho", "entregue", "obs"]
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        w.writeheader()
        w.writerows(linhas)

    def conta(sub, nome):
        n = len(sub)
        k = sum(sim(c["voltou_ao_poder"]) for c in sub)
        v = sum(sim(c["voltou_ao_pais"]) for c in sub)
        e = sum(sim(c["entregue"]) for c in sub)
        return {"grupo": nome, "n": n, "voltou_ao_pais": v, "voltou_ao_poder": k, "ic95_poder": wilson(k, n), "entregue": e,
                "quem_voltou_ao_poder": [f"{c['nome']} ({c['caminho']})" for c in sub if sim(c["voltou_ao_poder"])],
                "quem_foi_entregue": [c["nome"] for c in sub if sim(c["entregue"])]}

    eua = [c for c in linhas if c["grupo"] == "eua"]
    comp = [c for c in linhas if c["grupo"] == "comparacao"]
    parecidos = [c for c in eua if c["regime_casa"] == "democracia" and c["tipo"] in ("processado", "derrotado_na_urna")]
    eua_apoiados = [c for c in eua if sim(c["eua_apoio_declarado"])]
    democracia = [c for c in linhas if c["regime_casa"] == "democracia"]
    urna = [c for c in linhas if c["tipo"] == "derrotado_na_urna"]
    # teste do passado: deixa um de fora; prevê com a taxa dos outros do mesmo grupo
    brier, brier_50 = [], []
    for c in linhas:
        outros = [o for o in linhas if o["grupo"] == c["grupo"] and o["id"] != c["id"]]
        p = (sum(sim(o["voltou_ao_poder"]) for o in outros) + 1) / (len(outros) + 2)
        r = 1 if sim(c["voltou_ao_poder"]) else 0
        brier.append((p - r) ** 2)
        brier_50.append(0.25)
    anos = [c["anos_ate_voltar"] for c in linhas if sim(c["voltou_ao_poder"]) and isinstance(c.get("anos_ate_voltar"), (int, float))]
    extra = {l["id"]: l for l in csv.DictReader(open(RAIZ / "dados" / "e2_extra.csv", encoding="utf-8"))}
    saida = lambda c: int(str(c["saiu"])[:4])
    ate_poder = lambda c: int(extra[c["id"]]["anos_ate_o_poder"]) if extra.get(c["id"], {}).get("anos_ate_o_poder") else None

    def horizonte(sub, h):  # só entra quem já teve h anos de observação até 2026
        obs = [c for c in sub if saida(c) + h <= 2026]
        k = [c["nome"] for c in obs if ate_poder(c) is not None and ate_poder(c) <= h]
        return {"anos": h, "observados": len(obs), "voltaram": len(k), "ic95": wilson(len(k), len(obs)), "quem": k}

    maduros = [c for c in linhas if saida(c) <= 2016]
    maduros_eua = [c for c in maduros if c["grupo"] == "eua"]
    abertos = [c["nome"] for c in linhas if saida(c) > 2016]
    sem_nao_abrigados = [c for c in eua if not extra.get(c["id"], {}).get("nao_abrigado_de_fato")]
    mesmos_bolsonaro = ("jair-bolsonaro", "eduardo-bolsonaro", "ramagem")
    parecidos_fora_do_grupo = [c for c in parecidos if c["id"] not in mesmos_bolsonaro]
    p_global = sum(sim(c["voltou_ao_poder"]) for c in linhas) / len(linhas)
    brier_const = statistics.mean((p_global - (1 if sim(c["voltou_ao_poder"]) else 0)) ** 2 for c in linhas)
    brier_global = []
    for c in linhas:
        outros = [o for o in linhas if o["id"] != c["id"]]
        pg = (sum(sim(o["voltou_ao_poder"]) for o in outros) + 1) / (len(outros) + 2)
        brier_global.append((pg - (1 if sim(c["voltou_ao_poder"]) else 0)) ** 2)
    caminhos = Counter(c["caminho"] for c in linhas if sim(c["voltou_ao_poder"]))
    return {
        "n_casos": len(linhas), "todos": conta(linhas, "todos"), "eua": conta(eua, "abrigados nos EUA"), "comparacao": conta(comp, "abrigados em outro país"),
        "parecidos": conta(parecidos, "EUA, vindos de democracia, processados ou derrotados"), "parecidos_nomes": [c["nome"] for c in parecidos],
        "eua_com_apoio": conta(eua_apoiados, "EUA, com apoio declarado"), "eua_com_apoio_nomes": [c["nome"] for c in eua_apoiados],
        "vindos_de_democracia": conta(democracia, "todos vindos de democracia"), "derrotados_na_urna": conta(urna, "derrotados na urna"),
        "derrotados_nomes": [c["nome"] for c in urna], "caminhos": dict(caminhos), "anos_ate_voltar_mediana": statistics.median(anos) if anos else None,
        "anos_ate_voltar": anos, "brier_leave_one_out": round(statistics.mean(brier), 3), "brier_chute": 0.25,
        "brier_taxa_unica": round(brier_const, 3), "brier_taxa_global_fora_um": round(statistics.mean(brier_global), 3),
        "horizontes_todos": [horizonte(linhas, h) for h in (4, 8, 12)], "horizontes_eua": [horizonte(eua, h) for h in (4, 8, 12)],
        "anos_ate_o_poder": {c["nome"]: ate_poder(c) for c in linhas if ate_poder(c) is not None},
        "maduros": conta(maduros, "saíram até 2016"), "maduros_eua": conta(maduros_eua, "saíram até 2016, nos EUA"), "ainda_abertos": abertos,
        "eua_sem_nao_abrigados": conta(sem_nao_abrigados, "EUA, sem Somoza e o xá"), "parecidos_fora_do_grupo": conta(parecidos_fora_do_grupo, "parecidos, sem Jair, Eduardo e Ramagem"),
        "grupo_politico_voltou": {c["nome"]: extra[c["id"]]["grupo_politico_voltou"] for c in linhas if extra.get(c["id"], {}).get("grupo_politico_voltou")},
        "cargo_nacional_depois": {c["nome"]: extra[c["id"]]["cargo_nacional_depois"] for c in linhas if extra.get(c["id"], {}).get("cargo_nacional_depois")},
        "apoio_sensibilidade": {"como_codificado": "2 de 6", "kim_entra_eduardo_sai": "3 de 6", "e_chalabi_conta": "4 de 6"},
    }


def e3():
    d = j("e3_derrotas.json")
    casos = d["casos"]
    return {"n": len(casos), "reconheceu": sum(c["reconheceu"] == "sim" for c in casos), "sancao": sum(c["sancao_ou_tarifa_nova"] == "sim" for c in casos),
            "apoio_golpe_oposicao": sum(c["apoio_a_golpe_ou_oposicao"] == "sim" for c in casos), "forca": sum(c["forca_militar"] == "sim" for c in casos),
            "relacao": dict(Counter(c["relacao_em_12m"] for c in casos)), "descartados": len(d.get("descartados", [])),
            "casos": [{"caso": c.get("id") or c.get("caso"), "reconheceu": c["reconheceu"], "sancao": c["sancao_ou_tarifa_nova"], "golpe_oposicao": c["apoio_a_golpe_ou_oposicao"], "forca": c["forca_militar"], "relacao": c["relacao_em_12m"]} for c in casos]}


def e4():
    d = j("e4_escada.json")
    br = d["brasil"]
    sobe = [x for x in br if x.get("direcao") == "sobe"]
    desce = [x for x in br if x.get("direcao") == "desce"]
    por_tipo = Counter(x.get("tipo") for x in sobe)
    militar = sum("militar" in str(x.get("tipo")).lower() for x in br)
    comp = {p: {"n": len(v), "sobe": sum(x.get("direcao") == "sobe" for x in v), "desce": sum(x.get("direcao") == "desce" for x in v)} for p, v in d["comparacao"].items()}
    with open(RES / "e4_escada_brasil.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["data", "tipo", "direcao"])
        for x in br:
            w.writerow([x.get("data"), x.get("tipo"), x.get("direcao")])
    cat = {l["id"]: l["categoria"] for l in csv.DictReader(open(RAIZ / "dados" / "e4_categorias.csv", encoding="utf-8"))}
    dirigidas = [x for x in sobe if x["id"] not in cat]
    datas = sorted(date.fromisoformat(x["data"]) for x in dirigidas)
    # P08: janela de 240 dias, de 02/11/2026 a 30/06/2027; quantas janelas iguais desde jul/2025 tiveram medida dirigida
    inicio, fim, cheias, total = date(2025, 7, 1), date(2026, 11, 2) - timedelta(days=240), 0, 0
    while inicio <= fim:
        total += 1
        cheias += any(inicio <= d <= inicio + timedelta(days=240) for d in datas)
        inicio += timedelta(days=1)
    return {"n": len(br), "sobe": len(sobe), "desce": len(desce), "sobe_por_tipo": dict(por_tipo), "medidas_militares": militar, "comparacao": comp,
            "dirigidas_ao_brasil": len(dirigidas), "ids_dirigidas": [x["id"] for x in dirigidas], "outras_que_subiam": dict(Counter(cat.values())),
            "ultima_dirigida": str(datas[-1]), "janelas_240d_com_medida_pct": round(cheias * 100 / total, 1), "janelas_240d": total}


def e5():
    f = j("e5_forca.json")
    f = f if isinstance(f, list) else f["casos"]
    sem_aval = [x for x in f if str(x.get("aval_local")) == "nao" and x.get("populacao_alvo_mi") and x.get("tipo") != "contingencia"]
    maior = max(sem_aval, key=lambda x: x["populacao_alvo_mi"])
    s = j("e5_sinais.json")
    tipos = Counter(t["brasil_hoje"] for t in s["tipos_de_sinal"])
    return {"n": len(f), "por_tipo": dict(Counter(x["tipo"] for x in f)), "maior_alvo_sem_aval": {"pais": maior["pais"], "ano": maior["ano"], "pop_mi": maior["populacao_alvo_mi"]},
            "brasil_pop_mi": 214, "razao_brasil_maior_alvo": round(214 / maior["populacao_alvo_mi"], 1), "sinais_antes_venezuela": len(s["sinais_antes_da_captura"]),
            "tipos_de_sinal": len(s["tipos_de_sinal"]), "sinais_brasil": dict(tipos),
            "dias_antes_da_captura": {x["tipo"]: (date(2026, 1, 3) - date.fromisoformat(x["data"] if len(x["data"]) == 10 else x["data"] + "-01")).days for x in reversed(s["sinais_antes_da_captura"]) if "abre caminho" not in x["sinal"]},
            "tabela_sinais": [{"tipo": t["tipo"], "brasil": t["brasil_hoje"]} for t in s["tipos_de_sinal"]],
            "tabela_forca": [{"ano": x["ano"], "pais": x["pais"], "tipo": x["tipo"], "pop": x.get("populacao_alvo_mi"), "aval": x.get("aval_local")} for x in f]}


def e6():
    linhas = list(csv.DictReader(open(RAIZ / "dados" / "e6_hipoteses.csv", encoding="utf-8")))
    hip = [k for k in linhas[0] if k.startswith("H")]
    placar = {h: {"contra": sum(l[h] == "-" for l in linhas), "a_favor": sum(l[h] == "+" for l in linhas)} for h in hip}
    por_alvo = {a: {h: {"contra": sum(l[h] == "-" for l in linhas if l["sobre"] == a), "a_favor": sum(l[h] == "+" for l in linhas if l["sobre"] == a)} for h in hip} for a in sorted({l["sobre"] for l in linhas})}
    r = {"n_evidencias": len(linhas), "placar": placar, "por_alvo": por_alvo, "ordem": sorted(hip, key=lambda h: (placar[h]["contra"], -placar[h]["a_favor"]))}
    p2 = RAIZ / "dados" / "e6_segunda_codificacao.csv"
    if p2.exists():
        l2 = list(csv.DictReader(open(p2, encoding="utf-8")))
        pares = [(a[h], b[h]) for a, b in zip(linhas, l2) for h in hip]
        r["concordancia_segunda_codificacao_pct"] = round(sum(x == y for x, y in pares) * 100 / len(pares), 1)
        r["placar_segunda_codificacao"] = {h: {"contra": sum(l[h] == "-" for l in l2), "a_favor": sum(l[h] == "+" for l in l2)} for h in hip}
    return r


def citacoes():
    p = RES / "citacoes.csv"
    if not p.exists():
        return None
    l = list(csv.DictReader(open(p, encoding="utf-8")))
    return {"trechos": len(l), "achados": sum(x["achado"] == "True" for x in l), "paginas": len({x["url"] for x in l}), "paginas_capturadas": len({x["url"] for x in l if x["capturada"] == "True"}), "por_situacao": dict(Counter(x["situacao"] for x in l))}


def main():
    conc = {l["campo"]: l for l in csv.DictReader(open(RES / "e2_concordancia.csv", encoding="utf-8"))}
    resumo = {"lido_ate": "2026-11-02", "e2": e2(), "e2_concordancia": conc, "e3": e3(), "e4": e4(), "e5": e5(), "e6": e6(), "citacoes": citacoes()}
    p = RES / "previsoes_final.json"
    if p.exists():
        resumo["e7"] = json.load(open(p, encoding="utf-8"))
    json.dump(resumo, open(RES / "RESUMO.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps({k: resumo["e2"][k] for k in ("n_casos", "todos", "eua", "comparacao", "parecidos", "parecidos_nomes", "eua_com_apoio", "eua_com_apoio_nomes", "vindos_de_democracia", "derrotados_na_urna", "caminhos", "brier_leave_one_out", "brier_taxa_unica", "brier_taxa_global_fora_um", "horizontes_todos", "horizontes_eua", "maduros", "maduros_eua", "ainda_abertos", "eua_sem_nao_abrigados", "parecidos_fora_do_grupo", "grupo_politico_voltou", "anos_ate_o_poder")}, ensure_ascii=False, indent=0))
    print(json.dumps({k: resumo[k] for k in ("e3", "e4", "e6")}, ensure_ascii=False)[:1800])
    print(json.dumps({k: v for k, v in resumo["e5"].items() if not k.startswith("tabela")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
