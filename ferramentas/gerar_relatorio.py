"""Escreve RELATORIO.md, RESUMO_SIMPLES.md e docs/LEITURA_DA_IA.md a partir de resultados/RESUMO.json.

Uso: python ferramentas/gerar_relatorio.py
Número à mão não entra: o que é contagem sai do RESUMO; o que é fato de notícia traz a fonte.
"""
import csv
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
R = json.loads((RAIZ / "resultados" / "RESUMO.json").read_text(encoding="utf-8"))
E2, E3, E4, E5, E6, E7 = R["e2"], R["e3"], R["e4"], R["e5"], R["e6"], R["e7"]
C = R.get("citacoes") or {}
E8 = json.loads((RAIZ / "dados" / "casos" / "e8_brasil.json").read_text(encoding="utf-8"))
E8 = E8 if isinstance(E8, list) else E8["itens"]
PQ = {q["id"]: q for q in E7["perguntas"]}
CE = {c["id"]: c for c in E7["cenarios"]}
CONC = R["e2_concordancia"]
VAL = list(csv.DictReader((RAIZ / "resultados" / "validacao_independente.csv").open(encoding="utf-8")))


def v8(prefixo):
    return next(x["valor"] for x in E8 if x["indicador"].startswith(prefixo))


def br(x):
    return f"{x:g}".replace(".", ",")


def pct(q):
    return f"{br(PQ[q]['com_historia'])}%"


def rate(d):
    return f"{d['voltou_ao_poder']} de {d['n']}"


EUA_X = v8("Exportações do Brasil para os EUA, jan-set 2026")
CHI_X = v8("Exportações do Brasil para a China, jan-set 2026")
TAR = v8("Quanto das importações americanas")
DOL = v8("Dólar PTAX")
IBOV = v8("Dólar comercial e Ibovespa")
ordem = sorted(E7["perguntas"], key=lambda q: -q["com_historia"])
tabela_prev = "\n".join(f"| {q['id']} | {q['pergunta']} | {q['prazo']} | **{br(q['com_historia'])}%** ({q['faixa']}) | {br(q['menor'])} a {br(q['maior'])} | {br(q['sem_historia'])}% |" for q in ordem)
tabela_cen = "\n".join(f"| **{c['cenario']}** | {c['descricao']} | **{c['com_historia_normalizado']:.0f}%** | {br(c['menor'])} a {br(c['maior'])} |" for c in E7["cenarios"])
tabela_sinais = "\n".join(f"| {t['tipo']} | {t['brasil']} |" for t in E5["tabela_sinais"])
tabela_forca = "\n".join(f"| {x['ano']} | {x['pais']} | {x['tipo']} | {x['pop'] if x['pop'] else 'não se aplica'} | {x['aval']} |" for x in E5["tabela_forca"])
tabela_derrota = "\n".join(f"| {c['caso']} | {c['reconheceu']} | {c['sancao']} | {c['golpe_oposicao']} | {c['forca']} | {c['relacao']} |" for c in E3["casos"])
nomes_h = {"H2_narrativa_e_midterms": "Narrativa política e eleições nos EUA", "H3_china_e_influencia": "China e influência no hemisfério", "H4_minerais": "Terras raras", "H1_lealdade": "Lealdade aos Bolsonaro", "H5_aposta_de_rubio": "Aposta pessoal de Rubio e entorno"}
tabela_h = "\n".join(f"| {nomes_h[h]} | {E6['placar'][h]['contra']} | {E6['placar'][h]['a_favor']} |" for h in E6["ordem"])
cit = f"{C.get('achados', '?')} de {C.get('trechos', '?')} trechos achados na página capturada por este projeto ({C.get('paginas_capturadas', '?')} de {C.get('paginas', '?')} páginas abriram para o robô)"
val_ok = sum(l["passou"] == "True" for l in VAL)

