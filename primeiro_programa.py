import os

restaurantes = [
    {'nome': 'Akira', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Corleone', 'categoria': 'Italiana', 'ativo': True},
    {'nome': 'Sanjino', 'categoria': 'Italiana', 'ativo': False}
]


def exibir_nome_do_programa():
    '''
    Exibe o nome do programa em um formato de arte ASCII.

    Output: Exibe o título formatado do programa.
    '''
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)


def exibir_subtitulo(texto):
    '''
    Exibe um subtítulo formatado para seção específica.

    Input: texto (str) - Título da seção a ser exibido.
    Output: Exibe o subtítulo formatado com bordas.
    '''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


def opcao_invalida():
    '''
    Exibe uma mensagem de erro para opção inválida.

    Output: Exibe a mensagem 'Opção Inválida!\n'.
    '''
    print('Opção Inválida!\n')


def voltar_ao_menu_principal():
    '''
    Pausa para o usuário e retorna ao menu principal.

    Output: Espera uma entrada do usuário e chama a função main() para reiniciar o menu.
    '''
    input('\nDigite uma tecla para voltar ao menu ')
    main()


def exibir_opcoes():
    '''
    Exibe as opções de menu para o usuário.

    Output: Lista as opções disponíveis no menu.
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair \n')


def finalizar_app():
    '''
    Exibe uma mensagem de encerramento do programa.

    Output: Exibe 'Finalizando app'.
    '''
    exibir_subtitulo("Finalizando app")


def cadastrar_novo_restaurante():
    '''
    Cadastra um novo restaurante com nome, categoria e estado inicial 'desativado'.

    Input: Solicita o nome e categoria do restaurante ao usuário.
    Output: Adiciona o restaurante à lista e exibe mensagem de sucesso.
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()


def listar_restaurantes():
    '''
    Lista todos os restaurantes cadastrados com seu nome, categoria e status.

    Output: Exibe a lista completa dos restaurantes com seus respectivos atributos.
    '''
    exibir_subtitulo('Listando os restaurantes:')
    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        status = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {status}")
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    '''
    Alterna o estado ativo de um restaurante especificado pelo usuário.

    Input: Solicita o nome do restaurante.
    Output: Exibe mensagem confirmando o estado alternado ou informa que o restaurante não foi encontrado.
    '''
    exibir_subtitulo('Alternando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()


def escolher_opcao():
    '''
    Lê a escolha do usuário e executa a função correspondente.

    Input: Entrada numérica do usuário para seleção de opção.
    Output: Chama a função correspondente ou exibe mensagem de opção inválida.
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    '''
    Executa o programa principal, exibindo o menu e processando as escolhas.

    Output: Inicia a interface de menu e aguarda escolha do usuário.
    '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
