# Auditoria de método e de linguagem

**Feita em 02/nov/2026** sobre `RELATORIO.md`, `RESUMO_SIMPLES.md`, `docs/LEITURA_DA_IA.md` e `docs/PLANO.md`, conferidos contra `dados/casos/*.json`, `resultados/`, `dados/previsoes/` e os textos da pasta do vídeo 22 no repositório de documentação (`referencias/textos/`). 19 problemas, em ordem de gravidade. Nada foi alterado nos arquivos auditados.

## Alta gravidade

### 1. A hipótese é contrariada pelo critério que o próprio plano escreveu

- **Trecho:** RESUMO: "Quando Washington queria alguém de volta, houve tropa ou apoio de ocupação, e em país pequeno." RELATORIO §3: "Os dois casos que o abrigo americano ajudou a colocar no poder eram de país pequeno ou em guerra, com presença militar americana." LEITURA 6: "A hipótese inicial sobreviveu com corte."
- **Problema:** dos 3 abrigados nos EUA que chegaram ao poder, só Aristide voltou com força americana. Kim Dae-jung foi eleito em 1997, 12 anos depois de voltar, sem papel americano no resultado. Diem foi nomeado por Bao Dai em 1954; nenhuma fonte do arquivo fala em tropa americana no Vietnã nesse ano. O PLANO diz que derrubaria a hipótese "casos de abrigados pelos EUA que voltaram ao poder sem força americana nem colapso". Kim e, com a dúvida marcada, Diem se encaixam. O texto diz o contrário e ainda descreve o Vietnã de 1954 como país "com presença militar americana".
- **Evidência:** `resultados/e2_casos_final.csv` (kim-dae-jung: caminho `eleicao`; diem: caminho `acordo`); `dados/casos/e2_passada_b.json` (diem: "incerto": true, "governo apoiado pelos EUA"; kim: "apoio dos EUA foi à libertação"); `docs/PLANO.md` (seção "O que derrubaria").
- **Redação corrigida:** "Dos 3 abrigados nos EUA que chegaram ao poder, só Aristide voltou com força americana. Diem foi nomeado por Bao Dai em 1954, com apoio dos EUA, e Kim Dae-jung foi eleito em 1997, depois da democratização. Pelo critério escrito no plano, esses dois casos contrariam a hipótese de que, sem força ou colapso, o abrigo não leva ao poder. O que a base sustenta é mais estreito: em 3 de 22, o abrigo americano esteve na história de um retorno ao poder, por três caminhos (acordo, eleição, força)." Para o RESUMO: "Dos 3 que voltaram ao poder, um voltou com tropa americana, um por nomeação com apoio americano e um por eleição, anos depois."

### 2. A codificação de "apoio declarado" é incoerente e decide a tabela

- **Trecho:** RELATORIO §3, linha "Nos EUA, com apoio declarado de Washington | 6 | 4 | **2** | 9.7% a 70.0%"; e "Guaidó, Machado e Chalabi tiveram apoio e não chegaram à chefia".
- **Problema:** Eduardo Bolsonaro entra como "sim" enquanto a anotação do próprio caso diz "sem declaração de apoio a ele como exilado". Kim Dae-jung entra como "não" depois de divergência entre as passadas, e a passada B registra que o governo americano interveio para comutar a pena. Chalabi foi presidente rotativo do Conselho de Governo por um mês, nomeado pelos EUA, e está marcado como incerto; o texto diz que não chegou à chefia. A conclusão do grupo (2 de 6) vira 3 de 6 ou 4 de 6 com escolhas igualmente defensáveis.
- **Evidência:** `resultados/e2_divergencias.csv` (kim-dae-jung, eua_apoio_declarado: nao x sim); `resultados/e2_casos_final.csv` (eduardo-bolsonaro e chalabi, campo obs); `dados/casos/e2_passada_b.json` (chalabi "incerto": true).
- **Redação corrigida:** "2 de 6 como codificado. Com as dúvidas registradas, a conta muda: 3 de 6 (18,8% a 81,2%) se Kim Dae-jung entrar como apoiado e Eduardo Bolsonaro sair, e 4 de 6 se Chalabi, que presidiu por um mês o Conselho de Governo nomeado pelos EUA, também contar. Com margem tão larga, a tabela não separa quem teve apoio de quem não teve." Trocar "não chegaram à chefia" por "Guaidó e Machado não chegaram à chefia; Chalabi só presidiu o Conselho de Governo por um mês, em rodízio".

