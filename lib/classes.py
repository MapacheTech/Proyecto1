class estudiante():
    def __init__(self, matricula, apellidoNombre, edad):
        self.matricula = matricula
        self.apellidoNombre = apellidoNombre
        self.edad = edad
        self.calificacion = []
        pass
    
    def setCalificacion(self, calificacion):
        self.calificacion.append(calificacion)
        pass
    
    def promedio(self):
        pass
    
    def __str__(self):
        return
class estudianteGraduado(estudiante):
    def __init__(self, matricula, apellidoNombre, edad, fecha, tesis):
        super().__init__(matricula, apellidoNombre, edad)
        self.fecha = fecha
        self.tesis = tesis
        pass
    def chkGrad():
        
        pass
    
    
    pass
