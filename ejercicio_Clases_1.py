class Vehiculo:
    Color = None
    Ruedas = None
    Puertas = None
    
class Coche(Vehiculo):
    Velocidad = None
    Cilindrada = None

F = Coche()
F.Color = "Rojo"
F.Ruedas = 4
F.Puertas = 4
F.Velocidad = 220
F.Cilindrada = 800


print("Mi coche es de color", F.Color, "tiene", F.Ruedas,"ruedas y", F.Puertas,"Puertas y", F.Velocidad, "km/h y", F.Cilindrada, "CV")