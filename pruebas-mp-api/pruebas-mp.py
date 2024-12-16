import mercadopago
from datetime import datetime, timezone
from dotenv import load_dotenv, find_dotenv
import os



# Cargamos el .env
load_dotenv()

# Configura el cliente
sdk = mercadopago.SDK(os.getenv('API_KEY'))

# Sacamos la fecha actual
tiempo_actual = datetime.now(timezone.utc)
fecha_transferencia = tiempo_actual.strftime('%Y-%m-%dT%H:%M:%SZ')

# Definimos la función para obtener las transferencias
def obtener_transferencias(fecha_inicio, fecha_fin):
    transfers = []
    
    filtros = {
        "range": "date_created",
        "begin_date": fecha_inicio,
        "end_date": fecha_fin,
#        "status": "approved"  # Opcional: Solo transferencias aprobadas
    }
    
    response = sdk.payment().search(filters=filtros)
    
    print(response)

    
    for element in response['response']['results']:
        transfers.append(element)

    return transfers  # Aquí están las transferencias
    
# Obtenemos las transferencias con la función creada anteriormente
transfers = obtener_transferencias('2024-11-14T00:00:00Z', fecha_transferencia)


# Mostramos todas las transferencias
for transfer in transfers:
    try:
        print(transfer)
    except:
        print('No t.d.')
    print('\n')
    #print(transfer['payer']['identification']['number'] + str(transfer['transaction_amount']) + '\n')
