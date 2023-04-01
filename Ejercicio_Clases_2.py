class alumno:
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def dar_datos(self):
        print("Nombre del alumno:", self.nombre)
        print("Nota del alumno:", self.nota)
        
    def aprobado(self):
        if self.nota >= 5 and self.nota <= 10:
            print(self.nombre, "ha aprobado con un", self.nota)
        elif self.nota < 5 and self.nota >= 0:
            print(self.nombre, "ha suspendido con un", self.nota)
        
x = alumno("Javier", 10)
x.dar_datos()
x.aprobado()