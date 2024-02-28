import re

contactos = {
"sergio" : 671408033
}
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
        inputNumber:int = input("Escribe un número de telefono: ")
        patternNumber = r"[0-9]"
        if re.search(patternNumber, inputNumber):
            return inputNumber
        else:
            print("Numero de telefono invalido.")
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

    if action == "añadir":
        añadir()

    elif action == "eliminar":
        eliminar()
    
    elif action == "actualizar":
        actualizar()
    
    elif action == "buscar":
        buscar()

    elif action == "salir":
        return print("Cerrando la agenda de contactos...")
    
    else:
        print(f"No se ha encontrado ninguna acción que se llame: {action}")
        agenda(input("Selecciona otra acción: "))

    agenda(input("Elije otra acción: "))



agenda(input("Que acción quieres realizar(añadir/eliminar/actualiar/buscar/salir): "))


print("Se ha cerrado la agenda de contactos.")