from functools import reduce
from itertools import product
from typing import Generator

from utilidades import Pelicula, Genero


# ----------------------------------------------------------------------------
# Parte 1: Cargar dataset
# ----------------------------------------------------------------------------

def cargar_generos(ruta: str) -> Generator:
    with open(ruta, "r") as generos:
        for genero in generos:
            genero = genero.strip().split(",")
            if genero[0] != "genero":
                genero_pelicula = genero[0]
                id_pelicula = int(genero[1])
                yield Genero (genero_pelicula, id_pelicula)

def cargar_peliculas(ruta: str) -> Generator:
    with open(ruta, "r") as peliculas:
        for pelicula in peliculas:
            pelicula = pelicula.strip().split(",")
            if pelicula[0] != "id":
                id_pelicula = int(pelicula[0])
                titulo = pelicula[1]
                director = pelicula[2]
                estreno = int(pelicula[3])
                rating = float(pelicula[4])
                yield Pelicula(id_pelicula, titulo, director, estreno, rating)

# ----------------------------------------------------------------------------
# Parte 2: Consultas sobre generadores
# ----------------------------------------------------------------------------


def obtener_directores(generador_peliculas: Generator) -> Generator:
    return map(lambda pelicula: pelicula.director, generador_peliculas)


def obtener_estrenos(generador_peliculas: Generator, estreno: int) -> Generator:
    filtro = filter(lambda pelicula: pelicula.estreno >= estreno, generador_peliculas)
    return map(lambda pelicula: pelicula.titulo, filtro)
   
    
    
def obtener_str_titulos(generador_peliculas: Generator) -> str:
    mapeo = map(lambda pelicula: pelicula.titulo, generador_peliculas)
    return ", ".join(mapeo)

def filtrar_peliculas(
    generador_peliculas: Generator,
    director: str | None = None,
    rating_min: float | None = None,
    rating_max: float | None = None,
) -> filter:
    if director != None and rating_min == None and rating_max == None:
        return filter(lambda pelicula: pelicula.director == director, generador_peliculas)
    elif rating_max != None and director == None and rating_min == None:
        return filter(lambda pelicula: pelicula.rating <= rating_max, generador_peliculas)
    elif rating_min != None and director == None and rating_max == None:
        return filter(lambda pelicula: pelicula.rating >= rating_min, generador_peliculas)
    elif director != None and rating_max != None and rating_min == None:
        filtro_director = filter(lambda pelicula: pelicula.director == director, generador_peliculas)
        return filter(lambda pelicula: pelicula.rating <= rating_max, filtro_director)
    elif director != None and rating_min != None and rating_max == None:
        filtro_director = filter(lambda pelicula: pelicula.director == director, generador_peliculas)
        return filter(lambda pelicula: pelicula.rating >= rating_min, filtro_director)
    elif rating_min != None and rating_max != None and director == None:
        filtro_max = filter(lambda pelicula: pelicula.rating <= rating_max, generador_peliculas)
        return filter(lambda pelicula: pelicula.rating >= rating_min, filtro_max)
    else:
        filtro_director = filter(lambda pelicula: pelicula.director == director, generador_peliculas)
        filtro_max = filter(lambda pelicula: pelicula.rating <= rating_max, filtro_director)
        return filter(lambda pelicula: pelicula.rating >= rating_min, filtro_max)

def filtrar_peliculas_por_genero(
    generador_peliculas: Generator,
    generador_generos: Generator,
    genero: str | None = None,
) -> Generator:
    
    combinaciones = product(generador_peliculas, generador_generos)
    pares_con_mismo_id = filter(lambda par: par[0].id_pelicula == par[1].id_pelicula, combinaciones)
    if genero:
        return filter(lambda par: par[1].genero == genero, pares_con_mismo_id)
    
    return pares_con_mismo_id


def filtrar_titulos(
    generador_peliculas: Generator, director: str, rating_min: float, rating_max: float
) -> str:
    peliculas_con_director = filter(lambda pelicula: pelicula.director == director, generador_peliculas)

    if rating_max is not None and rating_min is None:
        peliculas_filtradas = filter(lambda pelicula: pelicula.rating <= rating_max, peliculas_con_director)
        
    elif rating_min is not None and rating_max is None:
        peliculas_filtradas =  filter(lambda pelicula: pelicula.rating >= rating_min, peliculas_con_director)

    elif rating_max is not None and rating_min is not None:
        peliculas_filtradas = filter(lambda pelicula: rating_min <= pelicula.rating <= rating_max  , peliculas_con_director)
        
    else:
        peliculas_filtradas = peliculas_con_director
        
    titulos = map(lambda pelicula: pelicula.titulo, peliculas_filtradas)
    
    return ", ".join(titulos) 
        
