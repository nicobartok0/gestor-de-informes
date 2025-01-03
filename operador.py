from lector import Lector
from controlador_mp import Controlador_MP
from movimiento import Movimiento
from controlador_db import Controlador_DB
import datetime

class Operador:
    def __init__(self) -> None:
        self.movimientos = []
        self.lector = Lector()
        self.controlador_mp = Controlador_MP()
        self.controlador_api = Controlador_DB()


    def cargar_caja_chica(self, ruta, sucursal, met_pago):
        movimientos = self.lector.cargar_caja_chica(ruta, sucursal, met_pago)
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

    def obtener_transferencias_mp(self, dia, mes, año, dia_fin, mes_fin, año_fin):
        fecha = f'{año}-{mes}-{dia}T00:00:00Z'
        fecha_fin = f'{año_fin}-{mes_fin}-{dia_fin}T00:00:00Z'
        movimientos = self.controlador_mp.obtener_transferencias(fecha_inicio=fecha, fecha_fin=fecha_fin)
        for movimiento in movimientos:
            self.movimientos.append(movimiento)
        print(self.movimientos)
    
    def return_egresos(self, filtro):
        egresos = []
        if filtro == None:
            for movimiento in self.movimientos:
                print(movimiento.tipo)
                if movimiento.tipo == 'EGRESO':
                    egresos.append(movimiento)
        else:
            for movimiento in self.movimientos:
                if filtro == 'OTRO':
                    if movimiento.sector not in ['ALVEAR', 'SAN RAFAEL', 'SAN MARTIN', 'GRANJA', 'ADMIN', 'FRIGO']:
                        egresos.append(movimiento)
                else:
                    if movimiento.tipo == 'EGRESO' and movimiento.sector == filtro:
                        egresos.append(movimiento)
        return egresos

    def return_ingresos(self, filtro):
        ingresos = []
        if filtro == None:
            for movimiento in self.movimientos:
                if movimiento.tipo == 'INGRESO':
                    ingresos.append(movimiento)
        else:
            for movimiento in self.movimientos:
                if filtro == 'OTRO':
                    if movimiento.sector not in ['ALVEAR', 'SAN RAFAEL', 'SAN MARTIN', 'GRANJA', 'ADMIN', 'FRIGO']:
                        ingresos.append(movimiento)
                else:
                    if movimiento.tipo == 'INGRESO' and movimiento.sector == filtro:
                        ingresos.append(movimiento)

        return ingresos
    
    def añadir_movimiento(self, mov:dict):
        self.movimientos.append(Movimiento(mov))

    def generar_informe(self, fecha_inicio, fecha_final):
        self.lector.escribir_informe(self.movimientos, fecha_inicio, fecha_final)


    def cargar_excel(self, ruta):
        operaciones = self.lector.cargar_informe(ruta)
        for operacion in operaciones:
            self.movimientos.append(operacion)

    def obtener_sucursales(self):
        print(self.controlador_api.obtener_sucursales())

    def cargar_movimientos_db(self, fecha_inicio, fecha_final):
        movimientos_filtrados = []
        fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%d-%m-%Y')
        fecha_final = datetime.datetime.strptime(fecha_final, '%d-%m-%Y')
        for movimiento in self.movimientos:    
            fecha = datetime.datetime.strptime(movimiento.fecha, '%d-%m-%Y')
            if fecha_inicio <= fecha <= fecha_final:
                movimientos_filtrados.append(movimiento)

        self.controlador_api.añadir_movimientos(movimientos=movimientos_filtrados)

    def cargar_registro_contrable(self, ruta, estado):
        if estado == 'Ingresos':
            movimientos = self.lector.cargar_registro_contrable(ruta, sheetname='Ingresos')
            for movimiento in movimientos:
                
                self.movimientos.append(movimiento)
        else:
            movimientos = self.lector.cargar_registro_contrable(ruta, sheetname='Egresos')
            for movimiento in movimientos:
                
                self.movimientos.append(movimiento)

        
        print(self.movimientos)
                
    