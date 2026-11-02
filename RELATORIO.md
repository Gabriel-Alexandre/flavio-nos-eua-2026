# Flávio nos EUA: o que esperar

**Lido até 2026-11-02.** Análise feita pelo Claude (Anthropic), a pedido de Gabriel Alexandre. As previsões entraram em commit em 02/nov/2026, antes das eleições americanas de 03/nov.

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
| Volta ao poder por esse caminho? | Dos 22 abrigados nos EUA, 3 voltaram; dos 7 mais parecidos com ele, 0 |
| Os EUA vão invadir? | 2% até 2030, a faixa mais baixa da escala. Dos 16 tipos de sinal que vieram antes da captura de Maduro, 3 existem hoje em relação ao Brasil, 5 em parte e 8 não aparecem |
| O que é mais provável? | **A pressão longa** (54%), e nova medida americana até junho de 2027 (72%) |

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

39 casos desde 1945, duas passadas independentes. Concordância: 100% em quem voltou ao poder, 100% em quem foi entregue e 80% no tipo de caso. Lista em `resultados/e2_casos_final.csv`.

| Grupo | Casos | Voltaram ao país | Voltaram ao poder | Margem de 95% | Entregues |
|---|---|---|---|---|---|
| Abrigados nos EUA | 22 | 11 | **3** | 4.7% a 33.3% | 3 |
| Abrigados em outro país | 17 | 10 | **3** | 6.2% a 41.0% | 1 |
| Nos EUA, com apoio declarado de Washington | 6 | 4 | **2** | 9.7% a 70.0% | 0 |
| Mais parecidos: nos EUA, vindos de democracia, processados ou derrotados | 7 | 4 | **0** | 0% a 35.4% | 2 |

**Quem voltou ao poder:** Ngo Dinh Diem (acordo); Kim Dae-jung (eleicao); Jean-Bertrand Aristide (forca_estrangeira); Juan Domingo Perón (eleicao); Ruhollah Khomeini (colapso_revolucao); Nawaz Sharif (eleicao). Mediana de 5,5 anos até voltar ao país.

**Os mais parecidos:** Alejandro Toledo, Ricardo Martinelli, Jair Bolsonaro, Eduardo Bolsonaro, Alexandre Ramagem, Ricardo Anaya, Carlos Andrés Pérez. Alejandro Toledo, Ricardo Martinelli foram entregues.

**Leitura.** Estar nos EUA não aparece como vantagem nem como desvantagem para voltar ao poder: as taxas são parecidas e as margens se sobrepõem. O que muda é como se volta. Entre os apoiados por Washington, Aristide voltou com tropas americanas e Diem por nomeação com apoio americano. Guaidó, Machado e Chalabi tiveram apoio e não chegaram à chefia; na Venezuela, os EUA capturaram Maduro e passaram a tratar Delcy Rodríguez como presidente. Os dois casos que o abrigo americano ajudou a colocar no poder eram de país pequeno ou em guerra, com presença militar americana.

**O que contraria a leitura:** Hidaka, Kubota e Yukawa (2025) dizem que a maioria dos líderes exilados volta e retoma o poder. Lemos o resumo. A base deles é de líderes que perderam o cargo, em geral sob regime fechado; a nossa inclui candidatos e opositores, e casos ainda abertos. Exílio não é o fim da carreira, e Perón levou 17 anos. Por isso a conclusão é sobre o caminho, e não sobre o destino dele.

**Teste do passado:** prever o desfecho de cada caso com a taxa dos outros do mesmo grupo dá nota de Brier 0.144, contra 0.25 do chute de meio a meio. Boa parte disso é só porque voltar ao poder é raro; não mede a capacidade de prever Flávio.

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

**Leitura:** o reconhecimento é a regra (8 de 9), e força militar nos 12 meses, 0 de 9. As duas rupturas foram Palestina 2006 e Venezuela 2024. Chile 1970 mostra que a pressão pode durar anos: o golpe veio em 1973, fora da janela.

## 5. A escada contra o Brasil

33 medidas de jan/2025 a nov/2026: 26 para cima, 7 para baixo, 0 militares. Para comparar, Colômbia 7 e 5, México 5 e 5, Canadá 6 e 4, África do Sul 8 e 2.

- **Sobe e desce:** a Magnitsky de Moraes durou de 30/07 a 12/12/2025. A tarifa de 40% caiu em 20/02/2026 pela Suprema Corte americana, e não por acordo.
- **Hoje:** 25% pela Seção 301 desde 22/07/2026, mais 12,5% da ação global sobre cerca de 60 economias. Dos US$ 39.6 bi que os EUA compraram do Brasil em 2024, US$ 8.5 bi pagam os 25% cheios, pelas medidas lidas.
- **Literatura:** sanções dão certo em cerca de um terço dos casos (Hufbauer et al.), e Pape conta 5 de 115. Mudar regime: 29 de 90. EUA sozinhos, de 1970 a 2014: 11 de 54. Metas limitadas e alvos democráticos rendem mais.
- **O efeito aqui:** a Reuters diz que analistas veem várias das medidas como contraproducentes, e parte ajudou a popularidade de Lula.

