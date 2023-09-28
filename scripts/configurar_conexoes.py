# scripts/configurar_conexoes.py
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser

# Criação de conexões personalizadas
session = settings.Session()

conn_id = "exemplo_conn"
conn_uri = "http://exemplo.com"

new_conn = models.Connection(
    conn_id=conn_id,
    conn_uri=conn_uri,
    conn_type="http",
)

session.add(new_conn)
session.commit()
session.close()

# Criação de usuário
user = PasswordUser(models.User())
user.username = "seu_usuario"
user.password = "sua_senha"

session = settings.Session()
session.add(user)
session.commit()
session.close()
