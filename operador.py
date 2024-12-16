from lector import Lector
from controlador_mp import Controlador_MP
from movimiento import Movimiento

class Operador:
    def __init__(self) -> None:
        self.movimientos = []
        self.lector = Lector()
        self.controlador_mp = Controlador_MP()


    def cargar_caja_chica(self, ruta, sucursal):
        movimientos = self.lector.cargar_caja_chica(ruta, sucursal)
        for movimiento in movimientos:
            self.movimientos.append(movimiento)
        print(self.movimientos)
        print(f'SUCURSAL {sucursal}')
        
    def cargar_consolidacion_gastos(self, ruta, fecha):
        movimientos = self.lector.cargar_consolidacion_gastos(ruta, fecha)
        for movimiento in movimientos:
            self.movimientos.append(movimiento)
        print(self.movimientos)
        print(f'FEHCA {fecha}')

    def cargar_api_key(self, api_key):
        self.controlador_mp.cargar_sdk(api_key)
        print(self.controlador_mp.sdk)    

    def obtener_transferencias_mp(self, dia, mes, año):
        fecha = f'{año}-{mes}-{dia}T00:00:00Z'
        movimientos = self.controlador_mp.obtener_transferencias(fecha_inicio=fecha)
        for movimiento in movimientos:
            self.movimientos.append(movimiento)
        print(self.movimientos)
    
    def return_egresos(self):
        egresos = []
        for movimiento in self.movimientos:
            if movimiento.tipo == 'EGRESO':
                egresos.append(movimiento)

        return egresos

    def return_ingresos(self):
        ingresos = []
        for movimiento in self.movimientos:
            if movimiento.tipo == 'INGRESO':
                ingresos.append(movimiento)

        return ingresos
    
    def añadir_movimiento(self, mov:dict):
        self.movimientos.append(Movimiento(mov))

    def generar_informe(self):
        self.lector.escribir_informe(self.movimientos)

    def cargar_excel(self, ruta):
        operaciones = self.lector.cargar_informe(ruta)
        for operacion in operaciones:
            self.movimientos.append(operacion)

