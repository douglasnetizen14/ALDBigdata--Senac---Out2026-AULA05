nota1 = float(input("primeira nota:  "))
nota2 = float(input("segunda  nota:  "))
nota3 = float(input("terceira nota:  "))
nota4 = float(input("quarta  nota:  "))

media = (nota1 + nota2 + nota3 + nota4)  / 4

print (f"media final:  {media:.2f}")
if media >= 7:
    print ("aprovado")
elif media >= 5:
    print ("em recuperação")
else:
    print ("reprovado")    

