import argparse
from src.create_measurements import (
    build_test_data,
    build_weather_station_name_list,
    estimate_file_size,
)
from src.loader import insert_values


def generator(num_rows_to_create: int) -> None:
    """
    Measurements generator
    """
    weather_station_names = build_weather_station_name_list()
    print(estimate_file_size(weather_station_names, num_rows_to_create))
    build_test_data(weather_station_names, num_rows_to_create)
    print("Arquivo de teste finalizado.")


def pipeline(num_rows_to_create: int) -> None:
    generator(num_rows_to_create)
    insert_values()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Gera dados de medição e carrega as métricas no DuckDB."
    )
    parser.add_argument(
        "--value_gen",
        type=int,
        required=True,
        help="Quantidade de linhas a gerar (mínimo de 10000).",
    )
    args = parser.parse_args()
    pipeline(args.value_gen)


if __name__ == "__main__":
    main()