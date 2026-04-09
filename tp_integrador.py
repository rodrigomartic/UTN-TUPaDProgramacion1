# #EJERCICIO 1---"CAJA DEL KIOSCO"
name=input("Ingrese el nombre del Cliente:") # Pedimos al cajero el nombre del cliente.

#Validamos que el nombre tenga solo letras y no sea una cadena vacia.
while not name.isalpha() or name=="": 
   print("Error: El nombre solo debe contener Letras y no debe estar vacio.")
   name= input("Por favor, Intente devuelta:")
print("--- Bienvenid@ a Kiosco.DEV ---")
print(f"Cliente: {name.capitalize()}!") # Mostramos el nombre con la inicial en mayuscula.

#Pedimos la cantidad de productos y nos aseguramos de que sea un numero valido mayor a cero
cantidad_productos= input("Ingrese la cantidad a Comprar:")
while not cantidad_productos.isdigit() or cantidad_productos== "0":
   print("Debe ingresar un número mayor a 0")
   cantidad_productos= input("Por favor, Ingrese la cantidad a Comprar:")
cantidad_productos = int(cantidad_productos) # Convertimos a entero para poder usarlo en el ciclo for.

#Creamos las variables para acumular los montos y el texto del resumen de productos.
detalle_productos = ""
total_sin_d=0
total_con_d=0

#Iteramos segun la cantidad definida para solicitar datos de cada producto.
for i in range(cantidad_productos):
   #Solicitamos y validamos que el precio sea un numero entero.
   precio = input(f"Producto {i+1} - Precio: ") 
   while not precio.isdigit():
      print("Error! Por favor ingrese un numero positivo.")
      precio=(input("Ingrese el Precio:"))
   
   precio= int(precio)
   total_sin_d += precio # Sumamos al total bruto (sin descuentos)

#Validamos la respuesta del descuento (solo S o N) y usamos . lower() por si el cajero
#Ingresa "s" o "S", "n" o "N".

   tiene_desc = input("¿Tiene descuento? (S/N): ").lower()
   while tiene_desc != "s" and tiene_desc != "n":
         print("Error: Ingrese solo 'S' o 'N'.")
         tiene_desc = input("¿Tiene descuento? (S/N): ").lower() 
   
   #Creamos el renglon de texto para el resumen final
   detalle_productos += f"Producto {i+1} - Precio: ${precio:.2f} | Descuento: {tiene_desc.upper()}\n"
   
   #Aplicamos la logica de descuento si corresponde (10% de descuento)
   if tiene_desc== "s":
      total_con_d += precio-(precio * 0.10)

   else:
      total_con_d=total_con_d+precio # Si no hay descuento, sumamos el precio original.

ahorro= total_sin_d - total_con_d
promedio= total_con_d / cantidad_productos

print(f"\nCliente:{name.capitalize()}")
print(f"Cantidad de Productos:{cantidad_productos}")
print("\n--- RESUMEN DE PRODUCTOS ---")
print(detalle_productos)
print(f"Total sin descuentos: ${total_sin_d:.2f}")
print(f"Total con descuentos: ${total_con_d:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por productos: ${promedio:.2f}")


# # EJERCICIO2---“Acceso al Campus y Menú Seguro”

user="alumno"
password="python123"
intentos= 0
acceso= False

while intentos <3 and acceso==False:  
   usuario= input("Ingrese su nombre de Usuario:")
   contraseña= input("Ingrese su Contraseña:")

   if usuario==user and contraseña==password:
      print("---Bienvenid@ al Campus Virtual de la UTN San Nicolas---")
      acceso=True
      if acceso:
         opcion =""
         while opcion != "4":
            print("--- Menu Principal ---")
            print("1-Ver estado de inscripcion")
            print("2-Cambiar clave")
            print("3-Mostrar mensaje motivacional")
            print("4-Salir")
            opcion=input("Elija una opcion:")

            if not opcion.isdigit():
               print("Error: ingrese un número válido.")
               
            elif opcion =="1":
               print("Estado: Inscripto a 4 materias")
            elif opcion =="2":
               password_old=input("Ingrese su contraseña actual:")
               if password_old==password:
                  new_password=input("Ingrese su nueva contraseña:")
                  new_password_verify=input("Confirme su nueva contraseña:")
                  if len(new_password) >=6 and new_password == new_password_verify:
                     print("Contraseña creada correctamente:")
                     password=new_password
                  else:
                     print("Error: las claves no coinciden o son muy cortas (minimo 6).")
               else:
                  print("Contraseña actual incorrecta!")
            
            elif opcion=="3":
               print("Todo lo puedo en Cristo que me fortalece. Filipenses 4:13 ")
            
            elif opcion=="4":
               break
            
            else:
               print("Error: opcion fuera de rango.") 
            
            
   else:
      print("Error! Datos incorrectos.")
      intentos += 1
      print(f"Intento {intentos}/3") 
   
