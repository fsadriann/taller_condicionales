# programa para realizar un préstamo bancario

#input

ingresos = int(input("¿Cuáles son sus ingresos actuales?: "))


#processing

if ingresos>945200:
    deuda = int(input("¿Tiene alguna deuda actualmente?: "))
    if deuda == 0:
        rta = "el prestamo es aprobado"
    else:
        rta = "el prestamo no es aprobado"
else:
    rta = "el prestamo no es aprobado"

#output

print(rta)