import csv
# el programa deberá calcular el ganador de votos validos considerando que los siguientes datos son proporcionados:
## region,provincia,distrito,dni,candidato,esvalido
# Si hay un candidato con >50% de votos válidos retornar un array con un string con el nombre del ganador
# Si no hay un candidato que cumpla la condicion anterior, retornar un array con los dos candidatos que pasan a segunda vuelta
# Si ambos empatan con 50% de los votos se retorna el que apareció primero en el archivo
# el DNI debe ser valido (8 digitos)
class CalculaGanador:

    def leerdatos(self):
        with open('0204.csv', 'r') as csvfile:
            next(csvfile)
            datareader = csv.reader(csvfile)
            return [fila for fila in datareader] # for por compresion para no usar mucha memoria en el programa


    def contar_votos(self, data): # separamos la parte de contar votos para hacerlo más eficiente
        votosxcandidato = {fila[4]: 0 for fila in data if fila[5] == '1'} #uso de diccionarios para lograr un mejor rendimiento
        for fila in data:
            if fila[5] == '1':
                votosxcandidato[fila[4]] += 1 # El conteo de votos se actualiazara en el diccionario
        return votosxcandidato

    def calcularganador(self, data):
        votosxcandidato = dict(sorted(self.contar_votos(data).items(), key=lambda item: item[1], reverse=True)) #ordenamos el diccionario de mayor a menor
        print(votosxcandidato)
        for candidato, votos in votosxcandidato.items():
            print(f'candidato: {candidato} votos validos: {votos}') #fstrisngs para la concatenacion de strings más facil
        return f'El ganador es : {list(votosxcandidato.keys())[0]}, con un total de {list(votosxcandidato.values())[0]} votos.'#retorna el ganador

c = CalculaGanador()
#c.calcularvotos(c.leerdatos())
datatest = [
['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
]
print(c.calcularganador(datatest))
