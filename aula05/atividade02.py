# Estrutura Match Case

print('''
[1]- marketing
[2]- financeiro
[3 a 5]-adm
[6 a 10] - TI
[10 a 20]-sg
''')

opcao = int(input('escolha uma opção: '))

match opcao:
    case 1:
        print('marketing')

    case  2:
         print('financeiro')

    case  3 | 4 | 5:
        print('adm')

    case opcao if 6 <= opcao <=9:
        print('TI')

    case opcao if 10 <= opcao <=20:
        print ('sg')

    case _:
        print('invalido')


codigo = int(input("Digite o cÃ³digo de origem: "))


if codigo == 1:

    print("Sul")

elif codigo == 2:
    print("Norte")[
elif codigo == 3:

    print("Leste")[span_3](start_span)[span_3](end_span)

elif codigo == 4:

    print("Oeste")[span_4](start_span)[span_4](end_span)

elif codigo == 5 or codigo == 6:

    print("Nordeste")[span_5](start_span)[span_5](end_span)

elif 7 <= codigo <= 9:

    print("Sudeste")[span_6](start_span)[span_6](end_span)

elif codigo == 10:

    print("Centro-Oeste")[span_7](start_span)[span_7](end_span)

elif codigo == 11:

    print("Noroeste")[span_8](start_span)[span_8](end_span)

else:

    print("Importado")[span_9](start_span)[span_9](end_span)