RELATORIO = f"""# Flávio nos EUA: o que esperar

**Lido até {R['lido_ate']}.** Análise feita pelo Claude (Anthropic), a pedido de Gabriel Alexandre. As previsões entraram em commit em 02/nov/2026, antes das eleições americanas de 03/nov.

## O que este projeto não consegue dizer

- Quem pagou o jato, quando a saída foi decidida, e por onde exatamente ele saiu do Brasil.
- A intenção de ninguém. Os motivos abaixo são o que as evidências sustentam mais, em julgamento declarado da IA.
- Se os inquéritos têm fundamento. Flávio nega as acusações, e a PF diz que ele não é foragido.
- O que Trump decide amanhã. A própria Reuters registra que ele pode mudar de ideia.
- A base de casos é pequena e foi escolhida por critério, e não é um censo. As previsões são dos modelos da Anthropic, que não são uma multidão diversa, e modelos ainda perdem de previsores humanos treinados.

## 1. A resposta

| Pergunta | Resposta |
|---|---|
| Os EUA ajudaram? | A entrada, sim: Rubio disse em público que Trump deixou claro que ele seria *"paroled"*. O jato liga a um assessor de Trump, segundo Reuters, NYT e WSJ. A saída do Brasil não tem prova de participação americana. A Argentina aparece mais na parte física |
| Ele pediu asilo? | Não há registro. Entrou por parole humanitária. O NYT diz que ele deve pedir residência |
| Trump apoia? | Abriu a porta e disse *"I won't get involved"*. Sem planos de encontrá-lo, e a Reuters diz que sem planos de apoiar a pretensão dele |
| Trump falou em fraude de novo? | Sim, várias vezes até 31/10, sem prova |
| Volta ao poder por esse caminho? | Dos {E2['eua']['n']} abrigados nos EUA, {E2['eua']['voltou_ao_poder']} voltaram; dos {E2['parecidos']['n']} mais parecidos com ele, {E2['parecidos']['voltou_ao_poder']} |
| Os EUA vão invadir? | {pct('P01')} até 2030, a faixa mais baixa da escala. Dos {E5['tipos_de_sinal']} tipos de sinal que vieram antes da captura de Maduro, {E5['sinais_brasil']['existe']} existem hoje em relação ao Brasil, {E5['sinais_brasil']['parcial']} em parte e {E5['sinais_brasil']['nao']} não aparecem |
| O que é mais provável? | **{CE['C1']['cenario']}** ({CE['C1']['com_historia_normalizado']:.0f}%), e nova medida americana até junho de 2027 ({pct('P08')}) |

## 2. As 72 horas

Fontes em `dados/casos/e1_originais.json`, com trechos conferidos, e na pasta do vídeo no repositório de documentação.

| Parte | O que sustenta | Situação |
|---|---|---|
| Ordem de entregar passaportes | nota da PF: representação em 25/10, intimação em 26/10, prazo de 24 horas não cumprido | confirmado. A PF pediu 7 minutos depois da confirmação do TSE; a hora da decisão de Moraes não foi divulgada |
| A ponte | Migraciones: 22h50 e embarque às 23h30. Fantástico: 3 registros na van, 22h37, 22h40 e 23h11, com só o 1º válido | a passagem está confirmada; o horário tem conflito entre as fontes |
| Brasília até a ponte | Fantástico: linha de investigação com voo às 5h05 por Buenos Aires. Assessoria de Willer Tomaz nega | não resolvido |
| O jato | Baires Fly, LV-JQW, Guayaquil, Opa-locka. Dono à AFP: US$ 150 mil, de conta empresarial nos EUA, por corretor. Clarín, 28/10: empresas ligadas à embaixada americana contrataram | confirmado o voo; quem pagou, não |
| Jason Miller | Reuters, NYT, WSJ. Correio da Manhã, citando o Metrópoles, diz que ele confirmou; outra versão diz que não comentou | apurado por três veículos; a confirmação dele tem conflito |
| Argentina | Migraciones e o chefe de Gabinete Santilli: entrada legal. Repórter da C5N viu escolta e placa diplomática. Clarín coloca Caputo no local. Ordem de Milei, jato-isca e SIDE em campo aparecem no Río Negro, e não no texto do Clarín de 28/10 | participação oficial provável; os detalhes têm uma fonte |
| Ex-agente do Mossad | Fantástico nomeia Menachem Booky Halevy; CNN Brasil sem nome | a presença tem duas fontes; não prova ação do Mossad |
| Entrada nos EUA | transcript do Departamento de Estado: *"He had previously held a visa"* e *"paroled"*. Registro DT, até 27/10/2027, obtido pela imprensa. Passaporte diplomático cancelado | parole confirmada; a data, só pelo registro |

## 3. O que aconteceu com quem esteve nesse lugar

{E2['n_casos']} casos desde 1945, duas passadas independentes. Concordância: {float(CONC['voltou_ao_poder']['concordancia']) * 100:.0f}% em quem voltou ao poder, {float(CONC['entregue']['concordancia']) * 100:.0f}% em quem foi entregue e {float(CONC['tipo']['concordancia']) * 100:.0f}% no tipo de caso. Lista em `resultados/e2_casos_final.csv`.

| Grupo | Casos | Voltaram ao país | Voltaram ao poder | Margem de 95% | Entregues |
|---|---|---|---|---|---|
| Abrigados nos EUA | {E2['eua']['n']} | {E2['eua']['voltou_ao_pais']} | **{E2['eua']['voltou_ao_poder']}** | {E2['eua']['ic95_poder'][0]}% a {E2['eua']['ic95_poder'][1]}% | {E2['eua']['entregue']} |
| Abrigados em outro país | {E2['comparacao']['n']} | {E2['comparacao']['voltou_ao_pais']} | **{E2['comparacao']['voltou_ao_poder']}** | {E2['comparacao']['ic95_poder'][0]}% a {E2['comparacao']['ic95_poder'][1]}% | {E2['comparacao']['entregue']} |
| Nos EUA, com apoio declarado de Washington | {E2['eua_com_apoio']['n']} | {E2['eua_com_apoio']['voltou_ao_pais']} | **{E2['eua_com_apoio']['voltou_ao_poder']}** | {E2['eua_com_apoio']['ic95_poder'][0]}% a {E2['eua_com_apoio']['ic95_poder'][1]}% | {E2['eua_com_apoio']['entregue']} |
| Mais parecidos: nos EUA, vindos de democracia, processados ou derrotados | {E2['parecidos']['n']} | {E2['parecidos']['voltou_ao_pais']} | **{E2['parecidos']['voltou_ao_poder']}** | {E2['parecidos']['ic95_poder'][0]}% a {E2['parecidos']['ic95_poder'][1]}% | {E2['parecidos']['entregue']} |

**Quem voltou ao poder:** {'; '.join(E2['eua']['quem_voltou_ao_poder'] + E2['comparacao']['quem_voltou_ao_poder'])}. Mediana de {br(E2['anos_ate_voltar_mediana'])} anos até voltar ao país.

**Os mais parecidos:** {', '.join(E2['parecidos_nomes'])}. {', '.join(E2['parecidos']['quem_foi_entregue'])} foram entregues.

**Leitura.** Estar nos EUA não aparece como vantagem nem como desvantagem para voltar ao poder: as taxas são parecidas e as margens se sobrepõem. O que muda é como se volta. Entre os apoiados por Washington, Aristide voltou com tropas americanas e Diem por nomeação com apoio americano. Guaidó, Machado e Chalabi tiveram apoio e não chegaram à chefia; na Venezuela, os EUA capturaram Maduro e passaram a tratar Delcy Rodríguez como presidente. Os dois casos que o abrigo americano ajudou a colocar no poder eram de país pequeno ou em guerra, com presença militar americana.

**O que contraria a leitura:** Hidaka, Kubota e Yukawa (2025) dizem que a maioria dos líderes exilados volta e retoma o poder. Lemos o resumo. A base deles é de líderes que perderam o cargo, em geral sob regime fechado; a nossa inclui candidatos e opositores, e casos ainda abertos. Exílio não é o fim da carreira, e Perón levou 17 anos. Por isso a conclusão é sobre o caminho, e não sobre o destino dele.

**Teste do passado:** prever o desfecho de cada caso com a taxa dos outros do mesmo grupo dá nota de Brier {E2['brier_leave_one_out']}, contra {E2['brier_chute']} do chute de meio a meio. Boa parte disso é só porque voltar ao poder é raro; não mede a capacidade de prever Flávio.

## 4. Quando o preferido de Washington perde

{E3['n']} casos em que a preferência americana tem fonte; {E3['descartados']} descartados por falta dela, entre eles Brasil 2022. Hungria com janela parcial.

| Caso | Reconheceu | Sanção ou tarifa nova | Apoio a golpe ou oposição | Força | Relação em 12 meses |
|---|---|---|---|---|---|
{tabela_derrota}

**Leitura:** o reconhecimento é a regra ({E3['reconheceu']} de {E3['n']}), e força militar nos 12 meses, {E3['forca']} de {E3['n']}. As duas rupturas foram Palestina 2006 e Venezuela 2024. Chile 1970 mostra que a pressão pode durar anos: o golpe veio em 1973, fora da janela.

## 5. A escada contra o Brasil

{E4['n']} medidas de jan/2025 a nov/2026: {E4['sobe']} para cima, {E4['desce']} para baixo, {E4['medidas_militares']} militares. Para comparar, Colômbia {E4['comparacao']['colombia']['sobe']} e {E4['comparacao']['colombia']['desce']}, México {E4['comparacao']['mexico']['sobe']} e {E4['comparacao']['mexico']['desce']}, Canadá {E4['comparacao']['canada']['sobe']} e {E4['comparacao']['canada']['desce']}, África do Sul {E4['comparacao']['africa_do_sul']['sobe']} e {E4['comparacao']['africa_do_sul']['desce']}.

- **Sobe e desce:** a Magnitsky de Moraes durou de 30/07 a 12/12/2025. A tarifa de 40% caiu em 20/02/2026 pela Suprema Corte americana, e não por acordo.
- **Hoje:** 25% pela Seção 301 desde 22/07/2026, mais 12,5% da ação global sobre cerca de 60 economias. Dos US$ {TAR['total_importado_2024_us_bi']} bi que os EUA compraram do Brasil em 2024, US$ {TAR['paga_25_cheio_us_bi']} bi pagam os 25% cheios, pelas medidas lidas.
- **Literatura:** sanções dão certo em cerca de um terço dos casos (Hufbauer et al.), e Pape conta 5 de 115. Mudar regime: 29 de 90. EUA sozinhos, de 1970 a 2014: 11 de 54. Metas limitadas e alvos democráticos rendem mais.
- **O efeito aqui:** a Reuters diz que analistas veem várias das medidas como contraproducentes, e parte ajudou a popularidade de Lula.

## 6. Os EUA vão usar a força?

**Base do medo, tudo real:** captura de Maduro; Trump na ONU em 22/09; vídeo da Doutrina Monroe; PCC e CV designados; ofício do Itamaraty de 01/07 falando em *"possibilidade do uso da força militar"*; ministro Múcio, *"abrir o portão"*, em 04/08; 1964 e a Brother Sam, navios prontos e nunca usados.

**Negativa:** o Departamento de Estado disse que a lei da designação não contempla ação militar. ⚠️ Trump negou ataque à Venezuela 64 dias antes da captura, então negativa sozinha não encerra.

**Tamanho:** o maior alvo sem aval foi {E5['maior_alvo_sem_aval']['pais']}, {br(E5['maior_alvo_sem_aval']['pop_mi'])} milhões. O Brasil tem {E5['brasil_pop_mi']} milhões, {br(E5['razao_brasil_maior_alvo'])} vezes mais. Tropas em 2026 só aparecem em países que aceitaram, ou em treinamento.

**Sinais, um por um** (*"nao"* é ausência nas páginas abertas, e não prova):

| Tipo de sinal antes de Maduro | Brasil hoje |
|---|---|
{tabela_sinais}

**O que mudaria a resposta:** navios e aviões perto da costa; aviso da FAA; acusação formal contra autoridade do governo; ultimato; autorização pública à CIA; coalizão com vizinhos sobre o Brasil.

**O risco mais realista, sem tropa:** a designação alcança banco. White & Case diz que medidas contra um banco brasileiro dependente de dólar *"could be existential"*.

<details><summary>Tabela da força no hemisfério</summary>

| Ano | País | Tipo | População (mi) | Aval local |
|---|---|---|---|---|
{tabela_forca}

</details>

## 7. Por que receber o Flávio

Matriz de hipóteses concorrentes (Heuer), `dados/e6_hipoteses.csv`. É julgamento da IA, e não medida; {E6['n_evidencias']} evidências.

| Hipótese | Evidências contra | A favor |
|---|---|---|
{tabela_h}

**Leitura:** a que menos sofre com as evidências é a narrativa política, com as eleições americanas no meio: Trump ligou o Brasil à fraude dos democratas no comício do Texas, na semana da votação. Os minerais explicam o interesse no Brasil, e os EUA já têm posição com Lula no governo. Nenhuma fala oficial sobre a entrada cita minerais; mas Dino abriu inquérito em 27/10, a pedido do PT, sobre suspeita de troca de apoio por terras raras, e isso não prova irregularidade.

## 8. O que muda no Brasil

| Indicador | Número | Fonte |
|---|---|---|
| Exportações aos EUA, jan a set/2026 | US$ {EUA_X['2026']} bi, {br(EUA_X['variacao_pct'])}% | ComexStat |
| Exportações à China, jan a set/2026 | US$ {CHI_X['2026']} bi, +{br(CHI_X['variacao_pct'])}% | ComexStat |
| Dólar PTAX, 23/10 e 30/10 | R$ {br(DOL['23/10'])} e R$ {br(DOL['30/10'])}, +{br(DOL['alta_23_a_30_pct'])}% | Banco Central |
| Ibovespa na semana | {br(IBOV['ibov_queda_semana_pct'])}% de queda | imprensa |

⚠️ O mercado reagiu à reeleição e ao quadro fiscal, e não dá para atribuir isso ao caso Flávio.

| Cenário | Efeito |
|---|---|
| A pressão longa | exportador para os EUA segue com tarifa; o comércio continua indo para a China |
| O acordo | alívio de tarifa e minerais com refino; custo político dos dois lados |
| A escalada | risco em banco e fintech; câmbio mais volátil |

## 9. O que esperar

**Cenários até o fim de 2027** (mediana de {len(E7['modelos'])} modelos, depois de ver a história; somados a 100):

| Cenário | O que é | Chance | Menor a maior |
|---|---|---|---|
{tabela_cen}

**As perguntas, para conferir na data** (`dados/previsoes/`):

| # | Pergunta | Prazo | Com a história | Entre modelos | Sem a história |
|---|---|---|---|---|---|
{tabela_prev}

**O que a história mudou nas IAs:** em média, {br(E7['mudanca_media_absoluta'])} pontos. A mudança maior foi na nova medida contra o Brasil, de {br(PQ['P08']['sem_historia'])}% para {br(PQ['P08']['com_historia'])}%. Na invasão, nada: já estava no piso. Discordância média entre modelos: {br(E7['discordancia_media_entre_modelos'])} pontos.

**Datas:** 03/nov midterms · 13/nov prazo de Rubio · nov G7 · 14 e 15/dez G20 · até 18/dez diplomação · 05/jan posse · 31/jan fim do mandato · 27/out/2027 fim da parole.

## 10. O que circula

{chr(10).join(f"- **{l['afirmacao']}** ({l['canal']}): {l['o_que_e_real']}." for l in csv.DictReader((RAIZ / 'dados' / 'e9_o_que_circula.csv').open(encoding='utf-8')))}

## 11. Validação

- Citações: {cit}. Página que recusa o robô fica registrada; o trecho dela segue da leitura do agente.
- Números: {val_ok} de {len(VAL)} refeitos por outro caminho, em `resultados/validacao_independente.csv`, com os exilados recontados sobre a 2ª passada.
- Revisão por 3 leitores: `docs/REVISAO_ADVERSARIAL.md`.

Refazer: `docs/REPLICAR.md`.
"""

