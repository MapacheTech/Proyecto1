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
        ZeroDivisionError
        try:
            promedio = sum(self.calificacion)/len(self.calificacion)
        except Exception as e:
            print(f"Error: {e}")    
        return promedio
    
    def __str__(self):
        return f"Matricula: {self.matricula} Nombre: {self.apellidoNombre} Edad: {self.edad} Calificaciones: {self.calificacion}"
class estudianteGraduado(estudiante):
    def __init__(self, matricula, apellidoNombre, edad):
        super().__init__(matricula, apellidoNombre, edad)
        pass
    def chkGrad(self):
        promedio = self.promedio()
        graduado = ""
        if promedio <= 5.9:
            graduado = "No"
        else:
            graduado = "Si"
        return graduado
    
    def setFecha(self, fecha):
        self.fecha = fecha
        return fecha
    
    def chckFecha(self):
        promedio = self.promedio()
        
        fechaGrad = ""
        if promedio <= 5.9:
            fechaGrad = "N/A"
        else:
            fecha = self.fecha
            fechaGrad = fecha
        return fechaGrad
    
    def setTesis(self, tesis):
        self.tesis = tesis
        return tesis
    
    def chckTesis(self):
        promedio = self.promedio()
        
        tesisGrad = ""
        if promedio <= 5.9:
            tesisGrad = "N/A"
        else:
            tesis = self.tesis
            tesisGrad = tesis
        return tesisGrad
    
    def __str__(self):
        promedio = self.promedio()
        if promedio <= 5.9:
            return f"Matricula: {self.matricula} Nombre Completo: {self.apellidoNombre} Edad: {self.edad} Estudiante No Graduado"
        else:
            return f"Matricula: {self.matricula} Nombre Completo: {self.apellidoNombre} Edad: {self.edad} Graduado el: {self.fecha} Con la Tesis: {self.tesis}"