"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    f = open('data.csv', 'r')
    lines = f.readlines()
    
    total = sum(map(lambda line: int(line.split('\t')[1] if line.split('\t') else 0), lines))

    return total


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    f = open('data.csv', 'r')
    lines = f.readlines()

    # Crear lista de letras sin repetirlas y ordenarlas 
    words = list(set(map(lambda line: line.split('\t')[0] if line.split('\t') else '', lines)))
    words.sort()

    # Contar cuantas letras hay de cada una
    result = [(word, len(list(filter(lambda line: line.split('\t')[0] == word, lines)))) for word in words]

    return result


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    f = open('data.csv', 'r')
    lines = f.readlines()
    linec1_filter = lambda line: line.split('\t')[0] if line.split('\t') else ''
    linec2_filter = lambda line: int(line.split('\t')[1]) if line.split('\t') else 0

    # Crear lista de letras sin repetirlas y ordenarlas 
    words = list(set(map(linec1_filter, lines)))
    words.sort()

    # Contar cuantas letras hay de cada una
    word_filter = lambda word: filter(lambda line: (line.split('\t')[0] if line.split('\t') else '') == word, lines)

    result = [(word, sum(map(linec2_filter, word_filter(word)))) for word in words]

    return result


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    f = open('data.csv', 'r')
    lines = f.readlines()
    linec3_filter = lambda line: line.split('\t')[2] if line.split('\t') else ''

    date_filter = lambda date: date.split('-')[1]
    dates_list = list(map(linec3_filter, lines))

    month_list = list(map(date_filter, dates_list))
    months = list(set(month_list))
    months.sort()

    month_filter = lambda month_f: list(filter(lambda month: month == month_f, month_list))

    result = [(month_f, len(month_filter(month_f))) for month_f in months]

    return result


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    f = open('data.csv', 'r')
    lines = f.readlines()
    linec1_filter = lambda line: line.split('\t')[0] if line.split('\t') else ''
    linec2_filter = lambda line: int(line.split('\t')[1]) if line.split('\t') else 0

    # Crear lista de letras sin repetirlas y ordenarlas 
    words = list(set(map(linec1_filter, lines)))
    words.sort()

    # Sacar valor maximo y minimo de cada letra
    word_filter = lambda word: filter(lambda line: (line.split('\t')[0] if line.split('\t') else '') == word, lines)

    result = [(word, max(map(linec2_filter, word_filter(word))), min(map(linec2_filter, word_filter(word)))) for word in words]
    return result


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    f = open('data.csv', 'r')
    lines = f.readlines()
    linec5_filter = lambda line: line.split('\t')[4].split(',')
    
    # Crear lista de letras sin repetirlas y ordenarlas 
    key_value_list = [key_value.strip('\n').split(':') for line_c5 in map(linec5_filter, lines) for key_value in line_c5]
    keys = list(set([k for k, v in key_value_list]))
    keys.sort()

    result = []
    for key in keys:
        values_per_key = list(map(lambda kvi: int(kvi[1]), filter(lambda kvj: kvj[0] == key, key_value_list)))
        min_value = min(values_per_key)
        max_value = max(values_per_key)
        result.append((key, min_value, max_value))

    return result


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    f = open('data.csv', 'r')
    lines = f.readlines()
    linec1_filter = lambda line: line.split('\t')[0] if line.split('\t') else ''
    linec2_filter = lambda line: int(line.split('\t')[1]) if line.split('\t') else 0

    # Crear lista de numeros sin repetirlas y ordenarlas 
    numbers = list(set(map(linec2_filter, lines)))
    numbers.sort()

    # Crear lista de filas que tengan el 'number' en la columna 2
    number_filter = lambda number: filter(lambda line: int(line.split('\t')[1]) == number, lines)

    result = [(number, list(map(linec1_filter, number_filter(number)))) for number in numbers]

    return result


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    f = open('data.csv', 'r')
    lines = f.readlines()
    linec1_filter = lambda line: line.split('\t')[0] if line.split('\t') else ''
    linec2_filter = lambda line: int(line.split('\t')[1]) if line.split('\t') else 0

    # Crear lista de letras sin repetirlas y ordenarlas 
    numbers = list(set(map(linec2_filter, lines)))
    numbers.sort()

    # Contar cuantas letras hay de cada una
    number_filter = lambda number: filter(lambda line: int(line.split('\t')[1]) == number, lines)

    result = [(number, sorted(set(map(linec1_filter, number_filter(number))))) for number in numbers]

    return result


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    f = open('data.csv', 'r')
    lines = f.readlines()
    linec5_filter = lambda line: line.split('\t')[4].split(',')
    
    # Crear lista de letras sin repetirlas y ordenarlas 
    key_value_list = [key_value.strip('\n').split(':') for line_c5 in map(linec5_filter, lines) for key_value in line_c5]
    keys = list(set([k for k, v in key_value_list]))
    keys.sort()

    result = {}
    for key in keys:
        values_per_key = list(map(lambda kvi: int(kvi[1]), filter(lambda kvj: kvj[0] == key, key_value_list)))
        result[key] = len(values_per_key)

    return result


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
