numero = int(input("Cual es el numero para dividir "))

checador = numero % 2

if numero == 0:
    print("No es ninguno")
elif numero == 2 or numero == -2:
    print("numero par y primo")
elif checador == 0:
    print("numero par")
else:
    print("numero primo")