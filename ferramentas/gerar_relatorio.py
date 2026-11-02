"""Escreve RELATORIO.md, RESUMO_SIMPLES.md e docs/LEITURA_DA_IA.md a partir de resultados/RESUMO.json.

Uso: python ferramentas/gerar_relatorio.py
Número à mão não entra: o que é contagem sai do RESUMO; o que é fato de notícia traz a fonte.
"""
import csv
import json
import re
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
nomes_h = {"H2_narrativa_e_midterms": "Narrativa política e eleições nos EUA", "H3_china_e_influencia": "China e influência no hemisfério", "H4_minerais": "Terras raras", "H1_lealdade": "Lealdade aos Bolsonaro", "H5_aposta_de_rubio": "Aposta pessoal de Rubio e entorno", "H6_conviccao_de_perseguicao": "Convicção declarada de perseguição e proteção"}
tabela_h = "\n".join(f"| {nomes_h[h]} | {E6['por_alvo']['entrada'][h]['a_favor']} e {E6['por_alvo']['entrada'][h]['contra']} | {E6['por_alvo']['retorica'][h]['a_favor']} e {E6['por_alvo']['retorica'][h]['contra']} | {E6['placar_segunda_codificacao'][h]['a_favor']} e {E6['placar_segunda_codificacao'][h]['contra']} |" for h in nomes_h)
tabela_horizonte = "\n".join(f"| {a['anos']} anos | {a['voltaram']} de {a['observados']} | {a['ic95'][0]}% a {a['ic95'][1]}% | {b['voltaram']} de {b['observados']} |" for a, b in zip(E2["horizontes_todos"], E2["horizontes_eua"]))
tabela_anos = ", ".join(f"{n} em {a}" for n, a in sorted(E2["anos_ate_o_poder"].items(), key=lambda x: x[1]))
tabela_grupo = ", ".join(f"{n} ({a})" for n, a in sorted(E2["grupo_politico_voltou"].items(), key=lambda x: x[1]))
sit = C.get("por_situacao", {})
cit = f"{C.get('trechos', '?')} trechos: {sit.get('achado')} achados na página capturada, {sit.get('achado_com_diferenca')} com diferença pequena de redação, {sit.get('resposta_de_api')} são respostas de API, {sit.get('pagina_recusou')} em páginas que recusam o robô (quase todas da Britannica, usada na 2ª passada) e {sit.get('nao_achado')} não achados, listados em `resultados/citacoes.csv`"
val_ok = sum(l["passou"] == "True" for l in VAL)