### 3. A seção de validação está com marcadores vazios e cita arquivos que não existem

- **Trecho:** RELATORIO §11: "Citações: ? de ? trechos achados na página capturada por este projeto (? de ? páginas abriram para o robô)." Também "Revisão por 3 leitores: `docs/REVISAO_ADVERSARIAL.md`." e "Refazer: `docs/REPLICAR.md`." PLANO: "Relatório por rodadas (`docs/RODADAS.md`)." RELATORIO §2: "com trechos conferidos".
- **Problema:** o script de conferência não rodou (`citacoes` é `null` no RESUMO.json), os três arquivos citados não existem em `docs/` e o §2 afirma trechos conferidos. O leitor recebe uma promessa de checagem que o repositório não cumpre.
- **Evidência:** `resultados/RESUMO.json` (`"citacoes": null`); listagem de `docs/` (só `LEITURA_DA_IA.md`, `PLANO.md` e esta pasta); `ferramentas/gerar_relatorio.py` linhas 210 a 214.
- **Redação corrigida:** rodar `ferramentas/conferir_citacoes.py` e preencher os números reais, ou escrever "Citações: conferência automática ainda não feita; os trechos foram lidos pelo agente nas páginas abertas." Remover as três referências a arquivos até eles existirem. No §2, trocar "com trechos conferidos" por "com trechos lidos pelo agente".

### 4. A contradição com o estudo de 2025 é de definição, e a explicação dada não tem sustento

- **Trecho:** RELATORIO §3: "Hidaka, Kubota e Yukawa (2025) dizem que a maioria dos líderes exilados volta e retoma o poder. Lemos o resumo. A base deles é de líderes que perderam o cargo, em geral sob regime fechado; a nossa inclui candidatos e opositores, e casos ainda abertos." RESUMO: "acaba voltando, pela política de casa".
- **Problema:** a versão de trabalho de 2022 do mesmo estudo está na pasta de textos e traz os números. São 91 líderes de 1970 a 2014, sem recorte por regime. Voltaram 53 (58%; 68% sem contar quem segue no exílio). Desses 53, 58% recuperaram algum cargo público e outros 19% voltaram à chefia de Estado, cerca de 11% dos 91. A taxa de voltar ao país (54%, 21 de 39) e a de chefia do Executivo (15%, 6 de 39) são da mesma ordem. "Retoma o poder" no resumo quer dizer cargo público, e não chefia. A frase "em geral sob regime fechado" e o "pela política de casa" não aparecem no resumo nem no texto lido.
- **Evidência:** `referencias/textos/metodo/osaka-lideres-exilio.txt` (seções 2, 3.1 e 3.2); `referencias/textos/metodo/ideas-lideres-exilio-2025.txt` (resumo do artigo de 2025); `resultados/e2_casos_final.csv`.
- **Redação corrigida:** "Hidaka, Kubota e Yukawa (2025) dizem que a maioria dos líderes exilados volta e retoma o poder. Na versão de trabalho de 2022 (91 líderes, 1970 a 2014), 58% voltaram ao país; desses, 58% recuperaram algum cargo público e 19% voltaram à chefia de Estado, cerca de 11% do total. A nossa taxa de chefia do Executivo é de 15% (6 de 39), da mesma ordem. A diferença está no que conta como 'retomar o poder', e não na base. Lemos a versão de 2022 e o resumo do artigo de 2025; os números do artigo podem diferir." No RESUMO: "um estudo diz que a maioria dos líderes exilados volta ao país, e que cerca de um em cada nove volta à chefia de Estado."

### 5. "33 medidas contra o Brasil" inclui medidas que não são isso

