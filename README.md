# 🎂 Calculadora de Idade em Python

Este projeto é um avanço nos meus estudos de Python. Embora o desafio inicial fosse apenas capturar e exibir a data de nascimento do usuário, eu expandi o escopo para incluir uma **função completa para calcular a idade** com base na data atual.

## 🎯 Objetivo e Funcionalidades

O objetivo principal deste script é praticar a manipulação de datas e a lógica condicional em Python.

**Funcionalidades:**

* Recebe o dia, mês e ano de nascimento como entrada do usuário.
* Utiliza o módulo `datetime` para obter a data atual.
* Calcula a idade exata considerando se o aniversário já passou no ano corrente.
* Exibe a data de nascimento e a idade calculada.

## 💻 Código-Fonte

```python
from datetime import datetime
def calcular_idade(dia_nascimento, mes_nascimento, ano_nascimento):

    data_atual = datetime.today();
    ano_atual = data_atual.year;
    mes_atual = data_atual.month;
    dia_atual = data_atual.day;

    idade = ano_atual - ano_nascimento;

    if mes_atual < int(mes_nascimento) or (mes_atual == int(mes_nascimento) and dia_atual < int(dia_nascimento)): idade -= 1

    return idade;

dia = int(input('Digite o dia do seu nascimento: '));
mes = int(input('Digite o mês do seu nascimento: '));
ano = int(input('Digite o ano do seu nascimento: '));

idade = calcular_idade(dia, mes, ano);

print('Você nasceu em: ', dia, '/', mes, '/', ano);
print('Sua idade é: ', idade, 'anos');