## 6. Os EUA vão usar a força?

**Base do medo, tudo real:** captura de Maduro; Trump na ONU em 22/09; vídeo da Doutrina Monroe; PCC e CV designados; ofício do Itamaraty de 01/07 falando em *"possibilidade do uso da força militar"*; ministro Múcio, *"abrir o portão"*, em 04/08; 1964 e a Brother Sam, navios prontos e nunca usados.

**Negativa:** o Departamento de Estado disse que a lei da designação não contempla ação militar. ⚠️ Trump negou ataque à Venezuela 64 dias antes da captura, então negativa sozinha não encerra.

**Tamanho:** o maior alvo sem aval foi Venezuela, 28,52 milhões. O Brasil tem 214 milhões, 7,5 vezes mais. Tropas em 2026 só aparecem em países que aceitaram, ou em treinamento.

**Sinais, um por um** (*"nao"* é ausência nas páginas abertas, e não prova):

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

Matriz de hipóteses concorrentes (Heuer), `dados/e6_hipoteses.csv`. É julgamento da IA, e não medida; 17 evidências.

| Hipótese | Evidências contra | A favor |
|---|---|---|
| Narrativa política e eleições nos EUA | 1 | 4 |
| China e influência no hemisfério | 1 | 3 |
| Terras raras | 3 | 2 |
| Lealdade aos Bolsonaro | 4 | 3 |
| Aposta pessoal de Rubio e entorno | 4 | 2 |

**Leitura:** a que menos sofre com as evidências é a narrativa política, com as eleições americanas no meio: Trump ligou o Brasil à fraude dos democratas no comício do Texas, na semana da votação. Os minerais explicam o interesse no Brasil, e os EUA já têm posição com Lula no governo. Nenhuma fala oficial sobre a entrada cita minerais; mas Dino abriu inquérito em 27/10, a pedido do PT, sobre suspeita de troca de apoio por terras raras, e isso não prova irregularidade.

## 8. O que muda no Brasil

| Indicador | Número | Fonte |
|---|---|---|
| Exportações aos EUA, jan a set/2026 | US$ 27.46 bi, -6,5% | ComexStat |
| Exportações à China, jan a set/2026 | US$ 84.68 bi, +12% | ComexStat |
| Dólar PTAX, 23/10 e 30/10 | R$ 5,0377 e R$ 5,4212, +7,6% | Banco Central |
| Ibovespa na semana | 18,12% de queda | imprensa |

⚠️ O mercado reagiu à reeleição e ao quadro fiscal, e não dá para atribuir isso ao caso Flávio.

| Cenário | Efeito |
|---|---|
| A pressão longa | exportador para os EUA segue com tarifa; o comércio continua indo para a China |
| O acordo | alívio de tarifa e minerais com refino; custo político dos dois lados |
| A escalada | risco em banco e fintech; câmbio mais volátil |

## 9. O que esperar

**Cenários até o fim de 2027** (mediana de 4 modelos, depois de ver a história; somados a 100):

| Cenário | O que é | Chance | Menor a maior |
|---|---|---|---|
| **A pressão longa** | Flávio nos EUA sem poder; posse normal; tarifa e visto como moeda; conversa intermitente; sem ruptura e sem acordo amplo até o fim de 2027 | **54%** | 42 a 58 |
| **O acordo** | Trump e Lula negociam: tarifa e minerais em troca do embaixador e de cooperação; Flávio perde importância para Washington | **23%** | 20 a 28 |
| **A escalada** | Nova sanção forte, bancos ou Pix atingidos pela designação, autoridades de volta à lista, prisão decretada com recusa americana; sem ação militar | **20%** | 18 a 28 |
| **A força** | Ação militar americana em território brasileiro sem aval do Brasil | **2%** | 1 a 3 |

**As perguntas, para conferir na data** (`dados/previsoes/`):