- **Trecho:** RELATORIO §5: "33 medidas de jan/2025 a nov/2026: 26 para cima, 7 para baixo, 0 militares." RESUMO: "33 medidas contra o Brasil".
- **Problema:** a contagem soma 3 medidas do Brasil contra os EUA (br-017, br-025, br-028), 3 medidas globais não dirigidas ao Brasil (br-001, br-002, br-024), o ofício do Itamaraty (br-022), uma reportagem (br-030) e a parole e as falas de Rubio e Trump (br-031, br-032), que o próprio arquivo diz não serem medida contra o Brasil. São pelo menos 10 dos 33. O arquivo também registra que a busca "esgotou o limite antes de varrer set/out de 2026", e isso não aparece no relatório. A comparação com Colômbia, México, Canadá e África do Sul fica desigual.
- **Evidência:** `dados/casos/e4_escada.json` (campos `convencoes`, `pontos_que_mudam_a_pesquisa_do_video`, `sem_confirmar`; ids br-001, 002, 017, 022, 024, 025, 028, 030, 031, 032).
- **Redação corrigida:** "33 registros na linha do tempo de jan/2025 a 02/nov/2026. Pelo menos 10 não são medida americana dirigida ao Brasil (medidas globais, medidas do Brasil contra os EUA, um ofício, uma reportagem e a entrada de Flávio). Nenhum registro é militar. A busca não varreu bem setembro e outubro de 2026, então a contagem de 'para cima' pode estar baixa nesse período." Para a comparação com outros países, contar só medidas dirigidas ao país nos dois lados ou retirar a frase.

### 6. Duas linhas da tabela das 72 horas se contradizem sobre a ponte

- **Trecho:** RELATORIO §2: "A ponte | Migraciones: 22h50 e embarque às 23h30. Fantástico: 3 registros na van ... | a passagem está confirmada; o horário tem conflito entre as fontes" e, na linha seguinte, "Brasília até a ponte | Fantástico: linha de investigação com voo às 5h05 por Buenos Aires".
- **Problema:** o Fantástico diz que "apesar do registro de entrada terrestre, a principal linha de investigação" é que Flávio chegou a Puerto Iguazú de avião, vindo de Buenos Aires, e esperou dentro da aeronave a chegada da família. Se essa linha vale, a passagem dele pela ponte não está confirmada. O registro de Migraciones confirma a entrada de quatro pessoas pelo posto, e não onde Flávio estava. A linha do ex-agente repete o problema: o IBTimes (via CNN Brasil) diz que ele acompanhou Flávio ao cruzar a fronteira, e o Fantástico o põe em outra van, sete minutos antes.
- **Evidência:** `referencias/textos/saida/otempo-fantastico-carros.txt` (trechos "Flávio ficou dentro de jato aguardando chegada de mulher e filhas" e "Apesar do registro de entrada terrestre"); `saida/terra-bastidores-fantastico.txt` linhas 23 a 36; `saida/ibtimes-mossad-jato.txt` linha 17; `dados/casos/e1_originais.json` (E1-b1, E1-b2, E1-i1).
- **Redação corrigida:** "A ponte | Migraciones registra a entrada de quatro pessoas às 22h50 pela ponte Tancredo Neves. O Fantástico registra três entradas na mesma van (22h37, 22h40 e 23h11) e diz que a principal linha de investigação é que Flávio chegou de avião e esperou a família na pista | o registro de entrada é confirmado; que Flávio estava na van não é". Na linha do Mossad: "um homem apontado como ex-oficial do Mossad; o Fantástico o põe em outra van, a CNN Brasil ao lado de Flávio; não prova ação do Mossad". Avaliar tirar o nome próprio, porque o IBTimes diz que a identidade não foi tornada pública.

## Média gravidade

### 7. "Parole humanitária" afirma mais do que o governo disse

- **Trecho:** RELATORIO §1: "Entrou por parole humanitária."
- **Problema:** Rubio só diz "paroled". A palavra "humanitária" vem do Terra e do DN, que dizem "teriam entrado" com permissão por "razões humanitárias", a partir do código "DT" obtido pelo O Globo. O próprio Terra explica que essa admissão serve para "razões humanitárias" ou para "benefício público significativo". O governo não disse qual.
- **Evidência:** `referencias/textos/oficial/state-rubio-atlanta.txt` ("he would be paroled into the country, and he was"); `saida/terra-parole-um-ano.txt`; `dados/casos/e1_originais.json` (E1-a4, E1-h4).
- **Redação corrigida:** "Entrou por parole, uma permissão temporária de entrada. Rubio não disse o motivo; a imprensa lê o registro 'DT' como parole humanitária ou por benefício público significativo. Não é visto nem asilo, e vale até 27/10/2027."

### 8. O relatório declara que não julga intenção e julga

