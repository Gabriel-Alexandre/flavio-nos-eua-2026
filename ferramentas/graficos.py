"""Gráficos 1920x1080 a partir de resultados/RESUMO.json e dos dados.

Uso: python ferramentas/graficos.py  (grava em resultados/figuras/)
"""
import csv
import json
import textwrap
from datetime import date
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
RES = RAIZ / "resultados"
FIG = RES / "figuras"
R = json.loads((RES / "RESUMO.json").read_text(encoding="utf-8"))
CASOS = RAIZ / "dados" / "casos"
AZUL, VERM, CINZA, VERDE, OURO = "#2D6A8A", "#C8553D", "#6B6B6B", "#2E8B57", "#C9902B"
CLARO = "#D9D9D9"
RODAPE = "github.com/Gabriel-Alexandre/flavio-nos-eua-2026 · análise feita pelo Claude"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 22, "axes.spines.top": False, "axes.spines.right": False})


def nova(titulo, subtitulo):
    fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
    fig.subplots_adjust(left=0.08, right=0.95, top=0.78, bottom=0.14)
    fig.suptitle(titulo, x=0.05, y=0.965, ha="left", fontsize=36, fontweight="bold")
    fig.text(0.05, 0.86, subtitulo, ha="left", fontsize=21, color="#444444")
    return fig, ax


def salvar(fig, nome, fonte):
    fig.text(0.05, 0.05, f"Fonte: {fonte}", fontsize=15, color="#555555")
    fig.text(0.05, 0.018, RODAPE, fontsize=15, color="#555555")
    FIG.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG / f"{nome}.png")
    plt.close(fig)


def g01_rota():
    fig, ax = nova("O caminho até Miami", "27 e 28/out/2026, pelos registros de migração e de voo")
    pts = {"Brasília": (-47.9, -15.8), "Foz do Iguaçu\nPuerto Iguazú": (-54.6, -25.6), "Guayaquil": (-79.9, -2.2), "Opa-locka, Miami": (-80.3, 25.9)}
    ax.plot(*zip(pts["Foz do Iguaçu\nPuerto Iguazú"], pts["Guayaquil"], pts["Opa-locka, Miami"]), color=AZUL, lw=5)
    ax.plot(*zip(pts["Brasília"], pts["Foz do Iguaçu\nPuerto Iguazú"]), color=VERM, lw=5, ls="--")
    for nome, (x, y) in pts.items():
        ax.scatter(x, y, s=260, color="#222222", zorder=3)
        ax.text(x + 1.4, y, nome, fontsize=24, va="center", fontweight="bold")
    ax.text(-58, -15, "Brasília até a ponte:\nvan ou avião?\nsem resposta", color=VERM, fontsize=21, ha="right", va="center")
    ax.text(-66, 4, "jato LV-JQW\nregistro de voo", color=AZUL, fontsize=21, ha="left", va="center")
    ax.set_xlim(-95, -30)
    ax.set_ylim(-32, 32)
    ax.axis("off")
    salvar(fig, "g01_rota", "Dirección Nacional de Migraciones (Argentina), monitores de voo, Fantástico")


def g02_quem_fez_o_que():
    fig, ax = nova("Os EUA ajudaram? Depende da parte", "O que cada parte da saída tem de sustentação")
    linhas = [("A entrada nos EUA", "Trump decidiu. Rubio disse em público:\n\"he would be paroled\"", "dito pelo governo", VERDE),
              ("O jato da Argentina", "Assessor de Trump, pela Reuters.\nDono: pago de conta em banco americano", "apuração da imprensa", OURO),
              ("A passagem pela Argentina", "Escolta e veículo oficial vistos por repórter.\nGoverno diz: \"entrou por Migraciones\"", "agentes argentinos no local", OURO),
              ("A saída do Brasil", "Reuters: contato com funcionários dos EUA.\nAjuda do governo nesse trecho, sem prova", "sem prova de ajuda", CINZA)]
    ax.axis("off")
    for i, (a, b, c, cor) in enumerate(linhas):
        y = 0.86 - i * 0.26
        ax.text(0, y + 0.035, a, fontsize=27, fontweight="bold", va="center")
        ax.text(0, y - 0.05, c, fontsize=21, color=cor, fontweight="bold", va="center")
        ax.text(0.42, y, b, fontsize=23, va="center")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    salvar(fig, "g02_quem_fez_o_que", "state.gov (31/out), Reuters, AFP, Clarín, Fantástico, nota da PF")


