def mensaje_programa(numero:int):
# muestra un mensaje dependiendo la opcion que recibe por parametros
    mensaje=""
    if numero == 1:    
        mensaje = f"\n{"*"*26}  Menu  {"*"*26}\n\nA)Normalizar Objetos.\nB)Mostrar Temas.\nC)Ordenar Temas por sesion mayor.\nD)Promedio de vistas\nE)Mostar video con mas reproduccion.\nf)Mostrar los videos cuyo código comiencen con la palabra nick.\nG)Buscar colaborador por nombre.\nH)Mostrar los temas por mes.\nX)Salir.\n\n{"*"*60} \n"
    elif numero == 2:
        mensaje = "Debe ingresar los datos solicitado en la opcion `A` "    
    elif numero == 3:
        mensaje=f"\nCerrando programa.....\n"
    elif numero == 4:
        mensaje = "\n***** Objectos Normalizados con exito *****\n" 
    elif numero == 5:
        mensaje = "\n***** Uuups los objectos ya fueron normalizados   *****\n" 
    elif numero == 6:
        mensaje=f"\nNo hay coincidencia.....\n"      
    else:
        mensaje = "\n**** Algo salio mal, ingrese los datos correctamente ****\n**** Verifique que los objectos se hallan normalizado correctamente ****\n"        

    print(mensaje)    
