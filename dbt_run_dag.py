from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'imran',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='dbt_run_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:

    dbt_run = BashOperator(
        task_id='run_dbt_models',
        bash_command='cd /usr/app/dbt && dbt run --profiles-dir . --log-path /tmp/dbt-logs',
    )

    dbt_test = BashOperator(
        task_id='test_dbt_models',
        bash_command='cd /usr/app/dbt && dbt run --profiles-dir . --log-path /tmp/dbt-logs',
    )

    dbt_run >> dbt_test
