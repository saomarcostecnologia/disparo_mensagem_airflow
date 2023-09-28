# meu_dag.py
from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from datetime import datetime

default_args = {
    'owner': 'seu_nome',
    'start_date': datetime(2023, 9, 28),
    'retries': 1,
}

dag = DAG(
    'enviar_email_diario',
    default_args=default_args,
    schedule_interval='@daily',
)

enviar_email = EmailOperator(
    task_id='enviar_email',
    to='seu_email@gmail.com',
    subject='Assunto do Email Diário',
    html_content='Conteúdo do seu email diário',
    dag=dag,
)
