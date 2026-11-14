# 1billion row challenge

Implementacao em Python e DuckDB para o One Billion Row Challenge (1BRC), responsavel por gerar dados sinteticos de temperatura por estacao meteorologica, calcular agregacoes (media, minima e maxima por cidade) e persistir os resultados em um banco DuckDB.

## Requisitos

- Python >= 3.12
- [uv](https://docs.astral.sh/uv/) para gerenciamento de ambiente e dependencias
- Dependencia principal: `duckdb>=2.0.0`

## Estrutura do Projeto

```text
.
├── data/
│   └── weather_stations.csv    # Lista de estacoes usada na geracao dos dados
├── src/
│   ├── __init__.py             # Entrypoint padrao do pacote
│   ├── create_measurements.py  # Gerador do arquivo data/measurements.txt
│   ├── metrics.py              # Consulta DuckDB para calcular avg, min e max por cidade
│   ├── loader.py               # Criacao da tabela e insercao das metricas no DuckDB
│   └── main.py                 # Orquestrador do pipeline via CLI
├── pyproject.toml
└── README.md
```

## Instalacao

Na raiz do projeto, sincronize o ambiente virtual e as dependencias:

```powershell
uv sync
```

## Como Executar

Execute o pipeline completo a partir da raiz do projeto informando a quantidade de linhas a serem geradas em `--value_gen`:

```powershell
uv run python -m src.main --value_gen 100000
```

Observacoes sobre os parametros e saidas:
- `--value_gen`: parametro obrigatorio que define a quantidade de registros gerados em `data/measurements.txt`. Como o gerador processa lotes de `10000` linhas (`batch_size`), utilize valores maiores ou iguais a `10000`.
- O resultado agregado (`avg_temp`, `min_temp`, `max_temp`, `city`) e gravado na tabela `metrics` do arquivo `data/database.duckdb`.

Caso o arquivo `data/measurements.txt` ja exista e voce queira executar apenas o calculo e a carga no banco:

```powershell
uv run python -m src.loader
```
