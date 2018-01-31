import math

def cedula_es_valida(cedula):
    if len(cedula) != 10:
        return "No valida: debe ser de 10 digitos"
    else:
        if int(cedula[0:2]) > 24:
            return "No valida: Los primeros dos digitos no pertenecen a una provincia"
        if int(cedula[2]) > 6:
            return "No valida: el tercer digito debe ser menor a 6"
        coeficientes = '212121212'
        resultado = [0]*9
        for index in range(0, 9):
            producto = int(cedula[index])*int(coeficientes[index])
            if producto >= 10:
                producto -= 9
            resultado[index] = producto
        digito_validador = int(math.ceil(sum(resultado)/10.0))*10 - sum(resultado)
        if digito_validador != int(cedula[9]):
            return "No valida: no coincide el digito validador"
        return "Valida"
