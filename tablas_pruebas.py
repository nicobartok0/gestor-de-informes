import dearpygui.dearpygui as dpg
from movimiento import Movimiento

mov1 = {
        'tipo': 'EGRESO',
        'fecha': '13/12/2024',
        'categoria': 'AGUA',
        'met_pago': '-',
        'monto': '1000',
        'sector': 'ADMIN',
        'obs': ''
}

mov2 = {
        'tipo': 'EGRESO',
        'fecha': '15/12/2024',
        'categoria': 'SERVICIOS',
        'met_pago': '-',
        'monto': '10000',
        'sector': 'ADMIN',
        'obs': ''
}

mov3 = {
        'tipo': 'EGRESO',
        'fecha': '17/12/2024',
        'categoria': 'SERVICIOS',
        'met_pago': '-',
        'monto': '10000',
        'sector': 'ADMIN',
        'obs': ''
}

movimientos = [
    Movimiento(mov1),
    Movimiento(mov2),
    Movimiento(mov3)
]

dpg.create_context()

with dpg.window(label="Tutorial"):
    with dpg.table(header_row=False):

        # use add_table_column to add columns to the table,
        # table columns use child slot 0
        
        dpg.add_table_column(label='Tipo')
        dpg.add_table_column(label='Fecha')
        dpg.add_table_column(label='Categoría')
        dpg.add_table_column(label='Método de pago')
        dpg.add_table_column(label='Monto')
        dpg.add_table_column(label='Sector')
        dpg.add_table_column(label='Observación')
        
        # add_table_next_column will jump to the next row
        # once it reaches the end of the columns
        # table next column use slot 1
        for movimiento in movimientos:
            elementos = []
            for element in movimiento.__dict__.values():
                elementos.append(element)
            with dpg.table_row():
                for i in range(7):
                    dpg.add_text(f"{elementos[i]}")
for movimiento in movimientos:
    print(movimiento.__dict__)
dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()