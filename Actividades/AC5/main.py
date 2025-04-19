from typing import List
from clases import Tortuga
import pickle


###################
#### ENCRIPTAR ####
###################
def serializar_tortuga(tortuga: Tortuga) -> bytearray:
    try:
        tortuga_serializada = pickle.dumps(tortuga)
        return bytearray(tortuga_serializada)
    except AttributeError:
        raise ValueError

def verificar_rango(mensaje: bytearray, inicio: int, fin: int) -> None:
    if not (0 <= inicio < len(mensaje)):
        raise AttributeError(f"El valor de inicio ({inicio}) está fuera del rango del mensaje.")
    if not (0 <= fin < len(mensaje)):
        raise AttributeError(f"El valor de fin ({fin}) está fuera del rango del mensaje.")
    if fin < inicio:
        raise AttributeError(f"El valor de fin ({fin}) debe ser mayor o igual que el valor de inicio ({inicio}).")
    return None


def codificar_rango(inicio: int, fin: int) -> bytearray:
    inicio_bytes = inicio.to_bytes(3, byteorder='big')
    fin_bytes = fin.to_bytes(3, byteorder='big')
    return bytearray(inicio_bytes + fin_bytes)


def codificar_largo(largo: int) -> bytearray:
    return bytearray(largo.to_bytes(3, byteorder='big'))



def separar_msg(mensaje: bytearray, inicio: int, fin: int) -> List[bytearray]:
    m_extraido = bytearray()
    m_con_mascara = bytearray(mensaje)
    # Completar
    m_extraido = mensaje[inicio:fin+1]
    if len(m_extraido) % 2 != 0:
        m_extraido = m_extraido[::-1]
    for i, idx in enumerate(range(inicio, fin + 1)):
        m_con_mascara[idx] = i
    return [m_extraido, m_con_mascara]


def encriptar(mensaje: bytearray, inicio: int, fin: int) -> bytearray:
    # No modificar
    verificar_rango(mensaje, inicio, fin)

    m_extraido, m_con_mascara = separar_msg(mensaje, inicio, fin)
    rango_codificado = codificar_rango(inicio, fin)
    return (
        codificar_largo(fin - inicio + 1)
        + m_extraido
        + m_con_mascara
        + rango_codificado
    )


######################
#### DESENCRIPTAR ####
######################
def deserializar_tortuga(mensaje_codificado: bytearray) -> Tortuga:
    try:
        tortuga = pickle.loads(mensaje_codificado)
        return tortuga
    except ValueError:
        raise AttributeError


def decodificar_largo(mensaje: bytearray) -> int:
    largo_bytes = mensaje[:3]
    largo = int.from_bytes(largo_bytes, byteorder='big')
    return largo



def separar_msg_encriptado(mensaje: bytearray) -> List[bytearray]:
    largo = decodificar_largo(mensaje)
    m_extraido = mensaje[3:3 + largo]  
    m_con_mascara = mensaje[3 + largo:-6]  
    rango_codificado = mensaje[-6:]  
    if len(m_extraido) % 2 != 0:
        m_extraido.reverse()
    return [m_extraido, m_con_mascara, rango_codificado]


def decodificar_rango(rango_codificado: bytearray) -> List[int]:
    inicio = int.from_bytes(rango_codificado[0:3], byteorder='big') 
    fin = int.from_bytes(rango_codificado[3:6], byteorder='big')     
    return [inicio, fin]


def desencriptar(mensaje: bytearray) -> bytearray:
    m_extraido, m_con_mascara, rango_codificado = separar_msg_encriptado(mensaje)
    inicio, fin = decodificar_rango(rango_codificado)
    for i in range(inicio, fin + 1):
        m_con_mascara[i] = m_extraido[i - inicio] 
    return m_con_mascara


if __name__ == "__main__":
    # Tortuga
    tama = Tortuga("Tama2")
    print("Nombre: ", tama.nombre)
    print("Edad: ", tama.edad)
    print(tama.celebrar_anivesario())
    print()

    # Encriptar
    original = serializar_tortuga(tama)
    print("Original: ", original)
    encriptado = encriptar(original, 6, 24)
    print("Encriptado: ", encriptado)
    print()

    # Desencriptar
    mensaje =  bytearray(b'\x00\x00\x13roT\x07\x8c\x94sesalc\x06\x8c\x00\x00\x00\x00\x00\x80\x04\x958\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12tuga\x94\x93\x94)\x81\x94}\x94(\x8c\x06nombre\x94\x8c\x05Tama2\x94\x8c\x04edad\x94K\x01ub.\x00\x00\x06\x00\x00\x18')
    desencriptado = desencriptar(mensaje)
    tama = deserializar_tortuga(desencriptado)

    # Tortuga
    print("Tortuga: ", tama)
    print("Nombre: ", tama.nombre)
    print("Edad: ", tama.edad)
