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



show_contacts()