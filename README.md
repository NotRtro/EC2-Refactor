# refactor-practice
Practica de refactor

## Integrantes 
* Rodo Vilcarromero
* Mauricio Alvarez
* Diego Pacheco
* Ronaldo Flores
* Salvador Olivares
* Alexandro Chamochumbi
* Jeffry Hilario

## Evaluacion : 

Clase CalculaGanador: Esta es la clase que contiene el programa y desde donde se instancia.

Método leerdatos: Este método lee los datos de un archivo CSV y devuelve una el dataframe del csv.

Método contar_votos: Este método toma los datos leídos y cuenta los votos para cada candidato. Utiliza un diccionario para almacenar los conteos y se actualiza segun que voto va ingresando.

Método calcularganador: Este método utiliza el método contar_votos para obtener los conteos de votos y los ordena segun los votos, luego imprime a todos los participantes con su cantidad respectiva de votos y finalmente imprime al ganador y su cantidad de votos con los que se llevo el primer puesto.
