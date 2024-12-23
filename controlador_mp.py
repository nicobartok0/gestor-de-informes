import mercadopago
from mercadopago.config import RequestOptions
from movimiento import Transferencia
from datetime import datetime, timezone, timedelta
#from dotenv import load_dotenv, find_dotenv
import os


class Controlador_MP:
    def __init__(self) -> None:
        self.sdk = None
        self.id = None

    def cargar_sdk(self, api_key):
        self.sdk = mercadopago.SDK(api_key)
        request_options = RequestOptions(access_token=api_key)
        self.id = self.sdk.user().get(request_options)['response']['id']
        print(self.id)

    def obtener_transferencias(self, fecha_inicio, fecha_fin):
        transfers = []
        # Sacamos la fecha actual


        # 2024-11-28T15:35:18Z
        filtros = {
            "range": "date_created",
            #"begin_date": fecha_inicio,
            #"end_date": fecha_fin,
            "begin_date": fecha_inicio,
            "end_date": fecha_fin,
    #        "status": "approved"  # Opcional: Solo transferencias aprobadas
            'limit': 1000
        }
        
        response = self.sdk.payment().search(filters=filtros)
        
        for r in response['response']['results']:
            if r['operation_type'] == 'money_transfer':
                print(r)
                print('\n')


        for element in response['response']['results']:
            fecha = element['date_created'][:10]
            fecha_formato = fecha[8:] +'-' + fecha[5:7] + '-' + fecha[:4]
            mov = {
                    'tipo': '',
                    'fecha': fecha_formato,
                    'categoria': 'Transferencia MP',
                    'met_pago': 'Transferencia',
                    'monto': element['transaction_amount'],
                    'sector': 'ADMIN',
                    'obs': ''
                }
            if element['operation_type'] == 'regular_payment':
                mov['tipo'] = 'EGRESO'
            elif element['operation_type'] == 'account_fund':
                mov['tipo'] = 'INGRESO'
            elif element['operation_type'] == 'money_transfer':
                try:
                    if element['payer_id'] == self.id:
                        mov['tipo'] = 'EGRESO'
                except:
                    mov['tipo'] = 'INGRESO'
            elif element['operation_type'] == 'bank_transfer':
                try:
                    mov['tipo'] = 'INGRESO'
                except:
                    mov['tipo'] = 'EGRESO'
            
            else:
                mov['tipo'] = 'DESCONOCIDO'

            #if element['collector_id']:
            #    collector_id=element['collector_id']
            transfers.append(Transferencia(mov=mov, op_type=element['operation_type'], status=element['status']))

        return transfers  # Aquí están las transferencias