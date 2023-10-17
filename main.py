agenda = {}

while True:
    print('--- Agenda telefonica ---')
    print('1 - Adicionar contato')
    print('2 = Editar contado(telefone)')
    print('3 - Remover contato')
    print('4 - Buscar contato')
    print('5 - Listar todos')
    print('6 - Sair')
    opcao = int(input('Selecione uma opção: '))
    if opcao == 1:
        nome = input('Digite o Nome do Contato: ')
        telefone = input('Digite o Telefone do Contato: ')
        agenda[nome] = telefone
        print('Contato Adicionado Com Sucesso!')
    elif opcao == 2:
        nome = input('Digite o Nome do Contato:')
        if nome in agenda:
            agenda[nome] = input('Digite o Novo Telefone:')
            print('Telefone Alterado com Sucesso!')
        else:
            print('Contato Não Encontrado!')
    elif opcao == 3:
        nome = input('Digite o Nome do Contato: ')
        if nome in agenda:
            del agenda[nome]
            print('Contato Removido com Sucesso!')
        else:
            print('Contato Não Encontrado!')
    elif opcao == 4:
        nome = input('Digite o Nome do Conteto: ')
        if nome in agenda:
            print(f'Telefone de {nome}: {agenda[nome]}')
        else:
            print('Contado Não Encontrado!')
    elif opcao == 5:
        for nome in agenda:
           print('Todos os Contatos')
           for nome in agenda:
               print(f'Nome: {nome} - Telefone:: {agenda[nome]}')
    elif opcao == 6:
        break
    else:
        print('Opção Inválida!')
