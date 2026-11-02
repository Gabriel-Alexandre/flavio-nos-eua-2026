"""Monta os dois textos que os modelos leem na E7: os fatos (A) e os fatos com a história (B).

Uso: python ferramentas/montar_dossie.py
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
R = json.load(open(RAIZ / "resultados" / "RESUMO.json", encoding="utf-8"))
PASTA = RAIZ / "dados" / "previsoes"

FATOS = """# Fatos até 02/nov/2026

- Em 25/10/2026, Lula venceu Flávio Bolsonaro com 51,79% a 48,21%. OEA e Carter Center validaram. O PL, o vice da chapa e o governador Tarcísio reconheceram. Flávio não reconheceu e alega fraude sem prova.
- Flávio é investigado no STF em dois inquéritos (lavagem com o advogado Willer Tomaz; corrupção, lavagem e evasão no caso do filme Dark Horse). Ele nega. A PF diz que ele não é foragido e não há mandado de prisão. O PT pediu prisão preventiva e Interpol, sem decisão.
- Em 25/10 a PF pediu e Moraes mandou entregar passaportes. Em 26/10 Flávio disse que não sairia. Em 27/10 cruzou para a Argentina, embarcou em jato privado e, em 28/10, chegou a Miami. Reuters, NYT e WSJ ligam Jason Miller, assessor de Trump, ao jato. Clarín liga o assessor de Milei à operação. Rubio, em 31/10: "We didn't facilitate anything [...] At least the U.S. Government was not involved directly", e que Trump deixou claro que ele seria "paroled".
- Status: parole humanitária, registro até 27/10/2027. NYT: deve pedir green card. O mandato de senador acaba em 31/01/2027; até lá, o art. 53 da Constituição limita a prisão.
- Trump: "another rigged election", "I like Lula", "we gave him a pass", "I won't get involved", "the election was a disgrace", "he can stay here as long as he wants", sem planos de encontrá-lo. Reuters: sem planos de apoiar a pretensão dele, embora possa mudar de ideia. Em carta, Flávio se disse "presidente eleito" e depois "líder do Brasil"; na live de 30/10 fala em Senado, crise econômica e nova eleição antes de 2030.
- EUA e Brasil: tarifa de 25% (Seção 301) desde 22/07/2026, mais 12,5% da ação global; Brasil sem aprovar o embaixador Danny Perez; EUA revogaram o visto da embaixadora Viotti em 04/08; PCC e CV designados terroristas em mai/2026. O Itamaraty escreveu em 01/07 que há risco de força militar; o Departamento de Estado negou. Rubio e o chanceler Vieira se falaram em Atlanta e devem se ver no G7. G20 em Doral em 14 e 15/12; a imprensa diz que Lula vai, sem confirmação oficial. Posse em 05/01/2027. 25 deputados democratas pediram resposta a Rubio até 13/11. Midterms em 03/11, com democratas à frente. Dino abriu inquérito em 27/10 sobre financiamento externo e suspeita de troca de apoio por terras raras.
"""


def historia():
    e2, e3, e4, e5 = R["e2"], R["e3"], R["e4"], R["e5"]
    return f"""

# O que a história mostra (levantamento deste projeto)

**Exilados ({e2['n_casos']} casos desde 1945, duas passadas independentes).** Abrigados nos EUA: {e2['eua']['voltou_ao_poder']} de {e2['eua']['n']} voltaram ao poder ({'; '.join(e2['eua']['quem_voltou_ao_poder'])}) e {e2['eua']['entregue']} foram entregues ({', '.join(e2['eua']['quem_foi_entregue'])}). Abrigados em outro país: {e2['comparacao']['voltou_ao_poder']} de {e2['comparacao']['n']}. Os mais parecidos com Flávio (nos EUA, vindos de democracia, processados ou derrotados): {e2['parecidos']['voltou_ao_poder']} de {e2['parecidos']['n']} voltaram ao poder, {e2['parecidos']['voltou_ao_pais']} voltaram ao país e {e2['parecidos']['entregue']} foram entregues ({', '.join(e2['parecidos_nomes'])}). Com apoio declarado dos EUA: {e2['eua_com_apoio']['voltou_ao_poder']} de {e2['eua_com_apoio']['n']}; Aristide com força americana, Diem por nomeação com apoio americano. Limite: alguns casos seguem abertos. Um estudo de 2025 (Hidaka, Kubota e Yukawa), com líderes depostos em geral, diz que a maioria volta e retoma o poder.

**Depois da derrota do preferido de Washington ({e3['n']} casos desde 1970).** Reconheceu em {e3['reconheceu']}; sanção nova em {e3['sancao']}; apoio a golpe ou oposição em {e3['apoio_golpe_oposicao']}; força militar em {e3['forca']} nos 12 meses seguintes. Relação: {e3['relacao']}. Amostra pequena.

**Escada contra o Brasil, jan/2025 a nov/2026.** {e4['n']} medidas: {e4['sobe']} para cima, {e4['desce']} para baixo, nenhuma militar. Magnitsky de Moraes durou de jul a dez/2025. Parte da tarifa caiu em fev/2026 pela Suprema Corte americana.

**Força no hemisfério, 1954 a 2026 ({e5['n']} casos).** Maior alvo sem aval: {e5['maior_alvo_sem_aval']['pais']}, {e5['maior_alvo_sem_aval']['pop_mi']} milhões; o Brasil tem {e5['brasil_pop_mi']} milhões, {e5['razao_brasil_maior_alvo']} vezes mais. Operações em terra em 2026 no Equador, com aval. Dos {e5['tipos_de_sinal']} tipos de sinal que antecederam a captura de Maduro, no Brasil hoje: {e5['sinais_brasil']}. Não aparecem: força naval e aérea perto do país, aviso da FAA, ultimato, CIA autorizada, acusação ao chefe de governo. Trump negou ataque à Venezuela 64 dias antes da captura, então negativa sozinha não separa os casos.

**Sanções (literatura).** Hufbauer et al.: cerca de um terço de sucesso; mudança de regime 29 de 90; EUA sozinhos em 1970-2014, 11 de 54. Pape: 5 de 115. O'Rourke: 64 operações encobertas e 6 abertas na Guerra Fria.
"""


PASTA.mkdir(parents=True, exist_ok=True)
(PASTA / "texto_A.md").write_text(FATOS, encoding="utf-8")
(PASTA / "texto_B.md").write_text(FATOS + historia(), encoding="utf-8")
print(len(FATOS), len(historia()))
