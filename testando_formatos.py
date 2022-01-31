try:
 with open('testando.txt', 'a') as arquivo:
     #o 'w' te permite criar arquivos por linhas de comando do with
     #o 'a' te permite adicionar informação
     #o 'r' te permite ler o arquivo
     arquivo.write('guilherme \n')
except Exception as error:
    print('algum erro ocorreu')
    print(error)