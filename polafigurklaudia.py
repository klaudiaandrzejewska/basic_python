# 1.Pierwsze linia to prośba o podanie rodzaju figury: (1 kwadrat| 2 prostokąt|3 trojkat| 4 koło)
# 2.kolejne linie inputu mają pobierać odpowiednie informacje zalenze od figury (np jesli wybrana figura to bedzie
# kwadrat, kolejne linie musze zapytac o dlugosc a i dlugosc b, jesli wybrana figura to koło: program ma prosic o promien koła).
#  Program ma tak dlugo pytać uzytkownika o wpisanie poprawnych wartości aż będą one poprawne.
# 3. wyprinotować wynik pola podanej figrtuy
import math


def kwa():
    while True:
        try:
            a = float(input('Dlugosc boku kwadratu: '))
            if a > 0:
                return a * a
            else:
                print('Zła wartość. Spróbuj ponownie!')
        except:
            print('Zła wartość. Spróbuj ponownie!')


def pro():
    while True:
        try:
            a = float(input('Dlugosc pierwszego boku prostokata: '))
            b = float(input('Dlugosc drugiego boku prostokata: '))
            if a and b > 0:
                return a * b
            else:
                print('Zła wartość. Spróbuj ponownie!')
        except:
            print('Zła wartość. Spróbuj ponownie!')


def tra():
    while True:
        try:
            a = float(input('Dlugosc pierwszej podstawy trapezu: '))
            b = float(input('Dlugosc drugiej podstawy trapezu: '))
            h = float(input('Wysokosc trapezu: '))
            if a and b and h > 0:
                return (a + b) * h / 2
            else:
                print('Zła wartość. Spróbuj ponownie!')
        except:
            print('Zła wartość. Spróbuj ponownie!')


def koło():
    while True:
        try:
            r = float(input('Długość promienia koła:'))
            if r > 0:
                return math.pi * (r ** 2)
            else:
                print('Zła wartość. Spróbuj ponownie!')
        except:
            print('Zła wartość. Spróbuj ponownie!')


def rom():
    while True:
        try:
            a = float(input('Dlugosc podstawy rombu: '))
            h = float(input('Wysokosc rombu: '))
            if a and h > 0:
                return a * h
            else:
                print('Zła wartość. Spróbuj ponownie!')
        except:
            print('Zła wartość. Spróbuj ponownie!')


while True:
    print('Program do liczenia powierzchni figur plaskich')
    print('\n')
    print('Wybierz figure:')
    print('[1] kwadrat')
    print('[2] prostokat')
    print('[3] trapez')
    print('[4] romb')
    print('[5] koło')
    print('[0] koniec')
    odp = int(input('Wybór: '))
    if (odp == 1):
        print('Pole:', kwa())
    elif (odp == 2):
        print('Pole:', pro())
    elif (odp == 3):
        print('Pole:', tra())
    elif (odp == 4):
        print('Pole:', rom())
    elif (odp == 5):
        print('Pole:', koło())
    else:
        break
    print('---')
