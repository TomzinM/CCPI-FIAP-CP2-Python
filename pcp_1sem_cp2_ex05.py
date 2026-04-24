# = = = Definição de Funções = = =
def pode_aprovar(idade, renda, valor):
    if idade <= 18:
        return False
    if valor > renda * 20:
        return False
    return True
 
 
def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10
 
 
def calcular_parcela(valor, taxa, parcelas):
    PMT = valor * ((taxa * (1 + taxa)**parcelas) / ((1 + taxa)**parcelas - 1))
    return PMT
 
 
def calcular_total(parcela, parcelas):
    return parcela * parcelas
 
 
def calcular_juros(total, valor):
    return total - valor


# = = = Programa Principal = = =

# 1. Solicitação de Dados
nome_cliente = input("Digite seu nome: ")
idade_cliente = int(input("Digite sua idade: "))
renda_mensal = float(input("Digite sua renda mensal: "))
emprestimo_desejado = float(input("Digite o valor do empréstimo desejado: "))
n_parcelas = int(input("Digite o número de parcelas (de 3 a 24): "))
 
# 2. Aprovação
print("\n" + "=" * 45)
 
if not pode_aprovar(idade_cliente, renda_mensal, emprestimo_desejado):
    print("  EMPRÉSTIMO NEGADO")
    if idade_cliente <= 18:
        print("  Motivo: cliente deve ter mais de 18 anos.")
    if emprestimo_desejado > renda_mensal * 20:
        print(f"  Motivo: valor máximo permitido é R$ {renda_mensal * 20:,.2f}")
else:
    # 3. Taxa de juros
    taxa = definir_taxa(n_parcelas)
 
    # 4. Cálculo das parcelas
    parcela = calcular_parcela(emprestimo_desejado, taxa, n_parcelas)
 
    # 5 e 6. Cálculos adicionais e exibição
    total = calcular_total(parcela, n_parcelas)
    juros = calcular_juros(total, emprestimo_desejado)
 
    print("EMPRÉSTIMO APROVADO!")

    print(f"Cliente             :   {nome_cliente}")
    print(f"Valor financiado    :   R$ {emprestimo_desejado:,.2f}")
    print(f"Parcelas            :   {n_parcelas}x")
    print(f"Taxa de juros       :   {taxa * 100:.0f}% ao mês")
    print(f"Valor da parcela    :   R$ {parcela:,.2f}")
    print(f"Total pago          :   R$ {total:,.2f}")
    print(f"Total de juros      :   R$ {juros:,.2f}")