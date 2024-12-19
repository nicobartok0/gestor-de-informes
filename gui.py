import dearpygui.dearpygui as dpg
from operador import Operador
from selector import Selector

# Creamos nuestro operador que se encargará de toda la lógica
operador = Operador()

# Utilizamos una variable global
selector = Selector()

# Configuración inicial de la ventana principal
dpg.create_context()
dpg.create_viewport(title="Gestión de Movimientos de Dinero", width=800, height=600)



# Función de callback para cuando seleccionan un archivo de CAJA CHICA
def file_selected_callback_cc(sender, app_data):
    
    print('Ruta: ' + str({app_data['file_path_name']}))
    print(dpg.get_value('combo_cc'))
    operador.cargar_caja_chica(ruta=app_data['file_path_name'], sucursal=dpg.get_value('combo_cc'), met_pago=dpg.get_value('metodo_pago_combo_2'))

# Función de callback para cuando seleccionan un archivo de CONSOLIDACIÓN DE GASTOS
def file_selected_callback_cg(sender, app_data):
    
    print('Ruta: ' + str({app_data['file_path_name']}))
    print(dpg.get_value('input_cg'))
    operador.cargar_consolidacion_gastos(ruta=app_data['file_path_name'], fecha=dpg.get_value('input_cg'))

# Función de callback para cuando seleccionan un archivo de CARGA DE EXCEL
def file_selected_callback_ci(sender, app_data):
    
    print('Ruta: ' + str({app_data['file_path_name']}))
    operador.cargar_excel(ruta=app_data['file_path_name'])


# Crear un cuadro de diálogo de selección de archivos CAJA CHICA
with dpg.file_dialog(directory_selector=False, show=False, callback=file_selected_callback_cc, id="file_dialog_id_cc", width=500, height=400):
    dpg.add_file_extension(".xlsx", color=(0, 255, 0, 255))  # Archivos .xlsx en verde
    dpg.add_file_extension(".xls", color=(255, 0, 0, 255))  # Archivos .xls en rojo
    dpg.add_file_extension(".*")                            # Otros archivos

# Crear un cuadro de diálogo de selección de archivos CONSOLIDACIÓN DE GASTOS
with dpg.file_dialog(directory_selector=False, show=False, callback=file_selected_callback_cg, id="file_dialog_id_cg", width=500, height=400):
    dpg.add_file_extension(".xlsx", color=(0, 255, 0, 255))  # Archivos .xlsx en verde
    dpg.add_file_extension(".xls", color=(255, 0, 0, 255))  # Archivos .xls en rojo
    dpg.add_file_extension(".*")                            # Otros archivos

# Crear un cuadro de diálogo de selección de archivos CARGAR EXCEL
with dpg.file_dialog(directory_selector=False, show=False, callback=file_selected_callback_ci, id="file_dialog_id_ci", width=500, height=400):
    dpg.add_file_extension(".xlsx", color=(0, 255, 0, 255))  # Archivos .xlsx en verde
    dpg.add_file_extension(".xls", color=(255, 0, 0, 255))  # Archivos .xls en rojo
    dpg.add_file_extension(".*")                            # Otros archivos

# Función para manejar los callback del menú
def menu_callback(sender, data, user_data):
    print(user_data)
    if user_data == 'OPCION_API_KEY':
        dpg.show_item('ventana_api_key')
    elif user_data == 'OPCION_CC':
        dpg.show_item('ventana_caja_chica')
    elif user_data == 'OPCION_CMP':
        dpg.show_item('ventana_transferencias_mp')
    elif user_data == 'OPCION_INFORME':
        generar_informe()
    elif user_data == 'OPCION_CARGA_INFORME':
        dpg.show_item('ventana_cargar_informe')
    else:
        dpg.show_item('ventana_consolidacion_gastos')
            
# Función para mostrar la ventana de API_KEY
def mostrar_ventana_api_key():
    dpg.show_item("ventana_api_key")

# Función para cerrar la ventana de API_KEY
def cerrar_ventana_api_key():
    dpg.hide_item("ventana_api_key")

# Función para mostrar la ventana de CAJA CHICA
def mostrar_ventana_caja_chica():
    dpg.show_item("ventana_caja_chica")

# Función para cerrar la ventana de CAJA CHICA
def cerrar_ventana_caja_chica():
    dpg.hide_item("ventana_caja_chica")

# Función para mostrar la ventana de CONSOLIDACIÓN GASTOS
def mostrar_ventana_consolidacion_gastos():
    dpg.show_item("ventana_consolidacion_gastos")

# Función para cerrar la ventana de CONSOLIDACIÓN GASTOS
def cerrar_ventana_consolidacion_gastos():
    dpg.hide_item("ventana_consolidacion_gastos")