RELATORIO = f"""# Flávio nos EUA: o que esperar

**Lido até {R['lido_ate']}.** Análise feita pelo Claude (Anthropic), a pedido de Gabriel Alexandre. As previsões entraram em commit em 02/nov/2026, antes das eleições americanas de 03/nov. A rodada 1 fica congelada em `dados/previsoes/rodada1/`; este relatório usa a rodada 2, feita depois da revisão adversarial, com o texto corrigido.

## O que este projeto não consegue dizer

- Quem pagou o jato, quando a saída foi decidida, e por onde exatamente ele saiu do Brasil.
- A intenção de ninguém. Os motivos abaixo são hipóteses comparadas, em julgamento declarado da IA, sem vencedor.
- Se os inquéritos têm fundamento. Flávio nega as acusações. A PF diz que as restrições, por si só, não fazem dele foragido.
- O que Trump decide amanhã. A própria Reuters registra que ele pode mudar de ideia.
- A base de casos é pequena e foi escolhida por critério, e não é um censo. As previsões são dos modelos da Anthropic, que não são uma multidão diversa, e modelos ainda perdem de previsores humanos treinados.

## 1. A resposta

| Pergunta | Resposta |
|---|---|
| Os EUA ajudaram? | Os EUA permitiram a entrada: Rubio disse que o presidente decidiu deixar entrar e que ele seria *"paroled into the country, and he was"*. O motivo oficial da parole não foi dito. O jato liga a um assessor de Trump pela Reuters, e por resumos pelo NYT e pelo WSJ. A saída do Brasil não tem prova de participação do governo americano. A Argentina aparece mais na parte física |
| Ele pediu asilo? | Não há registro. Entrou por parole humanitária. O NYT diz que ele deve pedir residência |
| Trump apoia? | Abriu a porta e disse *"I won't get involved"*. Sem planos de encontrá-lo, e a Reuters diz que sem planos de apoiar a pretensão dele |
| Trump falou em fraude de novo? | Sim, várias vezes até 31/10, sem apresentar prova |
| Volta ao poder por esse caminho? | Dos {E2['eua']['n']} abrigados nos EUA, {E2['eua']['voltou_ao_poder']} chegaram ao poder: um com tropas americanas, um nomeado com apoio americano e um eleito depois de 15 anos. Em até 12 anos, {E2['horizontes_todos'][2]['voltaram']} de {E2['horizontes_todos'][2]['observados']} entre todos, e nenhum por eleição. Flávio fala em voltar antes de 2030 |
| Os EUA vão invadir? | Tropas sem autorização até 2030: {pct('P01')}. Ataque contra PCC ou CV sem aval: {pct('P02')} até 2027 e {pct('P20')} até o fim do governo Trump. Dos {E5['tipos_de_sinal']} tipos de sinal que vieram antes da captura de Maduro, {E5['sinais_brasil']['existe']} existem hoje, {E5['sinais_brasil']['parcial']} em parte e {E5['sinais_brasil']['nao']} não, e os que existem são os mais antigos da sequência |
| O que é mais provável? | **{CE['C1']['cenario']}** ({CE['C1']['com_historia_normalizado']:.0f}%), e alguma medida americana nova até junho de 2027 ({pct('P08')}); sanção nominal a autoridade, {pct('P21')}; banco brasileiro atingido, {pct('P22')} |

## 2. As 72 horas

Fontes em `dados/casos/e1_originais.json`, com trechos conferidos, e na pasta do vídeo no repositório de documentação.

| Parte | O que sustenta | Situação |
|---|---|---|
| Ordem de entregar passaportes | nota da PF: representação em 25/10, intimação em 26/10, prazo de 24 horas não cumprido. A decisão não é pública: o conteúdo vem da nota. Flávio tinha imunidade até 31/01/2027 (art. 53), e a ADI 5526 do STF manda à Casa, em 24 horas, a medida que atrapalhe o mandato; se passaporte entra nisso é questão aberta | a ordem está descrita pela PF. A PF pediu 7 minutos depois da confirmação do TSE; a hora da decisão de Moraes não foi divulgada |
| A ponte | Migraciones: 22h50 e embarque às 23h30. Fantástico: 3 registros na van, 22h37, 22h40 e 23h11, com só o 1º válido | a passagem está confirmada; o horário tem conflito entre as fontes |
| Brasília até a ponte | Fantástico: linha de investigação com voo às 5h05 por Buenos Aires. Assessoria de Willer Tomaz nega | não resolvido |
| O jato | Baires Fly, LV-JQW, Guayaquil, Opa-locka. Dono à AFP: US$ 150 mil, de conta empresarial nos EUA, por corretor. Clarín, 28/10: empresas ligadas à embaixada americana contrataram | confirmado o voo; quem pagou, não |
| Jason Miller | Reuters; NYT e WSJ por resumos. Correio da Manhã, citando o Metrópoles, diz que ele confirmou; outra versão diz que não comentou | apurado pela Reuters e citado por outros; a confirmação dele tem conflito |
| Argentina | Migraciones e o chefe de Gabinete Santilli: entrada legal. Repórter da C5N viu escolta e placa diplomática. Clarín coloca Caputo no local. Ordem de Milei, jato-isca e SIDE em campo aparecem no Río Negro, e não no texto do Clarín de 28/10 | agentes argentinos estavam lá, por mais de uma fonte; quem ordenou tem uma fonte só |
| Homem apontado como ex-agente do Mossad | Fantástico e CNN Brasil | a presença tem duas fontes; não prova ação do Mossad |
| Entrada nos EUA | transcript do Departamento de Estado: *"He had previously held a visa"* e *"paroled"*. Registro DT, até 27/10/2027, obtido pela imprensa. Passaporte diplomático cancelado | parole confirmada; a data, só pelo registro |

## 3. O que aconteceu com quem esteve nesse lugar

{E2['n_casos']} casos desde 1945, duas passadas independentes. Concordância: {float(CONC['voltou_ao_poder']['concordancia']) * 100:.0f}% em quem voltou ao poder, {float(CONC['entregue']['concordancia']) * 100:.0f}% em quem foi entregue e {float(CONC['tipo']['concordancia']) * 100:.0f}% no tipo de caso. Lista em `resultados/e2_casos_final.csv`.

| Grupo | Casos | Voltaram ao país | Voltaram ao poder | Margem de 95% | Entregues |
|---|---|---|---|---|---|
| Abrigados nos EUA | {E2['eua']['n']} | {E2['eua']['voltou_ao_pais']} | **{E2['eua']['voltou_ao_poder']}** | {E2['eua']['ic95_poder'][0]}% a {E2['eua']['ic95_poder'][1]}% | {E2['eua']['entregue']} |
| Abrigados em outro país | {E2['comparacao']['n']} | {E2['comparacao']['voltou_ao_pais']} | **{E2['comparacao']['voltou_ao_poder']}** | {E2['comparacao']['ic95_poder'][0]}% a {E2['comparacao']['ic95_poder'][1]}% | {E2['comparacao']['entregue']} |
| Nos EUA, com apoio declarado de Washington | {E2['eua_com_apoio']['n']} | {E2['eua_com_apoio']['voltou_ao_pais']} | **{E2['eua_com_apoio']['voltou_ao_poder']}** | {E2['eua_com_apoio']['ic95_poder'][0]}% a {E2['eua_com_apoio']['ic95_poder'][1]}% | {E2['eua_com_apoio']['entregue']} |
| Mais parecidos: nos EUA, vindos de democracia, processados ou derrotados | {E2['parecidos']['n']} | {E2['parecidos']['voltou_ao_pais']} | **{E2['parecidos']['voltou_ao_poder']}** | {E2['parecidos']['ic95_poder'][0]}% a {E2['parecidos']['ic95_poder'][1]}% | {E2['parecidos']['entregue']} |

**Quanto tempo levou:** {tabela_anos} anos. Os casos ainda abertos pesam no denominador, então a taxa bruta subestima. A conta certa é por prazo, só com quem já teve aquele tempo de observação:

| Em até | Todos | Margem de 95% | Abrigados nos EUA |
|---|---|---|---|
{tabela_horizonte}

Só entre quem saiu até 2016, que já teve 10 anos: {rate(E2['maduros'])} no total e {rate(E2['maduros_eua'])} nos EUA. Sem Somoza e o xá, que não foram abrigados de fato: {rate(E2['eua_sem_nao_abrigados'])}. Seguem abertos {len(E2['ainda_abertos'])} casos, entre eles {', '.join(E2['ainda_abertos'][:6])}.

**O grupo volta mais que a pessoa.** Sem o próprio exilado, o grupo político chegou ao poder em {tabela_grupo}. Esses casos não aparecem como volta ao poder porque a pergunta é sobre o exilado.

**O que a regra escrita antes derrubou.** O plano dizia que a hipótese cairia se aparecessem abrigados nos EUA que voltaram ao poder sem força americana nem colapso. Apareceram: Kim Dae-jung, eleito, e Diem, nomeado. A frase inicial, *"abrigo americano não leva ao poder"*, caiu. Fica uma mais estreita: a porta aberta sozinha não foi caminho em prazo curto. Em até 4 anos só voltaram quem teve tropas americanas ou nomeação com apoio americano; por eleição, levou de 13 a 18 anos.

**A classe "mais parecidos" foi definida depois de ver os casos.** Dá {rate(E2['parecidos'])}. Tirando Jair, Eduardo e Ramagem, que são do mesmo grupo e estão abertos, {rate(E2['parecidos_fora_do_grupo'])}, com margem de {E2['parecidos_fora_do_grupo']['ic95_poder'][0]}% a {E2['parecidos_fora_do_grupo']['ic95_poder'][1]}%. Ricardo Anaya voltou e é senador: contando cargo nacional, 1 de 4. Serve de ilustração e não entra como conclusão.

**Apoio declarado muda com a codificação:** {E2['apoio_sensibilidade']['como_codificado']} como codificado; {E2['apoio_sensibilidade']['kim_entra_eduardo_sai']} com Kim Dae-jung e sem Eduardo; {E2['apoio_sensibilidade']['e_chalabi_conta']} se Chalabi, que presidiu por um mês o Conselho de Governo do Iraque, contar.

**Comparando com outro estudo:** Hidaka, Kubota e Yukawa olharam 91 líderes de 1970 a 2014: 58% voltaram ao país, e cerca de 11% do total voltou a chefiar o Estado, ordem parecida com os {round(E2['todos']['voltou_ao_poder'] * 100 / E2['todos']['n'])}% daqui. Lemos a versão de trabalho de 2022; o artigo de 2025 diz que a maioria volta e retoma o poder, e a diferença é o que cada um chama de poder.

**Teste do passado:** nota de Brier de {E2['brier_leave_one_out']} usando a taxa do grupo, {E2['brier_taxa_global_fora_um']} com a taxa geral e {E2['brier_taxa_unica']} com uma taxa única. Separar por grupo não ajudou: o que esse teste diz é que voltar ao poder é raro, e não que o abrigo muda alguma coisa.

## 4. Quando o preferido de Washington perde

{E3['n']} casos em que a preferência americana tem fonte; {E3['descartados']} descartados por falta dela, entre eles Brasil 2022. Hungria com janela parcial.

| Caso | Reconheceu | Sanção ou tarifa nova | Apoio a golpe ou oposição | Força | Relação em 12 meses |
|---|---|---|---|---|---|
{tabela_derrota}

**Brasil 2026, em aberto:** os governos falam, e Trump não felicitou Lula até aqui.

**Leitura:** o reconhecimento é a regra ({E3['reconheceu']} de {E3['n']}; na Hungria não localizamos felicitação formal). Força militar nos 12 meses seguintes: nenhuma nas fontes lidas, em {E3['n']} de {E3['n']}; muitos "não" são ausência de fonte. As duas rupturas foram Palestina 2006 e Venezuela 2024, e na Venezuela a captura de Maduro veio 17 meses depois da eleição, fora da janela. Chile 1970 mostra o mesmo: o golpe veio em 1973.

## 5. A escada contra o Brasil

{E4['n']} registros de jan/2025 a nov/2026. Medidas do governo americano dirigidas ao Brasil, para cima: **{E4['dirigidas_ao_brasil']}**, e a última é de 04/08/2026. Para baixo: **{E4['desce']}**. Militares: {E4['medidas_militares']}. Os outros registros que subiam a tensão ficam fora dessa conta: {E4['outras_que_subiam'].get('global', 0)} medidas globais, {E4['outras_que_subiam'].get('ato_do_brasil', 0)} atos do próprio Brasil, {E4['outras_que_subiam'].get('nomeacao', 0)} nomeações, {E4['outras_que_subiam'].get('fala_ou_evento', 0)} falas ou relatos e {E4['outras_que_subiam'].get('duplicata', 0)} repetida. A comparação com outros países não usa essa mesma regra e por isso não entra aqui.

**A conta da nova medida.** Em {E4['janelas_240d']} períodos de 240 dias desde jul/2025, {br(E4['janelas_240d_com_medida_pct'])}% tiveram ao menos uma medida dirigida; mas houve 248 dias seguidos sem nenhuma, de set/2025 a mai/2026, e elas vêm em surtos. A pergunta P08 é a mesma janela. Os modelos deram {pct('P08')}.

- **Sobe e desce:** a Magnitsky de Moraes durou de 30/07 a 12/12/2025. A tarifa de 40% caiu em 20/02/2026 pela Suprema Corte americana, e não por acordo.
- **Hoje:** 25% pela Seção 301 desde 22/07/2026, mais 12,5% da ação global sobre cerca de 60 economias. Dos US$ {br(TAR['total_importado_2024_us_bi'])} bi que os EUA compraram do Brasil em 2024, US$ {br(TAR['paga_25_cheio_us_bi'])} bi pagam os 25% cheios, pelas medidas lidas.
- **Literatura:** sanções dão certo em cerca de um terço dos casos (Hufbauer et al.), e Pape conta 5 de 115. Mudar regime: 29 de 90. EUA sozinhos, de 1970 a 2014: 11 de 54. Metas limitadas e alvos democráticos rendem mais.
- **O efeito aqui:** a Reuters diz que analistas veem várias das medidas como contraproducentes, e parte ajudou a popularidade de Lula.

## 6. Os EUA vão usar a força?

**Base do medo, tudo real:** captura de Maduro; Trump na ONU em 22/09; vídeo da Doutrina Monroe; PCC e CV designados; ofício do Itamaraty de 01/07 falando em *"possibilidade do uso da força militar"*; ministro Múcio em 04/08, em tom de brincadeira; 1964 e a Brother Sam, navios prontos e nunca usados.

**Negativa:** o Departamento de Estado disse que a lei da designação não contempla ação militar. ⚠️ Trump negou ataque à Venezuela 64 dias antes da captura, então negativa sozinha não encerra.

**Tamanho:** no hemisfério, o maior alvo sem aval foi {E5['maior_alvo_sem_aval']['pais']}, {br(E5['maior_alvo_sem_aval']['pop_mi'])} milhões; o Brasil tem {E5['brasil_pop_mi']} milhões. Fora do hemisfério a comparação encurta: os EUA estão em guerra com o Irã desde fev/2026, com 87 milhões de habitantes pela estimativa da Wikipedia, e o Brasil tem 2,5 vezes isso. O tamanho foi escolhido depois de ver os casos e não é teto: é uma razão de custo.

**O tempo dos sinais.** A designação veio {E5['dias_antes_da_captura']['designacao']} dias antes da captura de Maduro, a mobilização naval {E5['dias_antes_da_captura']['mobilizacao_naval']}, o ataque a barcos {E5['dias_antes_da_captura']['ataque_barcos']}, a FAA e o ultimato {E5['dias_antes_da_captura']['ultimato']}. O Brasil tem a designação há 5 meses. Comparado no mesmo relógio, parece a Venezuela do começo de 2025, e os sinais ausentes são os que vieram depois. Isso diz o que olhar, sem virar probabilidade: México, Colômbia e Cuba têm parte desses sinais sem captura, e a taxa de falso alarme não é conhecida.

**Sinais, um por um** (*"não"* é ausência nas páginas abertas, e não prova):

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

Matriz de hipóteses concorrentes (Heuer), `dados/e6_hipoteses.csv`. É julgamento, não medida, e não aponta vencedor: motivo é intenção, e intenção não se lê de fora. São {E6['n_evidencias']} evidências, separadas em duas perguntas, porque explicar a entrada e explicar a fala de Trump não são a mesma coisa. Cada célula traz a favor e contra.

| Hipótese | Sobre a entrada | Sobre a fala de Trump | Soma na 2ª codificação, feita às cegas |
|---|---|---|---|
{tabela_h}

Concordância entre as duas codificações: {br(E6['concordancia_segunda_codificacao_pct'])}% das células, a maioria delas zeros.

**Leitura:** a retórica de fraude conversa com as eleições americanas: Trump ligou o Brasil à fraude dos democratas no comício do Texas, na semana da votação. A entrada não se resolve assim: lealdade, convicção declarada de perseguição e a aposta de quem recomendou estão misturadas, e nas falas oficiais a palavra usada para justificar é tratamento injusto. Minerais e China explicam o interesse no Brasil, e os EUA já têm posição com Lula no governo. Nenhuma fala oficial sobre a entrada cita minerais; Dino abriu inquérito em 27/10, a pedido do PT, sobre suspeita de troca de apoio por terras raras, e inquérito não prova irregularidade.

## 8. O que muda no Brasil

| Indicador | Número | Fonte |
|---|---|---|
| Exportações aos EUA, jan a set/2026 | US$ {EUA_X['2026']} bi, {br(EUA_X['variacao_pct'])}% | ComexStat |
| Exportações à China, jan a set/2026 | US$ {CHI_X['2026']} bi, +{br(CHI_X['variacao_pct'])}% | ComexStat |
| Dólar PTAX, 23/10 e 30/10 | R$ {br(DOL['23/10'])} e R$ {br(DOL['30/10'])}, +{br(DOL['alta_23_a_30_pct'])}% | Banco Central |
| Ibovespa na semana | {br(IBOV['ibov_queda_semana_pct'])}% de queda | imprensa, ver `dados/casos/e8_brasil.json` |

⚠️ O mercado reagiu à reeleição e ao quadro fiscal, e não dá para atribuir isso ao caso Flávio.

| Cenário | Efeito |
|---|---|
| A pressão longa | exportador para os EUA segue com tarifa; o comércio continua indo para a China |
| O acordo | alívio de tarifa e minerais com refino; custo político dos dois lados |
| A escalada | risco em banco e fintech; câmbio mais volátil |

## 9. O que esperar

**Como ler:** são modelos da mesma empresa, com o mesmo texto, e a concordância entre eles não é confirmação independente. Abaixo de 5%, o número é mais o piso que eles usam do que uma medida: a invasão fica entre 1% e 2% com ou sem a história. A condição "com a história" é a mesma IA depois de ler o levantamento, e não um segundo olhar.

**Cenários até o fim de 2027** (mediana de {len(E7['modelos'])} modelos, depois de ver a história; somados a 100):

| Cenário | O que é | Chance | Menor a maior |
|---|---|---|---|
{tabela_cen}

**As perguntas, para conferir na data** (`dados/previsoes/`):

| # | Pergunta | Prazo | Com a história | Entre modelos | Sem a história |
|---|---|---|---|---|---|
{tabela_prev}

**O que a história mudou nas IAs:** em média, {br(E7['mudanca_media_absoluta'])} pontos. Nova medida contra o Brasil: de {br(PQ['P08']['sem_historia'])}% para {br(PQ['P08']['com_historia'])}%. Na invasão: de {br(PQ['P01']['sem_historia'])}% para {br(PQ['P01']['com_historia'])}%. Discordância média entre modelos: {br(E7['discordancia_media_entre_modelos'])} pontos. Da rodada 1 para a 2, com o texto corrigido: {E7['mudancas_rodada1'].strip()}.

**Datas:** 03/nov midterms · 13/nov prazo de Rubio · nov G7 · 14 e 15/dez G20 · até 18/dez diplomação · 05/jan posse · 31/jan fim do mandato · 27/out/2027 fim da parole.

## 10. O que circula

{chr(10).join(f"- **{l['afirmacao']}** ({l['canal']}): {l['o_que_e_real']}." for l in csv.DictReader((RAIZ / 'dados' / 'e9_o_que_circula.csv').open(encoding='utf-8')))}

## 11. Validação

- Citações: {cit}.
- Aritmética: {val_ok} de {len(VAL)} contas refeitas por outro caminho, em `resultados/validacao_independente.csv`, com os exilados recontados sobre a 2ª passada. Isso confere a conta, e não o julgamento de quem entrou em cada grupo.
- Revisão por 3 leitores: `docs/REVISAO_ADVERSARIAL.md`.

Refazer: `docs/REPLICAR.md`.
"""