if not acceso:
    print("Cuenta bloqueada.")


#Ejercicio3:Agenda de Turnos con Nombres (sin listas)

lunes1=""
lunes2=""
lunes3=""
lunes4=""

martes1="" 
martes2="" 
martes3=""
opcion=""

print("--- Bienvenid@ al Sistema de Gestion de Turnos  ---")
operador= input("Ingrese su nombre de administrador:")
print(f"Bienvenid@ {operador}")

while not operador.isalpha():
   print("Por favor ingrese un nombre que solo contenga Letras.")
   operador=input("Por favor, Ingrese un nombre valido:")
   

while opcion!="5":
   print("--- Menu Principal ---")
   print("1-Reservar Turno")
   print("2-Cancelar Turno")
   print("3-Ver agenda del dia")
   print("4-Ver resumen general")
   print("5-Cerrar sistema")
   opcion=input("Seleccione una opcion:")

   if opcion=="1":
      print("--- Reserva de Turno---")
      print("1-Lunes")
      print("2-Martes")
      dia=input("Elija un Dia:")
   
      if dia == "1":
         print("--- Registro para el Lunes ---")
         name = input("Ingrese su nombre: ")
         
         # Validamos letras
         while not name.isalpha():
            print("Error: El nombre solo debe contener letras.")
            name = input("Ingrese su nombre: ")

         # Filtro de repetidos (Comparamos con TODOS los turnos)
         if name == lunes1 or name == lunes2 or name == lunes3 or name == lunes4:
            print(f"Error: {name} ya tiene un turno asignado para el Lunes.")
         
         # Si no esta repetido, buscamos el primer lugar vacio
         else:
            if lunes1 == "":
               lunes1 = name
               print(f"Reserva exitosa para {name} (Lunes 8:00am)")
            elif lunes2 == "":
               lunes2 = name
               print(f"Reserva exitosa para {name} (Lunes 10:00am)")
            elif lunes3 == "":
               lunes3 = name
               print(f"Reserva exitosa para {name} (Lunes 12:00pm)")
            elif lunes4 == "":
               lunes4 = name
               print(f"Reserva exitosa para {name} (Lunes 14:00pm)")
            else:
                  print("Lo sentimos, no hay mas citas disponibles para el Lunes.")

      if dia == "2":
         print("--- Registro para el Martes ---")
         name = input("Ingrese su nombre: ")
         
         # Validamos letras
         while not name.isalpha():
            print("Error: El nombre solo debe contener letras.")
            name = input("Ingrese su nombre: ")

         # Filtro de repetidos (Comparamos con TODOS los turnos)
         if name == martes1 or name == martes2 or name == martes3:
            print(f"Error: {name} ya tiene un turno asignado para el Martes.")
         
         # Si no esta repetido, buscamos el primer lugar vacio
         else:
            if martes1 == "":
               martes1 = name
               print(f"Reserva exitosa para {name} (Martes 8:00am)")
            elif martes2 == "":
               martes2 = name
               print(f"Reserva exitosa para {name} (Martes 10:00am)")
            elif martes3 == "":
               martes3 = name
               print(f"Reserva exitosa para {name} (Martes 12:00pm)")
            else:
                  print("Lo sentimos, no hay mas citas disponibles para el Martes.")

   elif opcion == "2":
      print("--- Cancelar Turno ---")
      dia_baja = input("Elija día (1=Lunes, 2=Martes): ")
      
      if dia_baja == "1":
         nombre_baja = input("Nombre del paciente a cancelar: ")
         while not nombre_baja.isalpha():
            print("Error: El nombre solo debe contener letras.")
            nombre_baja = input("Ingrese su nombre: ")
            
         if nombre_baja == lunes1:
            lunes1 = ""
            print(f"Turno de {nombre_baja} cancelado.")
         elif nombre_baja == lunes2:
            lunes2 = ""
            print(f"Turno de {nombre_baja} cancelado.")
         elif nombre_baja == lunes3:
            lunes3 = ""
            print(f"Turno de {nombre_baja} cancelado.")
         elif nombre_baja == lunes4:
            lunes4 = ""
            print(f"Turno de {nombre_baja} cancelado.")
         else:
            print("No se encontro ese nombre en la agenda del Lunes.")  
         
      elif dia_baja == "2":
         nombre_baja = input("Nombre del paciente a cancelar: ")
         while not nombre_baja.isalpha():
            print("Error: El nombre solo debe contener letras.")
            nombre_baja = input("Ingrese su nombre: ")
         
         if nombre_baja == martes1:
            martes1 = ""
            print(f"Turno de {nombre_baja} cancelado.")
         elif nombre_baja == martes2:
            martes2 = ""
            print(f"Turno de {nombre_baja} cancelado.")
         elif nombre_baja == martes3:
            martes3 = ""
            print(f"Turno de {nombre_baja} cancelado.")
         else:
            print("No se encontro ese nombre en la agenda del Martes.")


   elif opcion=="3":
      print("--- Agenda ---")
      print("1-Lunes")
      print("2-Martes")
      dia= input("Que dia desea ver?")

      if dia =="1":
         print("--- LUNES ---")
         if lunes1 =="":
            print("Turno 1: Libre")
         else:
            print(f"Turno 1: {lunes1}")
         if lunes2 =="":
            print("Turno 2: Libre")
         else:
            print(f"Turno 2: {lunes2}")
         if lunes3 =="":
            print("Turno 3: Libre")
         else:
            print(f"Turno 3: {lunes3}")
         if lunes4 =="":
            print("Turno 4: Libre")
         else:
            print(f"Turno 4: {lunes4}")
      
      if dia=="2":
         print("--- Martes ---")
         if martes1 =="":
            print("Turno 1: Libre")
         else:
            print(f"Turno 1: {martes1}")
         if martes2 =="":
            print("Turno 2: Libre")
         else:
            print(f"Turno 2: {martes2}")
         if martes3 =="":
            print("Turno 3: Libre")
         else:
            print(f"Turno 3: {martes3}")

   elif opcion == "4":
      print("--- Resumen Citas ---")
      #Contador para el dia Lunes
      cant_lunes = 0
      if lunes1 != "": cant_lunes += 1
      if lunes2 != "": cant_lunes += 1
      if lunes3 != "": cant_lunes += 1
      if lunes4 != "": cant_lunes += 1

      # Contador para Martes
      cant_martes = 0
      if martes1 != "": cant_martes += 1
      if martes2 != "": cant_martes += 1
      if martes3 != "": cant_martes += 1

      libres_lunes = 4 - cant_lunes
      libres_martes = 3 - cant_martes

      print(f"Lunes: {cant_lunes} ocupados / {libres_lunes} libres.")
      print(f"Martes: {cant_martes} ocupados / {libres_martes} libres.")
      print("---------------------------------")
      
      if cant_lunes > cant_martes:
         print("El dia con mas citas es el Lunes.")
      elif cant_martes > cant_lunes:
         print("El dia con mas citas es el Martes.")
      else:
         print("Ambos dias tienen la misma cantidad de turnos ocupados.")
   
   elif opcion == "5":
      print("Gracias por usar el sistema de Gestion de Turnos. Hasta luego")
      break


