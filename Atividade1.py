import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

try:

    z = 1
    
    while(z==1):


        atividade = int(input("\nPressione o número da atividade que o senhor quer analisar! "
                              "\n Se o senhor quiser fechar o programa selecione o número 0: "))
        
        limpar_terminal()


        if(atividade == 0):
            z = 0
            print("Obrigado por analisar o meu algoritmo")



        elif(atividade == 1): #Escreva um programa que recebe a idade de uma pessoa e imprime "Maior de idade" se a idade    
                                        #for maior ou igual a 18, ou "Menor de idade" caso contrário.   
           
            limpar_terminal()


            idade = int(input("Vamos verificar se você é maior ou menor de idade \n Quantos anos você tem? "))


            if(idade >= 18 ):
                print("Maior de idade. Cuidado, já pode ser preso")

            else:
                print("Menor de idade")   





        elif(atividade == 2): #Crie um programa que solicita dois números ao usuário e exibe o maior deles.
            
            limpar_terminal()


            print("Vou exibir o maior número que você digitar")

            num1 =  int(input("Digite um números: "))
            num2 =  int(input("Digite outro números: "))


            if(num1 > num2):
                print(num1, " é maior que ", num2)

            elif(num2 > num1):
                print(num2, " é maior que ", num1)

            elif(num2 == num1):
                print(num2, " e ", num1, " são o mesmo valor")





        elif(atividade == 3): #Elabore um programa que verifica se um número digitado é positivo, negativo ou zero.
            
            limpar_terminal()



            numero = int(input("Digite um número e irei verificar se ele é positivo, negativo ou zero: "))


            if(numero < 0):
                print("O número é negativo")

            elif(numero > 0):
                print("O número é positivo")

            elif(numero == 0):
                print("O número é 0")





        elif(atividade == 4):   #Escreva um programa que calcule o preço a pagar por um produto, considerando um desconto de
                                                #10% caso o valor total seja maior que R$ 100,00.    

            valor = 0
            x = 1

            while(x==1):

                limpar_terminal()

                print("                                                                                     MERCADINHO DO MARQUINHOS\n"
                      "Produtos:\n"
                      "1 - Cerveja adulterada: R$ 35\n"
                      "2 - Maço de cigarro Derbi: R$ 42\n"
                      "3 - isqueiro sem gás: R$ 27\n"
                      "4 - pilha duracell: R$ 50\n"
                      "5 - semente de macarrão: R$ 82\n"
                      "PARA SAIR, APERTE 6")


                if(valor >= 100):
                    print("Parabéns, você ganhou 10%"" de desconto! sem o desconto você pagaria ", valor, "\n"
                          "Mas agora ira pagar penas ", int(-(valor * 0.10) + valor))


                else:
                    print("O valor total atual é :", valor)


                opcao = int(input())

                if(opcao == 1):
                    valor = valor + 35


                elif(opcao == 2):
                    valor = valor + 42


                elif(opcao == 3): 
                    valor = valor + 27   


                elif(opcao == 4): 
                    valor = valor + 50


                elif(opcao == 5): 
                    valor = valor + 82


                elif(opcao == 6):
                    x = 0


                else:
                    print("Coloque um valor valido")            





        elif(atividade == 5): #Crie um programa que avalie se três números podem ser lados de um triângulo.
                            #Para serem lados de um triângulo, a soma de dois lados deve ser maior que o terceiro lado.   
                             
            limpar_terminal()


            print("Vou avaliar três números e direi se eles podem formar um triângulo ou não\n")

            a = int(input("Fale qual o tamanho de um dos lados do triângulo: "))
            b = int(input("Fale o tamanho de mais um dos lados do triângulo: "))
            c = int(input("Qual o tamanho do último lado do triângulo? "))


            if(c < a + b and c > a and c > b ) or ( b < a + c and b > a and b > c) or (a < c + b and a > c and a > b):
                print("\nÉ possível criar um triângulo com esses valores")

            else:
                print("\nNão é possível criar um triângulo com esses valores")





        elif(atividade == 6): #6 - Faça um algoritmo para ler três notas e o número de faltas de um aluno e escr12ever qual a sua
                    #situação final: Aprovado, Reprovado por Falta ou Reprovado por Média. A média para aprovação é 7,0 e
                    #o limite de faltas é 25% do total de aulas. O número de aulas ministradas no semestre foi de 80. A
                    #reprovação por falta sobrepõe a reprovação por Média.
            limpar_terminal()
            print("Vamos verificar a média e faltas do aluno e retornar se ele reprovou ou não\n")
            limt_falta = 80 * 0.25
            faltas = int(input("Quantas faltas o aluno teve? "))
            nota1 = int(input("Qual a primeira nota? "))
            nota2 = int(input("Qual a segunda nota? "))
            nota3 = int(input("Qual a terceira nota? \n"))
            media = ((nota1 + nota2 + nota3) / 3)
            if(faltas <= limt_falta and media >= 69):
                print("O aluno foi APROVADO")
            elif(faltas > limt_falta and media >= 69):
                print("O aluno foi REPROVADO por falta")    
            elif(faltas <= limt_falta and media < 69):
                print("O aluno foi REPROVADO por nota")    
            else:
                print("O aluno foi REPROVADO por falta e nota")





        elif(atividade == 7): #Escreva um programa que leia três números e os imprima em ordem crescente.

            limpar_terminal()

            numero1 = input("Escreva o primeiro número: ")
            numero2 = input("Escreva o segundo número: ")
            numero3 = input("Escreva o terceiro número: ")


            numeros = [numero1, numero2, numero3]

            numeros.sort()
            print("Números em ordem crescente: ", numeros)




        elif(atividade == 8): #Crie um programa que calcule o índice de massa corporal (IMC) de uma pessoa, dado o peso em kg
                            #e a altura em metros. O IMC é calculado dividindo o peso pela altura ao quadrado. Depois, o programa
                                            #deve exibir uma mensagem de acordo com a faixa de IMC.
            limpar_terminal()
        

            altura = float(input("Vamos calcular o seu IMC. Para indicar a sua altura use ponto final no lugar da virgula.\nExemplo: 1.80 de altura\nQual é a sua altura? "))
            peso = float(input("Qual é o seu peso? "))

            IMC = peso / (altura * altura)

            
            
            print("\n")


            if(IMC <= 18.5):
                print(f"O seu IMC é {IMC:.2f}. Isso indica que você está abaixo do peso")

            elif(IMC > 18.5 and IMC <= 24.9):
                print(f"O seu IMC é {IMC:.2f}. Isso indica que você está com peso ideal")
        
            elif(IMC > 24.9 and IMC <= 29.9):
                print(f"O seu IMC é {IMC:.2f}. Isso indica que você está levemente acima peso")

            elif(IMC > 29.9 and IMC <= 34.9):
                print(f"O seu IMC é {IMC:.2f}. Isso indica que você está com obesidade I peso")

            elif(IMC > 34.9 and IMC <= 39.9):
                print(f"O seu IMC é {IMC:.2f}. Isso indica que você está com obesidade II peso")

            else:
                print(f"O seu IMC é {IMC:.2f}. Isso indica que você está com obesidade III (mórbida)")


        
        


        
        


        
        


        
                    



        elif(atividade == 9): #Crie um programa que determine se um número digitado pelo usuário é par ou ímpar. 

            limpar_terminal()


            nu = int(input("Digite um número e irei verificar se ele é par ou ímpar: "))


            if(nu % 2 == 0):
                print("O número é par")

            else:
                print("O número é ímpar")





        elif(atividade == 10): #Desenvolva um programa que calcule o preço final de um produto com base em seu valor original
                                                #e um percentual de desconto fornecido pelo usuário.    
            limpar_terminal()

            valor = 0

            Nome = input("Escolha um nome para a sua loja de roupa: ")
            limpar_terminal()


            produto = float(input(f"                                                                                     {Nome}"
                            "\nEscolha um produto para colocar desconto:\n"
                            "1 - Blusa: R$60\n"
                            "2 - calça: R$80\n"
                            "3 - Bolsa: R$90\n"
                            "4 - Jaqueta: R$120\n"
                            "5 - Regata: R$50\n"))

            if(produto == 1):
                valor = valor + 60

            elif(produto == 2):
                valor = valor + 80

            elif(produto == 3): 
                valor = valor + 90  

            elif(produto == 4): 
                valor = valor + 120

            elif(produto == 5): 
                valor = valor + 50


            if(produto == 1):
                pro = "Blusa"

            elif(produto == 2):
                pro = "calça"

            elif(produto == 3): 
                pro = "Bolsa"

            elif(produto == 4): 
                pro = "Jaqueta"

            elif(produto == 5): 
                pro = "Regata"


            desconto = float(input(f"Quantos porcento de desconto o senhor deseja colocar na {pro}? "))

            NoValor = - ((desconto / 100) * valor) + valor

            print("\nO preço normal da", pro, "é R$", valor, "Mas com o desconto fica R$", NoValor)





        elif(atividade == 11): #Faça um programa que determine se um número é positivo e par ao mesmo tempo.  
            
            limpar_terminal()


            n1 = float(input("Digite um número. Vamos verificar se o número é par e positivo: "))


            if(n1 < 0):
                NValor = "negativo"

            elif(n1 > 0):
                NValor = "positivo"

            else:
                NValor = "0"


            if(n1 % 2 == 0):
                Npar = "Par"

            else:
                Npar = "impar"


            print(f"O número digitado é {NValor} e é {Npar}")





        elif(atividade == 12): #Escreva um programa que leia um número de 1 a 7 e imprima o dia da semana correspondente
                                    #(considerando 1 como domingo, 2 como segunda-feira, etc.).
            
            limpar_terminal()


            Dia = int(input("Digite um número de 1 a 7 e eu direi a qual dia da semana ele corresponde: "))


            if(Dia == 1):
                print(f"O domingo é o {Dia}° dia da semana")

            elif(Dia == 2):
                print(f"O segunda é o {Dia}° dia da semana")

            elif(Dia == 3):
                print(f"O terça é o {Dia}° dia da semana")

            elif(Dia == 4):
                print(f"O quarta é o {Dia}° dia da semana")

            elif(Dia == 5):
                print(f"O quinta é o {Dia}° dia da semana")

            elif(Dia == 6):
                print(f"O sexta é o {Dia}° dia da semana")

            elif(Dia == 7):
                print(f"O sabado é o {Dia}° dia da semana")

            else:
                print("Você não digitou um número")





        elif(atividade == 13): #Desenvolva um programa que leia o ano de nascimento de uma pessoa e classifique-a em uma
                                    #das seguintes categorias: criança, adolescente, adulto ou idoso.
            limpar_terminal()


            nome = input("Digite um nome: ")
            anos = input(f"Quantos anos {nome} tem? ")


            if(anos >= 1 and anos <= 12):
                print(f"{nome} tem {anos} anos, logo é uma criança")

            elif(anos >= 13 and anos <= 18):
                print(f"{nome} tem {anos} anos, logo é um adolescente")

            elif(anos >= 18 and anos <= 59):
                print(f"{nome} tem {anos} anos, logo é um adulto")

            elif(anos >= 59 and anos <= 120):
                print(f"{nome} tem {anos} anos, logo é um Idoso")

            elif(anos >= 120):
                print(f"{nome} tem {anos} anos, logo é um imortal")

            else:
                print("Você colocou um valor invalido")





        elif(atividade == 14): #Escreva um programa que determine se uma senha digitada pelo usuário é válida. A senha é
                                #válida se tiver pelo menos 8 caracteres e conter letras maiúsculas, minúsculas e números.
            limpar_terminal()

            print("As senhas precisam conter pelo menos 8 caracteres e conter letras maiúsculas, minúsculas e números\n")

            senha = input("Digite sua senha: ")


            if (len(senha) == 8 and
                any(c.islower() for c in senha) and
                any(c.isupper() for c in senha) and
                any(c.isdigit() for c in senha)):
                print("Senha válida")

            else:
                print("Senha inválida")





        elif(atividade == 15): #Faça um programa que leia três notas de um aluno e calcule a média ponderada, considerando os
                                                         #pesos 2, 3 e 5 para as notas.
            limpar_terminal()


            print("                             Olá, seja bem vindo ao boletim do curso de ciência de dados\n Por favor, digite a nota de cada disciplina")
            mat = float(input("Nota de matemática peso 3: "))
            mtc = float(input("Nota de Metodologia do Trabalho Científico peso 2: "))
            py = float(input("Nota de Python peso 5: "))


            medi = ((mat * 3) + (mtc * 2) + (py * 5)) / (3 + 2 + 5)


            print(f"A média do aluno foi {medi}")





        elif(atividade == 16): #Desenvolva um programa que simule um sistema de login, onde o usuário deve digitar um nome
                            #de usuário e uma senha. O programa deve permitir o acesso apenas se o nome de usuário for "cd2" e a
                            #senha for "cd2_123". Mostra a mensagem informando usuário logado com sucesso ou login e/ou senha invalido.
            limpar_terminal()


            login = str(input("Digite o seu login: "))
            senha = str(input("Digite a sua senha: "))


            if(login == "cd2" and senha == "cd2_123"):
                print("usuário logado com sucesso")

            else:
                print("login e/ou senha invalido.")





        elif(atividade == 17): #Elabore um programa que leia o valor de três produtos e informe qual deles é o mais barato.
            limpar_terminal()


            print("Informe os preços de três produtos e eu direi qual deles é o mais barato.")

            prodA = float(input("Informe o valor da caixa de leite R$"))
            prodB = float(input("Informe o valor da barra de chocolate R$"))
            prodC = float(input("Informe o valor do presunto R$"))


            if(prodA < prodB and prodA < prodC):
                print(f"A caixa de leite é o produto mais barato. O seu preço é R${prodA}")

            elif(prodB < prodA and prodB < prodC):
                print(f"A barra de chocolate é o produto mais barato. O seu preço é R${prodA}")

            elif(prodC < prodB and prodC < prodA):
                print(f"O presunto é o produto mais barato. O seu preço é R${prodA}")

            else:
                print("Você colocou o mesmo valor nos produtos")





        elif(atividade == 18): #Escreva um programa que leia o nome de um mês e exiba o número correspondente.
            limpar_terminal()


            mes = str(input("Escreva o nome do mês e eu informarei o número dele: "))



            if(mes == "janeiro" or mes == "Janeiro"):
                NuMes = 1
                print(f"Janeiro é o mês {NuMes}")



            elif(mes == "fevereiro" or mes == "Fevereiro"):
                NuMes = 2
                print(f"Fevereiro é o mês {NuMes}")



            elif(mes == "março" or mes == "Março"):
                NuMes = 3
                print(f"Março é o mês {NuMes}")



            elif(mes == "maio" or mes == "Maio"):
                NuMes = 4
                print(f"Maio é o mês {NuMes}")



            elif(mes == "Junho" or mes == "junho"):
                NuMes = 5
                print(f"Junho é o mês {NuMes}")



            elif(mes == "Julho" or mes == "julho"):
                NuMes = 6
                print(f"Julho é o mês {NuMes}")



            elif(mes == "Agosto" or mes == "agosto"):
                NuMes = 7
                print(f"Agosto é o mês {NuMes}")



            elif(mes == "Setembro" or mes == "setembro"):
                NuMes = 8
                print(f"Setembro é o mês {NuMes}")



            elif(mes == "outubro" or mes == "Outubro"):
                NuMes = 9
                print(f"Outubro é o mês {NuMes}")



            elif(mes == "novembro" or mes == "Novembro"):
                NuMes = 10
                print(f"Novembro é o mês {NuMes}")



            elif(mes == "dezembro" or mes == "Dezembro"):
                NuMes = 11
                print(f"Dezembro é o mês {NuMes}")




except ValueError:
    print("ERRO: Você inseriu um ou mais valores inválidos.")   #   P r i m e i r a   a t i v i d a d e   d a   f a c u l  
 