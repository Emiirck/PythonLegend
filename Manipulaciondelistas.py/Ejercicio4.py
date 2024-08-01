
def modificar_cadena(texto):
    textom = texto.lower()
    
   
    letra_a_reemplazar = 'a'  
    letra_reemplazo = 'o'     
    texto_reemplazado = textom.replace(letra_a_reemplazar, letra_reemplazo)
    
   
    lista_palabras = texto_reemplazado.split()
    
   
    print("Cadena modificada:", texto_reemplazado)
    print("Lista de palabras:", lista_palabras)


modificar_cadena("Java es complicado")
