import mercadopago

# Configura el cliente
sdk = mercadopago.SDK("APP_USR-6203695664524092-112018-b709425ad6bd583997aa19831a0688b9-477760037")

def obtener_transferencias(fecha_inicio, fecha_fin):
    transfers = []
    
    filtros = {
        "range": "date_created",
        "begin_date": fecha_inicio,
        "end_date": fecha_fin,
#        "status": "approved"  # Opcional: Solo transferencias aprobadas
    }
    
    response = sdk.payment().search(filters=filtros)
    

    for element in response['response']['results']:
        transfers.append(element)

    return transfers  # Aquí están las transferencias
    
transfers = obtener_transferencias('2024-11-14T00:00:00Z', '2024-11-22T23:59:59Z')



for transfer in transfers:
    try:
        print(transfer)
    except:
        print('No t.d.')
    print('\n')
    #print(transfer['payer']['identification']['number'] + str(transfer['transaction_amount']) + '\n')