| # | Pergunta | Prazo | Com a história | Entre modelos | Sem a história |
|---|---|---|---|---|---|
| P08 | O governo dos EUA anuncia nova medida contra autoridade setor ou economia do Brasil | 2027-06-30 | **72%** (provável) | 70 a 72 | 57,5% |
| P15 | Flávio segue nos EUA com autorização renovada residência ou asilo depois da parole | 2027-10-27 | **67,5%** (provável) | 45 a 83 | 62,5% |
| P07 | Lula toma posse e os EUA mandam representante à cerimônia | 2027-01-05 | **66,5%** (provável) | 40 a 80 | 74% |
| P06 | Lula participa presencialmente da cúpula do G20 em Doral | 2026-12-15 | **55%** (chance parecida) | 45 a 68 | 52,5% |
| P05 | Trump e Lula conversam por telefone ou se encontram | 2026-12-15 | **50%** (chance parecida) | 35 a 55 | 50% |
| P12 | O STF decreta a prisão de Flávio Bolsonaro | 2027-06-30 | **37,5%** (improvável) | 22 a 42 | 37,5% |
| P17 | Flávio lidera entre os nomes da direita numa pesquisa nacional para 2030 | 2027-12-31 | **35%** (improvável) | 25 a 45 | 35% |
| P10 | O Brasil concede agrément a Danny Perez como embaixador dos EUA | 2027-06-30 | **30%** (improvável) | 20 a 33 | 25% |
| P18 | Câmara dos EUA faz audiência pública com o caso Flávio Bolsonaro entre os temas | 2027-06-30 | **30%** (improvável) | 20 a 40 | 30% |
| P09 | Os EUA reduzem a tarifa de 25% da Seção 301 contra o Brasil | 2027-06-30 | **23%** (improvável) | 14 a 30 | 29% |
| P13 | O Brasil pede formalmente a extradição de Flávio Bolsonaro | 2027-12-31 | **22,5%** (improvável) | 12 a 30 | 23,5% |
| P16 | Flávio volta ao Brasil | 2028-12-31 | **21,5%** (improvável) | 9 a 25 | 17,5% |
| P11 | Brasil e EUA assinam acordo governamental sobre minerais críticos | 2027-12-31 | **16,5%** (muito improvável) | 14 a 25 | 20% |
| P19 | Departamento de Estado responde publicamente às 15 perguntas dos 25 democratas | 2026-12-31 | **16%** (muito improvável) | 10 a 35 | 22,5% |
| P04 | Trump se reúne em público com Flávio Bolsonaro | 2027-03-31 | **13,5%** (muito improvável) | 6 a 25 | 12,5% |
| P02 | Os EUA fazem ataque militar em solo ou águas territoriais brasileiras contra PCC ou Comando Vermelho sem aval do Brasil | 2027-12-31 | **3,5%** (quase nenhuma chance) | 2 a 5 | 4% |
| P14 | Os EUA entregam Flávio Bolsonaro ao Brasil | 2027-12-31 | **3%** (quase nenhuma chance) | 2 a 4 | 2% |
| P01 | Tropas americanas entram em território brasileiro sem autorização do governo do Brasil | 2030-12-31 | **2%** (quase nenhuma chance) | 2 a 3 | 2% |
| P03 | O governo dos EUA reconhece Flávio Bolsonaro como presidente ou líder legítimo do Brasil | 2027-01-05 | **2%** (quase nenhuma chance) | 2 a 4 | 2,5% |

**O que a história mudou nas IAs:** em média, 3,1 pontos. A mudança maior foi na nova medida contra o Brasil, de 57,5% para 72%. Na invasão, nada: já estava no piso. Discordância média entre modelos: 16,3 pontos.

**Datas:** 03/nov midterms · 13/nov prazo de Rubio · nov G7 · 14 e 15/dez G20 · até 18/dez diplomação · 05/jan posse · 31/jan fim do mandato · 27/out/2027 fim da parole.

## 10. O que circula

- **Trump e a ordem para invadir o Brasil** (Lupa Política): O próprio vídeo diz que não há evidência pública de plano; o ofício do Itamaraty é real, e o Departamento de Estado negou.
- **Trump manda 600 soldados para a porta do Brasil** (Milson Alves - Brasil): NYT: cerca de 600 em treino no Panamá, Colômbia e Honduras; Task & Purpose: 500; embaixada no Panamá nega os 600 e diz 120.
- **Flávio recebe aviso de deportação e Trump vira as costas** (Análise Política): Fala de candidato democrata do Texas, não ordem; Trump disse que pode ficar; sem planos de encontrar é real.
- **Casa Branca assume comando da operação** (Jovem Pan 3 em 1): Apuração de um correspondente; Rubio e Trump decidiram a entrada; comando da saída sem segunda fonte.

## 11. Validação

- Citações: 744 de 850 trechos achados na página capturada por este projeto (466 de 494 páginas abriram para o robô). Página que recusa o robô fica registrada; o trecho dela segue da leitura do agente.
- Números: 33 de 33 refeitos por outro caminho, em `resultados/validacao_independente.csv`, com os exilados recontados sobre a 2ª passada.
- Revisão por 3 leitores: `docs/REVISAO_ADVERSARIAL.md`.

Refazer: `docs/REPLICAR.md`.
