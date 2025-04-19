import collections
from utilidades import Anime  # Debes utilizar esta nametupled
from os.path import join

#####################################
#       Parte 1 - Cargar datos      #
#####################################

def cargar_animes(ruta_archivo: str)      -> list:
    lista_de_animes = []
    animes = open(ruta_archivo, "r").readlines()
    for anime in animes:
        anime = anime.strip().split(",")
        anime[5]=anime[5].split(";")
        print(anime)
        anime_en_tupla = Anime(str(anime[0]), int(anime[1]), int(anime[2]), int(anime[3]), str(anime[4]), tuple(anime[5]))
        lista_de_animes.append(anime_en_tupla)

    return lista_de_animes


#####################################
#        Parte 2 - Consultas        #
#####################################
def animes_por_estreno(animes: list) -> dict:
    seguir = True
    dict_de_estrenos = {
                
        }
    for i in range (len(animes)):
        lista_de_animes = []
        estreno = animes[i].estreno
        for anime in animes:
            if anime.estreno == estreno:
                lista_de_animes.append(anime.nombre)
                dict_de_estrenos[anime.estreno] = lista_de_animes
                
    return dict_de_estrenos    
                
                
def descartar_animes(generos_descartados: set, animes: list) -> list:
    animes_sin_descartar = []
    for anime in animes:
        seguir = True
        for genero in anime.generos:
            if genero in generos_descartados:
                seguir = False
        if seguir:
            animes_sin_descartar.append(anime.nombre)
            
    return animes_sin_descartar


def resumen_animes_por_ver(*animes: Anime) -> dict:
    dict_resumen_animes = {
        
    }
    generos = set()
    capitulos_total = 0
    puntaje_promedio = float(0)
    if len(animes) != 0:
        for anime in animes:
            capitulos_total += anime.capitulos
            puntaje_promedio += anime.puntaje
            
            for genero in anime.generos:
                generos.add(genero)
        puntaje_promedio = round(puntaje_promedio/len(animes), 1)  
    dict_resumen_animes["capitulos total"] = capitulos_total
    dict_resumen_animes["generos"] = generos  
    dict_resumen_animes["puntaje promedio"] = puntaje_promedio     
    
    return dict_resumen_animes


def estudios_con_genero(genero: str, **estudios: list) -> list:
    animes_del_genero = []
    for estudio, animes in estudios.items():
        if any(genero in anime.generos for anime in animes):
            animes_del_genero.append(estudio)
            
    return animes_del_genero




if __name__ == "__main__":
    #####################################
    #       Parte 1 - Cargar datos      #
    #####################################
    animes = cargar_animes(join("data", "ejemplo.chan"))
    indice = 0
    for anime in animes:
        print(f"{indice} - {anime}")
        indice += 1

    #####################################
    #        Parte 2 - Consultas        #
    #####################################
    # Solo se usará los 2 animes del enunciado.
    datos = [
        Anime(
            nombre="Hunter x Hunter",
            capitulos=62,
            puntaje=9,
            estreno=1999,
            estudio="Nippon Animation",
            generos={"Aventura","Comedia", "Shonen", "Acción"},
        ),
        Anime(
            nombre="Sakura Card Captor",
            capitulos=70,
            puntaje=10,
            estreno=1998,
            estudio="Madhouse",
            generos={"Shoujo", "Comedia", "Romance", "Acción"},
        ),
    ]

    # animes_por_estreno
    estrenos = animes_por_estreno(datos)
    print(estrenos)

    # descartar_animes
    animes = descartar_animes({"Comedia", "Horror"}, datos)
    print(animes)

    # resumen_animes_por_ver
    resumen = resumen_animes_por_ver(datos[0], datos[1])
    print(resumen)

    # estudios_con_genero
    estudios = estudios_con_genero(
        "Shonen",
        Nippon_Animation=[datos[0]],
        Madhouse=[datos[1]],
    )
    print(estudios)
