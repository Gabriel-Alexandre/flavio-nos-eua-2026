# Revisão adversarial: viés contra Flávio e contra a direita

**Papel:** crítico de direita. **Lido em 02/nov/2026:** `RELATORIO.md`, `docs/LEITURA_DA_IA.md`, `docs/PLANO.md`, `dados/casos/`, `dados/previsoes/`, `resultados/`. Os números abaixo foram refeitos a partir de `resultados/e2_casos_final.csv` e `dados/casos/e4_escada.json`. Fora do repositório, só conferi um fato (ADI 5526, objeção 6).

Ordem: da mais forte para a mais fraca.

---

## 1. A classe "os 7 mais parecidos" não é independente e foi montada por filtros frágeis

**Problema.** O "0 de 7" abre a tabela de respostas e o resumo. Mas:
- 3 dos 7 são do mesmo caso que está em julgamento: Jair, Eduardo e Ramagem. A própria `obs` de Jair diz *"não é exílio prolongado"* (viagem de 3 meses). Eduardo e Ramagem saíram em 2025: cerca de 1 ano de observação.
- Ricardo Anaya (PAN, investigado pela FGR, foi aos EUA, chama de perseguição política) voltou em ago/2024 e é senador. Entra como "não voltou ao poder" porque a definição exige chefia do Executivo. Com "cargo eletivo nacional", seria 1 de 7.
- Quem entra no grupo depende das duas variáveis de pior concordância entre as passadas: `tipo` (79,5%, kappa 0,70) e `regime_casa` (74,4%, kappa 0,60). O filtro "processado ou derrotado" deixa de fora Aristide, a única democracia deposta, abrigada nos EUA, que voltou ao poder, e Mahuad e Sánchez de Lozada (condenado no Equador, segundo a `obs`, e com extradição negada pelos EUA, respectivamente). Aristide teve `regime_casa` dividido entre as passadas (democracia/autocracia).
- No grupo de 22, Somoza e o Xá estão contados como "abrigados nos EUA" embora a `obs` diga que Somoza *"não foi abrigado de fato"* e o Xá entrou só para tratamento médico.

**Onde.** `RELATORIO.md` §1 e §3 (tabela de grupos); `ferramentas/analise.py`, linha do filtro `parecidos`; `resultados/e2_casos_final.csv`; `resultados/e2_concordancia.csv`.

**Efeito se valer.**
- Sem Jair, Eduardo e Ramagem (não independentes ou ainda abertos): **0 de 4** (Toledo, Martinelli, Anaya, Carlos Andrés Pérez). Margem de 95% (Wilson): **0 a 49,0%**, contra os 0 a 35,4% publicados.
- Com Anaya contado por cargo eletivo nacional: **1 de 4 (25%)**.
- Grupo EUA sem Somoza e o Xá: **3 de 20 = 15,0%** (5,2% a 36,0%), contra 13,6%.
- Dos 4 restantes do "mais parecidos", 3 foram processados por corrupção (Toledo, Martinelli, Pérez), tipo de acusação que Flávio nega e que não é a de perseguição política alegada por Anaya e pelos Bolsonaro.

**Correção.** Mostrar a classe com e sem os casos do mesmo processo; publicar a sensibilidade a `tipo` e `regime_casa` (cada troca de classificação, o que muda); tirar "0 de 7" da tabela de respostas e do `RESUMO_SIMPLES.md` ou escrever junto o "0 de 4" e a margem; definir "voltou ao poder" também por cargo eletivo nacional e mostrar as duas versões.

---

## 2. Casos abertos contam como fracasso e o tempo de observação é ignorado

**Problema.** O desfecho é "voltou ao poder = não" para todo caso ainda em andamento. Quem voltou ao poder levou, no próprio levantamento: Aristide 3 anos, Diem 4, Sharif 13, Kim Dae-jung 15, Khomeini 15, Perón 18. **Mediana cerca de 14 anos.** Os 7 "mais parecidos" têm hoje entre 1 e 11 anos de observação (Toledo 9, Martinelli 11, Jair 4, Anaya 5, Eduardo 1, Ramagem 1, Pérez morreu em 2010). Nenhum chegou a 13. Com esse horizonte, 0 de 7 é o resultado esperado quer o caminho funcione, quer não.

