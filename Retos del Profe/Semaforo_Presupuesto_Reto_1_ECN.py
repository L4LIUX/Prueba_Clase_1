def evaluar_presupuesto(presupuesto, gasto):
    diferencia = presupuesto - gasto
    
    if diferencia > 0:
        aviso = f"Dentro del presupuesto, a usted le quedan ${diferencia:.2f}."
    elif diferencia == 0:
        aviso = "Has gastado todo su presupuesto. Saldo restante: $0.00."
    else:
        exceso = gasto - presupuesto
        aviso = f"¡C U I D A D O! Usted se has excedido por ${exceso:.2f} de su presupuesto."
        
    return diferencia, aviso

def main():
    print("=== CONTROL DE PRESUPUESTO SEMANAL ===")
    
    nombre = input("Ingresa tu nombre: ")
    presupuesto = float(input("Ingresa tu presupuesto semanal: "))
    gasto = float(input("Ingresa el monto del gasto realizado: "))
    categoria = input("Ingresa la categoría del gasto: ")

    resultado,  mensaje = evaluar_presupuesto(presupuesto, gasto)
    
    print("\n       ---RESUMEN DE GASTO---")
    print(f"Usuario: {nombre}")
    print(f"Presupuesto semanal: ${presupuesto:.2f}")
    print(f"Categoría del gasto: {categoria}")
    print(f"Monto gastado: ${gasto:.2f}")
    print(f"Dinero restante: ${resultado:.2f}")
    print(f"Estado: {mensaje}")

main()