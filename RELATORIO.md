# Flávio nos EUA: o que esperar

**Lido até 2026-11-02.** Análise feita pelo Claude (Anthropic), a pedido de Gabriel Alexandre. As previsões entraram em commit em 02/nov/2026, antes das eleições americanas de 03/nov. A rodada 1 fica congelada em `dados/previsoes/rodada1/`; este relatório usa a rodada 2, feita depois da revisão adversarial, com o texto corrigido.

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
| Volta ao poder por esse caminho? | Dos 22 abrigados nos EUA, 3 chegaram ao poder: um com tropas americanas, um nomeado com apoio americano e um eleito depois de 15 anos. Em até 12 anos, 2 de 25 entre todos, e nenhum por eleição. Flávio fala em voltar antes de 2030 |
| Os EUA vão invadir? | Tropas sem autorização até 2030: 1,75%. Ataque contra PCC ou CV sem aval: 2,5% até 2027 e 4% até o fim do governo Trump. Dos 16 tipos de sinal que vieram antes da captura de Maduro, 3 existem hoje, 5 em parte e 8 não, e os que existem são os mais antigos da sequência |
| O que é mais provável? | **A pressão longa** (57%), e alguma medida americana nova até junho de 2027 (70%); sanção nominal a autoridade, 14,5%; banco brasileiro atingido, 11% |

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

39 casos desde 1945, duas passadas independentes. Concordância: 100% em quem voltou ao poder, 100% em quem foi entregue e 80% no tipo de caso. Lista em `resultados/e2_casos_final.csv`.

| Grupo | Casos | Voltaram ao país | Voltaram ao poder | Margem de 95% | Entregues |
|---|---|---|---|---|---|
| Abrigados nos EUA | 22 | 11 | **3** | 4,7% a 33,3% | 3 |
| Abrigados em outro país | 17 | 10 | **3** | 6,2% a 41,0% | 1 |
| Nos EUA, com apoio declarado de Washington | 6 | 4 | **2** | 9,7% a 70,0% | 0 |
| Mais parecidos: nos EUA, vindos de democracia, processados ou derrotados | 7 | 4 | **0** | 0% a 35,4% | 2 |

**Quanto tempo levou:** Jean-Bertrand Aristide em 3, Ngo Dinh Diem em 4, Nawaz Sharif em 13, Kim Dae-jung em 15, Ruhollah Khomeini em 15, Juan Domingo Perón em 18 anos. Os casos ainda abertos pesam no denominador, então a taxa bruta subestima. A conta certa é por prazo, só com quem já teve aquele tempo de observação:

| Em até | Todos | Margem de 95% | Abrigados nos EUA |
|---|---|---|---|
| 4 anos | 2 de 34 | 1,6% a 19,1% | 2 de 18 |
| 8 anos | 2 de 29 | 1,9% a 22,0% | 2 de 16 |
| 12 anos | 2 de 25 | 2,2% a 25,0% | 2 de 14 |

Só entre quem saiu até 2016, que já teve 10 anos: 6 de 27 no total e 3 de 15 nos EUA. Sem Somoza e o xá, que não foram abrigados de fato: 3 de 20. Seguem abertos 12 casos, entre eles Alejandro Toledo, Juan Guaidó, María Corina Machado, Jair Bolsonaro, Eduardo Bolsonaro, Alexandre Ramagem.

**O grupo volta mais que a pessoa.** Sem o próprio exilado, o grupo político chegou ao poder em Benigno Aquino Jr. (1986), Benazir Bhutto (2008), Thaksin Shinawatra (2011), Evo Morales (2020), Ferdinand Marcos (2022), Manuel Zelaya (2022), Alberto Fujimori (2026). Esses casos não aparecem como volta ao poder porque a pergunta é sobre o exilado.

**O que a regra escrita antes derrubou.** O plano dizia que a hipótese cairia se aparecessem abrigados nos EUA que voltaram ao poder sem força americana nem colapso. Apareceram: Kim Dae-jung, eleito, e Diem, nomeado. A frase inicial, *"abrigo americano não leva ao poder"*, caiu. Fica uma mais estreita: a porta aberta sozinha não foi caminho em prazo curto. Em até 4 anos só voltaram quem teve tropas americanas ou nomeação com apoio americano; por eleição, levou de 13 a 18 anos.

