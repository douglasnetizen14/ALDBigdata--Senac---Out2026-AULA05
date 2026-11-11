codigo = int(input("digite o codigo de origem: "))


if codigo == 1:

    print("Sul")

elif codigo == 2:
    print("Norte")
elif codigo == 3:

    print("Leste")

elif codigo == 4:

    print("Oeste")

elif codigo == 5 or codigo == 6:

    print("Nordeste")

elif 7 <= codigo <= 9:

    print("Sudeste")

elif codigo == 10:

    print("Centro-Oeste")

elif codigo == 11:

    print("Noroeste")

else:

    print("Importado")