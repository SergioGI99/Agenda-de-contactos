import re, json

contactos: dict = {}
try:
    stored_agenda = open("stored-agenda.json", "r")
    contactos = json.load(stored_agenda)
except:
    stored_agenda = open("stored-agenda.json", "w")

def agenda(action: str):

    def input_name():
        inputName: str = input("Escribe el nombre del contacto: ")
        patternName = r"[A-Za-z]"
        if re.search(patternName, inputName):
            return inputName
        else:
            print("Nombre de contacto invalido.")
            return input_name()
    
    def input_number():
        inputNumber: int = input("Escribe un número de telefono: ")
        patternNumber = r"[0-9]"
        if re.search(patternNumber, inputNumber) and len(inputNumber) == 9:
            return inputNumber
        else:
            print("Numero de telefono invalido. (Compruebe que el número tenga 9 caracteres numéricos)")
            return input_number()
        
    def refresh():
        refresh = open("stored-agenda.json", "w")
        json.dump(contactos, refresh)
        refresh.close


    def add():
        name = input_name()
        if not name in contactos.keys():
            number = input_number()
            contactos[name] = number
            refresh()
            print(name, "ha sido añadido a la agenda.")
        else:
            print("El contacto ya existe")

    def search():
        name = input_name()
        if name == "Wally":
            print("La ultima vez fue visto con un jersey de rallas rojas y blancas.")
        if name in contactos.keys():
            search = contactos.get(name)
            print(f"El numero de ", name, " es ", search)
        else:
            print("El contacto no existe")

    def delete():
        name = input_name()
        if name in contactos.keys():
            confirmation = input(f"Vuelve a escribir el nombre para confirmar:\n")
            if name == confirmation:
                contactos.pop(name)
                refresh()
                print(f"{name} ha sido eliminado de la agenda")
            else:
                print("No coincide el nombre")
                delete()
        else:
            print("El nombre no aparece en la agenda")
        
    def update():
        name = input_name()
        if name in contactos.keys():
            new_number = input_number()
            contactos[name] = new_number
            refresh()
            print(f"{name} ha sido actualizado")
        else:
            print("El contacto no existe")

    def list():
        if len(contactos) == 0:
            print("La agenda está vacía.")
        else:
            for contacto in contactos:
                print("- ", contacto, ":", contactos[contacto])

    def exit():
        return print("Cerrando la agenda de contactos...")
    

    actions: dict = {
        "añadir": add,
        "eliminar": delete,
        "actualizar": update,
        "buscar": search,
        "lista": list
    }

    try:
        if action == "salir":
            return exit()
        else:
            actions[action]()
    except:
        print(f"No se ha encontrado ninguna acción que se llame: {action}")

    agenda(input("Selecciona otra acción: "))

agenda(input("¿Que acción quieres realizar?\n - añadir\n - eliminar\n - actualiar\n - buscar\n - lista\n - salir\n: "))

print("Se ha cerrado la agenda de contactos.")