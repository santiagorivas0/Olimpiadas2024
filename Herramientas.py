"""
Herramientas.py contiene funciones auxiliares:
- Valida y gestiona entradas del usuario.
- Facilita el manejo de fechas, enteros, flotantes y códigos específicos.
"""

from datetime import date

def solicitar_entero(titulo):
    ok = False
    texto_ingresado = input(titulo)
    entero = 0
    while not ok:
        try:
            entero = int(texto_ingresado)
        except ValueError:
            print("El valor ingresado no es correcto. Intente nuevamente.")
            texto_ingresado = input("Ingrese número: ")
        else:
            ok = True
    return entero

def solicitar_flotante(titulo):
    ok = False
    texto_ingresado = input(titulo)
    flotante = 0.0
    while not ok:
        try:
            flotante = float(texto_ingresado)
        except ValueError:
            print("El valor ingresado no es correcto. Intente nuevamente.")
            texto_ingresado = input("Ingrese número decimal: ")
        else:
            ok = True
    return flotante

def solicitar_fecha(titulo):
    ok = False
    print(titulo)
    dia = solicitar_entero("Ingrese el día: ")
    mes = solicitar_entero("Ingrese el mes: ")
    anio = solicitar_entero("Ingrese el año: ")
    fecha = None
    while not ok:
        try:
            fecha = date(anio, mes, dia)
        except ValueError:
            print("Ocurrió un error. Por favor intente nuevamente.")
            dia = solicitar_entero("Ingrese el día: ")
            mes = solicitar_entero("Ingrese el mes: ")
            anio = solicitar_entero("Ingrese el año: ")
        else:
            ok = True
    return fecha

def validar_codigo(codigo, longitud):
    #Valida que el código ingresado tenga la cantidad de dígitos especificada
    while len(str(codigo)) != longitud:
        print(f"Error. Usted ingresó un número que no contiene {longitud} dígitos.") #Muestra un mensaje de error si la longitud no es válida
        codigo = input(f"Ingrese un código identificador válido de {longitud} dígitos: ")
    return int(codigo)