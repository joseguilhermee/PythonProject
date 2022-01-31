#AGENDA ( 1 / 7 )

AGENDA = {}

AGENDA['Guilherme'] = {
    'telefone': '99999999',
    'email': 'guilherme@gmail.com',
}
AGENDA['Guilhermee'] = {
    'telefone': '99999999',
    'email': 'guilherme@gmail.com',
}

def layout():
    print('____________________________________')

def search_contact(contact):
    print("Telefone:", AGENDA[contact]['telefone'])
    print("Email:", AGENDA[contact]['email'])

def show_contacts():
    for contact in AGENDA:
        layout()
        print("NOME:", contact)
        search_contact(contact)
        layout()

def search(contact):
    layout()
    print('Nome:', contact)
    search_contact(contact)
    layout()

def add_contact(contato, telefone, email):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
    }
    print(f'---> contato { contato } adicionado com sucesso')

def modify_contact(contato, telefone, email):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
    }
    print(f'---> contato { contato } editado com sucesso')

def delete_contact(contato):
    AGENDA.pop(contato)
    print(f'---> contato { contato } excluido com sucesso')


def show_menu():
    print('1 - Mostrar todos os contatos')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('0 - Fechar agenda')

while True:
    show_menu()
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        show_contacts()
    elif opcao == '2':
        search(input('Digite o nome do contato: '))
    elif opcao == '3':
        add_contact(input('Digite o Nome: '), input('Digite o Telefone: '), input('Digite o Email '))
    elif opcao == '4':
        modify_contact(input('Digite o Nome de quem deseja modificar: '), input('Digite o Telefone: '), input('Digite o Email '))
    elif opcao == '5':
        delete_contact(input("Digite o contato que quer excluir: "))
    elif opcao == '0':
        print('Fechando programa')
        break
    else:
        print('Opção inválida')

