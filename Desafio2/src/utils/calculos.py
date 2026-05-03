def calcular_valor_venda(preco_unitario, quantidade):
    valor_bruto = preco_unitario * quantidade
    
    desconto = 0
    if quantidade > 10:
        desconto = valor_bruto * 0.05
    
    valor_final = valor_bruto - desconto
    
    return valor_final