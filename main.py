#DESARROLLO RETO 2
#LO PRIMERO ES CREAR LAS CLASES PRINCIPALES
clientes = [] #VARIABLE GLOBAL:

class SistemaVeterinaria:
    pass
    class Persona:
        id_conter = 1 #CONTADOR ES AUTOMATICAMENTE AUTOINCREMENTABLE

        def __init__(self, nombre, contacto):
            self.id = SistemaVeterinaria.Persona.id_counter           
            self.nombre = nombre
            self.contacto = contacto
            SistemaVeterinaria.Persona.id_counter += 1

    class Cliente(Persona):
        def __init__(self, nombre, contacto, direccion):
            super().__init__(nombre, contacto)
            self.direccion = direccion
            self.mascota = [] 

        def agregar_mascota(self, mascota):
            self.mascota.append(mascota) 

    class Mascota:
        id_counter = 1
        def __init__(self, nombre, especie, raza, edad):
            self.id = SistemaVeterinaria.mascota.id_counter
            self.nombre = nombre
            self.especie = especie
            self.raza = raza
            self.edad = edad
            self.historia_clinico = []
            SistemaVeterinaria.Persona.id_counter += 1               

    class Citas:
        id_counter = 1
        def __init__(self, fecha, hora, servicio, veterinario):
            self.id = SistemaVeterinaria.Citas.id_counter
            self.fecha = fecha
            self.hosra = hora
            self.servicio = servicio
            self.veterinario = veterinario
            SistemaVeterinaria.Citas.id_counnter += 1

#CREAMOS POR FUERA LOS METODOS O FUNCINES DEL SISTEMA VETERINARIO
def registrar_Cliente():
        print('===========REGISTRO DEL CLIENTE==========')
        nombre = input('ingrese nombre del cliente: ')
        contacto = input('ingrese contacto del cliente: ')
        direccion = input('ingrese direccion del cliente: ')
        cliente = SistemaVeterinaria.Cliente(nombre, contacto, direccion)      
        clientes.append(cliente)
        print('cliente agregado con exito')   

def registrar_mascota():
    print('==========REGISTRO DE MASCOTA==========')
    nombre_mascota = input('Nombre de la mascota: ')
    especie = input('Especie de la mascota: ')
    raza = input('Raza de la mascota: ')
    edad = input('Ingrese edad: ')
    mascota = SistemaVeterinaria.Mascota(nombre_mascota,especie, raza, edad)
    mascota.agregar_mascota(mascota)

def programar_CITA():
        cliente_id = int(input('ingrese el id del cliente: '))
        cliente = next((c for c in clientes if c.id == cliente_id), None)

        if not clientes:
            print('cliente no encontrado')
            return
        mascota_id = int(input('ingrese el id del cliente: '))
        mascotas = next((c for c in cliente.mascotas if c.id == cliente_id), None)

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
                pass
            
            if opc == '4':
                pass

            else:
                print('opcion no valida')            

menu_principal()        

    


