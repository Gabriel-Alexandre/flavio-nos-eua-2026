# Revisão adversarial: o crítico que acha que o relatório subestima o risco

**Data:** 02/nov/2026. Lido: `RELATORIO.md`, `docs/LEITURA_DA_IA.md`, `docs/PLANO.md`, `dados/casos/*`, `dados/previsoes/*`, `resultados/*` e `ferramentas/analise.py` e `agregar_previsoes.py`. Contas refeitas a partir dos próprios CSV e JSON. Internet usada para um fato só (objeção 6).

Em ordem de força.

## 1. O "2%" de força e a lista de 16 sinais não discriminam nada neste horizonte

**O problema.** A lista de sinais vem de um único caso (Venezuela). Em `dados/casos/e5_sinais.json` a sequência é: designação de grupos criminosos em 20/01 e 20/02/2025, diretiva secreta ao Pentágono em 08/08/2025, e só depois recompensa, navios, FAA, ultimato, espaço aéreo, bloqueio e captura (03/01/2026). Ou seja, os sinais "tardios" (a maioria dos 8 "nao") apareceram nos últimos 5 meses; a designação veio 11 meses antes. O Brasil, com PCC e CV designados em 29/05/2026 e base jurídica "parcial", está onde a Venezuela estava entre fev e jul/2025. O relatório compara o Brasil de hoje com a Venezuela do dia da captura e conclui "8 não aparecem". Além disso o próprio arquivo diz que "nao" é só ausência em páginas abertas (11 de 16 tipos com `incerto`), e o `RELATORIO.md` repete isso em uma linha, mas usa a contagem como argumento.

Segundo ponto: o "Tamanho" (7,5 vezes) sai de uma lista de 18 casos em que houve força (`e5_forca.json`), restrita ao hemisfério. É seleção no desfecho: falta o denominador de países ameaçados e não atacados, e falta qualquer país grande fora do hemisfério sem aval (por exemplo o Irã em jun/2025, cerca de 90 milhões; isto é conhecimento meu, não está no repositório).

Terceiro: o "2% até 2030" da tabela 1 é a pergunta P01, a mais estreita (tropa em terra, duas agências). A forma mais plausível de força, ataque a PCC e CV, é a P02: 3,5% só até 31/12/2027. Pior, o cenário C4 "A força" (ação militar em território brasileiro, mesmo horizonte) está em 2%, abaixo da P02, que é um subconjunto dele. Isso é incoerente. O 2% do C4 é ainda a mediana 2,5 arredondada para baixo (`cenarios`: 3, 2, 1, 3).

**Efeito se valer.** Com 3,5% em 14 meses (cerca de 3% ao ano), até o fim do mandato de Trump (20/01/2029, cerca de 26 meses) a força do tipo ataque limitado fica perto de 6%. O C4 deveria ser no mínimo 3,5% a 5%. A resposta "2%, faixa mais baixa" vira "3,5% a 6%, quase nenhuma chance a muito improvável". Não muda a conclusão qualitativa, mas muda a manchete e o tamanho do risco em cerca de 2 a 3 vezes.

**Correção.** Alinhar no tempo: contar quantos dos 16 sinais a Venezuela tinha em T-10 e T-6 meses e comparar com o Brasil hoje. Dizer que a lista de sinais não tem taxa de falso positivo (Colômbia, México e Cuba têm sinais parecidos e sem captura) e não vira probabilidade. Dar o P02 também até 2029. Fazer C4 maior ou igual a P02. Acrescentar a coluna "ameaçado e não atacado".

## 2. A P08 (nova medida contra o Brasil) em 72% contradiz a escada do próprio relatório

