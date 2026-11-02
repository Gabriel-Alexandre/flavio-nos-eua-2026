"""Junta as previsões dos modelos: mediana por pergunta e por cenário, faixa do ICD 203 e efeito de ver a história.

Uso: python ferramentas/agregar_previsoes.py
"""
import csv
import glob
import json
import statistics
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTA = RAIZ / "dados" / "previsoes"
FAIXAS = [(5, "quase nenhuma chance"), (20, "muito improvável"), (45, "improvável"), (55, "chance parecida"), (80, "provável"), (95, "muito provável"), (100, "quase certo")]


def faixa(p):
    return next(nome for limite, nome in FAIXAS if p <= limite)


def r1(pid):
    r = [json.load(open(a, encoding="utf-8")) for a in glob.glob(str(PASTA / "rodada1" / "*_B.json"))]
    v = [x["perguntas"][pid]["p"] for x in r if pid in x["perguntas"]]
    return statistics.median(v) if v else None


def main():
    arquivos = [json.load(open(a, encoding="utf-8")) for a in sorted(glob.glob(str(PASTA / "rodada2" / "*.json")))]
    perguntas = list(csv.DictReader(open(PASTA / "perguntas_r2.csv", encoding="utf-8")))
    cenarios = list(csv.DictReader(open(PASTA / "cenarios_r2.csv", encoding="utf-8")))
    saida = {"modelos": sorted({a["modelo"] for a in arquivos}), "n_respostas": len(arquivos), "perguntas": [], "cenarios": []}
    for q in perguntas:
        a = [x["perguntas"][q["id"]]["p"] for x in arquivos if x["condicao"] == "A"]
        b = [x["perguntas"][q["id"]]["p"] for x in arquivos if x["condicao"] == "B"]
        por_modelo = {x["modelo"]: x["perguntas"][q["id"]]["p"] for x in arquivos if x["condicao"] == "B"}
        mb, ma = statistics.median(b), statistics.median(a)
        saida["perguntas"].append({"id": q["id"], "pergunta": q["pergunta"], "prazo": q["prazo"], "resolve_sim_se": q["resolve_sim_se"], "sem_historia": ma, "com_historia": mb,
                                   "mudanca": round(mb - ma, 1), "menor": min(b), "maior": max(b), "media": round(statistics.mean(b), 1), "faixa": faixa(mb), "por_modelo": por_modelo,
                                   "rodada1": r1(q["id"])})
    for c in cenarios:
        a = [x["cenarios"][c["id"]] for x in arquivos if x["condicao"] == "A"]
        b = [x["cenarios"][c["id"]] for x in arquivos if x["condicao"] == "B"]
        saida["cenarios"].append({"id": c["id"], "cenario": c["cenario"], "descricao": c["descricao"], "sem_historia": statistics.median(a), "com_historia": statistics.median(b), "menor": min(b), "maior": max(b)})
    soma = sum(c["com_historia"] for c in saida["cenarios"])
    for c in saida["cenarios"]:
        c["com_historia_normalizado"] = round(c["com_historia"] * 100 / soma, 1)
    dif = [abs(q["mudanca"]) for q in saida["perguntas"]]
    saida["mudanca_media_absoluta"] = round(statistics.mean(dif), 1)
    amplitudes = [q["maior"] - q["menor"] for q in saida["perguntas"]]
    saida["discordancia_media_entre_modelos"] = round(statistics.mean(amplitudes), 1)
    grandes = sorted((q for q in saida["perguntas"] if q["rodada1"] is not None), key=lambda q: -abs(q["com_historia"] - q["rodada1"]))[:3]
    saida["mudancas_rodada1"] = ", ".join(f"{q['id']} de {q['rodada1']:g}% para {q['com_historia']:g}%".replace(".", ",") for q in grandes)
    json.dump(saida, open(RAIZ / "resultados" / "previsoes_final.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for q in saida["perguntas"]:
        print(q["id"], q["rodada1"], "=>", q["sem_historia"], "->", q["com_historia"], f"[{q['menor']}-{q['maior']}]", q["faixa"], "|", q["pergunta"][:60])
    for c in saida["cenarios"]:
        print(c["id"], c["cenario"], c["sem_historia"], "->", c["com_historia"], c["com_historia_normalizado"], f"[{c['menor']}-{c['maior']}]")
    print(saida["mudanca_media_absoluta"], saida["discordancia_media_entre_modelos"], saida["n_respostas"])


if __name__ == "__main__":
    main()