def barras_de_taxa(linhas, titulo, sub, nome, fonte):
    fig, ax = nova(titulo, sub)
    fig.subplots_adjust(left=0.40)
    ys = list(range(len(linhas)))[::-1]
    for y, (rot, k, n, cor) in zip(ys, linhas):
        ax.barh(y, 100, color=CLARO, height=0.55)
        ax.barh(y, 100 * k / n if n else 0, color=cor, height=0.55)
        ax.text(102, y, f"{k} de {n}", va="center", fontsize=28, fontweight="bold")
    ax.set_yticks(ys)
    ax.set_yticklabels([textwrap.fill(l[0], 26) for l in linhas], fontsize=23)
    ax.set_xlim(0, 125)
    ax.get_xaxis().set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    salvar(fig, nome, fonte)


def g03_exilados():
    e = R["e2"]
    h12 = e["horizontes_todos"][2]
    barras_de_taxa([("Abrigados nos EUA", e["eua"]["voltou_ao_poder"], e["eua"]["n"], AZUL),
                    ("Abrigados em outro país", e["comparacao"]["voltou_ao_poder"], e["comparacao"]["n"], CINZA),
                    ("Em até 12 anos, entre quem já teve esse tempo", h12["voltaram"], h12["observados"], OURO),
                    ("Por eleição, em até 12 anos", 0, h12["observados"], VERM)],
                   "Quem chegou ao poder saindo do exílio", f"{e['n_casos']} líderes e candidatos desde 1945; {len(e['ainda_abertos'])} casos seguem abertos", "g03_exilados",
                   "uma saída por pessoa; Bhutto, 1984 a 1988, fica fora da conta. Duas passadas com fontes conferidas; base deste projeto")


def g04_como_voltaram():
    fig, ax = nova("Os 6 que voltaram ao poder", "Quanto tempo levou, e como: em prazo curto só com tropa ou nomeação")
    ax.axis("off")
    nomes = {"Ngo Dinh Diem": ("Vietnã do Sul", "nomeado com apoio dos EUA, 4 anos", "EUA"), "Kim Dae-jung": ("Coreia do Sul", "eleição, 15 anos depois", "EUA"),
             "Jean-Bertrand Aristide": ("Haiti", "tropas americanas, 3 anos", "EUA"), "Juan Domingo Perón": ("Argentina", "eleição, 18 anos depois", "Espanha"),
             "Ruhollah Khomeini": ("Irã", "revolução, 15 anos depois", "França"), "Nawaz Sharif": ("Paquistão", "eleição, 13 anos depois", "Arábia S.")}
    for i, (n, (p, c, h)) in enumerate(nomes.items()):
        y = 0.92 - i * 0.17
        ax.text(0, y, n, fontsize=26, fontweight="bold", va="center")
        ax.text(0.36, y, p, fontsize=22, va="center", color="#444444")
        ax.text(0.52, y, c, fontsize=22, va="center")
        ax.text(1, y, h, fontsize=20, va="center", ha="right", color=AZUL if h == "EUA" else CINZA, fontweight="bold")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    salvar(fig, "g04_como_voltaram", "duas passadas independentes, com fontes conferidas; base deste projeto")


def g05_depois_da_derrota():
    e = R["e3"]
    barras_de_taxa([("Reconheceu o resultado", e["reconheceu"], e["n"], AZUL), ("Sanção ou tarifa nova", e["sancao"], e["n"], OURO),
                    ("Apoio a golpe ou à oposição", e["apoio_golpe_oposicao"], e["n"], VERM), ("Força militar", e["forca"], e["n"], VERM)],
                   "Quando o preferido de Washington perde", "O que os EUA fizeram nos 12 meses seguintes, em casos de 1970 a 2026", "g05_depois_da_derrota",
                   "base deste projeto; amostra pequena, com só casos em que a preferência tem fonte")


