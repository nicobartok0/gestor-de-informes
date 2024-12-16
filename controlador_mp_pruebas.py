from controlador_mp import Controlador_MP

controlador = Controlador_MP()
controlador.cargar_sdk('')
transferencias = controlador.obtener_transferencias('2024-11-01T14:30:00Z')
for transferencia in transferencias:
    print(f'Transferencia del {transferencia.fecha} de cantidad {transferencia.monto}, de tipo {transferencia.tipo}. Su op_type es {transferencia.op_type}')