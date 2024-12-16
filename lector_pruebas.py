from lector import Lector


lector = Lector()

lector.cargar_caja_chica('listado_caja_chica.xlsx', sucursal='ALVEAR')

#for movimiento in movimientos:
#    print(f'EGRESO DE FECHA {movimiento.fecha} MONTO: {movimiento.monto}')

movimientos = lector.cargar_consolidacion_gastos('consolidacion_gastos.xlsx', '27-Nov-24')
for movimiento in movimientos:
    print(f'MOVIMIENTO DE FECHA {movimiento.fecha}, {movimiento.categoria} DE MONTO {movimiento.monto}. El área es {movimiento.sector}')