# Función para mostrar la ventana de TRANSFERENCIAS MERCADO PAGO
def mostrar_ventana_transferencias_mp():
    dpg.show_item("ventana_transferencias_mp")

# Función para cerrar la ventana de TRANSFERENCIAS MERCADO PAGO
def cerrar_ventana_transferencias_mp():
    dpg.hide_item("ventana_transferencias_mp")

# Función para actualizar una tabla
def actualizar_tabla_ingresos(filtro):
    print('INGRESOS')
    # Limpiamos la tabla antes de actualizarla
    rows = dpg.get_item_children(item='tabla_ingresos', slot=1)
    for row in rows:
        dpg.delete_item(row)
    # Lógica de actualización de tabla utilizando los valores de diccionario de cada movimiento
    for movimiento in operador.return_ingresos(filtro):
        elementos = []
        for element in movimiento.__dict__.values():
            if element != 'INGRESO':
                elementos.append(element)
        with dpg.table_row(parent="tabla_ingresos"):
            for i in range(6):
                dpg.add_text(f"{elementos[i]}")

def actualizar_tabla_egresos(filtro):
    print('EGRESOS')
    # Limpiamos la tabla antes de actualizarla
    rows = dpg.get_item_children(item='tabla_egresos', slot=1)
    for row in rows:
        dpg.delete_item(row)
    # Lógica de actualización de tabla utilizando los valores de diccionario de cada movimiento
    for movimiento in operador.return_egresos(filtro):
            elementos = []
            for element in movimiento.__dict__.values():
                if element != 'EGRESO':
                    elementos.append(element)
            with dpg.table_row(parent="tabla_egresos"):
                for i in range(6):
                    dpg.add_text(f"{elementos[i]}")

def generar_informe():
    operador.generar_informe()

def añadir_movimiento():
    mov = {
        'tipo': dpg.get_value('tipo_combo'),
        'fecha': dpg.get_value('fecha_input'),
        'categoria': dpg.get_value('categoria_input'),
        'met_pago': dpg.get_value('metodo_pago_combo'),
        'monto': dpg.get_value('monto_input'),
        'sector': dpg.get_value('sucursales_combo'),
        'obs': dpg.get_value('observaciones_input') 
    }
    operador.añadir_movimiento(mov)
                    
                        
# LAMENTABLEMENTE HAY QUE EDITAR ESTO CADA VEZ QUE SE AÑADEN WIDGETS A LA APLICACIÓN. ESTO ESTÁ ASÍ TEMPORALMENTE.
# Función para elegir la tabla a actualizar
def actualizar_tabla(sender, app_data):
    tab = dpg.get_item_user_data(app_data)
    if tab == 'INGRESOS':
        print('ACTUALIZAR TABLA DE INGRESOS')
        actualizar_tabla_ingresos(filtro=None)
    elif tab == 'EGRESOS':
        print('ACTUALIZAR TABLA DE EGRESOS')
        actualizar_tabla_egresos(filtro=None)
    else:
        print(f'{app_data}')

def actualizar_selector(tabla):
    selector.set_tabla_actual(tabla)

def obtener_selector():
    return selector