def g06_escada():
    br = json.loads((CASOS / "e4_escada.json").read_text(encoding="utf-8"))["brasil"]
    ids = set(R["e4"]["ids_dirigidas"])
    br = [x for x in br if x["id"] in ids or x["direcao"] == "desce"]
    fig, ax = nova("A escada contra o Brasil", f"{R['e4']['dirigidas_ao_brasil']} medidas americanas dirigidas ao Brasil, {R['e4']['desce']} para baixo, {R['e4']['medidas_militares']} militares, até nov/2026")
    fig.subplots_adjust(left=0.05, right=0.97, bottom=0.2)
    cores = {"tarifa": OURO, "sancao": VERM, "visto": AZUL, "diplomatica": CINZA, "investigacao": VERDE, "designacao": "#6A4C93"}
    vistos = {}
    for x in br:
        d = date.fromisoformat(str(x["data"])[:10])
        sinal = 1 if x["direcao"] == "sobe" else -1
        chave = (d.year, d.month, sinal)
        vistos[chave] = vistos.get(chave, 0) + 1
        ax.scatter(d, sinal * vistos[chave], s=240, color=cores.get(x["tipo"], CINZA), zorder=3)
    ax.axhline(0, color="#222222", lw=2)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.text(date(2025, 1, 5), 4.3, "sobe", fontsize=24, fontweight="bold")
    ax.text(date(2025, 1, 5), -3.2, "desce", fontsize=24, fontweight="bold")
    for i, (k, c) in enumerate(cores.items()):
        ax.scatter(date(2025, 1, 15 + 0), 0, s=0)
        fig.text(0.05 + i * 0.155, 0.1, f"● {k.replace('diplomatica', 'diplomática').replace('sancao', 'sanção').replace('investigacao', 'investigação').replace('designacao', 'designação')}", color=c, fontsize=21, fontweight="bold")
    ax.set_ylim(-4, 6)
    salvar(fig, "g06_escada", "Federal Register, OFAC, USTR, state.gov, gov.br e imprensa; base deste projeto")


def g07_tamanho():
    casos = [x for x in R["e5"]["tabela_forca"] if x["pop"] and x["aval"] == "nao" and x["tipo"] != "contingencia" and not (x["pais"] == "Venezuela" and x["ano"] == 2025)]
    por_pais = {}
    for x in casos:
        rot = f"{x['pais']} {x['ano']}"
        por_pais[rot] = x["pop"]
    itens = sorted(por_pais.items(), key=lambda p: p[1])
    itens = sorted(itens + [("Irã 2026, fora do hemisfério", 87.0)], key=lambda p: p[1])
    fig, ax = nova("O tamanho encarece, e não impede", "População do alvo de força americana sem aval, em milhões; o hemisfério e a guerra do Irã")
    fig.subplots_adjust(left=0.27)
    nomes = [n for n, _ in itens] + ["Brasil hoje"]
    vals = [v for _, v in itens] + [R["e5"]["brasil_pop_mi"]]
    ax.barh(nomes, vals, color=[CINZA] * len(itens) + [VERM])
    for i, v in enumerate(vals):
        ax.text(v + 2, i, f"{v:.1f}".replace(".", ",").replace(",0", ""), va="center", fontsize=19, fontweight="bold")
    ax.tick_params(axis="y", labelsize=18)
    ax.get_xaxis().set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(0, 245)
    salvar(fig, "g07_tamanho", "base deste projeto, com fontes por caso; Irã: estimativa de 2026 na Wikipedia; não inclui ataques com aval do país")


