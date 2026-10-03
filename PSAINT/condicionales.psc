Algoritmo condicionales
	Escribir "Tipos de condicionales: Si-Entonces-SiNo (If, elif, else)"
	Definir temp, Presion Como Real
	Definir Respuesta Como Caracter
	Escribir "Ingresa la temperatura de el motor: "
	Leer temp
	Escribir "Ingresa la presion de las llantas: "
	Leer Presion
	Escribir "Operadores relacionales: <,>,=,<>"
	Escribir "Operadores logicos: Y, O, NO (And, Or, Not)"
	Si temp > 100 O presion > 1000
		Escribir "Fallo Critico en el motor"
		Escribir "Deseas apagar el motor?"
		Leer Respuesta
		Si Respuesta = "Si" 
			Escribir "Apagando motor..."
		SiNo
			Escribir "Fallo critico"
		FinSi
	SiNo
		Escribir "Niveles Adecuados"
	FinSi
FinAlgoritmo