with dpg.window(tag="MainWindow", label="Gestión de Movimientos de Dinero", width=800, height=560, pos=(0,30), menubar=True):

    # Este es el menú de opciones de la barra de arriba a la izquierda. Acá se añaden las nuevas opciones. Todas deben hacer
    # referencia a "menu_callback", y después según el user_data se modifica menu_callback para identificar cuál de las opciones
    # fue clickeada, y qué función se ejecutará en consecuencia.

    with dpg.menu_bar():
        with dpg.menu(label='Opciones'):
            dpg.add_menu_item(label='Cargar API_KEY', callback=menu_callback, user_data='OPCION_API_KEY')
            dpg.add_menu_item(label='Cargar caja chica', callback=menu_callback, user_data='OPCION_CC')
            dpg.add_menu_item(label='Cargar consolidación de gastos', callback=menu_callback, user_data='OPCION_CG')
            dpg.add_menu_item(label='Cargar transferencias de Mercado Pago', callback=menu_callback, user_data='OPCION_CMP')
            dpg.add_menu_item(label='Realizar informe automático general', callback=menu_callback, user_data='OPCION_INFORME')
            dpg.add_menu_item(label='Cargar de informe automático general', callback=menu_callback, user_data='OPCION_CARGA_INFORME')

  
    # Crear el Value Registry
    with dpg.value_registry():
        # Registrar el calor de la tab actual
        dpg.add_string_value(tag="tab_actual", default_value="Texto inicial")

    # Crear el contenedor de pestañas
    with dpg.tab_bar(callback=actualizar_tabla):

        # Pestaña 1: Formulario para ingresar movimientos
        with dpg.tab(label="Agregar Movimiento", user_data='agregar_movimiento'):
            
            
            dpg.add_text("Ingrese los detalles del movimiento:")
            
            # Tipo
            dpg.add_text("Tipo:")
            dpg.add_combo(["INGRESO", "EGRESO"], tag="tipo_combo", default_value="INGRESO")
            
            # Fecha
            dpg.add_text("Fecha (DD/MM/YYYY):")
            dpg.add_input_text(tag="fecha_input", hint="Ej. 26-11-2024", width=150)
            
            # Categoría
            dpg.add_text("Categoría:")
            dpg.add_combo(["Aditivos", "Afiliado", "Alimento Granja", "Alquiler", 
                           "Colaboración", "Combustible", "Consumo Personal", "Descartables", 
                           "Desinfección", "Dosis de inseminación", "Frío Andino", 
                           "Gastos administrativos", "Gastos bancarios", "Higiene y seguridad", 
                           "Honorarios profesionales", "Indumentaria", "Insumos", 
                           "Laboratorio/Medicamentos/Vacunas granja", "Librería", "Limpieza", 
                           "Mano de Obra/Contratista", "Mantenimiento Vehículos", "Maquinas/Herramientas", 
                           "Matadero", "Material de construcción", "Medicina Laboral", "Mercadería para la venta", 
                           "Publicidad", "Retiro", "Seguros", "Servicio Técnico", "Servicios e Impuestos", 
                           "Sindicatos", "Stopcar", "Sueldos", "Transporte/Encomienda"], 
                          tag="categoria_input", default_value="Efectivo")
            
            # Método de pago
            dpg.add_text("Método de Pago:")
            dpg.add_combo(["Transferencia", "Efectivo", "Depósito", "Cheque emitido", "Cheque endosado", "Débito automático", 
                           "Caja chica Buenos Aires", "Acreditación", "Caja chica Alvear", "Caja chica San Rafael", 
                           "Caja chica San Martín","Otro"], 
                          tag="metodo_pago_combo", default_value="Efectivo")
            
            # Sucursal
            dpg.add_text("Sucursal / Área:")
            dpg.add_combo(["ALVEAR", "SAN RAFAEL", "SAN MARTIN", "FRIGO", "CASA CENTRAL", "GRANJA", "OTRO"], 
                          tag="sucursales_combo", default_value="Alvear")
            
            # Monto
            dpg.add_text("Monto:")
            dpg.add_input_text(tag="monto_input", hint="Ingrese un monto", width=150)
            
            # Observaciones
            dpg.add_text("Observaciones:")
            dpg.add_input_text(tag="observaciones_input", hint="Detalles adicionales", multiline=True, width=300, height=100)

            # Botón de envío de dato
            dpg.add_button(label='Enviar movimiento', tag='env_mov', callback=añadir_movimiento)

        # Pestaña 2: Tabla de ingresos
        with dpg.tab(label="Tabla de Ingresos", user_data='INGRESOS', tag='tab_ingresos'):
            actualizar_selector('INGRESOS')
            dpg.add_text("Lista de Ingresos:")
            dpg.add_text('Filtrado por área')
            dpg.add_combo(["ALVEAR", "SAN RAFAEL", "SAN MARTÍN", "FRIGO", "CASA CENTRAL", "GRANJA", "OTRO"], 
                          tag="sucursales_combo_f_e", default_value="-", callback=lambda: actualizar_tabla_ingresos(filtro=dpg.get_value('sucursales_combo_f_e')))
            with dpg.table(header_row=True, tag="tabla_ingresos"):
                dpg.add_table_column(label="Fecha")
                dpg.add_table_column(label="Categoría")
                dpg.add_table_column(label="Método de Pago")
                dpg.add_table_column(label="Monto")
                dpg.add_table_column(label="Sucursal")
                dpg.add_table_column(label="Observaciones")

        # Pestaña 3: Tabla de egresos
        with dpg.tab(label="Tabla de Egresos", user_data='EGRESOS', tag='tab_egresos'):
            actualizar_selector('EGRESOS')
            dpg.add_text("Lista de Egresos:")
            dpg.add_text('Filtrado por área')
            dpg.add_combo(["ALVEAR", "SAN RAFAEL", "SAN MARTÍN", "FRIGO", "CASA CENTRAL", "GRANJA", "OTRO"], 
                          tag="sucursales_combo_f_i", default_value="-", callback=lambda: actualizar_tabla_egresos(filtro=dpg.get_value('sucursales_combo_f_i')))
            with dpg.table(header_row=True, tag="tabla_egresos"):
                dpg.add_table_column(label="Fecha")
                dpg.add_table_column(label="Categoría")
                dpg.add_table_column(label="Método de Pago")
                dpg.add_table_column(label="Monto")
                dpg.add_table_column(label="Sucursal")
                dpg.add_table_column(label="Observaciones")

