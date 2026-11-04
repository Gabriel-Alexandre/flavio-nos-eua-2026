"""Refaz os números centrais por outro caminho, sem importar ferramentas/analise.py.

Uso: python ferramentas/validacao_independente.py
Compara com resultados/RESUMO.json e grava resultados/validacao_independente.csv.
A contagem de exilados é refeita sobre a passada B, que foi codificada sem ver a passada A.
"""
import csv
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
R = json.loads((RAIZ / "resultados" / "RESUMO.json").read_text(encoding="utf-8"))
b = json.loads((RAIZ / "dados" / "casos" / "e2_passada_b.json").read_text(encoding="utf-8"))
lista = list(csv.DictReader((RAIZ / "dados" / "casos" / "lista_e2.csv").open(encoding="utf-8")))
g = {l["id"]: l["grupo"] for l in lista}
e3 = json.loads((RAIZ / "dados" / "casos" / "e3_derrotas.json").read_text(encoding="utf-8"))["casos"]
e4 = json.loads((RAIZ / "dados" / "casos" / "e4_escada.json").read_text(encoding="utf-8"))["brasil"]
e5 = json.loads((RAIZ / "dados" / "casos" / "e5_forca.json").read_text(encoding="utf-8"))
e5 = e5 if isinstance(e5, list) else e5["casos"]
s = json.loads((RAIZ / "dados" / "casos" / "e5_sinais.json").read_text(encoding="utf-8"))["tipos_de_sinal"]
prev = [json.loads(p.read_text(encoding="utf-8")) for p in (RAIZ / "dados" / "previsoes" / "rodada3").glob("*.json")]


def s_(v):
    return str(v).lower() in ("sim", "true")


def contar(pred, campo):
    return sum(1 for c in b if pred(c) and s_(c[campo]))


def mediana(xs):
    xs = sorted(xs)
    n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


pares = [
    ("casos na lista", len(lista), R["e2"]["n_casos"]),
    ("casos na passada B", len(b), R["e2"]["n_casos"]),
    ("EUA, voltaram ao poder (passada B)", contar(lambda c: g[c["id"]] == "eua", "voltou_ao_poder"), R["e2"]["eua"]["voltou_ao_poder"]),
    ("EUA, voltaram ao país (passada B)", contar(lambda c: g[c["id"]] == "eua", "voltou_ao_pais"), R["e2"]["eua"]["voltou_ao_pais"]),
    ("EUA, entregues (passada B)", contar(lambda c: g[c["id"]] == "eua", "entregue"), R["e2"]["eua"]["entregue"]),
    ("comparação, voltaram ao poder (passada B)", contar(lambda c: g[c["id"]] == "comparacao", "voltou_ao_poder"), R["e2"]["comparacao"]["voltou_ao_poder"]),
    ("derrota: reconheceu", sum(c["reconheceu"] == "sim" for c in e3), R["e3"]["reconheceu"]),
    ("derrota: força", sum(c["forca_militar"] == "sim" for c in e3), R["e3"]["forca"]),
    ("escada: total", len(e4), R["e4"]["n"]),
    ("escada: sobe", sum(x["direcao"] == "sobe" for x in e4), R["e4"]["sobe"]),
    ("força: casos", len(e5), R["e5"]["n"]),
    ("sinais: existe", sum(x["brasil_hoje"] == "existe" for x in s), R["e5"]["sinais_brasil"]["existe"]),
    ("sinais: não", sum(x["brasil_hoje"] == "nao" for x in s), R["e5"]["sinais_brasil"]["nao"]),
    ("previsões: respostas", len(prev), R["e7"]["n_respostas"]),
]
for q in R["e7"]["perguntas"]:
    pares.append((f"mediana {q['id']}", mediana([p["perguntas"][q["id"]]["p"] for p in prev if p["condicao"] == "B"]), q["com_historia"]))

falhas = 0
with (RAIZ / "resultados" / "validacao_independente.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["numero", "refeito", "no_resumo", "passou"])
    for nome, a, c in pares:
        ok = a == c
        falhas += not ok
        w.writerow([nome, a, c, ok])
        if not ok:
            print("FALHOU", nome, a, c)
print(f"{len(pares) - falhas} de {len(pares)} passaram")
sys.exit(1 if falhas else 0)