- **Trecho:** RELATORIO, abertura: "A intenção de ninguém. Os motivos abaixo são o que as evidências sustentam mais, em julgamento declarado da IA." Seção "7. Por que receber o Flávio". LEITURA 1: "Trump usa o caso mais do que aposta nele."
- **Problema:** a lista de limites diz que o projeto não diz a intenção de ninguém e, três seções depois, ordena motivos de Trump e de Rubio. A matriz conta evidências a favor e contra; ela não mede motivo. "Usa o caso" atribui um propósito.
- **Evidência:** `dados/e6_hipoteses.csv` (17 evidências com sinais +, - e 0 atribuídos pela IA); `docs/LEITURA_DA_IA.md` item 1.
- **Redação corrigida:** abertura: "A intenção de ninguém. A seção 7 compara hipóteses de motivo pelo número de evidências a favor e contra, em julgamento da IA, e não decide entre elas." Seção 7: "Hipóteses sobre o motivo". LEITURA 1: "Até 31/10, as falas de Trump sobre o caso são curtas, vêm junto com acusações de fraude eleitoral e não trouxeram ato além da parole."

### 9. O cenário "A força" fica abaixo de uma pergunta que ele contém, e a soma não fecha

- **Trecho:** RELATORIO §9: "| **A força** | Ação militar americana em território brasileiro sem aval do Brasil | **2%** | 1 a 3 |"; "somados a 100"; e no §1 "Os EUA vão invadir? | 2% até 2030".
- **Problema:** P02 (ataque a PCC ou CV em solo ou águas brasileiras sem aval, até 2027) está em 3,5%. Ele é um caso de ação militar em território brasileiro sem aval, logo o cenário não pode ser menor. Nas 8 respostas dos 4 modelos, o cenário ficou abaixo da pergunta (por exemplo, com a história: fable 3 e 5, haiku 2 e 3, opus 1 e 2, sonnet 3 e 4). Os valores arredondados 54, 23, 20 e 2 somam 99. A resposta de "invadir" (2%) responde por tropas (P01), e a chance de ataque até 2027 é maior.
- **Evidência:** `resultados/previsoes_final.json` (cenarios C4 com_historia_normalizado 2,5; P02 com_historia 3,5); `dados/previsoes/rodada1/*.json`; `dados/previsoes/perguntas.csv`.
- **Redação corrigida:** reconciliar C4 com P02 (C4 não menor que 3,5%) e renormalizar, ou escrever a diferença de definição. Mostrar uma casa decimal (54,5; 22,8; 20,3; 2,5) ou trocar por "soma 100, com arredondamento". No §1: "Os EUA vão usar a força? Tropas em solo brasileiro sem aval: 2% até 2030. Ataque a PCC ou CV em território brasileiro sem aval: 3,5% até 2027."

### 10. "Tropas só em países que aceitaram" contradiz a tabela do próprio relatório; Múcio sai sem o contexto

- **Trecho:** RELATORIO §6: "Tropas em 2026 só aparecem em países que aceitaram, ou em treinamento." e "ministro Múcio, *"abrir o portão"*, em 04/08".
- **Problema:** a tabela de força lista, em 2026, a captura de Maduro (aval "nao") e o bloqueio a Cuba (aval "nao"). Quanto a Múcio, o texto do Poder360 diz que ele falou "em tom de brincadeira", ao defender mais verba, e que o Brasil não tem equipamento para enfrentar os EUA. O trecho guardado em `e5_sinais.json` para essa URL trata do visto da embaixadora, não de Múcio, e a página não está em `dados/capturas/`. Aparece em "Base do medo, tudo real" sem esse contexto.
- **Evidência:** `dados/casos/e5_forca.json` (venezuela-jan-2026, cuba-2026-bloqueio-petroleo); `dados/casos/e5_sinais.json` (url mucio-diz-que-abriria-o-portao); `referencias/textos/invasao/poder360-mucio-portao.txt`.
- **Redação corrigida:** "Em 2026, a força sem aval do país aparece na captura de Maduro e no bloqueio de petróleo a Cuba. Operações com aval, como no Equador, e tropas em treinamento no Panamá, na Colômbia e em Honduras são outra coisa." E: "o ministro Múcio disse em 04/08, em tom de brincadeira, que 'abriria o portão', porque o Brasil não tem equipamento nem dinheiro para enfrentar os EUA, ao pedir mais verba para a Defesa". Mover essa frase para fora de "tudo real" ou marcá-la como fala de ministro, e não como sinal americano.

### 11. "Força militar nos 12 meses, 0 de 9" omite o caso que tem força depois da janela e os "não" por ausência

