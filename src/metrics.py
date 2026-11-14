from pathlib import Path
import duckdb

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "measurements.txt"


def get_metrics_by_each_city(con: duckdb.DuckDBPyConnection | None = None):
    conn = con or duckdb
    return conn.sql(
        f"""
        SELECT
            CAST(AVG(temperature) AS DECIMAL(3,1)) AS avg_temp,
            MIN(temperature) AS min_temp,
            MAX(temperature) AS max_temp,
            station AS city
        FROM read_csv(
            '{DATA_PATH.as_posix()}',
            AUTO_DETECT=FALSE,
            sep=';',
            columns={{'station': 'VARCHAR', 'temperature': 'DECIMAL(3,1)'}}
        )
        GROUP BY 4
        ORDER BY 4
        """
    )