No grupo "apoio declarado de Washington", Machado entra como fracasso: voltou à Venezuela em **25/10/2026**, 8 dias antes da data de leitura, e a `obs` do projeto diz que está *"sem cargo"*. Guaidó (3 anos), Eduardo e Ramagem (1 ano) também contam como "não chegou". O relatório reconhece "casos ainda abertos" só ao comentar o estudo de 2025 (Hidaka, Kubota e Yukawa), sem dizer quantos são. A única mediana publicada, **5,5 anos**, é de volta *ao país*, e aparece logo depois de "quem voltou ao poder", o que sugere a leitura errada.

**Onde.** `RELATORIO.md` §1 (linha "Volta ao poder por esse caminho?") e §3.

**Efeito se valer.** Dos 6 que voltaram ao poder, só 2 foram em até 5 anos (Diem e Aristide, os dois com mão americana). Quem voltou por eleição levou 13 a 18 anos. Um horizonte de 2030 (4 anos) separa bem o caminho da força, mas 0 de 7 não diz nada sobre 2034 ou 2038. O texto deve dizer isso, e não deixar o 0 como se fosse evidência contra a volta pela urna.

**Correção.** Coluna `censurado` e `anos_de_observação` em cada caso; curva de sobrevivência (Kaplan-Meier) com intervalo; publicar a probabilidade em 4, 8 e 12 anos; separar "voltou por eleição" de "voltou por força ou colapso"; marcar os casos de 2025 e 2026 como em aberto na tabela, não como zero.

---

## 3. O "teste do passado" mostra que o agrupamento não prevê nada, e o relatório o apresenta ao contrário

**Problema.** A nota de Brier 0,144 é comparada com 0,25 (chute 50%). O comparador correto é a taxa-base. Com 6 voltas em 39 casos, prever sempre 15,4% dá Brier **0,130**. Refeito em deixa-um-de-fora com a taxa global (mesma suavização do script): **0,137**. O modelo por grupo tem **0,144**. Ou seja, saber o grupo do caso piora a previsão em relação a ignorar o grupo. O texto diz "boa parte disso é só porque voltar ao poder é raro", mas não diz que ficou pior que a constante.

**Onde.** `RELATORIO.md` §3, parágrafo "Teste do passado"; `ferramentas/analise.py` (laço `brier`, `brier_50 = 0.25`). O mesmo agrupamento ("0 de 7", "3 de 22") foi entregue aos 4 modelos no texto B de `dados/previsoes/texto_B.md`.

**Efeito se valer.** A diferença entre os grupos (EUA 13,6%, outros 17,6%, mais parecidos 0%) não passa por validação: não há ganho de previsão fora da amostra. A frase "dos 7 mais parecidos com ele, 0" na tabela de respostas parece achado, e é ruído de amostra pequena.

**Correção.** Publicar os três números (0,130; 0,137; 0,144) e dizer que o grupo não acrescenta informação sobre a taxa-base; trocar o comparador de 0,25 para a constante; tirar o "0 de 7" da linha de resposta.

---

## 4. Falta a hipótese que o governo americano declara, e a vencedora é sustentada por falas sobre outro assunto

**Problema.** A matriz de hipóteses (Heuer) testa lealdade, narrativa e eleições, China, terras raras e aposta de Rubio. Não há "preocupação declarada com perseguição política, devido processo e proteção de um opositor sob ordem do STF" (nas palavras de Trump: *"treated very unfairly"*; em `e4_escada.json`, a Magnitsky de 2025 foi aplicada por *"detenções arbitrárias e censura"*; a entrada foi por parole humanitária). É a hipótese que os próprios atores declaram. Pode-se descartá-la depois de testar, mas não de omiti-la.

Das 4 evidências a favor de H2 (narrativa e midterms), 3 são falas de Trump em comício sobre os democratas (linhas 1, 4 e 5 do CSV) e a quarta é a posição dos republicanos da Flórida. Nenhuma é sobre por que recebeu Flávio. A linha 1 ("treated very unfairly") aparece em H1 e H2, mas não existe coluna onde conte para a razão declarada.

