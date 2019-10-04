agenda = []


def mostrar_todos():
    # verifica se existem contatos na agenda
    if agenda.__len__() > 0:
        # Itera sobre os contatos da agenda
        for contato in agenda:
            print(agenda.index(contato), ' - ', contato)
    else:
        print('Não existem contatos na agenda!')


def inserir_contato(nome):
    # Insere um novo nome de contato na agenda
    agenda.append(nome)
    print('Contato inserido com sucesso!')


def alterar_contato(id):
    # Verifica se o id do contato existe
    if agenda.__len__() > id:
        novo_nome = input('Informe o nome do contato: ')
        agenda[id] = novo_nome
    else:
        print('Contato não encontrado!')


def buscar_id(id):
    if agenda.__len__() > id:
        print(agenda[id])
    else:
        print('Contato não encontrado!')


def excluir_id(id):
    if agenda.__len__() > id:
        agenda.__delitem__(id)
        print('Contato excluido com sucesso!')
    else:
        print('Contato não encontrado!')


# Menu do sisteminha
print('#########################')
print('#     MENU - AGENDA     #')
print('# 1 - Acessar Agenda    #')
print('# 2 - Inserir Contato   #')
print('# 3 - Alterar Contato   #')
print('# 4 - Buscar pelo ID    #')
print('# 5 - Buscar por nome   #')
print('# 6 - Excluir por ID    #')
print('# 7 - Excluir Agenda    #')
print('# 8 - Sair              #')
print('#########################')

op = 0
while op != 8:

    op = int(input('Opção: '))

    if op == 1:
        mostrar_todos()

    elif op == 2:
        nome = input('Informe o nome do contato: ')
        inserir_contato(nome)

    elif op == 3:
        id = int(input('Informe o id do contato: '))
        alterar_contato(id)

    elif op == 4:
        id = int(input('Informe o id do contato: '))
        buscar_id(id)

    elif op == 5:
        pass

    elif op == 6:
        id = int(input('Informe o id do contato: '))
        excluir_id(id)

    elif op == 7:
        pass

    elif op == 8:
        pass

    else:
        print('Opção inválida!')