import menuAdm
import geral
import leitor


op = 0
usuarios_lista = [{"ID": 1, "login": 'rene88', "senha": '123'}]
jornal2 = {'rene88':[{"titulo": 'a', "conteudo": 'ab', "comentarios": []},
                     {"titulo": 'kk', "conteudo": 'kkpp', "comentarios": []}]}

# programa principal
while True:

    op = geral.menuprincipal()

    if op >= 5:
        print('Opção Inválida pq eu quero !')

    if op == 1:
        menuAdm.cadastrarAdm(usuarios_lista)
    elif op == 2:
        leitor.cadastrarLeitor(usuarios_lista)

    elif op == 3:
        nomeusuario = input('Digite o login: ')
        senha = input('Digite a senha: ')

        tipo = geral.login(usuarios_lista, nomeusuario, senha)

        if tipo == 1:
            menuAdm.exibirMenuAdm(nomeusuario, jornal2)

        elif tipo == 2:
            leitor.exibirMenuLeitor(nomeusuario, jornal)

        else:
            print('usuario ou senha incorretos')


    elif op == 4:
        break
print('<>' * 30)
print('Saindo do jornal!')


