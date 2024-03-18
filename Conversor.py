sair = False

while sair == False:
    print("=-==-==-==-==-= Menu de Opções =-==-==-==-==-=")

    print('''
        [1] Criar uma lista
        [2] Calculadora
        [3] Conversor
        [4]
        ''')

    Op = int(input("Escolha uma opção: "))

    if Op == 1:
        Lista = []
        Itens = int(input("Quantidade de itens na lista: "))
        for i in range(Itens):
            x = input("Item: ")
            Lista.append(x)
        print(Lista)

        z = input("Deseja continuar? ")
        if z == 'n':
            print("Finalizado...")
            sair = True


    elif Op == 2:
        # int transforma string em número inteiro
        num1 = int(input("Digite um número: "))
        operador = input(
            "Digite o operador (+(soma),-(subtração),/(divisão),*(multiplicação),**(elevado), */(Raiz Quadrada), /*(Raiz Cúbica): ")

    # */ Raiz Quadrada
        if operador == "*/":
            print("A raiz quadrada de {} é {}".format(num1, (num1 ** 0.5)))
    # */ Raiz Cúbica
        elif operador == "/*":
            print("A raiz cúbica de {} é {}".format(num1, (num1 ** 1/3)))
    # + soma
        elif operador == "+":
            num2 = int(input("Digite outro número: "))
            print("A soma entre {} e {} é {}".format(num1, num2, (num1 + num2)))
    # - subtração
        elif operador == "-":
            num2 = int(input("Digite outro número: "))
            print("A subtração entre {} e {} é {}".format(num1, num2, (num1 - num2)))
    # / divisão
        elif operador == "/":
            num2 = int(input("Digite outro número: "))
            print("A divisão entre {} e {} é {}".format(num1, num2, (num1 / num2)))
    # * multiplicação
        elif operador == "*":
            num2 = int(input("Digite outro número: "))
            print("A multiplicação entre {} e {} é {}".format(num1, num2, (num1 * num2)))
    # ** Elevado
        elif operador == "**":
            num2 = int(input("Digite outro número: "))
            print("O número {} elevado a {} é {}".format(num1, num2, (num1 ** num2)))

        z = input("Deseja continuar? ")
        if z == 'n':
            print("Finalizado...")
            sair = True

    elif Op == 3:

        print('''
                [1] Distância
                [2] Peso
                ''')

        converter = int(input("O que deseja conveter? "))

        if converter == 1:
            print('''
                [1] Quilômetro (km)
                [2] Hectômetro (hm)
                [3] Decâmetro (dam)
                [4] Metro (m)
                [5] Decâ­metro (dm)
                [6] Centi­metro (cm)
                [7] Mili­metro (mm)
                ''')

            op1 = input('Unidade a ser convertida: ')
            op2 = input('Unidade para conversão: ')

# =-=-=-=-=-=-=-=-=-= KM =-=-=-=-=-=-=-=-=-=-=-=-

# KM p/ HM

            if op1 == 'km' and op2 == 'hm':
                q = float(input('Valor: '))
                m = print("{} km em hectômetros são {} hm".format(q, (q * 10)))

# KM p/ DAM

            elif op1 == 'km' and op2 == 'dam':
                q = float(input('Valor: '))
                m = print("{} km em decâmetros são {} dm".format(q, (q * 100)))

# KM p/ M

            elif op1 == 'km' and op2 == 'm':
                q = float(input('Valor: '))
                m = print("{} km em metros são {} m".format(q, (q * 1000)))

# KM p/ DM

            elif op1 == 'km' and op2 == 'dm':
                q = float(input('Valor: '))
                m = print("{} km em decâ­metros são {} dm".format(q, (q * 10000)))

# KM p/ CM

            elif op1 == 'km' and op2 == 'cm':
                q = float(input('Valor: '))
                m = print("{} km em centi­metros são {} cm".format(q, (q * 100000)))

# KM p/ MM

            elif op1 == 'km' and op2 == 'mm':
                q = float(input('Valor: '))
                m = print("{} km em mili­metros são {} mm".format(q, (q * 1000000)))

# =-=-=-=-=-=-=-=-=-= HM =-=-=-=-=-=-=-=-=-=-=-=-