**A classe "mais parecidos" foi definida depois de ver os casos.** Dá 0 de 7. Tirando Jair, Eduardo e Ramagem, que são do mesmo grupo e estão abertos, 0 de 4, com margem de 0% a 49,0%. Ricardo Anaya voltou e é senador: contando cargo nacional, 1 de 4. Serve de ilustração e não entra como conclusão.

**Apoio declarado muda com a codificação:** 2 de 6 como codificado; 3 de 6 com Kim Dae-jung e sem Eduardo; 4 de 6 se Chalabi, que presidiu por um mês o Conselho de Governo do Iraque, contar.

**Comparando com outro estudo:** Hidaka, Kubota e Yukawa olharam 91 líderes de 1970 a 2014: 58% voltaram ao país, e cerca de 11% do total voltou a chefiar o Estado, ordem parecida com os 15% daqui. Lemos a versão de trabalho de 2022; o artigo de 2025 diz que a maioria volta e retoma o poder, e a diferença é o que cada um chama de poder.

**Teste do passado:** nota de Brier de 0.144 usando a taxa do grupo, 0.137 com a taxa geral e 0.13 com uma taxa única. Separar por grupo não ajudou: o que esse teste diz é que voltar ao poder é raro, e não que o abrigo muda alguma coisa.

## 4. Quando o preferido de Washington perde

9 casos em que a preferência americana tem fonte; 11 descartados por falta dela, entre eles Brasil 2022. Hungria com janela parcial.

| Caso | Reconheceu | Sanção ou tarifa nova | Apoio a golpe ou oposição | Força | Relação em 12 meses |
|---|---|---|---|---|---|
| chile-1970 | sim | sim | sim | nao | fria |
| haiti-1990 | sim | nao | nao | nao | normal |
| israel-1996 | sim | nao | nao | nao | normal |
| palestina-2006 | sim | sim | sim | nao | ruptura |
| nicaragua-2006 | sim | nao | nao | nao | normal |
| argentina-2019 | sim | nao | nao | nao | normal |
| venezuela-2024 | nao | sim | sim | nao | ruptura |
| alemanha-2025 | sim | nao | nao | nao | fria |
| hungria-2026 | sim | nao | nao | nao | normal |

**Brasil 2026, em aberto:** os governos falam, e Trump não felicitou Lula até aqui.

**Leitura:** o reconhecimento é a regra (8 de 9; na Hungria não localizamos felicitação formal). Força militar nos 12 meses seguintes: nenhuma nas fontes lidas, em 9 de 9; muitos "não" são ausência de fonte. As duas rupturas foram Palestina 2006 e Venezuela 2024, e na Venezuela a captura de Maduro veio 17 meses depois da eleição, fora da janela. Chile 1970 mostra o mesmo: o golpe veio em 1973.

## 5. A escada contra o Brasil

33 registros de jan/2025 a nov/2026. Medidas do governo americano dirigidas ao Brasil, para cima: **11**, e a última é de 04/08/2026. Para baixo: **7**. Militares: 0. Os outros registros que subiam a tensão ficam fora dessa conta: 3 medidas globais, 4 atos do próprio Brasil, 2 nomeações, 5 falas ou relatos e 1 repetida. A comparação com outros países não usa essa mesma regra e por isso não entra aqui.

**A conta da nova medida.** Em 250 períodos de 240 dias desde jul/2025, 97,2% tiveram ao menos uma medida dirigida; mas houve 248 dias seguidos sem nenhuma, de set/2025 a mai/2026, e elas vêm em surtos. A pergunta P08 é a mesma janela. Os modelos deram 70%.

