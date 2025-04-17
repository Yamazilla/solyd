AGENDA = {}

def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
            print("-----------------------------------------------")
    
    else:
        print("Agenda vazia")


def buscar_contato(contato):
    try: 
        print("Nome:", contato)
        print("Telefone:", AGENDA[contato]["telefone"]) 
        print("E-mail:", AGENDA[contato]["email"])
        print("Endereço:", AGENDA[contato]["endereco"])
        print("-----------------------------------------------")

    except KeyError:
        print(">>>>Contato inexistente")

    except Exception as error:
        print(">>>> Um erro inesperado ocorreu")

def ler_detalhes_contato():
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o e-mail do contato: ")
    endereco = input("Digite o endereço do contato: ")
    return telefone, email, endereco

def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco,
    }
    save()
    print()
    print(">>>>> Contato {} adicionado/editado com sucesso!".format(contato))
    print()

def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        save()
        print()
        print(">>>> Contato {} excluido com sucesso!".format(contato))
        print()
    
    except KeyError:
        print(">>>>Contato inexistente")

    except Exception as error:
        print(">>>> Um erro inesperado ocorreu")

def exportar_contatos(filename):
    try:
        with open(filename, "w") as file:
            for contato in AGENDA:
                telefone = AGENDA[contato]["telefone"]
                email = AGENDA[contato]["email"]
                endereco = AGENDA[contato]["endereco"]
                file.write("{},{},{},{}\n".format(contato, telefone, email, endereco))

        print(">>>> Agenda exportada com sucesso")
    
    except Exception as error:
        print(">>>> Algum erro ocorreu ao exportar contatos")
        print(error)

def importar_contatos(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                detalhes = line.strip().split(",")
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(nome, telefone, email, endereco)


    except FileNotFoundError:
        print(">>>> Arquivo não encontrado")

    except Exception as error:
        print(">>>> Algum erro ocorreu")
        print(error)      

def save():
    exportar_contatos("database.csv")

def load():
    try:
        with open("database.csv" "r") as file:
            lines = file.readlines()
            for line in lines:
                detalhes = line.strip().split(",")
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    "telefone": telefone, 
                    "email": email,
                    "endereco": endereco,
                }

    except FileNotFoundError:
        print(">>>> Arquivo não encontrado")

    except Exception as error:
        print(">>>> Algum erro ocorreu")
        print(error)  
    

def imprimir_menu():
    print("-----------------------------------------------")
    print("1 - Mostrar todos os contatos da agenda")
    print("2 - Buscar contatos")
    print("3 - Incluir contatos na agenda")
    print("4 - Editar contato existete")
    print("5 - Excluir contato da agenda")
    print("6 - Exportar agenda")
    print("7 - Importar contatos .csv")
    print("0 - Fechar agenda")
    print("-----------------------------------------------")

load()

while True:

    imprimir_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_contatos()

    elif opcao == "2":
        contato = input("Digite o nome do contato desejado: ")
        buscar_contato(contato)

    elif opcao == "3":
        contato = input("Digite o nome do contato: ")

        try:

            AGENDA[contato]
            print(">>>> Contato ja existente")
             
        except KeyError:
            
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
            buscar_contato(contato)

    elif opcao == "4":
        try:

            AGENDA[contato]
            print(">>>> Editando contato: ", contato)
             
            incluir_editar_contato(contato)
            buscar_contato(contato)
            

        except KeyError:
            print(">>>> Contato inexistente")

    elif opcao == "5":
        contato = input("Digite o nome do contato que deseja excluir: ")
        excluir_contato(contato)

    elif opcao == "6":
        filename = input("Digite o nome do arquivo a ser exportado: ")
        exportar_contatos(filename)

    elif opcao == "7":
        filename = input("Digite o nome do arquivo: ")
        importar_contatos(filename)


    elif opcao == "0":
        print(">>>>Encerrando agenda")
        break

    else:
        print(">>>>Opção invalida")