def cadastrarAdm(usuarios_lista):
    print('CADASTRAMENTO DE LOGIN E SENHA ADM')
    print()
    while True:
        nome = input('Digite seu nome: ')
        loginAdm = input('Cadastre o seu login: ')
        senha = input('Cadastre a sua senha: ')

        # Verifique se o login já existe na lista
        login_existe = False
        for usuario in usuarios_lista:
            if usuario["login"] == loginAdm:
                print('Login já existe.')
                login_existe = True
                break
        if not login_existe:
            DicionarioUsuarioAdm = {"ID": 1, "login": loginAdm, "senha": senha}
            usuarios_lista.append(DicionarioUsuarioAdm)

        resp = ' '
        while resp not in 'SsNn':
            resp = input('Deseja continuar cadastrando? Responda [S/N]: ')
        if resp == 'N' or resp == 'n':
            break


def criarNoticia(nomeUsuario, jornal):
    while True:
        titulo = input('Digite o título da notícia: ')
        conteudo = input('Digite o conteúdo da notícia: ')
        nova_publicacao = {"titulo": titulo, "conteudo": conteudo, "comentarios": []}
        if nomeUsuario in jornal.keys():
            jornal[nomeUsuario].append(nova_publicacao)
        else:
            jornal[nomeUsuario] = [nova_publicacao]
        print('Notícia publicada com sucesso.')

        resp = ' '
        while resp not in 'SsNn':
            resp = input('Deseja adicionar outra publicação? [S/N]:  ')
        if resp == 'N' or resp == 'n':
            break

def exibirMenuAdm(nomeUsuario, DicionarioNoticia):

    while(True):
        print('[1] PUBLICAR NOTÍCIAS')
        print('[2] EDITAR NOTÍCIAS')
        print('[3] REMOVER NOTÍCIAS')
        print('[4] SAIR')
        op = int(input('Digite a sua opção: '))

        if op == 1:
           criarNoticia(nomeUsuario, DicionarioNoticia)
        elif op == 2:
            editarNoticia2(nomeUsuario, DicionarioNoticia)
        elif op == 3:
            deletarNoticia2(nomeUsuario, DicionarioNoticia)
        elif op == 4:
            break



def editarNoticia(nomeusuario, DicionarioNoticia):
    print('Escolha a publicação que deseja editar:')
    for i, publicacao in enumerate(DicionarioNoticia["publicacoes"]):
        print(f'{i + 1}. {publicacao["titulo"]}')
    escolha = int(input('Escolha um número: '))

    if 1 <= escolha <= len(DicionarioNoticia["publicacoes"]):
        publicacao = DicionarioNoticia["publicacoes"][escolha - 1]
        novo_titulo = input('Digite o novo título (ou pressione Enter para manter o atual): ')
        novo_conteudo = input('Digite o novo conteúdo (ou pressione Enter para manter o atual): ')
        if novo_titulo:
            publicacao["titulo"] = novo_titulo
        if novo_conteudo:
            publicacao["conteudo"] = novo_conteudo
        print('Notícia editada com sucesso.')
        exibirMenuAdm(nomeusuario, DicionarioNoticia)
    else:
        print('Escolha de publicação inválida.')


def editarNoticia2(nomeUsuario, jornalNoticias):

    exibirNoticias(nomeUsuario, jornalNoticias)
    indEditar = int(input('digite o numero da noticia'))
    while (indEditar < 0 or indEditar >= len(jornalNoticias[nomeUsuario])):
        indEditar = int(input('digite o numero da noticia'))

    novotitulo = input('Digite o título da notícia: ')
    novoconteudo = input('Digite o conteúdo da notícia: ')

    jornalNoticias[nomeUsuario][indEditar]["titulo"] = novotitulo
    jornalNoticias[nomeUsuario][indEditar]["conteudo"] = novoconteudo

    print(jornalNoticias)

def exibirNoticias(nomeUsuario, jornalNoticias):
    if nomeUsuario in jornalNoticias.keys():

        listnews = jornalNoticias[nomeUsuario]

        for i in range(len(listnews)):
            print(f'{i} - {listnews[i]["titulo"]}')
            print(f'{listnews[i]["conteudo"]}\n')

    else:
        print('nao existe nenhuma noticia publicada por este usuario')


def deletarNoticia2(nomeUsuario, DicionarioNoticia):
    exibirNoticias(nomeUsuario, DicionarioNoticia)

    indRemover = int(input('digite o numero da noticia'))
    while (indRemover < 0 or indRemover >= len(DicionarioNoticia[nomeUsuario])):
        indRemover = int(input('digite o numero da noticia'))

    DicionarioNoticia[nomeUsuario].pop(indRemover)

    print(DicionarioNoticia[nomeUsuario])



def deletarNoticia(DicionarioNoticia):
    for i, publicacao in enumerate(jornal["publicacoes"]):
        print(f'{i + 1}. {publicacao["titulo"]}')
    print('Escolha a publicação que deseja remover:')
    escolha = int(input())
    if 1 <= escolha <= len(jornal["publicacoes"]):
        confirmacao = input('Tem certeza de que deseja remover esta notícia? (s/n): ')
        if confirmacao == 'S' or confirmacao == 's':
            publicacao = jornal["publicacoes"].pop(escolha - 1)
            print(f'A notícia {publicacao["titulo"]} foi removida com sucesso.')
        else:
            print('A remoção da notícia foi cancelada.')
    else:
        print('Escolha de publicação inválida.')

