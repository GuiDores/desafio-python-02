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