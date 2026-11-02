"""Confere se cada trecho citado nos dados está mesmo na página capturada.

Uso: python ferramentas/conferir_citacoes.py [--capturar] [--navegador]
Lê os JSON de dados/casos/, monta dados/fontes.csv, captura com ferramentas/capturar.py e grava
resultados/citacoes.csv com o trecho, a fonte e se foi achado.
"""
import csv
import glob
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CAPTURAS = RAIZ / "dados" / "capturas"


def id_da_url(url: str) -> str:
    return hashlib.sha256(url.encode()).hexdigest()[:16]


def normal(texto: str) -> str:
    texto = unicodedata.normalize("NFKC", texto).lower()
    texto = re.sub(r"\[\s*[\w ]{1,12}\s*\]", "", texto)  # marca de nota da Wikipedia
    texto = re.sub(r"-\s+", "-", texto)  # hifenização de PDF
    texto = re.sub(r"[\"'“”‘’«»*_\[\]()]", "", texto)
    return re.sub(r"\s+", " ", texto).strip()


def itens(obj, arquivo, caminho=""):
    """Acha todo dicionário com 'fontes' dentro do JSON, em qualquer profundidade."""
    if isinstance(obj, dict):
        if isinstance(obj.get("fontes"), list):
            rotulo = obj.get("id") or obj.get("afirmacao") or obj.get("indicador") or obj.get("caso") or obj.get("pais") or caminho
            for f in obj["fontes"]:
                if isinstance(f, dict) and f.get("url"):
                    yield {"arquivo": arquivo, "item": str(rotulo)[:80], "url": f["url"], "trecho": f.get("trecho", "")}
        for k, v in obj.items():
            if k != "fontes":
                yield from itens(v, arquivo, f"{caminho}/{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from itens(v, arquivo, f"{caminho}/{i}")


def main():
    todos = []
    for arq in sorted(glob.glob(str(RAIZ / "dados" / "casos" / "*.json"))):
        todos += list(itens(json.load(open(arq, encoding="utf-8")), Path(arq).name))
    urls = sorted({t["url"] for t in todos})
    with open(RAIZ / "dados" / "fontes.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "url"])
        for u in urls:
            w.writerow([id_da_url(u), u])
    if "--capturar" in sys.argv:
        extra = ["--navegador"] if "--navegador" in sys.argv else []
        subprocess.run([sys.executable, str(RAIZ / "ferramentas" / "capturar.py"), str(RAIZ / "dados" / "fontes.csv"), *extra], check=False)
    achados = 0
    (RAIZ / "resultados").mkdir(exist_ok=True)
    with open(RAIZ / "resultados" / "citacoes.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["arquivo", "item", "url", "capturada", "achado", "situacao", "trecho"])
        for t in todos:
            cap = CAPTURAS / f"{id_da_url(t['url'])}.txt"
            texto = normal(cap.read_text(encoding="utf-8", errors="ignore")) if cap.exists() else ""
            trecho = normal(t["trecho"])
            ok = bool(trecho) and trecho in texto
            if not ok and trecho and texto:  # hifenização e reticências: aceita se 80% das janelas de 6 palavras baterem
                pal = trecho.split()
                janelas = [" ".join(pal[i:i + 6]) for i in range(0, max(1, len(pal) - 5), 3)]
                ok = sum(j in texto for j in janelas) / len(janelas) >= 0.8
            achados += ok
            api = t["trecho"].lstrip().startswith(("{", "[")) or "api-comexstat" in t["url"] or "olinda.bcb" in t["url"]
            parcial = False
            if not ok and trecho and texto:
                pal = trecho.split()
                janelas = [" ".join(pal[i:i + 4]) for i in range(0, max(1, len(pal) - 3), 2)]
                parcial = sum(j in texto for j in janelas) / len(janelas) >= 0.6
            situacao = "achado" if ok else "resposta_de_api" if api else "pagina_recusou" if not texto else "achado_com_diferenca" if parcial else "nao_achado"
            w.writerow([t["arquivo"], t["item"], t["url"], bool(texto), ok, situacao, t["trecho"]])
    print(f"{achados} de {len(todos)} trechos achados; {len(urls)} páginas")


if __name__ == "__main__":
    main()