- **Sobe e desce:** a Magnitsky de Moraes durou de 30/07 a 12/12/2025. A tarifa de 40% caiu em 20/02/2026 pela Suprema Corte americana, e não por acordo.
- **Hoje:** 25% pela Seção 301 desde 22/07/2026, mais 12,5% da ação global sobre cerca de 60 economias. Dos US$ 39,6 bi que os EUA compraram do Brasil em 2024, US$ 8,5 bi pagam os 25% cheios, pelas medidas lidas.
- **Literatura:** sanções dão certo em cerca de um terço dos casos (Hufbauer et al.), e Pape conta 5 de 115. Mudar regime: 29 de 90. EUA sozinhos, de 1970 a 2014: 11 de 54. Metas limitadas e alvos democráticos rendem mais.
- **O efeito aqui:** a Reuters diz que analistas veem várias das medidas como contraproducentes, e parte ajudou a popularidade de Lula.

## 6. Os EUA vão usar a força?

**Base do medo, tudo real:** captura de Maduro; Trump na ONU em 22/09; vídeo da Doutrina Monroe; PCC e CV designados; ofício do Itamaraty de 01/07 falando em *"possibilidade do uso da força militar"*; ministro Múcio em 04/08, em tom de brincadeira; 1964 e a Brother Sam, navios prontos e nunca usados.

**Negativa:** o Departamento de Estado disse que a lei da designação não contempla ação militar. ⚠️ Trump negou ataque à Venezuela 64 dias antes da captura, então negativa sozinha não encerra.

**Tamanho:** no hemisfério, o maior alvo sem aval foi Venezuela, 28,52 milhões; o Brasil tem 214 milhões. Fora do hemisfério a comparação encurta: os EUA estão em guerra com o Irã desde fev/2026, com 87 milhões de habitantes pela estimativa da Wikipedia, e o Brasil tem 2,5 vezes isso. O tamanho foi escolhido depois de ver os casos e não é teto: é uma razão de custo.

**O tempo dos sinais.** A designação veio 348 dias antes da captura de Maduro, a mobilização naval 137, o ataque a barcos 123, a FAA e o ultimato 43. O Brasil tem a designação há 5 meses. Comparado no mesmo relógio, parece a Venezuela do 1º semestre de 2025, e os sinais ausentes são os que vieram depois. Isso diz o que olhar, sem virar probabilidade: México, Colômbia e Cuba têm parte desses sinais sem captura, e a taxa de falso alarme não é conhecida.

**Sinais, um por um** (*"não"* é ausência nas páginas abertas, e não prova):

| Tipo de sinal antes de Maduro | Brasil hoje |
|---|---|
| designacao de organizacoes criminosas como terroristas | existe |
| designacao do governo ou do chefe de Estado, acusacao formal e recompensa | nao |
| sancoes, tarifas e punicao diplomatica | existe |
| mobilizacao naval ou aerea perto do pais | nao |
| tropas terrestres na regiao | parcial |
| comando operacional dedicado, com sede em Miami | parcial |
| coalizao regional com acordos de operacoes conjuntas | nao |
| fala do presidente ameacando usar a forca | parcial |
| oficio ou alerta do governo alvo e negativa do governo dos EUA | existe |
| declaracao do Departamento de Defesa (Guerra) sobre o pais | nao |
| ataques a embarcacoes ou alvos em territorio do pais | nao |
| embaixada em crise: fechamento, evacuacao, sem chefe | parcial |
| aviso a aviacao ou fechamento de espaco aereo | nao |
| autorizacao publica de operacoes da CIA no pais | nao |
| ultimato direto ao chefe de governo | nao |
| base juridica interna para usar a forca contra grupos designados | parcial |

**O que mudaria a resposta:** navios e aviões perto da costa; aviso da FAA; acusação formal contra autoridade do governo; ultimato; autorização pública à CIA; coalizão com vizinhos sobre o Brasil.

**O risco mais realista, sem tropa:** a designação alcança banco. White & Case diz que medidas contra um banco brasileiro dependente de dólar *"could be existential"*.

<details><summary>Tabela da força no hemisfério</summary>

