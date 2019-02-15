diccionario = {1: 'hola',  
               2:"mundo",  
               3:"desde", 
               "cuatro": "diccionario"}

print(type(diccionario))

print(diccionario["cuatro"])

for keys, value in diccionario.items():
    print(f"""llave{keys}valor-{value}""")

    persona = {}

    persona["nombre"] = "Jorge"
    persona["apellido"] = "Valdez"
    PERSONA["edad"] = 23

    for datos, value in persona.items():
        print(f"""{datos}-{value}""")


        if "correo" in persona:
            print(f"""el correo es{persona["correo"]}""")
        else:
            print("no tiene correo")

            if persona.get("altura") == None:
                persona["altura"]="1.80mts"

            print(persona.get("altura"))


