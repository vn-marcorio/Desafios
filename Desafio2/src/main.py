from calculos import calcular_valor_venda

produtos = []
vendas = []

while True:
    print("\n--- SISTEMA DA LOJA (Iniciante) ---")
    print("1. Cadastrar Produto")
    print("2. Realizar Venda")
    print("3. Relatório de Vendas")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: R$ "))
        estoque = int(input("Estoque: "))
        produtos.append({"nome": nome, "preco": preco, "estoque": estoque})
        print("Produto cadastrado!")

    elif opcao == "2":
        if not produtos:
            print("Cadastre um produto primeiro!")
            continue

        for i in range(len(produtos)):
            p = produtos[i]
            print(f"{i} - {p['nome']} (Estoque: {p['estoque']})")
        
        indice = int(input("Número do produto: "))
        qtd = int(input("Quantidade: "))

        if qtd <= produtos[indice]["estoque"]:
            valor_da_venda = calcular_valor_venda(produtos[indice]["preco"], qtd)
            
            cliente = input("Nome do cliente: ")

            produtos[indice]["estoque"] -= qtd

            vendas.append({
                "cliente": cliente, 
                "item": produtos[indice]["nome"], 
                "valor": valor_da_venda
            })
            print(f"Venda de R$ {valor_da_venda:.2f} finalizada!")
        else:
            print("Estoque insuficiente!")

    elif opcao == "3":
        total_geral = 0
        print("\n--- RELATÓRIO ---")
        for v in vendas:
            print(f"Cliente: {v['cliente']} | Item: {v['item']} | Valor: R$ {v['valor']:.2f}")
            total_geral += v["valor"]
        print(f"Total da Loja: R$ {total_geral:.2f}")

    elif opcao == "4":
        break