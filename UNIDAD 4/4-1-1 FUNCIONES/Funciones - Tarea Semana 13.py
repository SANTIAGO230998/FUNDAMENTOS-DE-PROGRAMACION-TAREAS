#Desarrollo de Función para Calcular Temperaturas Promedio en Python
def funcion_calcular_promedio (temperaturas, ciudades):
    promedios = {} #Diccionario para almacenar los promedios de cada ciudad
    suma_temperaturas = 0  # Suma de todas las temperaturas de la ciudad
    total_dias = 0  # Total de días registrados para la ciudad

# Recorrer las ciudades y calcular el promedio total de cada ciudad
    for ciudad_idx, ciudad in enumerate (temperaturas):
        for semana in ciudad: #Recorrer cada semana en la ciudad
            suma_temperaturas += sum(dia["temp"]for dia in semana)  #Sumar las temperaturas de todos los días de la semana
            total_dias += len (semana) #Contar los días en esa semana

        # Calcular el promedio de temperatura de la ciudad
        promedio = suma_temperaturas / total_dias
        promedios[ciudades[ciudad_idx]] = round (promedio, 2) #Almacenar el promedio en el diccionario
    return promedios

# Declarar
# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Santo Domingo
        [   # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 27}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 23}
        ]
    ],
    [   # Portoviejo
        [   # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 34},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp":33}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 30}
        ]
    ],
    [   # Cuenca
        [   # Semana 1
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp":10}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 9},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 13},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 11}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp":13}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 5},
            {"day": "Martes", "temp":7 },
            {"day": "Miércoles", "temp": 9},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 11},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 10}
        ]
    ]
]

# Lista de nombres de ciudades
ciudades = ["Santo Domingo", "Portoviejo", "Cuenca"]

# Llamada a la función para calcular los promedios
promedios = funcion_calcular_promedio(temperaturas, ciudades)

for ciudad, promedio in promedios.items():
    print (f"El prromedio de temperatura en {ciudad} es: {promedio:.2f}°C")

