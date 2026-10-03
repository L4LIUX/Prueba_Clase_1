CATEGORIAS = ["materiales", "transporte", "servicios", "otros"]

def registrar_gasto(gastos: list[dict], id_g: int, cat: str, monto: float) -> None:
    cat_limpia = cat.strip().lower()
    if cat_limpia not in CATEGORIAS:
        raise ValueError(f"Categoría inválida. Debe ser: {', '.join(CATEGORIAS)}")
    if monto <= 0:
        raise ValueError("El monto debe ser un número positivo mayor a 0.")
    if any(g["id"] == id_g for g in gastos):
        raise ValueError(f"El ID {id_g} ya está registrado.")
    
    gastos.append({"id": id_g, "categoria": cat_limpia, "monto": monto})

def calcular_total(gastos: list[dict]) -> float:
    return sum(g["monto"] for g in gastos)

def calcular_saldo(presupuesto: float, gastos: list[dict]) -> float:
    return presupuesto - calcular_total(gastos)

def buscar_por_categoria(gastos: list[dict], cat: str) -> list[dict]:
    return [g for g in gastos if g["categoria"] == cat.strip().lower()]

def modificar_gasto(gastos: list[dict], id_g: int, monto: float) -> bool:
    if monto <= 0:
        raise ValueError("El monto debe ser mayor a 0.")
    for g in gastos:
        if g["id"] == id_g:
            g["monto"] = monto
            return True
    return False

def eliminar_gasto(gastos: list[dict], id_g: int) -> bool:
    for i, g in enumerate(gastos):
        if g["id"] == id_g:
            gastos.pop(i)
            return True
    return False

# ==========================================
# INTERFAZ DE CONSOLA
# ==========================================

def pedir_num(mensaje: str, tipo=float):
    while True:
        try:
            return tipo(input(mensaje).strip())
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

def mostrar_resumen(presupuesto: float, gastos: list[dict]):
    total = calcular_total(gastos)
    saldo = calcular_saldo(presupuesto, gastos)
    print("\n" + "="*40)
    print("        RESUMEN DE PRESUPUESTO")
    print("="*40)
    print(f"Presupuesto inicial : ${presupuesto:,.2f}")
    print(f"Total gastado       : ${total:,.2f}")
    print(f"Saldo disponible    : ${saldo:,.2f}")
    print("-" * 40)
    
    if saldo > 0:
        print("ESTADO: Dispones de saldo suficiente.")
    elif saldo == 0:
        print("ESTADO: Presupuesto en cero (agotado).")
    else:
        print("ESTADO: ¡ALERTA! Saldo negativo (déficit).")
    print("="*40)

def menu():
    gastos = []
    print("--- BITÁCORA DE GASTOS DE LABORATORIO ---")
    presupuesto = pedir_num("Ingrese el presupuesto inicial del laboratorio: $", float)

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar gasto")
        print("2. Consultar todos los gastos")
        print("3. Ver resumen de presupuesto")
        print("4. Buscar gastos por categoría")
        print("5. Modificar monto de un gasto")
        print("6. Eliminar un gasto")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                try:
                    i = pedir_num("ID del gasto: ", int)
                    c = input(f"Categoría ({'/'.join(CATEGORIAS)}): ")
                    m = pedir_num("Monto ($): ", float)
                    registrar_gasto(gastos, i, c, m)
                    print("Gasto registrado con éxito.")
                except ValueError as err:
                    print(f"Error: {err}")

            case "2":
                if not gastos:
                    print("No hay gastos registrados aún.")
                    continue
                print("\n--- LISTA DE GASTOS ---")
                for g in gastos:
                    print(f"ID: {g['id']} | Categoría: {g['categoria'].capitalize():<12} | Monto: ${g['monto']:,.2f}")

            case "3":
                mostrar_resumen(presupuesto, gastos)

            case "4":
                cat = input("Categoría a buscar: ")
                res = buscar_por_categoria(gastos, cat)
                if not res:
                    print(f"No se han encontraron gastos en '{cat}'.")
                    continue
                print(f"\n--- Coincidencias para '{cat.strip().lower()}' ---")
                for g in res:
                    print(f"ID: {g['id']} | Monto: ${g['monto']:,.2f}")

            case "5":
                try:
                    i = pedir_num("ID del gasto a modificar: ", int)
                    m = pedir_num("Nuevo monto ($): ", float)
                    if modificar_gasto(gastos, i, m):
                        print("Monto actualizado con exito.")
                    else:
                        print(f"ID {i} no encontrado.")
                except ValueError as err:
                    print(f"Error: {err}")

            case "6":
                i = pedir_num("ID del gasto a eliminar: ", int)
                if eliminar_gasto(gastos, i):
                    print("Gasto eliminado con exito.")
                else:
                    print(f"ID {i} no encontrado.")

            case "7":
                print("Gracias, Hasta luego...")
                break

            case _:
                print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()