| Ano | País | Tipo | População (mi) | Aval local |
|---|---|---|---|---|
| 1954 | Guatemala | encoberta | 3.52 | nao |
| 1961 | Cuba | encoberta | 7.29 | nao |
| 1962 | Cuba | bloqueio | 7.45 | nao |
| 1964 | Brasil | contingencia | 84.13 | nao |
| 1965 | República Dominicana | invasao | 3.9 | parcial |
| 1973 | Chile | encoberta | 10.08 | nao |
| 1981 | Nicarágua | encoberta | 3.71 | nao |
| 1983 | Granada | invasao | 0.089 | nao |
| 1989 | Panamá | invasao | 2.41 | nao |
| 1994 | Haiti | conjunta_com_aval | 7.49 | sim |
| 2004 | Haiti | operacao_limitada | 8.96 | incerto |
| 1986 | Bolívia | conjunta_com_aval | 6.04 | sim |
| 2025 | Venezuela | bloqueio | 28.52 | nao |
| 2026 | Venezuela | operacao_limitada | 28.52 | nao |
| 2025 | Caribe e Pacífico Oriental (barcos) | operacao_limitada | não se aplica | nao |
| 2026 | Equador | conjunta_com_aval | 18.16 | sim |
| 2026 | Guatemala | conjunta_com_aval | 18.08 | incerto |
| 2026 | Cuba | bloqueio | 9.44 | nao |

</details>

## 7. Por que receber o Flávio

Matriz de hipóteses concorrentes (Heuer), `dados/e6_hipoteses.csv`. É julgamento, não medida, e não aponta vencedor: motivo é intenção, e intenção não se lê de fora. São 21 evidências, separadas em duas perguntas, porque explicar a entrada e explicar a fala de Trump não são a mesma coisa. Cada célula traz a favor e contra.

| Hipótese | Sobre a entrada | Sobre a fala de Trump | Soma na 2ª codificação, feita às cegas |
|---|---|---|---|
| Narrativa política e eleições nos EUA | 1 e 1 | 3 e 0 | 3 e 1 |
| China e influência no hemisfério | 3 e 1 | 0 e 0 | 1 e 1 |
| Terras raras | 2 e 3 | 0 e 0 | 1 e 3 |
| Lealdade aos Bolsonaro | 3 e 2 | 2 e 2 | 3 e 4 |
| Aposta pessoal de Rubio e entorno | 2 e 2 | 0 e 2 | 3 e 0 |
| Convicção declarada de perseguição e proteção | 3 e 3 | 2 e 1 | 3 e 1 |

Concordância entre as duas codificações: 85,7% das células, a maioria delas zeros.

**Leitura:** a retórica de fraude conversa com as eleições americanas: Trump ligou o Brasil à fraude dos democratas no comício do Texas, na semana da votação. A entrada não se resolve assim: lealdade, convicção declarada de perseguição e a aposta de quem recomendou estão misturadas, e nas falas oficiais a palavra usada para justificar é tratamento injusto. Minerais e China explicam o interesse no Brasil, e os EUA já têm posição com Lula no governo. Nenhuma fala oficial sobre a entrada cita minerais; Dino abriu inquérito em 27/10, a pedido do PT, sobre suspeita de troca de apoio por terras raras, e inquérito não prova irregularidade.

## 8. O que muda no Brasil

| Indicador | Número | Fonte |
|---|---|---|
| Exportações aos EUA, jan a set/2026 | US$ 27.46 bi, -6,5% | ComexStat |
| Exportações à China, jan a set/2026 | US$ 84.68 bi, +12% | ComexStat |
| Dólar PTAX, 23/10 e 30/10 | R$ 5,0377 e R$ 5,4212, +7,6% | Banco Central |
| Ibovespa na semana | 18,12% de queda | imprensa, ver `dados/casos/e8_brasil.json` |

⚠️ O mercado reagiu à reeleição e ao quadro fiscal, e não dá para atribuir isso ao caso Flávio.

| Cenário | Efeito |
|---|---|
| A pressão longa | exportador para os EUA segue com tarifa; o comércio continua indo para a China |
| O acordo | alívio de tarifa e minerais com refino; custo político dos dois lados |
| A escalada | risco em banco e fintech; câmbio mais volátil |

## 9. O que esperar

**Como ler:** são modelos da mesma empresa, com o mesmo texto, e a concordância entre eles não é confirmação independente. Abaixo de 5%, o número é mais o piso que eles usam do que uma medida: a invasão fica entre 1% e 2% com ou sem a história. A condição "com a história" é a mesma IA depois de ler o levantamento, e não um segundo olhar.