ACENTO = {"designacao de organizacoes criminosas como terroristas": "Designação de organizações criminosas como terroristas", "sancoes, tarifas e punicao diplomatica": "Sanções, tarifas e punição diplomática",
          "oficio ou alerta do governo alvo e negativa do governo dos EUA": "Ofício ou alerta do governo alvo e negativa dos EUA", "tropas terrestres na regiao": "Tropas terrestres na região",
          "comando operacional dedicado, com sede em Miami": "Comando operacional dedicado, com sede em Miami", "fala do presidente ameacando usar a forca": "Fala do presidente ameaçando usar a força",
          "embaixada em crise: fechamento, evacuacao, sem chefe": "Embaixada em crise: fechamento, evacuação, sem chefe", "base juridica interna para usar a forca contra grupos designados": "Base jurídica interna para usar a força contra grupos designados",
          "designacao do governo ou do chefe de Estado, acusacao formal e recompensa": "Designação do governo ou do chefe de Estado, acusação e recompensa", "mobilizacao naval ou aerea perto do pais": "Mobilização naval ou aérea perto do país",
          "coalizao regional com acordos de operacoes conjuntas": "Coalizão regional com operações conjuntas", "declaracao do Departamento de Defesa (Guerra) sobre o pais": "Declaração do Departamento de Defesa sobre o país",
          "ataques a embarcacoes ou alvos em territorio do pais": "Ataques a barcos ou alvos no território do país", "aviso a aviacao ou fechamento de espaco aereo": "Aviso à aviação ou fechamento do espaço aéreo",
          "autorizacao publica de operacoes da CIA no pais": "Autorização pública de operações da CIA no país", "ultimato direto ao chefe de governo": "Ultimato direto ao chefe de governo"}


def g08_sinais():
    fig, ax = nova("Os sinais que vieram antes de Maduro", "Cada tipo de sinal, e se aparece hoje em relação ao Brasil nas páginas lidas")
    ax.axis("off")
    cor = {"existe": VERM, "parcial": OURO, "nao": CINZA}
    txt = {"existe": "existe", "parcial": "parcial", "nao": "não"}
    linhas = sorted(R["e5"]["tabela_sinais"], key=lambda t: ["existe", "parcial", "nao"].index(t["brasil"]))
    meio = (len(linhas) + 1) // 2
    for col, parte in enumerate((linhas[:meio], linhas[meio:])):
        for i, t in enumerate(parte):
            x = col * 0.51
            y = 0.97 - i * 0.123
            ax.text(x, y, textwrap.fill(ACENTO.get(t["tipo"], t["tipo"]), 36), fontsize=17, va="center")
            ax.text(x + 0.47, y, txt[t["brasil"]], fontsize=20, color=cor[t["brasil"]], fontweight="bold", ha="right", va="center")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    salvar(fig, "g08_sinais", "base deste projeto; 'não' é ausência nas páginas abertas, e não prova de que não existe")


def g09_motivos():
    p = R["e6"]["placar"]
    nomes = {"H2_narrativa_e_midterms": "Narrativa e eleições nos EUA", "H3_china_e_influencia": "China e influência", "H4_minerais": "Terras raras", "H1_lealdade": "Lealdade aos Bolsonaro", "H5_aposta_de_rubio": "Aposta de Rubio", "H6_conviccao_de_perseguicao": "Convicção de perseguição"}
    fig, ax = nova("Por que receber o Flávio?", f"{R['e6']['n_evidencias']} evidências, 6 hipóteses: a matriz não aponta vencedor")
    fig.subplots_adjust(left=0.36)
    ordem = R["e6"]["ordem"][::-1]
    for i, h in enumerate(ordem):
        ax.barh(i, -p[h]["contra"], color=VERM, height=0.55)
        ax.barh(i, p[h]["a_favor"], color=AZUL, height=0.55)
        ax.text(-p[h]["contra"] - 0.15, i, str(p[h]["contra"]), ha="right", va="center", fontsize=26, color=VERM, fontweight="bold")
        ax.text(p[h]["a_favor"] + 0.15, i, str(p[h]["a_favor"]), ha="left", va="center", fontsize=26, color=AZUL, fontweight="bold")
    ax.set_yticks(range(len(ordem)))
    ax.set_yticklabels([nomes[h] for h in ordem], fontsize=24)
    ax.axvline(0, color="#222222", lw=2)
    ax.set_xlim(-6, 6)
    ax.get_xaxis().set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.text(-3, len(ordem) - 0.35, "contra", color=VERM, fontsize=24, fontweight="bold", ha="center")
    ax.text(3, len(ordem) - 0.35, "a favor", color=AZUL, fontsize=24, fontweight="bold", ha="center")
    salvar(fig, "g09_motivos", "classificação feita pela IA, publicada em dados/e6_hipoteses.csv; é julgamento, não medida")