# Crear la ventana para cargar la API_KEY (oculta al inicio)
with dpg.window(tag="ventana_api_key", label="Cargar API_KEY", width=400, height=200, show=False):
    dpg.add_text("Ingrese su API_KEY:")
    dpg.add_input_text(tag="input_api_key", hint="Ej. abc123xyz", password=True, width=300)
    dpg.add_button(label="Guardar", callback=lambda: operador.cargar_api_key(dpg.get_value('input_api_key')))
    
    dpg.add_button(label="Cerrar", callback=cerrar_ventana_api_key)

# Crear la ventana para cargar CAJA CHICA (oculta al inicio)
with dpg.window(tag="ventana_caja_chica", label="Cargar caja chica", width=400, height=200, show=False):
    dpg.add_text("CAJA CHICA")
    dpg.add_text('Este EXCEL de Caja Chica corresponde a la sucursal: ')
    dpg.add_combo(tag='combo_cc', items=['SAN RAFAEL', 'ALVEAR', 'SAN MARTÍN', 'FRIGO', 'CASA CENTRAL', 'GRANJA', 'CAMPO'])
    dpg.add_text('Con el método de pago: ')
    dpg.add_combo(["Transferencia", "Efectivo", "Depósito", "Cheque emitido", "Cheque endosado", "Débito automático", 
                           "Caja chica Buenos Aires", "Acreditación", "Caja chica Alvear", "Caja chica San Rafael", 
                           "Caja chica San Martín","Otro"], 
                          tag="metodo_pago_combo_2", default_value="Efectivo")
    dpg.add_text('Ruta del archivo excel: ')
    dpg.add_button(tag='button_ruta_excel_cc', label='Buscar EXCEL', callback=lambda: dpg.show_item('file_dialog_id_cc'))

# Crear la ventana para cargar CONSOLIDACIÓN DE GASTOS (oculta al inicio)
with dpg.window(tag="ventana_consolidacion_gastos", label="Cargar consolidación de gastos", width=400, height=200, show=False):
    dpg.add_text("CONSOLIDACIÓN DE GASTOS")
    dpg.add_text('Este EXCEL de Consolidación de Gastos corresponde a la fecha: ')
    dpg.add_input_text(tag='input_cg', hint='Ej: 27-Nov-24')
    dpg.add_text('Ruta del archivo excel: ')
    dpg.add_button(tag='button_ruta_excel_cg', label='Buscar EXCEL', callback=lambda: dpg.show_item('file_dialog_id_cg'))

# Crear la ventana para cargar TRANSFERENCIAS DE MERCADO PAGO (oculta al inicio)
with dpg.window(tag='ventana_transferencias_mp', label='Cargar transferencias de Mercado Pago', width=400, height=200, show=False):
    dpg.add_text('Cargar transferencias de Mercado Pago')
    dpg.add_text('Cargar todas las transferencias desde la fecha: ')
    dpg.add_input_text(tag= 'dia_mp', label='Día (DD)')
    dpg.add_input_text(tag= 'mes_mp', label='Mes (MM)')
    dpg.add_input_text(tag= 'año_mp', label='Año (YYYY)')
    dpg.add_input_text(tag= 'dia_mp_fin', label='Día (DD)')
    dpg.add_input_text(tag= 'mes_mp_fin', label='Mes (MM)')
    dpg.add_input_text(tag= 'año_mp_fin', label='Año (YYYY)')
    dpg.add_button(label='Obtener transferencias', callback=lambda: operador.obtener_transferencias_mp(dia=dpg.get_value('dia_mp'), mes=dpg.get_value('mes_mp'), año=dpg.get_value('año_mp')
                                                                                                       , dia_fin=dpg.get_value('dia_mp_fin'),mes_fin=dpg.get_value('mes_mp_fin'),año_fin=dpg.get_value('año_mp_fin')))

# Crear la ventana para CARGAR LOS INFORMES AUTOMÁTICOS AL OPERADOR
with dpg.window(tag='ventana_cargar_informe', label='Cargar Informe', width=400, height=200, show=False):
    dpg.add_text("CARGA DE INFORME")
    dpg.add_text('Ruta del archivo excel: ')
    dpg.add_button(tag='button_ruta_excel_ci', label='Buscar EXCEL', callback=lambda: dpg.show_item('file_dialog_id_ci'))


# Configuración y visualización del viewport
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("MainWindow", True)
dpg.start_dearpygui()
dpg.destroy_context()