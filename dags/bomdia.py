from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta

# Define o nome da DAG
dag_id = 'enviar_email_diario'

# Define as configurações da DAG
default_args = {
    'owner': 'Gabriel',
    'start_date': days_ago(1),  # Defina a data de início da DAG
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Crie a instância da DAG
dag = DAG(
    dag_id,
    default_args=default_args,
    schedule_interval=timedelta(days=1),  # Define a frequência diária
)

# Define o operador de e-mail
send_email = EmailOperator(
    task_id='enviar_email',
    to=['gus.hmp@gmail.com'],  # Substitua pelo seu endereço de e-mail
    subject='Bom dia!',
    html_content='<p>Olá, tenha um ótimo dia!</p>',
    dag=dag,
)

# Configure a ordem das tarefas
send_email

if __name__ == "__main__":
    dag.cli()
