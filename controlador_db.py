import requests

class Controlador_DB:
    def __init__(self):
        self.API_ROUTE = 'http://127.0.0.1:5000/'
        self.proxies = {'https': 'http://127.0.0.1:5000'}

    def obtener_sucursales(self):
        req = f'{self.API_ROUTE}obtener_sucursales'
        response = requests.get(req, verify=False)
        return response.json()
    
    def añadir_movimientos(self, movimientos):
        #tipo, fecha, categoria, metodo_pago, monto, sucursal_fk, observacion
        data = []
        for movimiento in movimientos:

            mov_dict = {
                'tipo': movimiento.tipo,
                'fecha': f'{movimiento.fecha[6:]}-{movimiento.fecha[3:5]}-{movimiento.fecha[:2]}',
                'categoria': movimiento.categoria,
                'metodo_pago': movimiento.met_pago,
                'monto': movimiento.monto,
                'area': movimiento.sector,
                'observacion': movimiento.obs
            }
            data.append(mov_dict)
        req = f'{self.API_ROUTE}añadir_movimientos'
        response = requests.post(req, json=data)
        print(response)
        