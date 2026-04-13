def caminhao_calculo(peso, origem, codigo):
    preco_produto = 1
    peso_kilo = 1000 * peso

    if origem == 1:
        imposto = 1.35
    elif origem == 2:
        imposto = 1.25
    elif origem == 3:
        imposto = 1.15
    elif origem == 4:
        imposto = 1.05
    else:
        imposto = 1.00

    if 10 <= codigo <= 20:
        preco_produto = 100
    elif 21 <= codigo <= 30:
        preco_produto = 250
    elif 31 <= codigo <= 40:
        preco_produto = 340

    preco_bruto = preco_produto * peso_kilo
    preco_taxado = preco_bruto * imposto

    print(f"O preço bruto foi de R${preco_bruto:.0f}, e após imposto é de R${preco_taxado:.0f}.")


caminhao_calculo(20, 2, 32)