- **Trecho:** RELATORIO §4: "o reconhecimento é a regra (8 de 9), e força militar nos 12 meses, 0 de 9."
- **Problema:** em Venezuela 2024 a captura de Maduro veio 17 meses depois da eleição, e o arquivo marca o campo como incerto e diz que o caso é "diferente dos demais". Outros campos "nao" de sanção, apoio e força são ausência de fonte, e o arquivo avisa. A Hungria foi codificada como reconhecimento "sim" sem felicitação formal localizada. O texto cita o golpe do Chile fora da janela e não cita a Venezuela, que é o caso mais próximo do tema.
- **Evidência:** `dados/casos/e3_derrotas.json` (venezuela-2024 obs; hungria-2026 obs; `resumo_contagem.aviso`).
- **Redação corrigida:** "Reconhecimento em 8 de 9 (na Hungria, sem felicitação formal localizada). Força militar nos 12 meses seguintes: nenhuma nas fontes lidas, em 9 de 9. Na Venezuela a captura de Maduro veio 17 meses depois da eleição, fora da janela. Vários 'nao' de sanção, apoio e força são ausência de fonte, e não fonte dizendo que não houve."

### 12. "Mais 12,5%" é dado como fato e a fonte do relatório diverge de si mesma

- **Trecho:** RELATORIO §5: "25% pela Seção 301 desde 22/07/2026, mais 12,5% da ação global sobre cerca de 60 economias."
- **Problema:** E8-19 registra divergência: Thompson Coburn e PIIE dizem que os 12,5% empilham com os 25% (37,5%); a Global Trade Alert diz que o tributo só substitui a Seção 122. A ordem final para o Brasil não foi aberta. E4 diz "37,5% em parte dos produtos". O texto passa a soma como certa, e a mesma frase está na ficha dada aos modelos de previsão.
- **Evidência:** `dados/casos/e8_brasil.json` (E8-18, E8-19, `incerto`: true); `dados/casos/e4_escada.json` (br-024); `dados/previsoes/texto_A.md`.
- **Redação corrigida:** "25% pela Seção 301 desde 22/07/2026. Desde 24/07 há também uma tarifa global de 12,5% sobre cerca de 60 economias; duas fontes dizem que ela se soma aos 25% em parte dos produtos (37,5%) e a Global Trade Alert diz que ela só substitui a tarifa temporária anterior."

### 13. "A PF diz que ele não é foragido" encurta a nota

- **Trecho:** RELATORIO, abertura: "a PF diz que ele não é foragido". RESUMO: "Ele não é foragido, segundo a PF."
- **Problema:** a nota diz que as restrições de passaporte, "por si só", não caracterizam foragido nem autorizam prisão. Isso é uma afirmação sobre o efeito da restrição, escrita depois de ele ter saído, e a mesma nota diz que não há registro oficial de saída. Resumir como "não é foragido" lê a nota como um atestado de situação.
- **Evidência:** `dados/casos/e1_originais.json` (E1-d1, trecho do Poder360); `dados/capturas` (título "PF diz que restrição de passaportes não torna Flávio Bolsonaro foragido").
- **Redação corrigida:** "A PF disse em nota que a restrição de passaporte, por si só, não torna Flávio foragido nem autoriza prisão, e que não há registro oficial da saída dele pelos postos brasileiros."

### 14. Rubio é resumido de um jeito que sugere contradição e que troca "permitir" por "ajudar"

- **Trecho:** RESUMO: "Trump decidiu deixar ele entrar, e Rubio disse isso em público ao mesmo tempo em que disse *"não facilitamos nada"*." RELATORIO §1: "Os EUA ajudaram? | A entrada, sim".
- **Problema:** Rubio respondeu a uma pergunta sobre ajudar a fuga. Disse "We didn't facilitate anything", que o presidente decidiu permitir a entrada, que "we were not involved in any of the arrangements he made in terms of leaving" e, depois, "At least the U.S. Government was not involved directly". Colocar as duas frases lado a lado sugere duplicidade. "Ajudaram a entrada" é leitura do relatório sobre um ato de admissão. As aspas em português traduzem uma fala em inglês.
- **Evidência:** `referencias/textos/oficial/state-rubio-atlanta.txt` linha 233; `docs/LEITURA_DA_IA.md` item 2.
- **Redação corrigida:** RESUMO: "Rubio disse que o presidente decidiu permitir a entrada, que ele chegaria como parole, e que o governo americano 'não esteve envolvido diretamente' nos arranjos da saída." RELATORIO §1: "Os EUA permitiram a entrada (decisão de Trump, segundo Rubio, por parole). Sobre a saída, Rubio nega envolvimento direto do governo; reportagens ligam um assessor de Trump ao jato."

