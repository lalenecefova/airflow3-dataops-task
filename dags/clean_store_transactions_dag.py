from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator
from datetime import datetime

with DAG(
    dag_id="clean_store_transactions",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["dataops", "spark", "minio"],
) as dag:

    run_spark_job = SSHOperator(
        task_id="run_cleaning_job_on_spark",
        ssh_conn_id="spark_client_ssh",
        command="python /opt/project/spark_jobs/clean_store_transactions.py",
    )

    run_spark_job
