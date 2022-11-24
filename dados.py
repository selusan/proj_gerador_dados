import random
import os
#cria as listas
nomes = ['Sergio','Mauro','Patricia','Mirna','Elton']
emails = ['sergio@hotmail.com','patricia@hotmail.com','mirna@hotmail.com','mauro@hotmail.com','elton@hotmail.com']
telefones = ['928563481','997514589','984563278','9846325871','984561237']
cidades = ['londrina','Maringa','Toledo','Camboriu','Barra Velha']
estados = ['SP','MG','PR','RS','SC']

print('---------------------------------------------------------------------------------')

opcao = ['']
lista_opcao = ['']
dado = ''
while True :
    print('Bem vindo ao Gerador de Dados de Testes - Para finalizar o programa, digite "parar"')
    print("------------------------------------------------------------------------------------")
    print("Escolha uma ou mais opções abaixo a serem geradas aleatóriamente")
    print("[1] - Nome")
    print("[2] - Email")
    print("[3] - Telefone")
    print("[4] - Cidade")
    print("[5] - Estado")
    opcao = input('Digite uma(as) opções: ').replace(',',"")
    if opcao != 'parar':        
        #receber a escolha do usuario
        print("------------------------------------------------------------------------------------")       
        #imprimir um ou mais dados escolhidos pelo usuario
        for item in opcao:
            if item =='1':
                dado=random.choice(nomes)
                # lista_opcao.append(dado)
                print(dado)
            elif item =='2':
                    dado=random.choice(emails)
                    # lista_opcao.append(dado)
                    print(dado)           
            elif item =='3':
                    dado=random.choice(telefones)
                    # lista_opcao.append(dado)
                    print(dado)
            elif item =='4':
                    dado=random.choice(cidades)
                    #lista_opcao.append(dado)
                    print(dado)                 
            elif item =='5':
                    dado=random.choice(estados)
                    #lista_opcao.append(dado)
                    print(dado)
            lista_opcao.append(dado)                        
        #apos gerar os dados perguntar se ele quer salvar em um arquivo txt
        salva_dados=input('Deseja salvar os dados em um arquivo? Digite s/n: ') 
        if salva_dados == 's' : 
            with open('dados.txt','a') as arquivo:
                for opcao in lista_opcao:
                    arquivo.write(f'{opcao}\n')
                    lista_opcao=['']                       
                   
    
    else:
        print("Saindo do programa....")
        break        



