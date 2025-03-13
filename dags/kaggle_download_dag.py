import sys
import os
from dotenv import load_dotenv

load_dotenv()

project_path = os.getenv("PROJECT_PATH")
download_path = os.getenv("DOWNLOAD_PATH")

if project_path:
    sys.path.append(project_path)
else:
    print("PROJECT_PATH not found in .env file.")

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.data_ingestion import download_and_unzip_kaggle_dataset 

# Default DAG args
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 13),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'kaggle_download_dag',
    default_args=default_args,
    description='A DAG to download and extract a Kaggle dataset',
    # schedule_interval='@daily',
    schedule_interval='*/5 * * * *',
    catchup=False,
)

download_task = PythonOperator(
    task_id='download_kaggle_dataset',
    python_callable=download_and_unzip_kaggle_dataset,
    op_kwargs={
        'dataset_origin': 'rashikrahmanpritom',
        'dataset_name': 'data-science-job-posting-on-glassdoor',
        'download_path': download_path,
    },
    dag=dag,
)

download_task
