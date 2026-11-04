# Rodadas

## Rodada 0: plano (02/nov, `3ae1866`)

Objetivo, método e critérios escritos antes de contar: classe de referência, Tetlock e Brier, Heuer, escala ICD 203.

## Rodada 1: previsões e primeira conta (02/nov, `5698a4d` às 11h55 e `ed313bf`)

19 perguntas e 4 cenários, 4 modelos, com e sem a história. Congelada em `dados/previsoes/rodada1/`. Resultado de cenários: 54,5 / 22,8 / 20,3 / 2,5.

## Rodada 2: depois da revisão (02/nov)

Mudou porque a revisão por 3 leitores achou erro meu. O que entrou:

| Item | Antes | Depois | Por quê |
|---|---|---|---|
| Tese | "abrigo americano não leva ao poder" | caiu: a porta aberta não é caminho rápido | a regra escrita antes dizia que cairia se houvesse abrigado nos EUA de volta ao poder sem força nem colapso; Kim Dae-jung e Diem são isso |
| Exilados | taxa bruta | taxa por prazo, só com quem já teve aquele tempo; grupo político separado da pessoa; casos maduros | caso aberto contava como fracasso |
| "Mais parecidos" | manchete, 0 de 7 | ilustração, com aviso; 0 de 4 sem o próprio grupo | a classe foi definida depois de ver os casos e 3 dos 7 são o mesmo grupo |
| Teste do passado | Brier contra chute | Brier contra taxa única | separar por grupo não melhorou nada |
| Escada | 26 sobem e 7 descem | 11 medidas dirigidas e 7 para baixo | a conta misturava medida global, ato do Brasil, nomeação e fala |
| Força | "o Brasil não cabe na lista" e tropas só com aval | tamanho é custo e não teto; guerra do Irã entra; sinais alinhados no tempo | tamanho foi escolhido depois, e Maduro e Cuba foram sem aval |
| Motivos | placar com vencedor | sem vencedor; H6 nova (convicção declarada de perseguição); entrada separada da retórica; 2ª codificação às cegas | motivo é intenção, e faltava a explicação que o próprio governo dá |
| Previsões | 19 perguntas | 24, com P20 a P24: ataque até 2029, sanção nominal, banco, Lei da Reciprocidade e STF contra americano | a escalada do lado brasileiro não estava medida |
| Texto das previsões | PF "não é foragido"; dois inquéritos | a frase exata da PF, três inquéritos pela Lupa, art. 53 e ADI 5526, argumento dele, soma das tarifas disputada | o texto favorecia uma leitura |
| Citações | 744 de 850 | situação por trecho: achado, diferença, API, recusa, não achado | PDF não era lido e nota de rodapé atrapalhava |

Nota: o texto da rodada 2 diz 348 dias para a designação, contando da ordem executiva de 20/01/2025; o relatório usa 317, a designação formal de 20/02/2025. A ordem de grandeza que os modelos leram é a mesma, e o texto ficou como eles leram. Também diz que o Irã tem "cerca de 90 milhões"; a estimativa capturada depois é de 87 milhões. Não muda a conta e o texto ficou como os modelos leram.

Da rodada 1 para a 2, os cenários foram para 56,6 / 18,7 / 21,7 / 3,0 e os números pequenos ficaram onde estavam. O que os modelos dizem de invasão não mudou com nenhuma correção, então não é sensível ao texto, e isso também é um limite.

## Depois da conferência do roteiro (02/nov)

A leitura frase a frase do roteiro (`VIDEO_022/CONFERENCIA_DO_ROTEIRO.md`, na documentação) voltou para cá: Benazir Bhutto fica fora da conta de uma saída por pessoa e isso passa a ser dito; o relógio da Venezuela vale só para a designação; a Reuters relata contato com funcionários americanos no caminho. As previsões não mudaram.

## Atualização de 04/nov, sem previsão nova

Busca dos fatos de 02 a 04/nov, guardada em `dados/depois_das_previsoes.csv` e no §11 do relatório: os democratas ganham a Câmara e o Senado (projeção de 04/nov), o deputado Robert Garcia pede a Rubio que devolva o Flávio, o Flávio registra presença no Senado de Miami, o Lula confirma o G20. Nenhuma conclusão mudou. As previsões de 02/nov ficam como estão; a rodada 3, abaixo, refaz as mesmas perguntas com esses fatos.

## Rodada 3: as previsões refeitas com os fatos de hoje (04/nov)

Pedido dele, para o vídeo falar do dia de hoje: as mesmas 24 perguntas e os mesmos 4 cenários, os mesmos 4 modelos, com e sem a história, agora com o texto `texto_A_r3.md` (fatos até 04/nov: democratas nas duas casas pelas projeções, a carta do Garcia pedindo a devolução, a presença do Flávio no Senado de Miami, o Lula confirmado no G20, a primeira aparição dele). Gravada em `dados/previsoes/rodada3/`; a 1 e a 2 ficam congeladas e são cobradas pela data delas.

| | Rodada 2 (02/nov) | Rodada 3 (04/nov) |
|---|---|---|
| Pressão longa | 56,6% | 51,7% |
| Acordo | 18,7% | 20,4% |
| Escalada | 21,7% | 23,4% |
| Força | 3,0% | 4,5% |
| Lula vai ao G20 (P06) | 56% | 80,5% |
| Audiência na Câmara americana (P18) | 28,5% | 46,5% |
| STF contra americano (P24) | 78,5% | 57,5% |
| Prisão do Flávio decretada (P12) | 39% | 25,5% (de 6% a 50% entre modelos) |
| Tropa sem autorização até 2030 (P01) | 1,75% | 2,75% |
| Ataque contra facção até jan/2029 (P20) | 4% | 6% |

**Leitura:** a ordem dos cenários não mudou e a pressão longa segue a mais provável. As mudanças grandes são as que o fato novo explica (o G20 confirmado, o Congresso democrata); as outras, como a prisão e o STF, estão dentro da discordância entre modelos (16,9 pontos em média) e não devem ser lidas como efeito dos fatos. A invasão segue abaixo de 3%.

## O que falta olhar

~~03/nov midterms~~ (democratas na frente nas duas casas) · 13/nov prazo de Rubio · G7 · 14 e 15/dez G20 · 18/dez diplomação · 05/jan posse · 31/jan fim do mandato · 27/out/2027 fim da parole.
