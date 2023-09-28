# plugins/operadores/meu_operador.py
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class MeuOperador(BaseOperator):

    @apply_defaults
    def __init__(self, meu_parametro, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.meu_parametro = meu_parametro

    def execute(self, context):
        # Lógica personalizada aqui
        print(f'Meu operador sendo executado com o parâmetro: {self.meu_parametro}')
