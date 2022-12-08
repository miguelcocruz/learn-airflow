from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

dag = DAG(
    dag_id="rocket_launch",
    schedule_interval=None,
    start_date=datetime(2022, 12, 1),
)

download_launches = BashOperator(task_id="download_launches", bash_command='')

get_pictures = BashOperator(task_id="get_pictures", bash_command='')

notify = BashOperator(task_id="notify", bash_command='')
