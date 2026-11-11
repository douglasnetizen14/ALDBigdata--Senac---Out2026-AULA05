nota = float(input("digite a nota: "))
frequencia = float(input("digite a frequencia (%): "))
mensalidade = float(input("digite valor da mensalidade: "))

if nota >= 7 and frequencia >= 75:
    bolsa = mensalidade * 0.20
    print (f"aluno aprovado para bolsa!")
    print (f"valor da bolsa: r$ {bolsa:.2f}")

else:
    print("aluno nao tem direito a bolsa.")