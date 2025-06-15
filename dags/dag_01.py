from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def my_python_task():
    print("Hello, Airflow!")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 1),
    'catchup': False
}

with DAG('dag_01', default_args=default_args, schedule='@daily') as dag:
    task1 = PythonOperator(
        task_id='print_hello',
        python_callable=my_python_task
    )

    task1