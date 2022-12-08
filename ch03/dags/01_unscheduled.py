from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

dag = DAG(
    dag_id="01_unscheduled",
    schedule_interval=None,
    start_date=datetime(2022, 12, 1),
)

fetch_events = BashOperator(
    task_id="fetch_events",
    bash_command="""
        mkdir -p /data &&
        curl -o /tmp/events.json events-api:5000/events
    """
)