**Onde.** `RELATORIO.md` §7; `dados/e6_hipoteses.csv`.

**Efeito se valer.** Em codificação minha, não verificada: a hipótese nova receberia "+" nas linhas 1 e 6 (Trump diz que foi tratado mal; Rubio recomendou a entrada e Trump assinou) e nenhum "-" óbvio entre as 17. Teria **2 a favor e 0 contra**, a mesma pontuação ou melhor que a "narrativa política" (4 a favor, 1 contra) em número de contras, que é o critério que Heuer manda usar. Cabe à IA dizer o resultado depois de codificar; o ponto é que hoje a hipótese nem entra.

**Correção.** Incluir H6 (convicção de perseguição ou proteção humanitária, como razão declarada e como razão real); codificar as 17 linhas de novo com duas passadas independentes, como se fez em E2; separar evidência *sobre a entrada* de evidência *sobre a retórica de Trump*; deixar "narrativa política" como julgamento, e não como a que "menos sofre".

---

## 5. A "escada contra o Brasil" conta 26 subidas, mas só cerca de 11 são medidas americanas dirigidas ao Brasil

**Problema.** `e4_escada.json` marca como "sobe" itens que não são medidas dos EUA contra o Brasil:
- 3 tarifas globais (aço 12/03/2025, recíproca de 02/04/2025, 12,5% de 24/07/2026 sobre cerca de 60 economias), que o próprio arquivo descreve como *"medida global, não dirigida ao Brasil"*;
- 3 atos do **governo brasileiro** (visto de Beattie 13/03/2026, vistos de Barnes e Samson 25/07/2026, enquadramento na Lei da Reciprocidade 13/08/2026), que o arquivo admite entrarem como "sobe da escalada bilateral", e o ofício do Itamaraty de 01/07/2026;
- 1 duplicata (30/07/2025, ordem executiva dos 40%, e 06/08/2025, entrada em vigor da mesma tarifa);
- 2 passos de nomeação de embaixador (01/06 e 07/08/2026);
- 5 falas, reportagens ou chegadas (11/09/2025, 24, 27, 28 e 31/10/2026).

Sobram **11 de 26** (investigação 301, tarifas de 07/2025 e 07/2026, vistos, Magnitsky de Moraes e da mulher, Viotti, designação de PCC e CV). Em dois pontos o relatório usa o número: o título "A escada contra o Brasil" e o texto entregue aos modelos (*"33 medidas: 26 para cima, 7 para baixo"*), e P08 ("nova medida") foi de 57,5% sem a história para **72%** com ela (não dá para isolar o efeito desta linha).

Também há comparação sem metodologia: "Colômbia 7 e 5, México 5 e 5, Canadá 6 e 4, África do Sul 8 e 2". A África do Sul tem 80% de subidas, igual ao Brasil (79%), e a contagem de cada país segue regra desconhecida. Não existe a coluna espelho: atos do STF e do governo brasileiro que os EUA citam como motivo (proibição da visita de Beattie a Bolsonaro, ordens contra plataformas americanas, o passaporte) aparecem só como contexto.

**Onde.** `RELATORIO.md` §5; `dados/casos/e4_escada.json` (campos `convencoes` e `brasil`); `resultados/e4_escada_brasil.csv`; `dados/previsoes/texto_B.md`.

**Efeito se valer.** A frase "26 para cima, 7 para baixo, 0 militares" cai para cerca de 11 medidas americanas dirigidas ao Brasil contra 7 recuos (3 dos quais são reuniões ou telefonemas, contados em pé de igualdade com tarifa). A razão sobe de 3,7 para 1 e passa a 1,6 para 1.

**Correção.** Separar quatro colunas (medida dirigida, medida global, ato do Brasil, fala ou evento); contar só a primeira na manchete; aplicar a mesma regra aos quatro países de comparação e dizer quem escolheu os países e por quê; incluir a coluna espelho dos atos brasileiros; refazer P08 com o texto corrigido ou dizer que ela foi respondida com a contagem antiga.

---

## 6. O lado de Moraes não recebe a lupa que Trump recebe

