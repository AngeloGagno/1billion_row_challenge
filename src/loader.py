from pathlib import Path
import duckdb
from src.metrics import get_metrics_by_each_city
import time
DB_PATH = Path(__file__).resolve().parent.parent / "data" / "database.duckdb"
def insert_values() -> None:
    begin = time.time()
    with duckdb.connect(str(DB_PATH)) as con:
        con.execute(
            "CREATE TABLE IF NOT EXISTS metrics "
            "(avg_temp DOUBLE, min_temp DOUBLE, max_temp DOUBLE, city VARCHAR)"
        )
        rel = get_metrics_by_each_city(con)
        con.execute("INSERT INTO metrics SELECT * FROM rel")
    took = time.time() - begin
    print(f"Took: {took:.2f} sec")   
    
if __name__ == "__main__":
    insert_values()