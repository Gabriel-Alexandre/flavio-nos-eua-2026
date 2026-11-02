# Fontes de dados

| Dado | De onde | Arquivo |
|---|---|---|
| A saída, a entrada e as falas | state.gov, nota da PF, Migraciones, Reuters, AFP, Clarín, Fantástico e outros | `dados/casos/e1_originais.json` |
| Exilados | Britannica, Wikipedia, encyclopedia.com e imprensa, em duas passadas | `dados/casos/e2_passada_a.json`, `e2_passada_b.json`, `dados/e2_extra.csv` |
| Derrota do preferido de Washington | imprensa e documentos do governo americano | `dados/casos/e3_derrotas.json` |
| Medidas contra o Brasil | Federal Register, OFAC, USTR, state.gov, gov.br | `dados/casos/e4_escada.json`, `dados/e4_categorias.csv` |
| Força no hemisfério e sinais | Airwars, CRS, imprensa, Wikipedia | `dados/casos/e5_forca.json`, `e5_sinais.json` |
| Literatura | Hufbauer et al., Pape, O'Rourke, Levin, Hidaka et al. | `dados/casos/e5_literatura.json` |
| Hipóteses | este projeto, com 2ª codificação às cegas | `dados/e6_hipoteses.csv`, `dados/e6_segunda_codificacao.csv` |
| Brasil | ComexStat, Banco Central, Amcham, White & Case, Simpson Thacher | `dados/casos/e8_brasil.json` |
| O que circula | YouTube, cartas e falas do Flávio | `dados/e9_o_que_circula.csv` |
| Previsões | modelos Claude, em condições separadas | `dados/previsoes/` |
| Texto de cada página | captura própria, com hash | `dados/capturas/`, `dados/MANIFESTO.json` |
| Situação de cada trecho citado | este projeto | `resultados/citacoes.csv` |

Wikipedia e enciclopédia só entram para fato histórico antigo, com 2ª passada independente. Fato de 2026 tem fonte primária ou duas de imprensa, ou fica marcado.