def g10_cenarios():
    c = R["e7"]["cenarios"][::-1]
    fig, ax = nova("O que esperar até o fim de 2027", f"Mediana de {len(R['e7']['modelos'])} modelos de IA, separados, depois de ver a história")
    fig.subplots_adjust(left=0.3)
    cores = {"C1": AZUL, "C2": VERDE, "C3": OURO, "C4": VERM}
    for i, x in enumerate(c):
        ax.barh(i, x["com_historia_normalizado"], color=cores[x["id"]], height=0.6)
        ax.text(x["com_historia_normalizado"] + 1, i, f"{x['com_historia_normalizado']:.0f}%", va="center", fontsize=30, fontweight="bold")
    ax.set_yticks(range(len(c)))
    ax.set_yticklabels([x["cenario"] for x in c], fontsize=26)
    ax.set_xlim(0, 75)
    ax.get_xaxis().set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    salvar(fig, "g10_cenarios", "previsões da rodada 3, registradas em commit em 04/nov/2026; são estimativas, e não fatos")


def g11_previsoes():
    q = sorted(R["e7"]["perguntas"], key=lambda x: x["com_historia"])
    curtos = {"P01": "Tropas dos EUA no Brasil sem aval (2030)", "P02": "Ataque dos EUA contra PCC/CV no Brasil (2027)", "P03": "EUA reconhecem o Flávio (posse)", "P14": "EUA entregam o Flávio (2027)",
              "P04": "Trump recebe o Flávio em público (mar/27)", "P19": "Rubio responde aos democratas (2026)", "P11": "Acordo de minerais EUA e Brasil (2027)", "P16": "Flávio volta ao Brasil (2028)",
              "P13": "Brasil pede a extradição (2027)", "P09": "EUA reduzem a tarifa de 25% (jun/27)", "P10": "Brasil aprova embaixador Perez (jun/27)", "P18": "Audiência na Câmara dos EUA (jun/27)",
              "P17": "Flávio lidera a direita para 2030 (2027)", "P12": "STF decreta prisão do Flávio (jun/27)", "P05": "Trump e Lula se falam (15/dez)", "P06": "Lula vai ao G20 em Doral (15/dez)",
              "P07": "EUA mandam representante à posse", "P15": "Flávio segue nos EUA com status (out/27)", "P08": "Nova medida dos EUA contra o Brasil (jun/27)", "P20": "Ataque contra PCC/CV sem aval (jan/29)", "P21": "Sanção nominal a autoridade (jun/27)",
              "P22": "Banco brasileiro atingido (jun/27)", "P23": "Brasil usa a Lei da Reciprocidade (jun/27)", "P24": "STF age contra americano ou plataforma (jun/27)"}
    fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
    fig.subplots_adjust(left=0.42, right=0.96, top=0.86, bottom=0.11)
    fig.suptitle(f"As {len(q)} previsões registradas", x=0.05, y=0.965, ha="left", fontsize=36, fontweight="bold")
    for i, x in enumerate(q):
        ax.plot([x["menor"], x["maior"]], [i, i], color=CLARO, lw=8, solid_capstyle="round")
        ax.scatter(x["com_historia"], i, s=170, color=AZUL, zorder=3)
        ax.text(max(x["maior"], x["com_historia"]) + 1.5, i, f"{x['com_historia']:g}%".replace(".", ","), va="center", fontsize=15, fontweight="bold")
    ax.set_yticks(range(len(q)))
    ax.set_yticklabels([curtos[x["id"]] for x in q], fontsize=12)
    ax.set_xlim(0, 100)
    ax.tick_params(axis="x", labelsize=15)
    ax.spines["left"].set_visible(False)
    salvar(fig, "g11_previsoes", "ponto: mediana dos modelos; barra: do menor ao maior. Para conferir na data")


