def validaMenu(opcao, min, max):
    while True:
        try:
            x = int(input(opcao))
            if min <= x < max:
                return x
            else:
                print(f"Digite um número válido entre {min} e {max-1}.")
        except ValueError:
            print("Digite um número válido.")

def criaArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, 'wt+'):
            pass
    except:
        print("Erro na criação do arquivo")
    else:
        print(f"Arquivo {nomeArquivo} foi criado com sucesso")

def existeArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, 'rt'):
            pass
    except FileNotFoundError:
        return False
    else:
        return True        

def cadastrarFilme(nomeArquivo, nomeFilme, anoFilme):
    try:
        with open(nomeArquivo, 'at') as arquivo:
            arquivo.write(f'{nomeFilme.ljust(20)}{anoFilme}\n')
    except:
        print(f'Erro ao abrir o arquivo')

def listarArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, 'rt') as Arquivo:
            conteudo = Arquivo.read()
            print(conteudo)
    except:
        print("Erro ao ler o arquivo")
    

Arquivo = 'Filmes.txt'
if existeArquivo(Arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(Arquivo)

while True:
    print("Menu".center(25))
    print("1 - Cadastre um novo filme")
    print("2 - Listar filmes")
    print("3 - Sair")

    op = validaMenu("Qual opção você deseja: ",1,4)

    if (op == 1):
        nomeFilme = input("Digite o nome do filme: ")
        anoFilme = input("Qual ano o filme foi lançado? ")
        cadastrarFilme(Arquivo, nomeFilme, anoFilme)

    elif (op == 2):
        print("Filmes      ","Lançamento")
        print("")
        listarArquivo(Arquivo)

    elif (op == 3):
        print("Programa Encerrado.")
        break