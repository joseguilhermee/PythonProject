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
    print('contato adicionado com sucesso')

add_contact('joao', '7777777', 'testando@gmail.com')

show_contacts()