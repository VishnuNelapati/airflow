from airflow import DAG
from airflow.operators.bash import BashOperator
from groups.group_downloads import downloads_task
from groups.group_transforms import transforms_tasks


from datetime import datetime

with DAG('group_dag' , start_date = datetime(2022,8,15),
        schedule_interval = '@daily' ,catchup = False) as dag:


    downloads = downloads_task()

    check_files = BashOperator(
        task_id = 'check_files',
        bash_command = "sleep 10"
    )

    transforms = transforms_tasks()

    downloads >> check_files >> transforms