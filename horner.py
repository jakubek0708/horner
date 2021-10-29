try: 
    stopien = int(input("podaj stopień wielomianu: "))

    czynniki_wielomianu = [int(input(f"podaj czynnik przy potędze {-i}: ")) for i in range(-stopien, 1)]

    liczba_zerująca = int(input("podaj liczbe zerującą: "))
    
except ValueError: 
    from sys import exit 
    print("Podana wartość nie jest liczbą")
    exit(0)

nowy_czynniki = [czynniki_wielomianu[0]]

print("\n Odpowiedzi: ")
for i in range(1, len(czynniki_wielomianu)):

    wynik_czynnik = liczba_zerująca*nowy_czynniki[i-1]+czynniki_wielomianu[i]

    nowy_czynniki.append(wynik_czynnik)

for i in range(-len(nowy_czynniki), -1):
    print(f"wspołczynnik przy potędze {abs(i+2)}: {nowy_czynniki[i]}")

print(f"reszta: {nowy_czynniki[-1]}")