SIMPLES = f"""# Resumo simples

**A pergunta:** depois da ida do Flávio para os EUA, o que esperar?

**Como:** a IA leu as fontes, montou {E2['n_casos']} casos de exilados desde 1945, {E3['n']} casos em que o preferido de Washington perdeu, {E5['n']} usos de força americana no continente e {E4['n']} registros de medidas e atos entre os dois países. Depois {len(E7['modelos'])} modelos responderam {len(E7['perguntas'])} perguntas, separados e com data.

**O que aconteceu:** Trump decidiu deixar ele entrar, e Rubio disse isso em público ao mesmo tempo em que disse *"não facilitamos nada"*. O jato liga a um assessor de Trump pela Reuters. A saída do Brasil não tem prova de participação do governo americano. Não há registro de asilo: é parole humanitária. A PF diz que as restrições, por si só, não fazem dele foragido, e ele nega as acusações.

**O que a história diz:** dos {E2['eua']['n']} abrigados nos EUA, {E2['eua']['voltou_ao_poder']} chegaram ao poder. Em até 12 anos, só Diem e Aristide, um nomeado com apoio americano e outro com tropas. Por eleição, levou de 13 a 18 anos. A frase "abrigo não leva ao poder" caiu pela regra escrita antes: Kim Dae-jung foi eleito. O que fica: a porta aberta não é caminho rápido, e muitas vezes quem volta é o grupo, sem a pessoa.

**Vão invadir?** Tropas sem autorização: {pct('P01')} até 2030. Ataque contra facção sem aval: {pct('P20')} até o fim do governo Trump. Dos {E5['tipos_de_sinal']} tipos de sinal que vieram antes de Maduro, {E5['sinais_brasil']['nao']} não aparecem hoje, mas os que existem são os primeiros da fila. O risco mais próximo é econômico: tarifa, visto e banco.

**O que esperar:** {CE['C1']['cenario'].lower()} ({CE['C1']['com_historia_normalizado']:.0f}%), {CE['C2']['cenario'].lower()} ({CE['C2']['com_historia_normalizado']:.0f}%), {CE['C3']['cenario'].lower()} ({CE['C3']['com_historia_normalizado']:.0f}%), {CE['C4']['cenario'].lower()} ({CE['C4']['com_historia_normalizado']:.0f}%).

**O limite:** amostra pequena; Trump muda de ideia; as IAs são todas da mesma empresa. As previsões ficaram registradas para serem cobradas.

Completo: [`RELATORIO.md`](RELATORIO.md).
"""