# HM p/ KM

            elif op1 == 'hm' and op2 == 'km':
                q = float(input('Valor hm: '))
                m = print("{} hm em quilômetros são {} km".format(q, (q / 10)))

# HM p/ DAM

            elif op1 == 'hm' and op2 == 'dam':
                q = int(input('Valor hm: '))
                m = print("{} hm em decâmetros são {} dam".format(q, (q * 10)))

# HM p/ M

            elif op1 == 'hm' and op2 == 'm':
                q = int(input('Valor hm: '))
                m = print("{} hm em metros são {} m".format(q, (q * 100)))

# HM p/ DM

            elif op1 == 'hm' and op2 == 'dm':
                q = int(input('Valor hm: '))
                m = print("{} hm em decâ­metros são {} dm".format(q, (q * 1000)))

# HM p/ CM

            elif op1 == 'hm' and op2 == 'cm':
                q = int(input('Valor hm: '))
                m = print("{} hm em centi­metros são {} cm".format(q, (q * 10000)))

# HM p/ MM

            elif op1 == 'hm' and op2 == 'mm':
                q = int(input('Valor hm: '))
                m = print("{} hm em milimetros são {} mm".format(q, (q * 1000000)))

# =-=-=-=-=-=-=-=-=-= DAM =-=-=-=-=-=-=-=-=-=-=-=-

# DAM p/

            elif op1 == 'dam' and op2 == 'km':
                q = int(input('Valor dam: '))
                m = print("{} dam em quilômetros são {} km".format(q, (q / 100)))

# DAM p/ HM
            elif op1 == 'dam' and op2 == 'hm':
                q = int(input('Valor dam: '))
                m = print('{} dam em hectômetros são {} hm'.format(q, (q / 10)))

# DAM p/ M

            elif op1 == 'dam' and op2 == 'm':
                q = int(input('Valor dam: '))
                m = print('{} dam em metros são {} m'.format(q, (q * 10)))

# DAM p/ DM

            elif op1 == 'dam' and op2 == 'dm':
                q = int(input('Valor dam: '))
                m = print("{} dam em decâ­metros são {} dm".format(q, (q * 100)))

# DAM p/ CM

            elif op1 == 'dam' and op2 == 'cm':
                q = int(input('Valor dam: '))
                m = print('{} dam em centi­metros são {} cm'.format(q, (q * 1000)))

# DAM p/ MM

            elif op1 == 'dam' and op2 == 'mm':
                q = int(input('Valor dam: '))
                m = print('{} dam em mili­metros são {}'.format(q, (q * 10000)))

# =-=-=-=-=-=-=-=-=-= M =-=-=-=-=-=-=-=-=-=-=-=-

# M p/ KM

            elif op1 == 'm' and op2 == 'km':
                q = float(input('Valor m: '))
                m = print('{} m em quilômetros são {} km'.format(q, (q / 1000)))

# M p/ HM

            elif op1 == 'm' and op2 == 'hm':
                q = float(input('Valor m: '))
                m = print('{} m em hectômetros são {} hm'.format(q, (q / 100)))

# M p/ DAM

            elif op1 == 'm' and op2 == 'dam':
                q = float(input('Valor m: '))
                m = print('{} m em decâmetros são {} dam'.format(q, (q / 10)))

# M p/ DM

            elif op1 == 'm' and op2 == 'dm':
                q = float(input('Valor em metros: '))
                m = print('{} m em deci­metros são {} dm'.format(q, (q * 10)))


# M p/ CM

            elif op1 == 'm' and op2 == 'cm':
                q = float(input('Valor em metros: '))
                m = print('{} m em centi­metros são {} cm'.format(q, (q * 100)))

# M p/ MM

            elif op1 == 'm' and op2 == 'mm':
                q = float(input('Valor em metros: '))
                m = print('{} m em mili­metros são {} mm'.format(q, (q * 1000)))

# =-=-=-=-=-=-=-=-=-= DM =-=-=-=-=-=-=-=-=-=-=-=-

# DM p/ KM

            elif op1 == 'dm' and op2 == 'km':
                q = float(input('Valor em deci­metros: '))
                m = print('{} dm em quilômetros são {} km'.format(q, (q / 10000)))

# DM p/ HM

            elif op1 == 'dm' and op2 == 'hm':
                q = float(input('Valor em deci­metros: '))
                m = print('{} dm em decâ­metros são {} hm'.format(q, (q / 1000)))

