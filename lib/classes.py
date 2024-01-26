class estudiante():
    def __init__(self, matricula, apellidoNombre, edad):
        self.matricula = matricula
        self.apellidoNombre = apellidoNombre
        self.edad = edad
        self.calificacion = []
        pass
    
    
    def setCalificacion(self, calificacion):
        self.calificacion.append(calificacion)
        return calificacion
    
    def promedio(self):
        promedio = sum(self.calificacion)/len(self.calificacion)
        return promedio
    
    def __str__(self):
        return f"Matricula: {self.matricula}\nNombre: {self.apellidoNombre}\nEdad: {self.edad}\nCalificaciones: {self.calificacion}"
class estudianteGraduado(estudiante):
    def __init__(self, matricula, apellidoNombre, edad, fecha, tesis):
        super().__init__(matricula, apellidoNombre, edad)
        self.fecha = fecha
        self.tesis = tesis
        pass
    def chkGrad(self):
        promedio = self.promedio()
        if promedio <= 7:
            print("\033[31m"+ str(promedio) + "\033[0m")
        else:
            print(promedio)
        pass
    

