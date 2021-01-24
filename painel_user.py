from os import system as s
import json, sys



banner_h = (''' 
using: python3 painel_user.py [options]
exe: python3 painel_user.py [remove] or python3 painel_user.py [r]
# User: user
# user removed.

para mais informações use python3 painel_user.py -h
''')
# ---
def clear():
    s('clear')

clear()
try:
    opc = sys.argv[1]
except:
    print(banner_h)
    exit()
# ---
if opc == 'add':
    class add_usuario():

        def usuario(user,  key, day, status):
            usuario = {
                user:{    
                    "key":key,
                    "days":day,
                    "status":status
                }
            }

            arquivo_json = json.dumps(usuario, indent=5)
            return arquivo_json

        user_name = input("Nome Do Usuario: ")
        key = input(f"Key Para {user_name}: ")
        day = input(f"Dias Restantes Do {user_name}: ")
        status = input(f"True/False: ")


        Json = usuario(user_name, key, day, status)
        arquivo = open(f'db/users/{user_name}.json', 'w')
        arquivo_name = f'{user_name}.json'


        arquivo.write(Json)
        print("Usuario Criado")
        exit()

if opc == 'remove' or opc == 'r':
    class rm_user:
        us = input('User: ')
        s(f'rm -rf db/users/{us}.json')
        print("Usuario Removido")
        exit()

# e q pra sair kk
if opc == 'find' or opc == 'f':
    class find():
        print('-----Users----')
        s('ls db/users/')
        print('--------------')
        exit()