# Tarea 3: Little DCCaesars 🧟🍕

## ALCANCE
1. El código logra definir de manera correcta las 20 funciones de consulta solicitadas, a excepción de la función de consulta anidada, la 
cual funciona parcialmente, ya que exite un error en el orden de los generadores a la hora de llamar a la funcion "total_ahorrado_pedidos"

## EJECUCION
En el módulo consultas.py se defininen todas las funciones de consulta, para que este módulo funcione de la manera esperada, debe estar 
en el mismo path que el modulo "funciones_extra.py", ademas, debe ser ejecutado con Python 3.11.X, con X >= 7.
Con esto claro, se debería crear otro módulo, donde en primera instancia se deberían cargar los datos usando las funciones de cargar datos,
y luego ejecutar las funciones de consulta según desee el usuario (cabe destacar que cada consulta pide distintos parámetros, dependiendo
de la consulta).

## LIBRERIAS EXTERNAS
Las librerias externas usadas para definir estas funciones son:
1. Typying : Any, Generator, Iterable (se usa principalemnte para seguir las reglas de PEP8)
2. itertools : cycle, islice, tee (principalemnte para un correcto manejo de los generadores)
3. collection : defaultdict  (usada para ir añadiendo valores al valor de una llave de un diccionario sin sobreescribir la llave-valor,
ademas para crear por defecto un par llave-valor si es que se llama una llave que no existe)

## LIBRERIAS PROPIAS
1. funciones_extra : calcular_ganancia, calcular_ahorro, calcular_ganancia_total_pedido (módulo creado con el fin de definir ciertas
funciones convenientes a la hora de usar filtros o mapeos, eliminando la necesidad de definir funciones lambda muy extensas)

## Supuestos y consideraciones adicionales
1. Se asume que a la hora de calcular int con round(), este ultimo se aplica luego de haber calculado y sumado los valores solicitados, 
por ejemplo si se quiere sacar las ganancias de un pedido, se calculan las ganancias de cada pizza, luego se suman, y finalmente se hace 
el round() (se asume gracias al issue #446) 
2. De la misma forma, se asume que la formula para calcular la ganancia de un pedido es (precio * cantidad * (1-descuento)). Tambien se asume
gracias al issue #446

# Actualizaciones Tarea

> 1 de octubre
1. Se hace un cambio en el enunciado, se agrega el formulario de entregas atrasadas.
2. Se hace un cambio en el enunciado, se explica que la forma de evaluar los tests es ternaria.

> 2 de octubre
1. Se hace un cambio en los tests públicos de la función pizzas_con_ingrediente. Cuando la función recibía el ingrediente "champiñones", 
la solución contenía pizzas que tenían "salsa de champiñones" siendo que eran dos ingredientes distintos. Ahora el test esta arreglado.
2. Se hace un cambio menor en el enunciado, en la función clientes_despues_hora se recibe la hora en formato "HH:MM" y no en formato "HH"

> 5 de octubre
1. Se agregó "timeout" en todos los tests: test_12_pizza_del_mes_carga_datos
2. Ajuste tests funciones ajustar_precio_segun_ingredientes y popularidad_mezcla_de_ingredientes. Se agregaron tests que verifican funcionamiento 
correcto cuando se tienen ingredientes que son substrings de otros ingredientes. Por ejemplo, al tener "tomate" como ingrediente, no considerar pizzas 
que tienen "salsa de tomate" y no "tomate". Este ajuste está relacionado con el ajuste número 1 del día 2 de octubre.

> 11 de octubre
1. Se arreglaron los datos de los tests de correctitud que recibían generadores de pedidos. Antes la información de la hora del pedido se encontraban 
en formato HH:MM, ahora se encuentran en formato HH:MM:SS tal como se encuentran estos datos en los archivos csv. Se arregló la desconcordancia entre 
tests de correctitud y tests de carga de datos (los tests de carga de datos sí respetaban el formato HH:MM:SS)