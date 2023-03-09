# Ejercicio 4

#input

peso = int(input("Digite el peso: "))
altura = float(input("Digite la altura: "))

imc = peso/altura**2

if imc < 16:
    msj = "criterio de ingreso al hospital"
else:
    if imc < 17:
        msj = "infrapeso"
    else:
        if imc > 18:
            msj = "bajo peso"
        else:
            if imc < 25:
                msj = "peso normal (saludable)"
            else:
                if imc < 30:
                    msj = "sobrepeso (obesidad grado 1)"
                else:
                    if imc<35:
                        msj = "sobrepeso crónico (obesidad grado 2)"
                    else:
                        if imc<40:
                            msj = "obesidad premórbida (obesidad grado 3)"
                        else:
                            if imc > 40:
                                msj = "obesidad mórbida (obesidad grado 4)"
                            else:
                                msj = "obesidad mórbida (obesidad grado 4)"

# output

print("su índice de peso es " + str(imc))
print(msj)