**Problema.** Para Trump, o relatório pede prova e escreve *"sem prova"*. Para a ordem do STF, aceita a nota da PF como verdade. A linha do relatório diz "confirmado" para a ordem de entregar passaportes. O registro `E1-d3` diz: *"Não consegui abrir a decisão"*. O que existe é a nota da PF (parte interessada) e o Poder360. O prazo de 24 horas *"não cumprido"* vem também só da PF. O texto nunca pergunta:
- qual é a base jurídica de entregar o passaporte de um senador no exercício do mandato, no dia seguinte à derrota na urna. O art. 53 aparece em `LEITURA_DA_IA.md` como proteção contra prisão, mas não na análise da ordem. A ADI 5526 (STF, 2017) decidiu que o STF pode impor cautelares a parlamentares e que as que impeçam o exercício do mandato dependem da Casa. Se o passaporte cai nessa regra é questão aberta, e o relatório nem a formula (conferido em notícias da época; não li o acórdão);
- por que a PF pediu a medida 7 minutos depois da confirmação do TSE (21h16), o que indica pedido preparado antes, e se há data anterior de decisão;
- o que são os dois inquéritos. O relatório diz em uma linha que Flávio nega, mas o texto entregue aos modelos descreve *"corrupção, lavagem e evasão no caso do filme Dark Horse"* como fato, e a `LEITURA_DA_IA.md` já pesa o "caso Dark Horse" pelo tratado de extradição. Não há denúncia nem mandado de prisão citados. O leitor não sabe o que está sendo investigado.

A lupa que cai sobre os americanos (jato, Miller, Mossad, Argentina: 7 linhas na tabela da §2) não cai sobre o STF (1 linha).

**Onde.** `RELATORIO.md` §2, linha "Ordem de entregar passaportes"; `dados/casos/e1_originais.json` (`E1-d1` a `E1-d3`); `docs/LEITURA_DA_IA.md` ponto 3.

**Efeito se valer.** A parte da história que explica por que os EUA agiram de um jeito (e a reação do governo americano à decisão do STF) fica sem a metade jurídica. O leitor que acredita na versão do STF e o que acredita na de Flávio recebem o mesmo texto e chegam a leituras opostas sem base para decidir. Não é possível dizer em número.

**Correção.** Linha nova na §2 com base jurídica, órgão que decidiu, data e hora (ou "não divulgada"), discussão do art. 53 e da ADI 5526; trocar "confirmado" por "descrito pela PF, decisão não lida"; uma linha por inquérito, com o que consta como imputação e o que não consta; mesma exigência de "duas fontes" aplicada à ordem e ao jato.

---

## 7. A seleção de fontes e de perguntas puxa para um lado

**Problema.**
- A base do E1 tem 7 URLs de uma deputada democrata (`kamlager-dove.house.gov`, a carta dos 25), CartaCapital, Congresso em Foco, Poder360, TMC, SBT News, Correio da Manhã. Nenhuma de Gazeta do Povo, Revista Oeste, Fox News ou da própria assessoria de Flávio, cuja versão (perseguição, saída por segurança) só entra via Infobae. Em `fontes.csv`, são 494 URLs: 83 da Wikipedia (17%), 3 da Jovem Pan e 1 da Fox (obituário de Pérez).
- A lista "o que circula" tem 4 vídeos: três de alarme de invasão ou abandono (Lupa Política, Milson Alves, Análise Política), um da Jovem Pan. Falta qualquer alegação que circula à direita sobre perseguição ou o STF, ou qualquer checagem do que Flávio disse na live de 30/10 e nas cartas.
- O texto que foi para os quatro modelos usa *"alega fraude sem prova"* e lembra que Flávio *"se disse 'presidente eleito' e depois 'líder do Brasil'"*. Não há frase equivalente que traga o argumento dele (perseguição) nem a linha da PF de que não há mandado de prisão no mesmo peso.
- As 19 perguntas são centradas no Flávio e nos EUA. Nenhuma pergunta e nenhum cenário trata de escalada do lado brasileiro (Lei da Reciprocidade, nova ordem do STF contra americanos ou empresas americanas), embora a própria escada registre quatro atos do Brasil. A "Escalada" (C3) é definida por ato dos EUA e por *"prisão decretada com recusa americana"*. P19 e P18 pedem resposta pública a 25 democratas e audiência na Câmara, ou seja, medem o que os adversários de Trump fazem.

