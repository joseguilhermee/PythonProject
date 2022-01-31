#AGENDA ( 1 / 7 )

AGENDA = {}


def layout():
    print('____________________________________')

def search_contact(contact):
    print("Telefone:", AGENDA[contact]['telefone'])
    print("Email:", AGENDA[contact]['email'])

def show_contacts():
    if AGENDA:
        for contact in AGENDA:
            layout()
            print("NOME:", contact)
            layout()
    else:
        layout()
        print('Agenda Vazia')
        layout()

def search(contact):
    try:
        layout()
        print('Nome:', contact)
        search_contact(contact)
        layout()
    except KeyError:
        layout()
        print('Contato Inexistente')
        layout()
    except Exception as error:
        layout()
        print('Um Erro inesperado ocorreu')
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
    try:
        AGENDA.pop(contato)
        print(f'---> contato { contato } excluido com sucesso')
    except KeyError:
        layout()
        print('Contato Inexistente')
        layout()
    except Exception as error:
        layout()
        print('Um Erro inesperado ocorreu')
        layout()


def show_menu():
    layout()
    print('1 - Mostrar todos os contatos')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contatos para CSV')
    print('0 - Fechar agenda')
    layout()

def export_contacts():
    try:
        with open('agenda.csv', 'w') as arquivo:
            arquivo.write('NOME, TELEFONE, EMAIL \n')
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email= AGENDA[contato]['email']
                arquivo.write(f"{contato};{telefone};{email} \n")
        print('Agenda exportada com sucesso')
    except:
        print("algum erro ocorreu")

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
    elif opcao == '6':
        export_contacts()
    elif opcao == '0':
        print('Fechando programa')
        break
    else:
        print('Opção inválida')
