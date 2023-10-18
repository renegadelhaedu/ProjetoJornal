print('{:=^90}'.format(' NOTICIAS QUENTES DA CATOLICA '))
print()

op = 0
usuarios = {}
jornal = {"publicacoes": []}

while True:
    print('{:=^40}'.format(' MENU PRINCIPAL '))
    print('[1] CADASTRO ADM')
    print('[2] CADASTRO LEITOR')
    print('[3] EFETUAR LOGIN')
    print('[4] SAIR')
    op = int(input('Digite a sua opção: '))

    if op == 1:
        print('CADASTRAMENTO DE LOGIN E SENHA ADM')
        print()
        while True:
            nome = input('Digite seu nome: ')
            nomeusuario = input('Cadastre o seu login: ')
            senha = input('Cadastre a sua senha: ')
            usuarios[nomeusuario] = [1, nome, senha]

            resp = ' '
            while resp not in 'SsNn':
                resp = input('Deseja continuar cadastrando? Responda [S/N] ')
            if resp.lower() == 'n':
                break

    elif op == 2:
        print('CADASTRAMENTO DE LOGIN E SENHA LEITOR')
        print()
        while True:
            nome = input('Digite seu nome: ')
            nomeusuario = input('Cadastre o seu login: ')
            senha = input('Cadastre a sua senha: ')
            usuarios[nomeusuario] = [2, nome, senha]

            resp = ' '
            while resp not in 'SsNn':
                resp = input('Deseja continuar cadastrando? Responda [S/N] ')
            if resp.lower() == 'n':
                break

    elif op == 3:
        nomeusuario = input('Digite o nome de usuário: ')
        senha = input('Digite a senha: ')
        tipo = 0
        if nomeusuario in usuarios and senha == usuarios[nomeusuario][2]:
            tipo = usuarios[nomeusuario][0]
            print('Parabéns, você está logado!')
        else:
            print('Usuário ou senha inválidos.')

        if tipo == 1:
            op = 999
            while True:
                print('[1] PUBLICAR NOTÍCIAS')
                print('[2] EDITAR NOTÍCIAS')
                print('[3] REMOVER NOTÍCIAS')
                print('[4] SAIR')
                op = int(input('Digite a sua opção: '))

                if op == 1:
                    titulo = input("Digite o título da notícia: ")
                    conteudo = input("Digite o conteúdo da notícia: ")
                    nova_publicacao = {"titulo": titulo, "conteudo": conteudo, "comentarios": []}
                    jornal["publicacoes"].append(nova_publicacao)
                    print("Notícia publicada com sucesso.")

                elif op == 4:
                    break

        elif tipo == 2:
            op = 999
            while True:
                print('[1] LISTAR PUBLICAÇÕES')
                print('[2] LER UMA PUBLICAÇÃO')
                print('[3] ADICIONAR COMENTÁRIO')
                print('[4] SAIR')
                op = int(input('Digite a sua opção: '))

                if op == 1:
                    for i, publicacao in enumerate(jornal["publicacoes"]):
                        print(f"{i + 1}. {publicacao['titulo']}")

                elif op == 2:
                    while True:
                        print("Digite o número da publicação que deseja ler (ou 0 para cancelar): ")
                        indice = int(input())
                        if indice == 0:
                            break
                        if 0 <= indice <= len(jornal["publicacoes"]):
                            publicacao = jornal["publicacoes"][indice - 1]
                            print(f"Título: {publicacao['titulo']}")
                            print(publicacao['conteudo'])
                            print("\nComentários:")
                            for i, comentario in enumerate(publicacao['comentarios'], start=1):
                                print(f"{i}. {usuarios[comentario['leitor']][1]}: {comentario['comentario']}")
                            break
                        else:
                            print("Número de publicação inválido. Tente novamente.")

                elif op == 3:
                    while True:
                        print("Digite o número da publicação para adicionar um comentário (ou 0 para cancelar): ")
                        indice = int(input())
                        if indice == 0:
                            break
                        if 0 <= indice <= len(jornal["publicacoes"]):
                            publicacao = jornal["publicacoes"][indice - 1]
                            print(f"Título: {publicacao['titulo']}")
                            print(publicacao['conteudo'])
                            nomeusuario = input("Digite o seu nome de usuário: ")
                            if nomeusuario in usuarios:
                                comentario = input("Digite o seu comentário: ")
                                publicacao['comentarios'].append({"leitor": nomeusuario, "comentario": comentario})
                                print("Comentário adicionado com sucesso.")
                            else:
                                print("Usuário não encontrado. Comentário não adicionado.")
                            break
                        else:
                            print("Número de publicação inválido. Tente novamente.")
                elif op == 4:
                    break

    elif op == 4:
        break
print('<>' * 30)
print('Saindo do jornal!')

