# Tarea 2: DCCampesino 🌻🧟

# ITEMS DEL CODIGO
1. Definición de clases, herencia y *properties* ✅ ✅
    Todas las clases están bien definidas, se usan las properties de manera adecuada y efectiva, y las sub clases hereda de manera correcta
    de sus clases padres
2. Inicio de la partida ✅✅
    El programa recibe de manera correcta los inputs recibidos en consola, y esta preparado para recibir inputs incorrectos y dar aviso
    del error en el input
3. Entidades ✅✅
    Ambas entities están definidas de manera correcta, y funcionan según lo estipulado en el enunciado
4. Flujo del programa✅✅
    El flujo de programa sucede de manera correcta, los menus funcionan segun lo estipulado en el enunciado, y es a prueba de errores, está
    preparado para recibir inputs erroneos y manejarlos de manera correcta para que el programa no se detenga
5. Simular día ✅✅
    La simulación del día ocurre segun lo esperado, la temperatura del jardin cambia de manera aleatoria dentro de los parametros recibidos, los 
    eventos suceden en el orden que se indica, y las probabilidades se calculan en base a lo leido por el archivo eventos.txt, los soles se calculan
    en base a los parametros leidos en parametros.py, la llegada de plantas sucede de manera aleatoria dentro de los parametros recibidos en el mismo
    archivo, y la presentacion del jardin se ve como se indica en el enunciado.
6. Archivos ✅✅
    Los 5 archivos funcionan y son leídos/importados de manera correcta, y el código está programado en base a los mismos, por ende son completamente
    modificables.

## Ejecución
El módulo principal a ejecutare es main.py, con una version de Python 3.11.X (con X >= 7) y debe ejecutarse junto a los parámetros en consola,
de la forma "py main.py [nombre_jardin][dificultad] donde nombre_jardin debe estar en jardines.txt y dificultad debe ser facil, normal, dificil.
Por ende, se deben crear los siguientes archivos:
1. jardines.txt
2. eventos.txt
3. plantas.txt
Todos deben estar en la carpeta data/ dentro del mismo directorio que main.py.

## Librerías externas
Las librerias externas usadas en el codigo son:
1. random : uniform, randint
2. abc : ABC, abstractmethod
3. sys : exit, argv

### Librerías propias
Se usa una sola libreria propia
1. funciones : coordenadas_alrededor, calcular_probabilidad : Hecha para reciclar/acortar codigo del archivo principal.

## Supuestos y consideraciones adicionales
1. Se asume que el nombre de las clases definidas en entidades.py no cambiarán, ya que no se estipula lo contrario.
2. Se asume que la informacion dentro de cada archivo seguirá la estructura que se indica y que esta no cambiará.


# Actualizaciones Tarea

> 30 de agosto
1. Se hace un cambio menor en el enunciado, en la sección __4.1 Jardín__, en Inventario Plantas se reemplaza la palabra __compradas__ por __que llegan__ y en la sección __5.4 Llegada de plantas__ se agrega que las plantas son __guardadas en el inventario__.
> 2 de septiembre
1. Se hace un cambio menor en el archivo __plantas.txt__ para que hayan 6 líneas erróneas. 
2. Se hace un cambio menor en el enunciado, se cambia ejemplo de archivo plantas.txt para que hayan 6 líneas erróneas. Además, se agregó explicación entrega atrasada.
> 6 de septiembre
1. Se hace un cambio menor en el enunciado, en la __Figura 11__ y __Figura 15__ la cantidad de solaretillos pasa de ser 3 a 4 para que estén de acorde con el tablero. 
> 9 de septiembre
1. Se hace un cambio menor en el enunciado, en la nota de pie 3 se agrega el nombre del jardín en el ejemplo.
