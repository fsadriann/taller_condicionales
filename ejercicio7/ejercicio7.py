# Programa para determinar si dados tres números enteros, la suma de los dos primeros es igual al tercero.

a = int(input("ingrese el valor de a: "))
b = int(input("ingrese el valor de b: "))
c = int(input("ingrese el valor de c: "))

# processing

p1 = a + b
p2 = a + c
p3 = b + c

if p1==c:
    resultado = c, "es la suma de" ,a, "y" ,b
else:
    if p2==b:
        resultado = b, "es la suma de" ,a,"y",c,
    else:
        if p3==a:
            resultado = a, "es la suma de" ,b, "y" ,c
        else:
            resultado =("ninguna es suma de los otros dos")

# output

print(resultado)