SIMPLES = f"""# Resumo simples

**A pergunta:** depois da ida do Flávio para os EUA, o que esperar?

**Como:** a IA leu as fontes, montou {E2['n_casos']} casos de exilados desde 1945, {E3['n']} casos em que o preferido de Washington perdeu, {E5['n']} usos de força americana no continente e {E4['n']} medidas contra o Brasil. Depois {len(E7['modelos'])} modelos responderam {len(E7['perguntas'])} perguntas, separados e com data.

**O que aconteceu:** Trump decidiu deixar ele entrar, e Rubio disse isso em público ao mesmo tempo em que disse *"não facilitamos nada"*. O jato liga a um assessor de Trump, segundo Reuters, NYT e WSJ. A saída do Brasil não tem prova americana. Não é asilo: é parole humanitária. Ele não é foragido, segundo a PF.

**O que a história diz:** dos {E2['eua']['n']} abrigados nos EUA, {E2['eua']['voltou_ao_poder']} voltaram ao poder; dos {E2['parecidos']['n']} mais parecidos com ele, {E2['parecidos']['voltou_ao_poder']}. Quando Washington queria alguém de volta, houve tropa ou apoio de ocupação, e em país pequeno. Mas exílio não é fim: um estudo de 2025 diz que a maioria dos líderes exilados acaba voltando, pela política de casa.

**Vão invadir?** {pct('P01')} até 2030, a faixa mais baixa. Dos {E5['tipos_de_sinal']} tipos de sinal que vieram antes de Maduro, {E5['sinais_brasil']['nao']} não aparecem no caso do Brasil. O risco real é econômico: tarifa, visto e banco.

**O que esperar:** {CE['C1']['cenario'].lower()} ({CE['C1']['com_historia_normalizado']:.0f}%), {CE['C2']['cenario'].lower()} ({CE['C2']['com_historia_normalizado']:.0f}%), {CE['C3']['cenario'].lower()} ({CE['C3']['com_historia_normalizado']:.0f}%), {CE['C4']['cenario'].lower()} ({CE['C4']['com_historia_normalizado']:.0f}%).

**O limite:** amostra pequena; Trump muda de ideia; as IAs são todas da mesma empresa. As previsões ficaram registradas para serem cobradas.

Completo: [`RELATORIO.md`](RELATORIO.md).
"""