**O problema.** A P08 conta sanção, tarifa adicional, revogação coletiva de vistos ou designação. Em `resultados/e4_escada_brasil.csv`, só com sanção, tarifa e designação "sobe" são 10 eventos em 20 meses; a maior pausa foi de 248 dias (22/09/2025 a 28/05/2026, o degelo). A janela da P08 tem cerca de 240 dias (02/nov a 30/jun). Em cerca de 350 janelas de 240 dias possíveis no histórico, só cerca de 8 (2%) não têm nenhum evento. Incluindo as medidas de visto, a maior pausa cai para 172 dias e nenhuma janela de 240 dias fica vazia. O modelo Opus cita "26 altas em 22 meses" e mesmo assim dá 72%. Sem a história ficava em 57,5%.

**Efeito se valer.** Se o degelo for o único regime que gera seca (cenário do acordo, 23%, com talvez 60% de chance de seca), a conta dá 0,23 x 0,6 + 0,77 x 0,05, ou seja, 18% de "nenhuma medida" e P08 perto de 82%. Pela frequência histórica pura, 95% ou mais. Subestimação de 10 a 23 pontos. E se a P08 é 82% a 95%, a descrição do C1 ("tarifa e visto como moeda", sem ruptura) precisa dizer que medidas novas fazem parte dele, e o C1 contra o C3 fica mais difícil de separar (ver 7).

**Correção.** Calcular a taxa histórica de medidas por tipo e fazer a P08 sair dela, com o degelo como cenário. Mostrar essa conta no relatório. Reportar a P08 separada para "sanção ou designação", que é a mais séria.

## 3. A taxa de "voltar ao poder" está contaminada por censura à direita, e o "0 de 7" é quase todo caso sem tempo de resolver

**O problema.** Os 6 casos que voltaram ao poder saíram todos até 2007 (Diem 1950, Perón 1955, Khomeini 1964, Kim 1982, Aristide 1991, Sharif 2000). Dos 12 casos que saíram em 2017 ou depois, 0 voltaram, e não podiam: a mediana é 5,5 anos e Perón levou 17. Nos 27 casos que saíram até 2016, são 6 de 27 (22%, margem 10,6 a 40,8), contra os 15% (6 de 39) que ficam na leitura. No grupo EUA com tempo de observação (saiu até 2016): 3 de 15 (20%). O "0 de 7" dos mais parecidos tem 4 casos recentes (Jair, Eduardo, Ramagem, Anaya, todos desde 2021), sobrando 3 casos maduros (Toledo, Martinelli, Carlos Andrés Pérez), dois dos quais foram entregues. O n efetivo é 3.

Há ainda escolha de subgrupo depois do dado. O `PLANO.md` fixou só "grupo EUA" e "comparação"; "mais parecidos" (`analise.py`, linha 75: democracia e processado ou derrotado) foi definido na análise. Os campos usados, `regime_casa` (74% de concordância, kappa 0,60) e `tipo` (80%, kappa 0,70), são os de menor concordância entre as duas passadas. A definição exclui Aristide (deposto), o único democrático abrigado nos EUA que voltou. Com "EUA e democracia, qualquer tipo": 1 de 10.

**Efeito se valer.** O número útil é "cerca de 1 em 5 dos casos com tempo de resolver", e não "3 de 22" nem "0 de 7". A leitura de que o abrigo "não aparece como vantagem" continua, mas a tranquilidade do 0 não.

**Correção.** Análise de sobrevivência (ou ao menos a taxa nos casos com 10 anos ou mais de observação). Declarar "mais parecidos" como pós-hoc e mostrar a sensibilidade a `regime_casa` e `tipo` nas duas passadas. Tirar o "0 de 7" da tabela 1.

## 4. A manchete escolhe os grupos de menor taxa e não conta retorno de grupo político

