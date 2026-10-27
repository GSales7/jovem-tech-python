ususario_autorizado = "admin"
senha_autorizada = "@dmin"

print("#################################################")
print("########## Bem-Vindo ao Estoque Fácil! ##########")
usuario_digitado = input("Digite o usuário: ")
senha_digitada = input("Digite a senha: ")
print("\n")

if usuario_digitado == ususario_autorizado and senha_digitada == senha_autorizada:
    print("Usuário Autorizado!")
else:
    print("Usuário Não Autorizado!")
