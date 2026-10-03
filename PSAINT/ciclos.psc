Algoritmo ciclos
	Escribir "Tipos de ciclos: Mientras (while) infinito"
	Escribir "Tipo de ciclo: Para (for) es finito"
	Definir lectura, suma, promedio Como Real
	Definir i, cantidadlectura Como Entero
	suma <- 0
	cantidadlectura <- 10
	Escribir "Comenzando calibración..., se tomaran 10 lecturas"
	Para i <- 1 Hasta cantidadlectura
		Escribir "Dime la lectura: "
		Leer lectura
		Escribir "La lectura actual es: ", lectura
		suma <- suma + lectura
	FinPara
	Escribir "La suma de datos guardados es: ", suma
FinAlgoritmo
