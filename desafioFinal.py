## Banco de Dados
ususario_autorizado = "admin"
senha_autorizada = "@dmin"
produtos_cadastrados = ["Teclado", "Mouse", "Monitor", "Fonte 12v"]


## Funções
def menu():
    print("ESCOLHA QUAL OPÇÃO DESEJA")
    print("1- Listar Produtos")
    print("2- Cadastrar Novos Produtos")
    print("3- Atualizar Produto Cadastrado")
    print("4- Excluir um Produto")
    print("0- Sair")
    opcao = input()
    return opcao


def listarProdutos(produtos):
    for produto in produtos:
        print(produto)
    print("")


def cadastrar(produtos):
    produtos.append(input("Novo Produto: ").capitalize())
    print("Produto Cadastrado com Sucesso!")
    print(produtos)
    print("")


def atualizar(produtos):
    print(produtos)
    produto_antigo = input("Qual produto deseja atualizar? ").capitalize()
    if produto_antigo in produtos:
        index = produtos.index(produto_antigo)
        novo_produto = input("Qual o novo produto? ").capitalize()
        produtos[index] = novo_produto
        print(produtos)
        print("Produto Atualizado Com Sucesso!")
        print("")
    else:
        print("Produto Não Encontrado!")


def remover(produtos):
    print(produtos)
    produtoRemover = input("Qual produto deseja remover? ").capitalize()
    produtos.remove(produtoRemover)
    print(produtos)
    print("Produto Removido Com Sucesso!")
    print("")


print("#################################################")
print("########## Bem-Vindo ao Estoque Fácil! ##########")
usuario_digitado = input("Digite o usuário: ")
senha_digitada = input("Digite a senha: ")
print("\n")

if usuario_digitado == ususario_autorizado and senha_digitada == senha_autorizada:
    # print("Usuário Autorizado!")
    operacao = menu()
    while operacao != "0":
        print("Operação: " + operacao)
        if operacao == "1":
            listarProdutos(produtos_cadastrados)
        elif operacao == "2":
            cadastrar(produtos_cadastrados)
        elif operacao == "3":
            atualizar(produtos_cadastrados)
        elif operacao == "4":
            remover(produtos_cadastrados)
        else:
            print("Opção Inválida!")
        operacao = menu()
else:
    print("Usuário Não Autorizado!")
