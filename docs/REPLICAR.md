# Refazer

Python 3.11, com `requests`, `beautifulsoup4`, `pypdf`, `matplotlib` e, para páginas que recusam o pedido direto, `playwright` com Edge.

```bash
python ferramentas/conferir_citacoes.py --capturar
python ferramentas/e2_concordancia.py
python dados/previsoes/preparar_r2.py
python ferramentas/agregar_previsoes.py
python ferramentas/analise.py
python ferramentas/validacao_independente.py
python ferramentas/gerar_relatorio.py
python ferramentas/graficos.py
python ferramentas/conferir_linguagem.py
```

As previsões são respostas de modelos, gravadas em `dados/previsoes/rodada1/`, `rodada2/` e `rodada3/` (04/nov, com `texto_A_r3.md`, `texto_B_r3.md` e as mesmas 24 perguntas em `perguntas_r3.csv`; `agregar_previsoes.py` usa a rodada 3 e compara com a 2). Refazer dá números parecidos, e não iguais: o que vale para cobrar é o que entrou em commit. Página da internet muda; o texto capturado com hash fica em `dados/capturas/` e `dados/MANIFESTO.json`.
