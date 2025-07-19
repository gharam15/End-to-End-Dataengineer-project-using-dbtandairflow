from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 5, 25),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'dbt_snowflake_workflow',
    default_args=default_args,
    description='Run dbt models using dbt Core',
    schedule_interval='@daily',
    catchup=False
) as dag:

    # Define the path to your dbt project
    DBT_PROJECT_DIR = "E:\dbt_project\snowflake_data_project"

    # Task 1: Run dbt models
    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command=f'cd {DBT_PROJECT_DIR} && dbt run'
    )

    # Task 2: Run dbt tests
    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command=f'cd {DBT_PROJECT_DIR} && dbt test'
    )

    dbt_run >> dbt_test
