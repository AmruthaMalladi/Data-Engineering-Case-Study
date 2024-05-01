from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('advertising_data_pipeline', default_args=default_args, description='AdvertiseX Data Pipeline', schedule_interval=timedelta(days=1))

ingest_data = BashOperator(task_id='ingest_data', bash_command='python /path/to/kafka_ingestion.py', dag=dag)
process_data = BashOperator(task_id='process_data', bash_command='python /path/to/data_processing.py', dag=dag)

ingest_data >> process_data
