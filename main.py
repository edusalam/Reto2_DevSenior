#DESARROLLO RETO 2
#LO PRIMERO ES CREAR LAS CLASES PRINCIPALES

#variable:
Clientes = []

class SistemaVeterinaria:
    pass

    class Persona:
        id_conter = 1
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

    class Mascota:
        id_counter = 1
        def __init__(self, nombre, especie, raza, edad):
            self.id = SistemaVeterinaria.mmascota.id_counter
            self.nombre = nombre
            self.especie = especie
            self.raza = raza
            self.edad = edad
            self.historia_clinico = []
        def agregar_mascota(self, mascota):
            self.mascota.append()
            
            self.id = SistemaVeterinaria.mascota.id_counter += 1

    class Citas:
        id_counter = 1
        def __init__(self, fecha, hora, sercicio, veterinario):
            self.id = SistemaVeterinaria.Citas.id_counter
            self.fecha = fecha
            self.hosra = hora

            SistemaVeterinaria.Citas-id_counnter += 1

    def registrarCliente():
        print('===========Registro Del Cliente==========')
        nombre = input('ingrese nombre del cliente: ')
        contacto = input('ingrese contacto del cliente')
        direccion = input('ingrese direccion del cliente')

        cliente = SistemaVeterinaria.clie(nonbre, contacto, direccion)

        print('======registro mascota====')
        nombre_mascota = input('nombree de la mascota')
        especie = input('especie de la mascota')
        raza = input('raza de la mascota')
        edad = input('ingrese edad')
        mascota = SistemaVeterinaria.Mascota(nombre_mascota,especie, raza)

        cliente.agregar_mascota(mascota)

        Clientes.append(cliente)
        print('cliente y mascota agregado con exito')    

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
            registrarCliente
        if opc == '2':
            pass
        if opc == '3':
            pass
        if opc == '4':
            pass
        else:
            print('opcion no valida')    
 
    menu_principal()

    


