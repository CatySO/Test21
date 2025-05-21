#Este metodo calcula la propina
def CalcularPropina(Total, Porc):
    return Total + (Total * Porc/100)
    
propina = int(input("Cuanto desea dejar de propina(10,15%): "))
total = CalcularPropina(1500, propina)

print(f"Debe pagar: {total}")