### 15. "Pix atingido pela designação" não tem sustento, e "menos debate" é afirmação solta

- **Trecho:** RELATORIO §9 e `cenarios.csv`, cenário A escalada: "bancos ou Pix atingidos pela designação". LEITURA 4: "o instrumento com mais alcance e menos debate".
- **Problema:** E8-27 procurou "Pix" em oito textos de escritórios sobre a designação e nenhum cita; a menção vem de uma hipótese de professor da FGV. O Pix aparece na investigação da Seção 301, que é outro processo. "Menos debate" não tem fonte, e o relatório mostra o ofício do Itamaraty e a resposta do Departamento de Estado em torno da designação.
- **Evidência:** `dados/casos/e8_brasil.json` (E8-27, `incerto`: true); `dados/casos/e5_sinais.json` (sinal de ofício e negativa).
- **Redação corrigida:** "Nova sanção forte, bancos atingidos pela designação, ou ação sobre o Pix na linha da Seção 301, autoridades de volta à lista, prisão decretada com recusa americana; sem ação militar". LEITURA 4: "A designação de PCC e CV é o instrumento americano de maior alcance financeiro, segundo os escritórios de advocacia lidos."

### 16. Os grupos têm fronteira frouxa e a contagem mistura situações

- **Trecho:** RELATORIO §1 e RESUMO: "Dos 22 abrigados nos EUA, 3 voltaram; dos 7 mais parecidos com ele, 0". PLANO: "Fora: quem saiu só para morrer no exílio sem atividade política conhecida é mantido".
- **Problema:** pelas anotações do arquivo, 3 dos 22 não ficaram abrigados: Somoza ("não foi abrigado de fato"), o Xá (anfitrião Egito, nos EUA só para tratamento médico) e Jair Bolsonaro ("não é exílio prolongado"). Bosch, em Porto Rico (território dos EUA), está no grupo "outro país". Dos 11 que "voltaram ao país", 3 foram extraditados (Pérez Jiménez, Toledo, Martinelli). Dos 7 mais parecidos, Eduardo Bolsonaro e Ramagem seguem fora, então o "0" é de agora, e não de desfecho. A tabela do §1 diz "3 voltaram" sem dizer "ao poder", ao lado de uma coluna "Voltaram ao país: 11". O PLANO se contradiz na regra ("Fora ... é mantido"). A mediana de 5,5 anos é só dos 6 que chegaram ao poder (dos 21 que voltaram ao país, a mediana é 4). Os códigos "eleicao", "forca_estrangeira" e "colapso_revolucao" saem crus no texto.
- **Evidência:** `resultados/e2_casos_final.csv` (campos obs de somoza, xa-ira, jair-bolsonaro, bosch, eduardo-bolsonaro, ramagem); `resultados/RESUMO.json` (`anos_ate_voltar_mediana`).
- **Redação corrigida:** "Dos 22 casos do grupo EUA (3 deles, pelas anotações, não chegaram a ser abrigados), 3 voltaram ao poder. Dos 7 mais parecidos com ele, nenhum voltou ao poder até hoje; dois ainda estão fora do Brasil, e dois foram extraditados." Na lista: "Diem, por nomeação; Kim Dae-jung, por eleição; Aristide, com força estrangeira; Perón, por eleição; Khomeini, pelo colapso do regime; Sharif, por eleição. Entre esses seis, a mediana foi de 5,5 anos até voltar ao país." Trocar a regra do PLANO por "é mantido, com essa anotação".

### 17. Atribuição de fonte nas linhas da Argentina e de Jason Miller

