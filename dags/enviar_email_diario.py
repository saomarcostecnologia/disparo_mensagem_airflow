from airflow import DAG
from airflow.providers.email.operators.email import EmailOperator
from datetime import datetime
from airflow.utils.dates import days_ago

# Argumentos padrão da DAG
default_args = {
    'owner': 'seu_nome',
    'start_date': days_ago(1),  # Pode ser ajustada para sua necessidade
    'retries': 1,
}

# Inicialização da DAG
dag = DAG(
    'enviar_email_diario',
    default_args=default_args,
    schedule_interval='@daily',  # Executar diariamente
    catchup=False,  # Impede a execução de backfills
)

# Configuração das credenciais do Gmail
email_config = {
    'smtp_user': 'gabrieltesteairflow@gmail.com',  # Seu endereço de e-mail do Gmail
    'smtp_password': 't5r4e32023',  # Sua senha do Gmail (não é recomendado)
    'smtp_port': 587,  # Porta SMTP do Gmail
    'smtp_host': 'smtp.gmail.com',  # Servidor SMTP do Gmail
    'smtp_starttls': True,
    'smtp_ssl': False,
}

# Definição do operador de envio de e-mail
enviar_email = EmailOperator(
    task_id='enviar_email',
    to=['destinatario@gmail.com'],  # Lista de destinatários
    subject='Bom Dia!',
    html_content='<p>Olá, tenha um ótimo dia!</p>',
    params=email_config,  # Passa as configurações do e-mail como parâmetros
    dag=dag,
)

# Defina a ordem das tarefas no DAG, adicionando-as à DAG após a criação
enviar_email
