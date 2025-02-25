#DESARROLLO RETO 2
#LO PRIMERO ES CREAR LAS CLASES PRINCIPALES
clientes = [] #VARIABLE GLOBAL:
mascotas = []

class SistemaVeterinaria:
    pass
    class Persona:
        id_counter = 1 #CONTADOR ES AUTOMATICAMENTE AUTOINCREMENTABLE

        def __init__(self, nombre, contacto):
            self.id = SistemaVeterinaria.Persona.id_counter           
            self.nombre = nombre
            self.contacto = contacto
            SistemaVeterinaria.Persona.id_counter += 1

    class Cliente(Persona):
        def __init__(self, nombre, contacto, direccion):
            super().__init__(nombre, contacto)
            self.direccion = direccion
            self.mascotas = [] 

        def agregar_mascota(self, mascota):
            self.mascotas.append(mascota) 

    class Mascota:
        id_counter = 1
        def __init__(self, nombre, especie, raza, edad):
            SistemaVeterinaria.mascota.id_counter += 1
            self.nombre = nombre
            self.especie = especie
            self.raza = raza
            self.edad = edad
            self.historia_clinico = []
            SistemaVeterinaria.Mascota.id_counter += 1    

        def agregar_cita(self,cita):
            self.historia_clinico.append(cita)


    class Citas:
        id_counter = 1
        def __init__(self, fecha, hora, servicio, veterinario):
            self.id = SistemaVeterinaria.Citas.id_counter
            self.fecha = fecha
            self.hora = hora
            self.servicio = servicio
            self.veterinario = veterinario
            SistemaVeterinaria.Citas.id_counter += 1
#funciones auxiliares
def validar_fecha(fecha):
    from datetime import datetime
    try:
        datetime.strptime(fecha,'%d-%d-%Y')
        return True
    except ValueError:
        return False
      

#CREAMOS POR FUERA LOS METODOS O FUNCINES DEL SISTEMA VETERINARIO
def registrar_Cliente():
        print('===========REGISTRO DEL CLIENTE==========')
        nombre = input('ingrese nombre del cliente: ')
        contacto = input('ingrese contacto del cliente: ')
        direccion = input('ingrese direccion del cliente: ')
        cliente = SistemaVeterinaria.Cliente(nombre, contacto, direccion)         
        clientes.append(cliente)
        print(f'cliente agregado con exito. ID: {cliente.id}')   

def registrar_mascota():
    print('==========REGISTRO DE MASCOTA==========')
    cliente_id = int(input('ingrese el id del cliente: '))
    cliente = next((c for c in clientes if c.id == cliente_id), None) #SENTENCIA
    if not cliente:
        print('cliente no encontrado')
        return
    nombre_mascota = input('Nombre de la mascota: ')
    especie = input('Especie de la mascota: ')
    raza = input('Raza de la mascota: ')
    edad = input('Ingrese edad de la mascota: ')
    mascota = SistemaVeterinaria.Mascota(nombre_mascota,especie, raza, edad)

    cliente.agregar_mascota(mascota)
    mascotas.append(mascota)
    print(f'mascota registrada con exito, ID: {mascota.id}')

def programar_cita():
    print('===========Programar Cita==============')
    cliente_id = int(input('ingrese el id del cliente: '))
    cliente = next((c for c in clientes if c.id == cliente_id), None) #SENTENCIA

    if not cliente:
            print('cliente no encontrado')
            return
    mascota_id = int(input('ingrese el id del cliente: '))
    mascota = next((m for m in cliente.mascotas if m.id == mascota_id), None)

    if not mascota:
        print('mascota no encontrado')
        return
    fecha = input('ingrese la fecha de la cita(DD-MM-YYYY):')
    while not validar_fecha(fecha):
        print('fecha invalida, por favor use el formato DD-MM-YYYY ')
        fecha = input('ingrese la fecha de la cita(DD-MM-YYYY):')
    hora = input('ingrese la hora del cita (HH:MM)')
    servicio = input('ingrese el servicio(consultorio, vacunacion, etc,):')
    veterinario = input('ingrese el nombre del veterinario')


    print('Cita agendada')

def consutlar_historial():
        pass

#menu principal
def menu_principal():
        while True:
            print('==================Menu Principal============')
            print('1. Registrar cliente')
            print('2. Registrar mascota')
            print('3. programar cita')
            print('4. Consultar historial')
            print('5. Salir\n')
            opc = input('seleccione una opcion: ')

            if opc == '1':
                registrar_Cliente()             
            elif opc == '2':
                registrar_mascota()
            
            elif opc == '3':
                programar_cita()
            
            elif opc == '4':
                consutlar_historial
            elif opc == '5':
                break

            else:
                print('opcion no valida')            

menu_principal()        

#creada con exito, la rama

    