**Cenários até o fim de 2027** (mediana de 4 modelos, depois de ver a história; somados a 100):

| Cenário | O que é | Chance | Menor a maior |
|---|---|---|---|
| **A pressão longa** | Flávio nos EUA sem poder; posse normal; tarifa e visto como moeda; conversa intermitente; sem ruptura e sem acordo amplo até o fim de 2027 | **57%** | 48 a 60 |
| **O acordo** | Trump e Lula negociam: tarifa e minerais em troca do embaixador e de cooperação; Flávio perde importância para Washington | **19%** | 18 a 25 |
| **A escalada** | Nova sanção forte, bancos atingidos pela designação ou ação sobre o Pix na linha da Seção 301, autoridades de volta à lista, prisão decretada com recusa americana; sem ação militar | **22%** | 20 a 24 |
| **A força** | Ação militar americana em território brasileiro sem aval do Brasil | **3%** | 2 a 5 |

**As perguntas, para conferir na data** (`dados/previsoes/`):

| # | Pergunta | Prazo | Com a história | Entre modelos | Sem a história |
|---|---|---|---|---|---|
| P24 | O STF toma medida nova contra cidadão, empresa ou plataforma americana | 2027-06-30 | **78,5%** (provável) | 50 a 88 | 66% |
| P07 | Lula toma posse e os EUA mandam representante à cerimônia | 2027-01-05 | **76,5%** (provável) | 55 a 78 | 70% |
| P08 | O governo dos EUA anuncia nova medida contra autoridade setor ou economia do Brasil | 2027-06-30 | **70%** (provável) | 62 a 80 | 62,5% |
| P15 | Flávio segue nos EUA com autorização renovada residência ou asilo depois da parole | 2027-10-27 | **64%** (provável) | 45 a 72 | 65% |
| P06 | Lula participa presencialmente da cúpula do G20 em Doral | 2026-12-15 | **56%** (provável) | 45 a 65 | 55% |
| P05 | Trump e Lula conversam por telefone ou se encontram | 2026-12-15 | **44%** (improvável) | 25 a 50 | 40% |
| P17 | Flávio lidera entre os nomes da direita numa pesquisa nacional para 2030 | 2027-12-31 | **40%** (improvável) | 17 a 55 | 39% |
| P12 | O STF decreta a prisão de Flávio Bolsonaro | 2027-06-30 | **39%** (improvável) | 25 a 55 | 37,5% |
| P10 | O Brasil concede agrément a Danny Perez como embaixador dos EUA | 2027-06-30 | **34%** (improvável) | 30 a 35 | 32,5% |
| P18 | Câmara dos EUA faz audiência pública com o caso Flávio Bolsonaro entre os temas | 2027-06-30 | **28,5%** (improvável) | 22 a 45 | 18,5% |
| P13 | O Brasil pede formalmente a extradição de Flávio Bolsonaro | 2027-12-31 | **26%** (improvável) | 20 a 35 | 19,5% |
| P09 | Os EUA reduzem a tarifa de 25% da Seção 301 contra o Brasil | 2027-06-30 | **22,5%** (improvável) | 18 a 30 | 26% |
| P16 | Flávio volta ao Brasil | 2028-12-31 | **16%** (muito improvável) | 6 a 30 | 18,5% |
| P11 | Brasil e EUA assinam acordo governamental sobre minerais críticos | 2027-12-31 | **15%** (muito improvável) | 13 a 17 | 17% |
| P21 | Os EUA aplicam sanção nominal nova (Magnitsky ou parecida) a autoridade brasileira | 2027-06-30 | **14,5%** (muito improvável) | 12 a 30 | 17% |
| P22 | Banco brasileiro é sancionado pelos EUA ou punido por ligação com PCC ou CV | 2027-06-30 | **11%** (muito improvável) | 7 a 25 | 9% |
| P04 | Trump se reúne em público com Flávio Bolsonaro | 2027-03-31 | **10%** (muito improvável) | 6 a 22 | 15% |
| P19 | Departamento de Estado responde publicamente às 15 perguntas dos 25 democratas | 2026-12-31 | **9,5%** (muito improvável) | 6 a 25 | 11% |
| P23 | O Brasil aplica medida concreta com base na Lei da Reciprocidade contra os EUA | 2027-06-30 | **7%** (muito improvável) | 6 a 15 | 7,5% |
| P20 | Os EUA fazem ataque militar em solo ou águas territoriais brasileiras contra PCC ou Comando Vermelho sem aval do Brasil | 2029-01-20 | **4%** (quase nenhuma chance) | 3 a 8 | 5% |
| P02 | Os EUA fazem ataque militar em solo ou águas territoriais brasileiras contra PCC ou Comando Vermelho sem aval do Brasil | 2027-12-31 | **2,5%** (quase nenhuma chance) | 1,5 a 5 | 2,75% |
| P01 | Tropas americanas entram em território brasileiro sem autorização do governo do Brasil | 2030-12-31 | **1,75%** (quase nenhuma chance) | 1 a 3,5 | 1% |
| P03 | O governo dos EUA reconhece Flávio Bolsonaro como presidente ou líder legítimo do Brasil | 2027-01-05 | **1,5%** (quase nenhuma chance) | 0,7 a 4 | 1,5% |
| P14 | Os EUA entregam Flávio Bolsonaro ao Brasil | 2027-12-31 | **1,25%** (quase nenhuma chance) | 0,6 a 2 | 1% |

