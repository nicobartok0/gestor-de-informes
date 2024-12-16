class Selector:
    def __init__(self):
        self.tabla_actual = 'DEFAULT'
    
    def get_tabla_actual(self):
        return self.tabla_actual
    
    def set_tabla_actual(self, tabla:str):
        self.tabla_actual = tabla