class Movimiento:
    def __init__(self, mov:dict) -> None:
        self.tipo = mov['tipo']
        self.fecha = mov['fecha']
        self.categoria = mov['categoria']
        self.met_pago = mov['met_pago']
        self.monto = mov['monto']
        self.sector = mov['sector']
        self.obs = mov['obs']

class Transferencia(Movimiento):
    def __init__(self, mov: dict, op_type, status) -> None:
        super().__init__(mov)
        self.op_type = op_type
        self.status = status
        self.collector_id = ''
        self.collector_nombre = ''