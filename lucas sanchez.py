from os import system
import random
system("cls")
dispensadores=("6", "10", "20")
dispensadores_lista=[]
registro=[]
dispensador6=0
dispensador10=0
dispensador20=0
disponibilidad_comunal=("concepcion", "talcahuano", "chiguayante", "hualpen", "san pedro")
def registro_pedido():
    while True:
     codigo_aleatorio=random.randint(1,9999)
     nombre=str(input("ingrese su nombre para registrar el pedido: "))
     if nombre.isalpha and len(nombre) > 3:
        ("cls")
        break
     else:
        print("vuelva a ingresar el nombre ")
    while True:
       apellido=str(input("ingrese su apellido: ")) 
       if apellido.isalpha and len(apellido) > 3:
          ("cls")
          break
       else:
          print("ingrese nuevamente el apellido")
    while True:
       comuna_cliente=str(input("ingrese la comuna en la cual se ubica: "))
       if comuna_cliente.isalpha and len(comuna_cliente) >3:
          ("cls") 
          break
       else: 
          print("ingrese nuevamente su direccion porque fue invalida")
    while True:
       print(dispensadores)       
       detalle_pedido=str(input("ingrese de cuantos litros necesita su dispensador: "))
       if detalle_pedido=="6":
          detalle_pedido=dispensador6=+1
          ("cls")
          break
       elif detalle_pedido=="10":
          detalle_pedido=dispensador10=+1
          ("cls")
          break
       elif detalle_pedido=="20":
          detalle_pedido=dispensador20=+1
          ("cls")
          break
       else:
          print("numero invalido")
    while True:
       cantidad=str(input("ingrese la cantidad que necesita: "))
       if cantidad.isnumeric:
           print("su codigo es:", codigo_aleatorio)
           ("cls")
           break
       else:
          print("ingrese nuevamente la cantidad")
          print("su codigo es:", codigo_aleatorio)

       registro=[codigo_aleatorio, nombre, apellido, comuna_cliente, detalle_pedido, cantidad]
       dispensadores_lista.append(registro)
       








def lista_pedidos():
    while True:
        print("la lista es la siguiente")
        for registro in dispensadores_lista:
            print(f'''
            ID:          nombre del cliente:    comuna del cliente:       cantidad del pedido:      disp6:        disp10:          disp20:
        {registro[0]}   {registro[1]}      {registro[3]}         {registro[4]}              {dispensador6}     {dispensador10}   {dispensador20}
                  {registro[2]}  
                                                                                                              ''')
            return















def imprimir_disponibilidad():
   while True:
    print(disponibilidad_comunal)
    op=str(input("ingrese alguno de los sectores mostrados anteriormente para su hoja de ruta: "))
    if op=="concepcion":
       print("concepcion esta dentro del radar")
       (open)=["archivo","w"]
       ("cls")
       break
    elif op=="talcahuano":
       print("talcahuano esta dentro del radar")
       ("cls")
       break
    elif op=="san pedro":
       print("san pedro esta dentro del radar")
       ("cls")
       break
    elif op=="chiguyante":
       print("chiguyante esta dentro del radar")
       ("cls")
       break
    elif op=="hualpen":
       print("hualpen est dentro del radar")
       ("cls")
       break
    else:
       print("no esta dentro del radar")
       








def busqueda_id():
   busqueda=str(input("ingrese el ID que desea buscar"))
   if busqueda.isnumeric:
      for busqueda in lista_pedidos():
         print(f'''
                        ID:          nombre del cliente:    comuna del cliente:       cantidad del pedido:      disp6:        disp10:          disp20:
    {busqueda[0]}   {registro[1]}      {registro[3]}         {registro[4]}              {dispensador6}     {dispensador10}   {dispensador20}
                  {registro[2]}  
               
               
               
               ''')
         





















while True:
   print('''
         1.Registrar pedido
         2.Lista de todos los pedidos
         3.Imprimir hoja de ruta
         4.Buscar pedido por ID
         5.Salir del programa

         
         
         
         
         ''')
   op_menu=str(input(":"))
   match op_menu:
      case "1":
         registro_pedido()
      case "2":
         lista_pedidos()
      case "3":
         imprimir_disponibilidad()
         
