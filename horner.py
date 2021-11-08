try:
    stopien = int(input("podaj stopień wielomianu: "))

    czynniki_wielomianu = [
        int(input(f"podaj czynnik przy potędze {-i}: ")) for i in range(-stopien, 1)]

    liczba_zerująca = int(input("podaj liczbe zerującą: "))

except ValueError:
    from sys import exit
    print("Podana wartość nie jest liczbą")
    exit(0)

wyniki = [czynniki_wielomianu[0]]

print("\nOdpowiedzi: ")
for i in range(1, len(czynniki_wielomianu)):

    wynik_czynnik = liczba_zerująca*wyniki[i-1]+czynniki_wielomianu[i]

    wyniki.append(wynik_czynnik)

for i in range(-len(wyniki), -1):
    print(f"wspołczynnik przy potędze {abs(i+2)}: {wyniki[i]}")

print(f"reszta: {wyniki[-1]}")