#Ejercicio 4: “Escape Room: La Boveda”

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzadura = 0

nombre_agente = input("Ingrese nombre del agente: ")
while not nombre_agente.isalpha():
   print("Error: El nombre debe contener solo letras.")
   nombre_agente = input("Ingrese nombre del agente: ")

# El juego sigue mientras...
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
   print(f"--- ESTADO ACTUAL ---")
   print(f"Agente: {nombre_agente} | Energia: {energia} | Tiempo: {tiempo}")
   print(f"Cerraduras: {cerraduras_abiertas}/3 | Alarma: {'ON' if alarma else 'OFF'}")
   
   print("Menu de acciones:")
   print("1. Forzar cerradura (-20 energia, -2 tiempo)")
   print("2. Hackear panel (-10 energía, -3 tiempo)")
   print("3. Descansar (+15 energia, -1 tiempo)")
   
   opcion = input("Elija una accion: ")

   while opcion != "1" and opcion != "2" and opcion != "3":
      print("Opcion no valida. Por favor, elija entre 1, 2 o 3.")
      opcion = input("Elija una accion: ")

   if opcion == "1":
      forzadura += 1
      energia -= 20
      tiempo -= 2
   
      # 1. Chequeo Anti-Spam
      if forzadura == 3:
         print("¡ERROR! Intentaste forzar demasiadas veces seguidas. La cerradura se trabo y salto la alarma.")
         alarma = True
      
      # 2. Chequeo Riesgo de Alarma (Solo si la racha no activo la alarma antes)
      elif energia < 40 and not alarma:
         print("RIESGO DE ALARMA: La baja energia hace que tus manos transpiren y tiemblen.")
         intento = input("Elige un numero del 1 al 3 para mantener la calma: ")
         while intento != "1" and intento != "2" and intento != "3":
            intento = input("Numero no valido. Elige 1, 2 o 3: ")
         
         if intento == "3":
               print("¡TE DETECTARON! La alarma ha comenzado a sonar.")
               alarma = True
      
      # 3. Exito: Solo si no hay alarma y no fallo el anti-spam
      if not alarma and forzadura < 3:
         cerraduras_abiertas += 1
         print("¡Click! Lograste abrir una cerradura.")
   
   elif opcion == "2":
      forzadura = 0  # Se corta la racha
      energia -= 10
      tiempo -= 3
      print("Iniciando secuencia de hackeo...")
      
      for i in range(1, 5):
         print(f"Hackeando sistema... Paso {i}/4")
         codigo_parcial += "AX" 
      
      if len(codigo_parcial) >= 8:
         print("¡CODIGO COMPLETADO! El panel se ha desbloqueado.")
         if cerraduras_abiertas < 3:
               cerraduras_abiertas += 1
               codigo_parcial = "" # Limpiamos el codigo para la siguiente
               print("Una cerradura se abrio automaticamente.")

   elif opcion == "3":
      forzadura = 0  # Se corta la racha
      tiempo -= 1
      recuperacion = 15
      
      if alarma:
         print("La alarma no te deja dormir bien... recuperas menos energia.")
         recuperacion -= 10
         
      energia += recuperacion
      if energia > 100:
         energia = 100
         
      print(f"Has descansado. Energia actual: {energia}")


