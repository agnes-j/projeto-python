print("Sistema de verificação de idade")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if idade < 0:
    print("Idade inválida.")
else:
    if idade >= 18:
        print(nome, "é maior de idade.")
    else:
        print(nome, "é menor de idade.")

