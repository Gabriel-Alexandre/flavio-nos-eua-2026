# Plano do projeto

**Escrito em 02/nov/2026, antes de qualquer contagem.** Relatório por rodadas (`docs/RODADAS.md`). As previsões de `dados/previsoes/` entram em commit antes do vídeo, porque são de coisas que ainda não aconteceram.

## Objetivo

Colocar a IA para estudar geopolítica e história, com métodos validados, e dizer o que esperar dos próximos passos depois da ida do Flávio Bolsonaro para os EUA, inclusive se os EUA vão usar a força. Não é previsão de destino. Não faz julgamento de voto, de intenção ou de culpa nos inquéritos.

## Hipótese de trabalho (para testar e poder derrubar)

Trump abriu a porta e, até aqui, não abriu o caminho. Abrigo americano, sozinho, não leva um exilado de volta ao poder; quando isso aconteceu, houve ocupação, guerra ou colapso do governo. A pressão mais provável é econômica e diplomática.

**O que derrubaria:** casos de abrigados pelos EUA que voltaram ao poder sem força americana nem colapso; ou medidas militares contra um país grande, com governo eleito, sem aval dele.

## Etapas

| Etapa | Pergunta | Método |
|---|---|---|
| E1 | o que aconteceu entre 25 e 28/10, por registro e por versão | leitura com dupla conferência |
| E2 | o que aconteceu com exilados parecidos | classe de referência, duas passadas independentes |
| E3 | o que os EUA fizeram nos 12 meses depois de o preferido perder | classe de referência |
| E4 | que medidas subiram e desceram contra o Brasil e outros | linha do tempo; literatura de sanções |
| E5 | quando os EUA usaram força no hemisfério, e que sinais vieram antes | indicadores e alerta |
| E6 | por que recebeu o Flávio | hipóteses concorrentes (Heuer) |
| E7 | o que esperar | cenários, escala ICD 203, previsões datadas, várias IAs separadas, nota de Brier depois |
| E8 | o que muda no Brasil | contrafactual simples |
| E9 | o que estão dizendo | checagem por afirmação |

## Regras da E2 (escritas antes)

**Entra:** chefe de Estado ou de governo, candidato à presidência, ou líder nacional da oposição, que saiu do país por derrota, deposição, processo ou repressão, de 1945 a 2026. A lista inicial está em `dados/casos/lista_e2.csv`, por dois critérios que não olham o resultado: **grupo EUA** (foi abrigado nos EUA) e **grupo comparação** (abrigado em outro país, em casos de grande repercussão citados na literatura ou pelo próprio Flávio). Fora: quem saiu só para morrer no exílio sem atividade política conhecida é mantido, com essa anotação, para não inflar a taxa de volta.

**Variáveis:** `saiu` (ano), `anfitriao`, `tipo` (deposto, derrotado_na_urna, processado, oposicao), `regime_casa` (democracia, hibrido, autocracia), `eua_apoio_declarado` (sim, nao), `voltou_ao_pais` (sim, nao), `anos_ate_voltar`, `voltou_ao_poder` (sim, nao: chefia do Executivo nacional ou cargo equivalente de comando), `caminho` (eleicao, forca_estrangeira, colapso_revolucao, acordo, nenhum), `entregue` (sim, nao: extradição ou deportação ao país de origem).

**Regra de contagem:** o estado até 02/nov/2026. Divergência entre passadas vai para adjudicação com a fonte; a concordância é publicada. Cada caso precisa de 2 fontes com trecho literal, conferido por script na página capturada.

## Regras da E7 (escritas antes)

Cada pergunta tem prazo e critério de resolução. Faixas do ICD 203: quase nenhuma 1-5%, muito improvável 5-20, improvável 20-45, chance parecida 45-55, provável 55-80, muito provável 80-95, quase certo 95-99. Cada modelo responde sem ver os outros. A resposta final é a mediana. A nota de Brier só se mede quando a pergunta resolver. Os modelos usados são todos da Anthropic neste projeto, e isso é um limite: não é uma multidão diversa.
