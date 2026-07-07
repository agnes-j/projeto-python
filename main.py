print("Sistema de verificação de idade")
nome = input("Digite seu nome: ")

# Laço de repetição para garantir que uma idade válida seja digitada
while True:
    try:
        idade = int(input("Digite sua idade: "))
        
        if idade < 0 or idade > 120:  # Validação para idades impossíveis
            print("Por favor, digite uma idade válida (entre 0 e 120 anos).")
        else:
            break  # Sai do laço se a idade for válida
            
    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números inteiros.")

# Verificação da maioridade
if idade >= 18:
    print(f"{nome} é maior de idade.")
else:
    print(f"{nome} é menor de idade.")
