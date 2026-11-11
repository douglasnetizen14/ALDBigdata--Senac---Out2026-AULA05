valor_compra = float(input("digite o valor da compra"))
fidelidade = input(" e cadastrato no progama de fidelidade? ? (s/n:  ").strip(). lower()

if valor_compra > 200 or fidelidade  == 's':
    valor_final = valor_compra 
    print("frete gratis aplicado !")

else:
    valor_final = valor_compra + 25.00
    print("frete de r$ 20.00 adicionado.")

print(f" o valor final da compra é: r$ {valor_final:.2f}")