# --- RESULTADOS FINALES ---
print("\n" + "="*30)
if cerraduras_abiertas == 3:
   print(f"¡VICTORIA! El agente {nombre_agente} ha abierto la boveda.")
   print(f"Recursos finales -> Energia: {energia} | Tiempo: {tiempo}")
elif alarma and tiempo <= 3:
   print("DERROTA: El sistema se bloqueo por la alarma. ¡TE ATRAPARON!")
elif energia <= 0:
   print("DERROTA: Te has quedado sin energia. El agente se desmayo.")
else:
   print("DERROTA: Se acabo el tiempo. La misión ha fallado.")
print("="*30)


#Ejercicio5: Escape Room:"La Arena del Gladiador

print("--- BIENVENIDO Al COLISEO ---")

name = input("Nombre del Gladiador: ")
while not name.isalpha():
   print("Error: Solo se permiten letras.")
   name = input("Nombre del Gladiador: ")

# Estadisticas 
hp_player = 100        
hp_enemy = 100        
pociones = 3              
dano_pesado_base = 15     
dano_enemigo = 12         
turno_gladiador = True   

# Ciclo de Combate
while hp_player > 0 and hp_enemy > 0:
   print(f"\n{name} (HP: {hp_player}) vs Enemigo (HP: {hp_enemy}) | Pociones: {pociones}")
   print("Elige acción:")
   print("1. Ataque Pesado")
   print("2. Rafaga Veloz ")
   print("3. Curarse")

   # Validacion numerica
   opcion = input("Opcion: ")
   while not opcion.isdigit() or (opcion != "1" and opcion != "2" and opcion != "3"):
      print("Error: Ingrese un número valido (1, 2 o 3).")
      opcion = input("Opcion: ")

   # Logica de las Acciones
   if opcion == "1":
      # Accion A: Ataque Pesado 
      dano_final = float(dano_pesado_base) 
      
      if hp_enemy < 20:
            dano_final = dano_final * 1.5 # Golpe Critico
            print("¡GOLPE CRITICO!")
      
      hp_enemy -= int(dano_final)
      print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")

   elif opcion == "2":
      # Accion B: Rafaga Veloz 
      print(">> ¡Inicias una rafaga de golpes!")
      for i in range(3):
            hp_enemy -= 5
            print("> Golpe conectado por 5 de daño")

   elif opcion == "3":
      # Accion C: Curarse
      if pociones > 0:
            hp_player += 30
            pociones -= 1
            print(f"Te has curado. Vida actual: {hp_player}")
      else:
            print("¡No quedan pociones! Pierdes el turno intentando buscar una.")

   # Turno del Enemigo
   # Solo ataca si no ha muerto por el ataque del jugador
   if hp_enemy > 0:
      hp_player -= dano_enemigo
      print(f">> ¡El enemigo te ataco por {dano_enemigo} puntos!")

# Paso 4: Fin del Juego
print("\n" + "="*20)
if hp_player > 0:
   print(f"¡VICTORIA! {name} ha ganado la batalla.")
else:
   print("DERROTA. NT Sera la proxima.")
print("="*20)