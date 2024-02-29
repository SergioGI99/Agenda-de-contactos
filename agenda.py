import re, json

contactos = {}

stored_agenda = open("stored-agenda.json", "r+")

contactos = json.load(stored_agenda)

def agenda(action):


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

    def añadir():
        name = input_name()
        if not name in contactos.keys():
            number = input_number()
            contactos[name] = number
            print(name, "ha sido añadido a la agenda.")
        else:
            print("El contacto ya existe")

    def buscar():
        name = input_name()
        if name in contactos.keys():
            search = contactos.get(name)
            print(f"El numero de ", name, " es ", search)
        else:
            print("El contacto no existe")

    def eliminar():
        name = input_name()
        if name in contactos.keys():
            confirmation = input(f"Vuelve a escribir el nombre para confirmar:\n")
            if name == confirmation:
                print(f"{name} ha sido eliminado de la agenda")
                contactos.pop(name)
            else:
                print("No coincide el nombre")
                eliminar()
        else:
            print("El nombre no aparece en la agenda")
        
    def actualizar():
        name = input_name()
        if name in contactos.keys():
            new_pass = input_number()
            contactos[name] = new_pass
            print(f"{name} ha sido actualizado")
        else:
            print("El contacto no existe")

    def agenda():
        for contacto in contactos:
            print(contacto, contactos[contacto])

    if action == "añadir":
        añadir()

    elif action == "eliminar":
        eliminar()
    
    elif action == "actualizar":
        actualizar()
    
    elif action == "buscar":
        buscar()

    elif action == "agenda":
        agenda()

    elif action == "salir":
        return print("Cerrando la agenda de contactos...")
    
    else:
        print(f"No se ha encontrado ninguna acción que se llame: {action}")
        agenda(input("Selecciona otra acción: "))

    agenda(input("Elije otra acción: "))



agenda(input("Que acción quieres realizar(añadir/eliminar/actualiar/buscar/agenda/salir): "))


stored_agenda = open("stored-agenda.json", "w+")

json.dump(contactos, stored_agenda)
stored_agenda.close

print("Se ha cerrado la agenda de contactos.")