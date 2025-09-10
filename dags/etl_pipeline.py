from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import sqlite3
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/input_data.csv")
DB_PATH = os.path.join(os.path.dirname(__file__), "../outputs/etl_output.db")

def extract():
    df = pd.read_csv(DATA_PATH)
    return df.to_json()  # pass via XCom

def transform(ti):
    df = pd.read_json(ti.xcom_pull(task_ids="extract"))
    df["total"] = df["quantity"] * df["price"]
    return df.to_json()

def load(ti):
    df = pd.read_json(ti.xcom_pull(task_ids="transform"))
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("sales", conn, if_exists="replace", index=False)
    conn.close()

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="etl_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    description="Simple ETL pipeline with Airflow",
) as dag:

    t1 = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    t2 = PythonOperator(
        task_id="transform",
        python_callable=transform,
    )

    t3 = PythonOperator(
        task_id="load",
        python_callable=load,
    )

    t1 >> t2 >> t3   # dependencies