**O problema.** A linha "Volta ao poder por esse caminho?" cita "3 de 22" e "0 de 7". O grupo mais próximo do Flávio, com facilitação declarada de Washington (parole confirmada por Rubio), está na tabela mas fora da linha: 2 de 6 (33%, margem 9,7 a 70,0). A codificação desse grupo está frouxa nas duas direções: Eduardo Bolsonaro entra como `sim` apesar de a própria observação dizer "sem declaração de apoio a ele como exilado", e Guaidó entra apesar de "o apoio terminou antes da saída". Sem os dois, 2 de 4. De qualquer modo é o grupo mais relevante, e o relatório o trata como nota.

"Voltar ao poder" é medido só por indivíduo. Marcos (filho eleito em 2022, grupo EUA), Thaksin (irmã e filha primeiras-ministras), Zelaya (esposa presidente em 2022) e Evo (Arce em 2020) são lidos como "não" nas observações. Para uma pergunta sobre o campo político do Flávio (a direita volta em 2030, com 48,21% no 2º turno), o retorno do grupo conta. Com ele: 10 de 39 (26%), grupo EUA 4 de 22 (18%), comparação 6 de 17 (35%).

**Efeito se valer.** A faixa passa de "3 a 15%" para "18 a 33%" conforme a definição. Hidaka, Kubota e Yukawa (2025), lidos só pelo resumo, dizem que a maioria dos exilados volta ao poder; o relatório responde com uma frase sobre a base e não refaz a conta na base deles.

**Correção.** Mostrar as três taxas (indivíduo, indivíduo mais grupo político, só casos maduros) lado a lado. Recodificar Eduardo e Guaidó e mostrar as duas versões. Ler o artigo inteiro ou escrever que o resumo contradiz e que não foi reconciliado.

## 5. O "teste do passado" (Brier 0,144 contra 0,25) é comparação com o adversário errado

**O problema.** A taxa constante de 6/39 dá Brier 0,130. Com leave-one-out global fica em 0,137. O modelo por grupo (EUA contra outros), de 0,144, é pior que ignorar o grupo. O `0,25` é o chute de meio a meio, que ninguém usaria. O relatório admite que "boa parte é porque voltar ao poder é raro", mas deixa a frase como suporte da tabela de grupos.

**Efeito se valer.** A diferença EUA contra outros (13,6% contra 17,6%) não tem poder preditivo medido. Qualquer conclusão do tipo "estar nos EUA não ajuda nem atrapalha" é ausência de informação, não resultado.

**Correção.** Trocar o 0,25 pela taxa-base e escrever "sem habilidade sobre a taxa-base". Deixar só a margem de 95% como fato.

## 6. A tabela do "preferido de Washington que perde" não codifica o caso atual e esconde que os "nao" são ausência de fonte

**O problema.** Dois pontos. (a) `e3_derrotas.json` avisa: "varios campos 'nao' de sancao, golpe e forca sao por ausencia de fonte". O `RELATORIO.md` imprime "força militar nos 12 meses, 0 de 9" sem esse aviso. Com 11 casos descartados por falta de fonte de preferência, entre eles Brasil 2022, a amostra são os episódios bem documentados. Só 2 casos são da era Trump. (b) O próprio Brasil 2026 não é codificado nas colunas "Reconheceu" e "Relação". Busca rápida (MercoPress e Buenos Aires Herald, 26/10): Trump disse que a eleição parecia "rigged", e Trump e Milei ficaram sem felicitar enquanto a maior parte da região felicitou Lula. Se o caso atual já é "tardou" ou "nao" em reconhecimento, ele já está fora do "8 de 9 reconhecem" e do grupo "normal", e mais perto de Venezuela 2024 e Palestina 2006, as duas rupturas (2 de 9 = 22%). Nos mesmos 9 casos, sanção nova apareceu em 3 de 9 (33%).

**Efeito se valer.** A frase "o reconhecimento é a regra" não se aplica ao caso. A taxa de ruptura sobe de zero (leitura implícita) para 22% na amostra, e a de sanção nova para 33% mesmo na amostra enviesada para o lado calmo.