LEITURA = f"""# Leitura da IA

Esta é a opinião da análise, separada dos fatos.

1. **Trump usa o caso mais do que aposta nele.** Fala de fraude, abre a porta e não dá o passo seguinte. Em seis dias, as falas não trouxeram prova nem ato além da parole.
2. **A palavra mais importante do caso é "directly".** Rubio disse *"We didn't facilitate anything"* e corrigiu para *"At least the U.S. Government was not involved directly"*. A distinção entre governo e pessoas do entorno é onde mora a resposta das 15 perguntas dos democratas.
3. **A data que importa para o Flávio é 31/01/2027.** Até lá, o art. 53 protege. Depois, prisão e pedido de extradição ficam mais fáceis. O tratado não nomeia lavagem nem evasão e nomeia suborno e peculato, o que me leva a achar, por inferência, que o caso Dark Horse pesa mais que o outro. Com Trump, a entrega é muito improvável; o risco dele é o próximo governo americano.
4. **O risco para o Brasil é o banco, não o fuzileiro.** A designação de PCC e CV é o instrumento com mais alcance e menos debate.
5. **O medo da invasão não é tolo, e tropa em território é a forma menos provável dele.** O Brasil tem governo reconhecido pelo mundo, superávit americano e um tamanho que encarece qualquer operação. O caminho menos improvável é um ataque pontual contra facção, sem aval, e a comparação honesta com a Venezuela é com o começo de 2025. A lista de sinais é o que eu olharia.
6. **A minha hipótese inicial caiu.** Eu tinha escrito que abrigo americano não leva ao poder, e a regra que eu mesmo escrevi antes derrubou isso: Kim Dae-jung foi eleito e Diem foi nomeado. O que ficou é mais estreito: Trump abriu a porta, e a porta não é caminho. Em prazo curto, só voltou quem teve tropa ou nomeação. Flávio diz que volta antes de 2030, e a base não tem nenhum caso de eleição em menos de 13 anos.
"""

RELATORIO = re.sub(r"(\d)\.(\d+%)", r"\1,\2", RELATORIO)
(RAIZ / "RELATORIO.md").write_text(RELATORIO, encoding="utf-8")
(RAIZ / "RESUMO_SIMPLES.md").write_text(SIMPLES, encoding="utf-8")
(RAIZ / "docs" / "LEITURA_DA_IA.md").write_text(LEITURA, encoding="utf-8")
print(len(RELATORIO), len(SIMPLES), len(LEITURA))
