# Creación de una función que calcule el descuento en compras en función del monto total de la compra y mostrar el monto final a pagar
# Definir la función
def calcular_descuento (monto_total,porcentaje_descuento1=10):
    descuento = monto_total * (porcentaje_descuento1/100) #Calcular el descuento
    return descuento #Devolver el monto del descuento

if __name__=="__main__":
    # Ingresar los montos
    monto1 = 3000
    monto2 = 5000

    # Llamada a la función1
    descuento1 = calcular_descuento (monto1)
    monto_final1 = monto1 - descuento1
    print (f" El monto de la compra es ${monto1}, el descuento es (10%): ${descuento1}, el monto final a pagar es: ${monto_final1}")
    
    # Llamada a la función 2
    porcentaje_descuento2 = 20
    descuento2 = calcular_descuento (monto2,porcentaje_descuento2)
    monto_final2 = monto2 - descuento2
    print (f" El monto de la compra es ${monto2}, el descuento es (20%): ${descuento2}, el monto final a pagar es: ${monto_final2}")

