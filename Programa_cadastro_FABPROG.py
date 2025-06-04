nome = []
print("cadastro FABPROG")
print("1 - cadastrar pessoa" )
print("2 - listar pessoas")
print("3 - excluir pessoa")
print("0 - sair")

codigo = int(input("insira o cadastro: "))

if codigo == 1:
    print("1 - cadastrar pessoa")
    #digite o nome da pessoa que deseja cadastrar
    nome = input("digite o nome da pessoa que deseja cadastrar: ")
elif codigo == 2:
    print("2 - listar pessoas ")
elif codigo == 3: 
    print("3 - excluir pessoa")
elif codigo == 0:
    print("0 - sair")

