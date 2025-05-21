def Convertir(fahrenheit):
    Celsius = (fahrenheit - 32)/1.8
    Kelvin = Celsius + 273.15
    return Celsius, Kelvin
    
fahrenheit = int(input("Ingrese los grados fahrenheit a Convertir: "))
C,K = Convertir(fahrenheit)
print(f"{fahrenheit}°F es igual a: {C}°C y {K}°K")

def ConvertirCK(fahrenheit, tipo):
    Celsius = (fahrenheit - 32)/1.8
    Kelvin = Celsius + 273.15
    if tipo == 1:
        return Celsius
    else:
        return Kelvin
        
fahrenheit = int(input("Ingrese los grados fahrenheit a Convertir: "))
opcion = int(input("Ingrese la opción deseada: \n 1.- Convertir a Celsius \n 2.- Convertir a Kelvin\n"))
if opcion == 1:
    Conversion = ConvertirCK(fahrenheit, 1)
    print(f"{fahrenheit}°F es igual a: {C}°C")
else:
    Conversion = ConvertirCK(fahrenheit, 2)
    print(f"{fahrenheit}°F es igual a: {K}°K")
    
    