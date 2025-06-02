import os
os.system("cls || clear")

livros = []


def cadastrar_livro():
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    ano = input("Ano de publicação: ")
    
    livro = {
        'titulo': titulo,
        'autor': autor,
        'ano': ano,
        'emprestado': False
    }
    livros.append(livro)
    print(f"Livro '{titulo}' cadastrado com sucesso!\n")

def listar_livros():
    if not livros:
        print(" Nenhum livro cadastrado.")
    else:
        print("\nLista de Livros:")
        for i, livro in enumerate(livros):
            status = "Emprestado" if livro['emprestado'] else "Disponível"
            print(f"{i + 1}. {livro['titulo']} - {livro['autor']} ({livro['ano']}) [{status}]")
    print()


def buscar_livro():
    busca = input("Digite o título ou parte dele: ").lower()
    encontrados = [livro for livro in livros if busca in livro['titulo'].lower()]
    
    if encontrados:
        print("\nLivros encontrados:")
        for livro in encontrados:
            status = "Emprestado" if livro['emprestado'] else "Disponível"
            print(f"- {livro['titulo']} ({livro['autor']}) [{status}]")
    else:
        print("Nenhum livro encontrado.")
    print()

def emprestar_devolver():
    listar_livros()
    try:
        num = int(input("Digite o número do livro para emprestar/devolver: "))
        if 1 <= num <= len(livros):
            livro = livros[num - 1]
            if livro['emprestado']:
                livro['emprestado'] = False
                print(f"Livro '{livro['titulo']}' devolvido com sucesso!")
            else:
                livro['emprestado'] = True
                print(f"Livro '{livro['titulo']}' emprestado com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")
    print()

def menu():
    while True:
        print("====== Biblioteca do Brasil ======")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Buscar livro por título")
        print("4. Emprestar/Devolver livro")
        print("5. Sair")
        print()
        opcao = input("Escolha uma opção: ")
        print()

        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            buscar_livro()
        elif opcao == '4':
            emprestar_devolver()
        elif opcao == '5':
            print("Encerrando sistema.")
            break
        else:
            print("Opção inválida.\n")


if __name__ == "__main__":
    menu()