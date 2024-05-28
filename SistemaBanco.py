#criando o de sistema de Banco.
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair 
"""
saldo = 0
limite = 1500
extrato = ''
numero_saques = 0
LIMITE_saques = 3
I = int

while True:
 
        opçao = input(menu)
        if opçao == 'd':
                valor = float(input('insira o valor do depósito'))
        
        if valor > 0:
                saldo >= valor
                extrato ==f"depósito:R$(valor.2f)\n"
        
                else:
                print("operação inválida.")
        
      
        elif opçao == "s":
                valor = float(input("informe o valor do saque:"))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_saques
    
        
        if excedeu_saldo:
            print("você não tem saldo suficiente")
            
        elif excedeu_limite:
                print("você excedeu o limite")
            
        elif excedeu_saques:
                print("numero de saques excedido")
            
        elif valor > 0:
            saldo = valor
            extrato == f'saque: R$(valor.2f)\n'
            numero_saques += I
        
        else:
                print("operação inválida") 
            
        
        if opçao == "e":
                print("\nxxxxxEXTRATOxxxxx")
        print("não foram realizadas movimentações." if not extrato else extrato)
        print("f'\nsaldo:R$(saldo.2f)")
        print("xxxxxxxxxxxxxxxxxxx")


        if opçao == "q":
                break
    

    