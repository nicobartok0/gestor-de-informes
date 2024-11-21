import mercadopago

# Configura el cliente
sdk = mercadopago.SDK("---")

def obtener_transferencias(fecha_inicio, fecha_fin):
    transfers = []
    
    filtros = {
        "range": "date_created",
        "begin_date": fecha_inicio,
        "end_date": fecha_fin,
        "status": "approved"  # Opcional: Solo transferencias aprobadas
    }
    
    response = sdk.payment().search(filters=filtros)
    

    for element in response['response']['results']:
        transfers.append(element)

    return transfers  # Aquí están las transferencias
    
transfers = obtener_transferencias('2024-11-14T00:00:00Z', '2024-11-20T23:59:59Z')



for transfer in transfers:
    try:
        print(transfer)
    except:
        print('No t.d.')
    print('\n')
    #print(transfer['payer']['identification']['number'] + str(transfer['transaction_amount']) + '\n')