LEITURA = f"""# Leitura da IA

Esta é a opinião da análise, separada dos fatos.

1. **Trump usa o caso mais do que aposta nele.** Fala de fraude, abre a porta e não dá o passo seguinte. Em seis dias, as falas não trouxeram prova nem ato além da parole.
2. **A palavra mais importante do caso é "directly".** Rubio disse *"We didn't facilitate anything"* e corrigiu para *"At least the U.S. Government was not involved directly"*. A distinção entre governo e pessoas do entorno é onde mora a resposta das 15 perguntas dos democratas.
3. **A data que importa para o Flávio é 31/01/2027.** Até lá, o art. 53 protege. Depois, prisão e pedido de extradição ficam possíveis. O tratado não lista lavagem nem evasão, mas lista suborno e peculato, e por isso o caso Dark Horse pesa mais que o outro. Com Trump, a entrega é quase nenhuma chance; o risco dele é o próximo governo americano.
4. **O risco para o Brasil é o banco, não o fuzileiro.** A designação de PCC e CV é o instrumento com mais alcance e menos debate.
5. **O medo da invasão não é tolo, e a comparação com a Venezuela é fraca.** O alvo tem {br(E5['razao_brasil_maior_alvo'])} vezes o tamanho, governo reconhecido pelo mundo e superávit americano. O que pede atenção é a lista de sinais, e não o discurso.
6. **A hipótese inicial sobreviveu com corte.** Eu ia escrever que exílio em Miami é o fim. O estudo de 2025 e Perón derrubam isso. O que ficou é mais estreito: abrigo americano sozinho não põe ninguém no poder.
"""

(RAIZ / "RELATORIO.md").write_text(RELATORIO, encoding="utf-8")
(RAIZ / "RESUMO_SIMPLES.md").write_text(SIMPLES, encoding="utf-8")
(RAIZ / "docs" / "LEITURA_DA_IA.md").write_text(LEITURA, encoding="utf-8")
print(len(RELATORIO), len(SIMPLES), len(LEITURA))
