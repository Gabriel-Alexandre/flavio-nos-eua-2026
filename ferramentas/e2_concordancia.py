"""Compara as duas passadas da E2, campo a campo, e grava concordância e kappa.

Uso: python ferramentas/e2_concordancia.py
"""
import csv
import json
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CAMPOS = ["tipo", "regime_casa", "eua_apoio_declarado", "voltou_ao_pais", "voltou_ao_poder", "caminho", "entregue"]


def carregar(nome):
    return {c["id"]: c for c in json.load(open(RAIZ / "dados" / "casos" / nome, encoding="utf-8"))}


def kappa(xs, ys):
    n = len(xs)
    po = sum(x == y for x, y in zip(xs, ys)) / n
    cx, cy = Counter(xs), Counter(ys)
    pe = sum(cx[k] * cy[k] for k in cx) / (n * n)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def main():
    a, b = carregar("e2_passada_a.json"), carregar("e2_passada_b.json")
    ids = sorted(set(a) & set(b))
    with open(RAIZ / "resultados" / "e2_concordancia.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["campo", "concordancia", "kappa", "n"])
        for campo in CAMPOS:
            xs = [str(a[i].get(campo)).lower() for i in ids]
            ys = [str(b[i].get(campo)).lower() for i in ids]
            con = sum(x == y for x, y in zip(xs, ys)) / len(ids)
            w.writerow([campo, round(con, 3), round(kappa(xs, ys), 3), len(ids)])
            print(campo, round(con, 3), round(kappa(xs, ys), 3))
    with open(RAIZ / "resultados" / "e2_divergencias.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "campo", "a", "b"])
        for i in ids:
            for campo in CAMPOS + ["anfitriao", "saiu", "anos_ate_voltar"]:
                if str(a[i].get(campo)).lower() != str(b[i].get(campo)).lower():
                    w.writerow([i, campo, a[i].get(campo), b[i].get(campo)])
    print("ids", len(ids))


if __name__ == "__main__":
    main()