**O que a história mudou nas IAs:** em média, 3,1 pontos. Nova medida contra o Brasil: de 62,5% para 70%. Na invasão: de 1% para 1,75%. Discordância média entre modelos: 16,6 pontos. Da rodada 1 para a 2, com o texto corrigido: P07 de 66,5% para 76,5%, P19 de 16% para 9,5%, P05 de 50% para 44%.

**Datas:** 03/nov midterms · 13/nov prazo de Rubio · nov G7 · 14 e 15/dez G20 · até 18/dez diplomação · 05/jan posse · 31/jan fim do mandato · 27/out/2027 fim da parole.

## 10. O que circula

- **Trump e a ordem para invadir o Brasil** (Lupa Política): O próprio vídeo diz que não há evidência pública de plano; o ofício do Itamaraty é real, e o Departamento de Estado negou.
- **Trump manda 600 soldados para a porta do Brasil** (Milson Alves - Brasil): NYT: cerca de 600 em treino no Panamá, Colômbia e Honduras; Task & Purpose: 500; embaixada no Panamá nega os 600 e diz 120.
- **Flávio recebe aviso de deportação e Trump vira as costas** (Análise Política): Fala de candidato democrata do Texas, não ordem; Trump disse que pode ficar; sem planos de encontrar é real.
- **Casa Branca assume comando da operação** (Jovem Pan 3 em 1): Apuração de um correspondente; Rubio e Trump decidiram a entrada; comando da saída sem segunda fonte.
- **A PF pediu a medida 7 minutos depois da confirmação do TSE** (Cartas e falas do Flávio): Real pela nota e pelos horários: pedido assinado às 21h16, 7 minutos depois da confirmação matemática; a hora da decisão de Moraes não foi divulgada.
- **Os números do TSE são matematicamente impossíveis** (Cartas e falas do Flávio): Alegação sem prova apresentada até aqui; a contagem foi testada nos vídeos da Investigação Aberta.
- **Saiu porque é perseguido pelo Judiciário** (Cartas e falas do Flávio): A entrevista é dele e a acusação de perseguição é opinião; há inquéritos e ele nega; art. 53 e ADI 5526 dão base para questionar a medida, sem decisão sobre isso.

## 11. Validação

- Citações: 850 trechos: 766 achados na página capturada, 19 com diferença pequena de redação, 23 são respostas de API, 38 em páginas que recusam o robô (quase todas da Britannica, usada na 2ª passada) e 4 não achados, listados em `resultados/citacoes.csv`.
- Aritmética: 38 de 38 contas refeitas por outro caminho, em `resultados/validacao_independente.csv`, com os exilados recontados sobre a 2ª passada. Isso confere a conta, e não o julgamento de quem entrou em cada grupo.
- Revisão por 3 leitores: `docs/REVISAO_ADVERSARIAL.md`.

Refazer: `docs/REPLICAR.md`.
