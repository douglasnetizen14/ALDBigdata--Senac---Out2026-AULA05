valor_pedido = float(input('digite o valor: '))
distancia = float(input('distancia:  '))

if valor_pedido > 50   and  distancia <= 3:
    valor_final = valor_pedido
    print('frete gratis')

else:
   
    print(f'frete de r$ {frete}')
    print(f'valor final: r$ {valor_final:.2f}')

 