**Onde.** `dados/casos/e1_originais.json` (`url`), `dados/fontes.csv`, `dados/e9_o_que_circula.csv`, `dados/previsoes/texto_A.md` e `texto_B.md`, `dados/previsoes/perguntas.csv`, `cenarios.csv`.

**Efeito se valer.** Não se mede em número. Os quatro modelos são da Anthropic e receberam o mesmo texto de partida (o relatório diz isso como limite), então qualquer inclinação do texto se repete nos quatro. O texto A (sem a história) e o B (com a história) têm o mesmo bloco de fatos, de modo que o enquadramento passa nos dois cenários.

**Correção.** Incluir pelo menos uma fonte de cada lado por afirmação (e dizer quando só há de um); trazer a posição de Flávio e dos aliados com a mesma extensão da dos adversários; acrescentar ao menos duas perguntas de escalada do lado brasileiro e uma pergunta sobre o STF (por exemplo, nova medida contra cidadão, empresa ou plataforma americana); trocar *"alega fraude sem prova"* por frase que cite a fonte da conclusão e o que foi testado (o repositório de hipóteses do 2º turno registra 4 hipóteses compatíveis com as duas leituras, segundo o registro da documentação).

---

## 8. Há afirmações sem fonte e a seção de validação foi publicada em branco

**Problema.**
- `RELATORIO.md` §11: *"Citações: ? de ? trechos achados ... (? de ? páginas abriram para o robô)"*. Os números não foram preenchidos. Não existe `resultados/citacoes.csv`, e a conferência de citações (`ferramentas/conferir_citacoes.py`) não foi rodada.
- O mesmo parágrafo remete a `docs/REVISAO_ADVERSARIAL.md` e a `docs/REPLICAR.md`, e o `PLANO.md` a `docs/RODADAS.md`. Nenhum dos três existe hoje.
- `LEITURA_DA_IA.md`, ponto 3: *"O tratado não lista lavagem nem evasão, mas lista suborno e peculato, e por isso o caso Dark Horse pesa mais que o outro"* e *"O art. 53 protege até 31/01/2027"*. Não há fonte nesses pontos em `dados/casos/`; as duas únicas capturas que citam tratado de extradição são da Wikipedia (Toledo) e da AP (Martinelli).
- §8: *"Ibovespa na semana: 18,12% de queda, fonte: imprensa"* sem veículo, data nem série. A frase seguinte, *"O mercado reagiu à reeleição e ao quadro fiscal"*, atribui uma causa e na mesma linha diz que não dá para atribuir.
- §7: o relatório diz que a matriz de hipóteses é *"julgamento da IA, e não medida"*, mas a leitura conclui que uma é "a que menos sofre", sem teste de sensibilidade nas 17 codificações.

**Onde.** `RELATORIO.md` §8, §7 e §11; `docs/LEITURA_DA_IA.md`; `docs/PLANO.md`.

**Efeito se valer.** Um leitor adversário encontra "? de ?" na seção que deveria provar que as citações são reais, e chama o resto de não verificado. O ponto do tratado é uma afirmação jurídica que ele pode contestar com um clique.

**Correção.** Rodar a conferência de citações e preencher os números, ou tirar a frase; criar os três arquivos citados ou tirar a referência; pôr fonte (o texto do tratado, ou a nota da época) no ponto 3, ou marcá-lo como opinião sem lastro; dar veículo e data ao Ibovespa e tirar a causa que a linha seguinte nega.

---

## O que resiste à crítica

O núcleo do relatório não depende dos pontos acima: reconhecimento do resultado em 8 de 9 casos, força militar em 0 de 9 e 2% para tropas até 2030 se mantêm com qualquer reclassificação; a linguagem sobre Flávio é neutra (parole, "não é foragido segundo a PF", "Flávio nega"), a fala de Trump de que ele foi "tratado muito mal" está citada, e o inquérito de Dino é descrito como sem prova de irregularidade. A conclusão central, "exílio não é fim" (Perón, estudo de 2025), é um corte a favor da direita que o relatório assume ao dizer que a hipótese inicial foi derrubada.
