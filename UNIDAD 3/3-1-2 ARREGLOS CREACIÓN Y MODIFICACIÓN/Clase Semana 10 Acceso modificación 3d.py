cubo = [
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ]
]

print (cubo)
cubo [1][0][0] = 777
#Imprimir el cubo de manera estructurada
for matriz in cubo:
    for fila in matriz:
        print (fila)