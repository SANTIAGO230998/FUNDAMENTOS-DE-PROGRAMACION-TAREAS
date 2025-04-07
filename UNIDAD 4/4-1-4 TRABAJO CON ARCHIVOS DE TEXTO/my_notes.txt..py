"""Tarea: Trabajo con Archivos de Texto en Python

En esta tarea, realizarás operaciones de lectura y escritura en archivos de texto en Python. Sigue las instrucciones detalladas a continuación:

Escritura de Archivo de Texto:

Crea un nuevo archivo llamado my_notes.txt.
Escribe al menos tres líneas de notas personales en el archivo.
Lectura de Archivo de Texto:

Abre el archivo my_notes.txt.
Lee el contenido del archivo línea por línea utilizando el método adecuado.
Muestra en la consola cada línea leída.
Cierre de Archivos:

Asegúrate de cerrar el archivo my_notes.txt después de realizar las operaciones necesarias.
Instrucciones Adicionales:

Utiliza métodos como write() y readline() para manipular el archivo de texto.
Agrega comentarios explicativos en tu código.
Guarda tu código en un repositorio de GitHub que ya hayas creado anteriormente para esta asignatura.
Sube el link donde se encuentra el código fuente de esta tarea en tu repositorio GitHub

# Ejemplo de Escritura y Lectura de Archivos en Python usando write() y readline()
# Nombre del archivo
file_name = "travel_itinerary.txt" """

# Ejemplo de Escritura y Lectura de Archivos en Python usando write() y readline()
# Nombre del archivo
file_name = "travel_itinerary.txt"

# Escritura en el archivo de texto (modo 'w' para escritura)
with open(file_name, 'w') as file:  # Usamos 'with' para manejo seguro del archivo
    # Escribimos cada actividad del itinerario en una línea
    file.write("1. Llegada al aeropuerto a las 8:00 AM.\n")
    file.write("2. Registro en el hotel a las 10:00 AM.\n")
    file.write("3. Desayuno en café local a las 10:30 AM.\n")
    file.write("4. Tour por el centro histórico a las 12:00 PM.\n")
    file.write("5. Almuerzo en restaurante típico a las 2:00 PM.\n")
    file.write("6. Visita al museo de arte moderno a las 4:00 PM.\n")
    file.write("7. Tiempo libre para compras a las 6:00 PM.\n")
    file.write("8. Cena con vista al mar a las 8:00 PM.\n")
    file.write("9. Caminata nocturna por el malecón a las 9:30 PM.\n")
    file.write("10. Regreso al hotel y descanso a las 11:00 PM.\n")
    # No necesitamos file.close() porque 'with' lo maneja automáticamente

# Lectura del archivo
print("\nItinerario de Viaje:")
with open(file_name, 'r') as file:
    linea = file.readline()  # Lee la primera línea
    while linea:  # Mientras haya líneas para leer
        print(linea.strip())  # Imprime la línea sin espacios/saltos adicionales
        linea = file.readline()  # Lee la siguiente línea