- **Trecho:** RELATORIO §2: "participação oficial provável; os detalhes têm uma fonte" e "O jato liga a um assessor de Trump, segundo Reuters, NYT e WSJ" (§1), "apurado por três veículos".
- **Problema:** a participação do governo argentino repousa em fontes anônimas ("otras fuentes oficiales"), em um repórter da C5N e no Clarín citando "fontes da Casa Rosada", enquanto Santilli e Migraciones dizem entrada legal e a Casa Rosada nega. "Provável" é nota do relatório, e não de fonte. NYT e WSJ são pagos e não foram abertos: o que há é SBT, Midiamax e AFP resumindo-os, mais a Reuters citando uma pessoa. O cargo de Miller diverge (assessor de Trump para a Reuters, funcionário de comunicações da Casa Branca para o NYT, segundo o Midiamax), e isso muda o peso do "não tem prova de participação americana" no mesmo parágrafo.
- **Evidência:** `dados/casos/e1_originais.json` (E1-b3, E1-c1, E1-c2, E1-g1, E1-h1, E1-h2); `referencias/textos/saida/otempo-fantastico-carros.txt`.
- **Redação corrigida:** Argentina: "Fontes anônimas e reportagens falam em planejamento com autoridades americanas e em acompanhamento de assessores do governo Milei; o governo argentino diz que a entrada foi legal e a Casa Rosada nega a articulação. Sem confirmação oficial". Miller: "A Reuters, citando uma pessoa, e o NYT e o WSJ, conhecidos aqui por resumos de outros veículos, ligam Jason Miller ao jato. A Reuters o chama de assessor de Trump; o NYT, segundo o Midiamax, de funcionário de comunicações da Casa Branca".

### 18. A leitura do tratado de extradição é inferência sem as acusações

- **Trecho:** LEITURA 3: "O tratado não lista lavagem nem evasão, mas lista suborno e peculato, e por isso o caso Dark Horse pesa mais que o outro."
- **Problema:** o tratado de 1961 lista suborno e peculato (itens 23 e 24), mas também receptação de dinheiro obtido ilegalmente e fraude por quem está em posição de confiança (19 e 20), que podem tocar lavagem. Existe a exceção para crime político, que a defesa pode usar. A ficha dada aos modelos fala em "corrupção, lavagem e evasão" no Dark Horse, sem dizer quais crimes são imputados. A ficha também diz "dois inquéritos", enquanto a Lupa lista três (Dark Horse, calúnia contra Lula, lavagem e evasão com Willer Tomaz).
- **Evidência:** `referencias/textos/oficial/camara-tratado-extradicao.txt` (lista de crimes); `oficial/un-tratado-extradicao.txt` linhas 197 a 207; `referencias/textos/flavio/lupa-carta.txt` linha 152; `dados/previsoes/texto_A.md`.
- **Redação corrigida:** "O tratado de 1961 lista suborno e peculato; lavagem e evasão de divisas não aparecem pelo nome, e o tratado prevê exceção para crime político. O que isso significa para cada inquérito depende das acusações, que este projeto não leu. Flávio é investigado em três inquéritos no STF, segundo a Lupa."

## Baixa gravidade

### 19. Pontos menores

- **Trecho:** "Fala de candidato democrata do Texas, não ordem" (§10). **Problema:** E1-f1 marca como incerto: o JB o chama de candidato ao Congresso, o Diario de Pernambuco de comentarista político. **Redação:** "Fala de Isaiah Martin, descrito como candidato democrata ao Congresso pelo Texas ou como comentarista, e não ordem do governo". **Evidência:** `dados/casos/e1_originais.json` (E1-f1).
- **Trecho:** §7: "Trump ligou o Brasil à fraude dos democratas no comício do Texas". **Problema:** a transcrição diz que os democratas são os maiores fraudadores e "Brazil is doing a pretty good job also", sem dizer o que o Brasil teria feito; o E1 avisa que "nisso" não está na transcrição. **Redação:** "No comício do Texas, Trump chamou os democratas de maiores fraudadores e acrescentou que o Brasil 'está fazendo um bom trabalho também', sem dizer em quê". **Evidência:** E1-e2.
- **Trecho:** §2: "Ex-agente do Mossad". **Problema:** a linha afirma no rótulo o que as fontes chamam de "apontado como ex-oficial". **Redação:** "Homem apontado como ex-oficial do Mossad". **Evidência:** `saida/otempo-fantastico-carros.txt` linha 55.
- **Trecho:** §3: "Alejandro Toledo, Ricardo Martinelli foram entregues." **Problema:** falta o "e" na lista de dois nomes. **Redação:** "Alejandro Toledo e Ricardo Martinelli foram entregues."
- **Trecho:** §7: "Os minerais explicam o interesse no Brasil, e os EUA já têm posição com Lula no governo." **Problema:** é conclusão da IA apresentada como fato, sem fonte na frase. **Redação:** "Os minerais explicam o interesse dos EUA no Brasil, e as fontes lidas mostram os EUA investindo em Serra Verde com Lula no governo." **Evidência:** `dados/e6_hipoteses.csv` (linha de Serra Verde).
