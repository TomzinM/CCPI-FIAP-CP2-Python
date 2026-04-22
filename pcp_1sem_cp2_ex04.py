nome_do_funcionario = input("Insira o nome do funcionário: ")

print(f'\n{1} Gerente')
print(f'{2} Analista')
print(f'{3} Assistente')
print(f'{4} Estagiário\n')

cargo = int(input("Insira o cargo: "))
salario_base = float(input("Insira o salário base: "))
horas = int(input("Insira a quantidade total de horas extras trabalhadas: "))
faltas = int(input("Insira a quantidade de faltas no mês: "))
recebeu_bonus = (input("O funcionário recebeu bônus por desempenho? [s] ou [n]: ")).lower()


def calcular_horas_extras(salario_base, horas):
    valor_hora_extra = (salario_base * 0.015) * horas
    return valor_hora_extra

def calcular_descontos_faltas(salario_base, faltas):
    salario_descontos = (salario_base * 0.02) * faltas
    return salario_descontos


def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus == "s":
        match cargo:
            case 1:
                bonus = 1000
            case 2:
                bonus = 500
            case 3:
                bonus = 300
            case 4:
                bonus = 100
            case _:
                print("Cargo inexistente")
                exit()
    else:
        bonus = 0
    return bonus

def salario_final():
    salario_total = salario_base + calcular_horas_extras(salario_base,
    horas) - calcular_descontos_faltas(salario_base, faltas) + calcular_bonus(cargo, recebeu_bonus)
    return salario_total

def resultado_final():
    print(f'\nO salário bruto de {nome_do_funcionario} é de R${salario_base}')

    print(f'O total de acréscimos no salário de {nome_do_funcionario} é de '
          f'R${calcular_horas_extras(salario_base, horas) + calcular_bonus(cargo, recebeu_bonus)}')

    print(f'O total de descontos no salário de {nome_do_funcionario} é de R${calcular_descontos_faltas(salario_base, faltas)}')

    print(f'O salário final de {nome_do_funcionario} é: R${salario_final()}')

resultado_final()