def g13_relogio():
    fig, ax = nova("O relógio da Venezuela", "Dias antes da captura de Maduro; o Brasil está a 5 meses da designação de PCC e CV")
    fig.subplots_adjust(left=0.05, right=0.97, bottom=0.14)
    marcos = [(R["e5"]["dias_antes_da_captura"]["designacao"], "designação", 0.55), (149, "recompensa", -0.35), (137, "navios na região", 0.35), (123, "ataque a barcos", -0.85), (80, "CIA autorizada", 0.85), (64, "Trump nega ataque", -0.35), (43, "FAA e ultimato", 0.35), (4, "ataque em terra", -0.85)]
    ax.axhline(0, color="#222222", lw=3)
    for d, t, lado in marcos:
        ax.plot([d, d], [0, lado], color=CINZA, lw=2)
        ax.scatter(d, 0, s=200, color=VERM, zorder=3)
        ax.text(d, lado + (0.04 if lado > 0 else -0.04), f"{t}\n{d} dias", ha="left" if t == "recompensa" else "center", va="bottom" if lado > 0 else "top", fontsize=19)
    hoje = R["e5"]["dias_antes_da_captura"]["designacao"] - (date(2026, 11, 2) - date(2026, 5, 28)).days
    ax.axvline(hoje, color=AZUL, lw=5)
    ax.text(hoje + 4, 1.28, "Brasil hoje, só pela designação", color=AZUL, fontsize=23, fontweight="bold", ha="right")
    ax.set_xlim(340, -15)
    ax.set_ylim(-1.3, 1.45)
    ax.axis("off")
    salvar(fig, "g13_relogio", "base deste projeto; alinhar pela designação é uma escolha, e os mesmos sinais apareceram em países sem captura")


def g12_comercio():
    e8 = json.loads((CASOS / "e8_brasil.json").read_text(encoding="utf-8"))
    e8 = e8 if isinstance(e8, list) else e8["itens"]
    def valor(prefixo):
        return next(x["valor"] for x in e8 if x["indicador"].startswith(prefixo))
    eua, china = valor("Exportações do Brasil para os EUA, jan-set 2026"), valor("Exportações do Brasil para a China, jan-set 2026")
    fig, ax = nova("Para quem o Brasil vende", "Exportações de janeiro a setembro, em bilhões de dólares")
    fig.subplots_adjust(left=0.15)
    xs = [0, 1, 3, 4]
    vs = [eua["mesmo_periodo_2025"], eua["2026"], china["mesmo_periodo_2025"], china["2026"]]
    ax.bar(xs, vs, color=[CLARO, AZUL, CLARO, VERM], width=0.85)
    for x, v, r in zip(xs, vs, ["2025", "2026", "2025", "2026"]):
        ax.text(x, v + 1.5, f"{v:.1f}".replace(".", ","), ha="center", fontsize=30, fontweight="bold")
        ax.text(x, -5, r, ha="center", fontsize=24)
    ax.text(0.5, -15, f"EUA, {eua['variacao_pct']:+.1f}%".replace(".", ",").replace("-", "−"), ha="center", fontsize=28, fontweight="bold", color=AZUL)
    ax.text(3.5, -15, f"China, {china['variacao_pct']:+.1f}%".replace(".", ","), ha="center", fontsize=28, fontweight="bold", color=VERM)
    ax.axis("off")
    ax.set_ylim(-20, 100)
    salvar(fig, "g12_comercio", "ComexStat, Ministério do Desenvolvimento, Indústria e Comércio")


for f in (g13_relogio, g01_rota, g02_quem_fez_o_que, g03_exilados, g04_como_voltaram, g05_depois_da_derrota, g06_escada, g07_tamanho, g08_sinais, g09_motivos, g10_cenarios, g11_previsoes, g12_comercio):
    f()
print(len(list(FIG.glob("*.png"))))
