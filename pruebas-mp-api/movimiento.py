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
    def __init__(self, mov: dict, status, refunded, refunded_amount) -> None:
        super().__init__(mov)
        self.status = status
        self.refunded = refunded
        self.refunded_amount = refunded_amount