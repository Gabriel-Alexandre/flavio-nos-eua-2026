"""Monta os textos e as perguntas da rodada 2. A rodada 1 fica congelada em rodada1/."""
import csv
from pathlib import Path

P = Path(__file__).parent
a = (P / "texto_A_r2.md").read_text(encoding="utf-8")
(P / "texto_B_r2.md").write_text(a + (P / "historia_r2.md").read_text(encoding="utf-8"), encoding="utf-8")

linhas = list(csv.DictReader(open(P / "perguntas.csv", encoding="utf-8")))
novas = [
    ("P20", "Os EUA fazem ataque militar em solo ou águas territoriais brasileiras contra PCC ou Comando Vermelho sem aval do Brasil", "2029-01-20", "ataque confirmado por um dos governos"),
    ("P21", "Os EUA aplicam sanção nominal nova (Magnitsky ou parecida) a autoridade brasileira", "2027-06-30", "ato do Tesouro ou do Departamento de Estado publicado; revogação de visto não conta"),
    ("P22", "Banco brasileiro é sancionado pelos EUA ou punido por ligação com PCC ou CV", "2027-06-30", "ato do Tesouro ou do FinCEN citando banco brasileiro"),
    ("P23", "O Brasil aplica medida concreta com base na Lei da Reciprocidade contra os EUA", "2027-06-30", "ato do governo brasileiro em vigor; abrir exame não conta"),
    ("P24", "O STF toma medida nova contra cidadão, empresa ou plataforma americana", "2027-06-30", "decisão pública de ministro ou turma com ordem, multa ou bloqueio"),
]
with open(P / "perguntas_r2.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id", "pergunta", "prazo", "resolve_sim_se"])
    for l in linhas:
        w.writerow([l["id"], l["pergunta"], l["prazo"], l["resolve_sim_se"]])
    w.writerows(novas)
with open(P / "cenarios_r2.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id", "cenario", "descricao"])
    w.writerows([
        ("C1", "A pressão longa", "Flávio nos EUA sem poder; posse normal; tarifa e visto como moeda; conversa intermitente; sem ruptura e sem acordo amplo até o fim de 2027"),
        ("C2", "O acordo", "Trump e Lula negociam: tarifa e minerais em troca do embaixador e de cooperação; Flávio perde importância para Washington"),
        ("C3", "A escalada", "Nova sanção forte, bancos atingidos pela designação ou ação sobre o Pix na linha da Seção 301, autoridades de volta à lista, prisão decretada com recusa americana; sem ação militar"),
        ("C4", "A força", "Ação militar americana em território brasileiro sem aval do Brasil"),
    ])