**Correção.** Incluir uma linha "Brasil 2026" com os campos preenchidos e a data da última checagem. Copiar o aviso do E3 para o relatório. Chamar a taxa de "limite inferior por ausência de fonte".

## 7. As previsões: família única de modelos, medianas que não fecham e histórico reaproveitado

**O problema.** (a) Os 4 modelos são da Anthropic (o relatório diz). Em todas as 8 respostas o P01 é 2 ou 3: é o prior do modelo, não um achado. O relatório lê "sem a história 2%, com a história 2%" como estabilidade. (b) A condição B recebe os resultados do próprio projeto, e o Opus cita na justificativa "8 de 16 sinais prévios ausentes". A condição B não é confirmação independente da análise, é a análise reentrando. (c) Contas: medianas dos cenários com história são 55 / 23 / 20,5 / 2,5 (soma 101). A tabela mostra 54 / 23 / 20 / 2 (soma 99), a normalização e o arredondamento sempre para baixo no C1 e no C4. O texto diz "somados a 100". (d) A mediana tira a cauda pessimista: o Haiku põe 28% na escalada e 42% na pressão longa; a mediana, 20,5%. P02 vai de 2 (Opus) a 6 (Fable, sem a história). (e) A discordância média entre modelos é de 16,3 pontos, e a tabela de cenários mostra "menor a maior" mas a manchete usa um número.

**Efeito se valer.** C4 em 2,5% e não 2%; C3 em 21 a 22% pela média; a faixa honesta do C3 é 18 a 28, com 28 dado por um dos quatro. Pouca mudança no centro, mas a incerteza entre modelos (16 pontos) é maior que quase todas as diferenças que o texto interpreta.

**Correção.** Reportar mediana e média e a faixa inteira; arredondar sem viés; mudar "somados a 100" ou normalizar de verdade; dizer na página que o 2% é piso de modelo (A igual a B) e não resultado do estudo.

## 8. O selo de "validado" é maior que a validação

**O problema.** `RELATORIO.md` §11 tem "Citações: ? de ? trechos" (marcadores sem preencher) e "Revisão por 3 leitores: `docs/REVISAO_ADVERSARIAL.md`" e "Refazer: `docs/REPLICAR.md`", que não existem no repositório (a pasta `docs` tem só `PLANO.md` e `LEITURA_DA_IA.md`; `docs/RODADAS.md`, citado no plano, também não). `ESTADO.md` ainda diz "antes de qualquer contagem". Dos "33 de 33 refeitos por outro caminho", 19 são as medianas P01 a P19 recalculadas do mesmo JSON, e 14 são recontagens do mesmo CSV: confere aritmética, não codificação. A concordância de 100% em `voltou_ao_poder` é entre duas passadas do mesmo tipo de leitor, com as mesmas lacunas de conhecimento; não detecta caso ausente.

**Efeito se valer.** O leitor entende que a base foi checada por fora, e foi checada só por dentro. Um caso ausente que mudasse a taxa (por exemplo exilados de volta ao poder que ninguém listou) não seria pego por nenhuma das validações citadas.

**Correção.** Preencher ou tirar a linha das citações. Publicar este arquivo e o de cada revisor. Fazer a lista E2 ser revisada por quem não a escreveu, procurando só o que falta (casos que voltaram ao poder e ficaram de fora). Escrever "aritmética conferida" em vez de "validado".

---

## O que resiste à crítica

A leitura dos fatos das 72 horas (E1), a escada com datas (33 medidas, com tipo e direção) e as ressalvas honestas dentro dos arquivos de dados (E5, E3) estão bem feitas. A conclusão central, que força militar contra o Brasil é improvável e que a pressão longa é o cenário mais provável, sobrevive a todas as objeções acima; o que muda é o tamanho do risco (2% vira 3,5% a 6%; P08 sobe de 72% para 82% a 95%) e a confiança na "taxa de volta ao poder", que é mais frouxa do que a tabela passa.
