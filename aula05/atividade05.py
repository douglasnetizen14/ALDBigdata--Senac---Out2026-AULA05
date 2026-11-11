numero = float(input("digite um numero: "))
match numero:
    case n if n > 0:
        print(" 10 e positivo")

    case n if n < 0:
                print(" 0- e negativo ")

    case _: 
        print (" 0 numero e zero ")
        

