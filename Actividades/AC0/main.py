from entities import Item, Usuario
from utils.pretty_print import print_canasta, print_items,print_usuario

def cargar_items() -> list:
    lista_instanciada = [] 
    items = open("utils/items.dcc" , "r").readlines()
    
    for i in range (len(items)):
        items[i]=items[i].strip().split(",")
        
    for item in items:
        item_instanciado = Item(str(item[0]), int(item[1]), int(item[2]))
        lista_instanciada.append(item_instanciado)
    return(lista_instanciada)

def crear_usuario(tiene_suscripcion:bool) -> Usuario: #clase
    usuario = Usuario(tiene_suscripcion)
    print_usuario(usuario)
    return(usuario)

if __name__ == "__main__":
    usuario = crear_usuario(True)# 1) Crear usuario (puede ser con o sin suscripcion)
    lista_items = cargar_items()# 2) Cargar los items
    print_items(lista_items) # 3) Imprimir todos los items usando los módulos de pretty_print
    for item in lista_items:  # 4) Agregar todos los items a la canasta del usuario
        Usuario.agregar_item(usuario, item)
    print_canasta(usuario) # 5) Imprimir la canasta del usuario usando los módulos de pretty_print
    usuario.comprar() # 6) Generar la compra desde el usuario 
    print_usuario(usuario) # 7) Imprimir el usuario usando los módulos de pretty_print

    


    






