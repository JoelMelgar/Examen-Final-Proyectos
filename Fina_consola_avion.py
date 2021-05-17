import psycopg2

roles = """
--------CONTROL DE BOLETOS--------
1.Administrador
2.Operador
3.Salir
"""

menu = """
--------BIENVENIDO A LA TAQUILLA DE VENTAS--------
Datos requeridos para la venta
1.Cantidad y Clase de boletos
2.Servicios Especiales
3.Calcular Factura
4.Salir
"""

precios= """
------------------------- PRECIOS -------------------------
        COMIDAS             BEBIDAS            PELICULAS
1ra clase = 50.00   1ra clase = 35.00   1ra clase = 70.00
2da clase = 40.00   2da clase = 25.00   2da clase = 55.00
3ra clase = 25.00   3ra clase = 10.00   3ra clase = 25.00
"""


pop = True
while pop == True:
    print(roles)
    try:
        opp = int(input("Ingrese el rol que desempeña o la opcion de Salir: "))
        if opp == 1:
            print("------------ACCESO DE ADMINISTRADOR--------------")
            print("Ingrese un usuario para registrarlo\n")
            userName = input("Ingrese un nombre de usuario: ")
            passsword = input("Ingrese una contraseña: ")
            Nombre = input("Ingrese su nombre: ")
        elif opp == 2:
            try: 
                usuario = input("Ingrese su nombre de usuario:\n")
                contraseña = input("Ingrese su contraseña:\n")
                if usuario == userName and contraseña == passsword:
                    print("ACCESO CONCEDIDO, BIENVENIDO ", Nombre)

                    opci = True
                    while opci == True:
                        print(menu)
                        try:
                            op = int(input("Ingrese los datos del cliente: "))
                            if op == 1:
                                try:
                                    try:
                                        clase = input("En que clase desa volar? primera/segunda/tercera \n")
                                        cant_boletos = int(input("Cuantos voletos desa comprar?: \n"))
                                        print("Agregados " + str(cant_boletos) +" boletos para volar en " + clase + " clase.")    
                                    except AssertionError as f:
                                        print("Ingreso un numero negativo")
                                except ValueError as e:
                                    print("Ingreso un caracter no permitido")
                            elif op == 2:
                                print(precios)
                                cant_servicios = 0
                                serv_comida = input("Desea contratar servicio de comida? si/no: \n")
                                if serv_comida == 'si' :
                                    cant_servicios = cant_servicios + 1

                                serv_bebida = input("Desea contratar servicio de bebida? si/no: \n")
                                if serv_bebida == 'si' :
                                    cant_servicios = cant_servicios + 1

                                serv_pelicula = input("Desea contratar servicio de pelicula? si/no: \n")
                                if serv_pelicula == 'si' :
                                    cant_servicios = cant_servicios + 1

                                print("Usted ha solicitado: " + str(cant_servicios) + " de nuestros servicios por boleto.")
                            elif op == 3:
                                comida1 = 50
                                comida2 = 40
                                comida3 = 25
                                
                                bebida1 = 35
                                bebida2 = 25
                                bebida3 = 10

                                pelicula1 = 70
                                pelicula2 = 55
                                pelicula3 = 25

                                subtotal1 = 0
                                subtotal2 = 0
                                subtotal3 = 0

                                descuento1=0
                                desc_total=0
                                descuento2=0
                                desc_tota2=0
                                descuento3=0
                                desc_tota3=0

                                subtotaldef = 0
                                totaldef = 0
                                descuentodef= 0

                                tot_servicios=0

                                tot_servicios=cant_servicios*cant_boletos

                                print("\nHa solicitado: " + str(cant_boletos) + " boletos, Para volar en: " + clase + " clase.")
                                print("Ha solicitado la cantidad total de: " + str(tot_servicios) + " servicios especiales siendo estos los siguientes:")
                                
                                if serv_comida == 'si' :
                                    print("- Comida")

                                if serv_bebida == 'si' :
                                    print("- Bebida")

                                if serv_pelicula == 'si' :
                                    print("- Pelicula")
                                

                                if clase == 'primera':
                                    if serv_comida == 'si':
                                        subtotal1 = subtotal1 + comida1 
                                    if serv_bebida == 'si':
                                        subtotal1 = subtotal1 + bebida1
                                    if serv_pelicula == 'si':
                                        subtotal1 = subtotal1 + pelicula1    
                                    subtotal11 = subtotal1 * cant_boletos
                                    print("El subtotal es: Q" +str(subtotal11))

                                    if serv_comida == 'si' and serv_bebida == 'si' and serv_pelicula == 'si':
                                        descuento1 = subtotal11*0.05
                                        desc_total = subtotal11 - descuento1
                                        print("Se le aplico un descuento de: Q" + str(descuento1))
                                        print("Su total es de: Q" + str(desc_total))
                                        descuentodef=descuento1
                                        totaldef=desc_total
                                        subtotaldef=subtotal11

                                    else:    
                                        print("Su total es de: Q" +str(subtotal11))
                                        descuentodef=descuento1
                                        totaldef=desc_total
                                        subtotaldef=subtotal11
                                    
                                    
                                

                                if clase == 'segunda':
                                    if serv_comida == 'si':
                                        subtotal2 = subtotal2 + comida2 
                                    if serv_bebida == 'si':
                                        subtotal2 = subtotal2 + bebida2
                                    if serv_pelicula == 'si':
                                        subtotal2 = subtotal2 + pelicula2    
                                    subtotal22 = subtotal2 * cant_boletos
                                    print("El subtotal es: Q" +str(subtotal22))

                                    if tot_servicios > 10:
                                        descuento2 = subtotal22*0.10
                                        desc_tota2 = subtotal22 - descuento2
                                        print("Se le aplico un descuento de: Q" + str(descuento2))
                                        print("Su total es de: Q" + str(desc_tota2))
                                        descuentodef=descuento2
                                        totaldef=desc_tota2
                                        subtotaldef=subtotal22

                                    else:    
                                        print("No contrato mas de 10 servicios\n")
                                        print("Su total es de: Q" +str(subtotal22))
                                        descuentodef=descuento2
                                        totaldef=subtotal22
                                        subtotaldef=subtotal22


                                if clase == 'tercera':
                                    if serv_comida == 'si':
                                        subtotal3 = subtotal3 + comida3 
                                    if serv_bebida == 'si':
                                        subtotal3 = subtotal3 + bebida3
                                    if serv_pelicula == 'si':
                                        subtotal3 = subtotal3 + pelicula3
                                    subtotal33 = subtotal3 * cant_boletos
                                    print("El subtotal es: Q" +str(subtotal33))

                                    if tot_servicios > 10:
                                        descuento3 = subtotal33*0.10
                                        desc_tota3 = subtotal33 - descuento3
                                        print("Se le aplico un descuento de: Q" + str(descuento3))
                                        print("Su total es de: Q" + str(desc_tota3))
                                        descuentodef=descuento3
                                        totaldef=desc_tota3
                                        subtotaldef=subtotal33

                                    else:
                                        print("No contrato mas de 10 servicios\n")    
                                        print("Su total es de: Q" +str(subtotal33))
                                        descuentodef=descuento3
                                        totaldef=subtotal33
                                        subtotaldef=subtotal33
                                
                                conexion1 = psycopg2.connect(host = "localhost", database = 'avion', user = 'postgres', password = "casacasa", port = '5432')
                                cursor = conexion1.cursor()
                                sql = "insert into ventas(subtotal, descuento, total, usuario) values (%s, %s, %s, %s)"
                                datos = (subtotaldef, descuentodef, totaldef, userName)
                                cursor.execute(sql, datos)
                                conexion1.commit()
                                print("Datos almacenados correctamente")
                                conexion1.close()

                            elif op == 4:
                                pop = False
                                opci = False
                                print("Gracias por volar con nosotros, Buen viaje")
                            else:
                                print("Opcion no valida")
                        except ValueError as l:
                            print("Ingreso un caracter no permitido")
             
                else:
                    if userName != usuario and passsword != contraseña:
                        print("Usuario y contraseña invalida")
                    elif userName != usuario:
                        print("Usuario invalido")
                    elif passsword != contraseña:
                        print("Contraseña invalida")
            except:
                print("No existe un usuario registrado")
        elif opp == 3:
            
            print("Gracias por utilizar la aplicacion")
        else:
            print("Opcion no valida")
    except ValueError as l:
        print("Ingreso un caracter no permitido")