# DM p/ DAM

            elif op1 == 'hm' and op2 == 'dam':
                q = float(input('Valor em deci­metros: '))
                m = print('{} dm em decimetros são {} dam'.format(q, (q / 100)))

# DM p/ M

            elif op1 == 'dm' and op2 == 'm':
                q = float(input('Valor em deci­metros: '))
                m = print('{} dm em metros são {} m'.format(q, (q / 10)))

# DM p/ CM

            elif op1 == 'dm' and op2 == 'cm':
                q = float(input('Valor em deci­metros: '))
                m = print('{} dm em centi­metros são {} cm'.format(q, (q * 10)))

# DM p/ MM

            elif op1 == 'dm' and op2 == 'mm':
                q = float(input('Valor em deci­metros: '))
                m = print('Â´{} dm em mili­metros são {} mm'.format(q, (q * 100)))

# =-=-=-=-=-=-=-=-=-= CM =-=-=-=-=-=-=-=-=-=-=-=-

# CM p/ KM

            elif op1 == 'cm' and op2 == 'km':
                q = float(input('Valor em centi­metros: '))
                m = print('{} cm em quilômetros são {} km'.format(q, (q / 100000)))

# CM p/ HM

            elif op1 == 'cm' and op2 == 'hm':
                q = float(input('Valor em centi­metros: '))
                m = print('{} cm em hectômetros são {} hm'.format(q, (q / 10000)))

# CM p/ DAM

            elif op1 == 'cm' and op2 == 'dam':
                q = float(input('Valor em centi­metros: '))
                m = print('{} cm em decimetros são {} dam'.format(q, (q / 1000)))

# CM p/ M

            elif op1 == 'cm' and op2 == 'm':
                q = float(input('Valor em centi­metros: '))
                m = print('{} cm em metros são {} m'.format(q, (q / 100)))

# CM p/ DM

            elif op1 == 'cm' and op2 == 'dm':
                q = float(input('Valor em centi­metros: '))
                m = print('{} cm em deci­metros são {} dm'.format(q, (q / 10)))

# CM p/ MM

            elif op1 == 'cm' and op2 == 'mm':
                q = float(input('Valor em centi­metros: '))
                m = print('{} cm em mili­metros são {} mm'.format(q, (q * 10)))

# =-=-=-=-=-=-=-=-=-= MM =-=-=-=-=-=-=-=-=-=-=-=-

# MM p/ KM

            elif op1 == 'mm' and op2 == 'km':
                q = float(input('Valor em mili­metros: '))
                m = print('{} mm em quilômetros são {} km'.format(q, (q / 1000000)))

# MM p/ HM

            elif op1 == 'mm' and op2 == 'hm':
                q = float(input('Valor em mili­metros: '))
                m = print('{} mm em hectômetros são {} hm'.format(q, (q / 100000)))

# MM p/ DAM

            elif op1 == 'mm' and op2 == 'dam':
                q = float(input('Valor em mili­metros: '))
                m = print('{} mm em decâmetros são {} dam'.format(q, (q / 10000)))

# MM p/ M

            elif op1 == 'mm' and op2 == 'm':
                q = float(input('Valor em mili­metros: '))
                m = print('{} mm em metros são {} m'.format(q, (q / 1000)))

# MM p/ DM

            elif op1 == 'mm' and op2 == 'dm':
                q = float(input('Valor em mili­metros: '))
                m = print('{} mm em deci­metros são {} dm'.format(q, (q / 100)))

# MM p/ CM

            elif op1 == 'mm' and op2 == 'cm':
                q = float(input('Valor em mili­metros: '))
                m = print('{} mm em centi­metros são {} cm'.format(q, (q / 10)))


        elif converter == 2:
            print('''
                [1] Quilograma (kg)
                [2] Hectograma (hg)
                [3] Decagrama (dag)
                [4] Grama (g)
                [5] Decigrama (dg)
                [6] Centigrama (cg)
                [7] Miligrama (mg)
                ''')

            opcao_1 = input('')
            opcao_2 = input('')

    elif Op == 4:
      print("Em desenvolvimento...")

    z = input("Deseja continuar? Sim/ Não: ")
    if z == 'não' or z == 'Não':
      print("Finalizado...")
      sair = True
