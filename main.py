class Cuenta:
    def __init__(self, numero_cuenta , pin, saldo=0):
        self.__numero_cuenta = numero_cuenta
        self.__pin = pin
        self.__saldo = saldo

    def verificar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if self.__saldo >= cantidad:
            self.__saldo -= cantidad
            return True
        else:
            print("Saldo insuficiente")
            return False

    def obtener_saldo(self):
        return self.__saldo

    def transferir(self, cantidad, cuenta_destino):
        if self.__saldo >= cantidad:
            self.__saldo -= cantidad
            cuenta_destino.depositar(cantidad)
            return True
        return False
        
    def obtener_numero_cuenta(self):
        return self.__numero_cuenta
    
class Banco:
    def __init__(self):
        self.__cuentas = {}

    def agregar_cuenta(self, cuenta):
        self.__cuentas[cuenta.obtener_numero_cuenta()] = cuenta
    def obtener_cuenta(self, numero_cuenta):
        return self.__cuentas.get(numero_cuenta)

            
class CajeroAutomatico:
    def __init__(self, banco):
        self.__banco = banco
        self.__cuenta_actual = None

    def iniciar_sesion(self, numero_cuenta, pin):
        cuenta = self.__banco.obtener_cuenta(numero_cuenta)
        if cuenta and cuenta.verificar_pin(pin):
            self.__cuenta_actual = cuenta
            return True
        else:
            return False
        
    def mostrar_menu(self):
        if self.__cuenta_actual:
            print("\nCajero Automatico")
            print("1. Consultar saldo")
            print("2. Realizar deposito")
            print("3. Realizar retiro")
            print("4. Transferir fondos")
            print("5. Salir")

            opcion = input("Seleccione una opcion: ")
            return opcion
        else:
            print("No hay una cuenta iniciada")
            return None
        
    def depositar(self, cantidad):
        if self.__cuenta_actual:
            self.__cuenta_actual.depositar(cantidad)
            print(f"Deposito de {cantidad} realizado correctamente")
        else:
            print("No hay una cuenta iniciada")
    
    def retirar(self, cantidad):
        if self.__cuenta_actual:
            if self.__cuenta_actual.retirar(cantidad):
                print(f"Retiro de {cantidad} realizado correctamente")
            else:
                print("Saldo insuficiente")
        else:
            print("No hay una cuenta iniciada")

    def consultar_saldo(self):
        if self.__cuenta_actual:
            print(f"Saldo actual: {self.__cuenta_actual.obtener_saldo()}")
        else:
            print("No hay una cuenta iniciada")

    def transferir(self, cantidad, numero_cuenta_destino):
        if self.__cuenta_actual:
            cuenta_destino = self.__banco.obtener_cuenta(numero_cuenta_destino)
            if cuenta_destino:
                if self.__cuenta_actual.transferir(cantidad, cuenta_destino):
                    print(f"Transferencia de {cantidad} realizada correctamente")
                else:
                    print("No hay suficiente saldo para la transferencia")
            else:
                print("No se encontró la cuenta destino")
        else:
            print("No hay una cuenta iniciada")

    def cerrar_sesion(self):
        if self.__cuenta_actual:
            self.__cuenta_actual = None
            print("Sesion cerrada correctamente")
        else:
            print("No hay una cuenta iniciada")


banco = Banco()
banco.agregar_cuenta(Cuenta(numero_cuenta="1234567890", pin="1234", saldo=1000))
banco.agregar_cuenta(Cuenta(numero_cuenta="1234567891", pin="1234", saldo=2000))

cajero = CajeroAutomatico(banco)

if cajero.iniciar_sesion("1234567890", "1234"):
    while True:
        opcion = cajero.mostrar_menu()
        if opcion == "1":
            cajero.consultar_saldo()
        elif opcion == "2":
            cajero.depositar(float(input("Ingrese la cantidad a depositar: ")))
        elif opcion == "3":
            cajero.retirar(float(input("Ingrese la cantidad a retirar: ")))
        elif opcion == "4":
            cajero.transferir(float(input("Ingrese la cantidad a transferir: ")), input("Ingrese el numero de cuenta destino: "))
        elif opcion == "5":
            cajero.cerrar_sesion()
            break
        else:
            print("Opcion no válida")
else:
        print("Numero de cuenta o PIN incorrectos")
