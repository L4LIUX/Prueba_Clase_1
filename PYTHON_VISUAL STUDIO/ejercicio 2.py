def calcular_disponible(presupuesto, gasto):
    return presupuesto - gasto

def obtener_estado(disponible):
    if disponible > 0:
        return "Aun tienes presupuesto"
    elif disponible == 0:
        return "Ya no tienes dinero, lo gastaste todo"
    else:
        return "Ya no tienes dinero, debes dinero"

def main():
    print("CONTROL DE PRESUPUESTO")
    nombre = input("Ingrese su nombre: ")
    categoria = input("Ingrese la categoria de gasto: ")
    presupuesto = float(input("Ingrese el presupuesto: "))
    gasto = float(input("Ingrese el gasto: "))

    valores_validos = presupuesto >= 0 and gasto >= 0

    if not valores_validos:
        print("Los valores ingresados no son validos, Por favor, ingrese bumeros positivos")
        return

    disponible = calcular_disponible(presupuesto, gasto)
    estado = obtener_estado(disponible)
    print("Resumen del presupuesto")
    print(f"Nombre: {nombre}")
    print(f"Categoría: {categoria}")
    print(f"Presupuesto: {presupuesto}")
    print(f"Gasto: {gasto}")
    print(f"Disponible: {disponible}")
    print(f"Estado: {estado}")
    
main()