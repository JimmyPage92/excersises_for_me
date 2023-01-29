from inspect import cleandoc
import sys

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#          print(a, end=' ')
#          a, b = b, a+b
#          print()
# fib(8)
#
# fruits = ['Banana', 'Apple', 'Lime']
# loud_fruits = [fruit.upper() for fruit in fruits]
# print(f'loud_fruits is',loud_fruits)
#
# for x,element in enumerate(fruits, start=1):
#     print(x, element)
#
#
# # List and the enumerate function
# list(enumerate(fruits))
# # [(0, 'Banana'), (1, 'Apple'), (2, 'Lime')]

# x = 0
# lista_liczb = []
# i = 0
# while x <= 4:
#     num = int(input('podaj liczbe: '))
#     i += num
#     print(i)
#     lista_liczb.append(i)
#     x += 1
#
# print(lista_liczb)

#od 0 do 200  podzielne przez 5 anie podzielne przez 7
# for i in range(201):
#     if i % 5 == 0 and i % 7 != 0:
#         print(f'liczba {i} jest podzielna przez 5 ale nie przez 7')

# names= ['michal', 'puszka', 'jeden', 'test', 'tester']
#
# name = input()
#
# if name=='michal':
#     print('masz dostep')
# else:
#     print('brak dostepu')

# ratings1 = {
#             "Arkadiusz": (2,1,2,3,2,3),
#             "Agnieszka": (4,2,1,3,4),
#             }
# #
# #
# for k,v in ratings1.items():
#     print(k)
#     print(v)
#     print()
#
# for key in ratings1:
#     print(f'{key} oceny {ratings1[key]}')


# people2 = [
#          {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
#          {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
#          {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}
#           ]
#
# for v in people2:
#     for k in v:
#         print(f'{k} : {v[k]}')
people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},
         }
#
# for key in people:
#     print(f'ID: {key}')
#     for seckey in people[key]:
#         print(f'{seckey}:{people[key][seckey]}')

# for k,v in people.items():
#     print(f'ID:{k}')
#     for k2 in v:
#         print(f'{k2}: {v[k2]}')

# cleandoc('''
# program do dodawania nowych definicji
# szukac istniejacych definicji
# usuwac wybrane definicje
# ''')
#
# program = {}
#
# # print('1: Dodaj definicje')
# # print('2: znajdz definicje')
# # print('3: usun definicje')
# # print('4: zakoncz- wyjscie  zprogramu')
# #
# # wybor_usera = int(input('co cchesz zrobic?? wcisnij liczbe od 1 do 4'))
# while True:
#         print('1: Dodaj definicje')
#         print('2: znajdz definicje')
#         print('3: usun definicje')
#         print('4: zakoncz- wyjscie  zprogramu')
#
#         wybor_usera = int(input('co cchesz zrobic?? wcisnij liczbe od 1 do 4'))
#         if wybor_usera == 1:
#                 definicja = input("Podaj definicje ktora chcesz dodac do slownika")
#                 wyjasnienie = input('wyjasnij definicje ktora chcesz dodac do slownika')
#                 program.update({definicja:wyjasnienie})
#                 print(program)
#         elif wybor_usera == 2:
#                 szukany_klucz = input('Wybierz definicje ktora chcesz znalesc')
#                 if szukany_klucz in program:
#                         print(f'Szukana definicja to: {program[szukany_klucz]}')
#                 else:
#                         print(f'nie znaleziono takiej definicji {szukany_klucz}')
#         elif wybor_usera == 3:
#                 definicja_do_usuniecia = input('Wybierz definicje do usuniecia z programu')
#                 program.pop(definicja_do_usuniecia)
#                 print(f'Usunales: {definicja_do_usuniecia}')
#         elif wybor_usera == 4:
#                 print('Wychodzimy z propgramu')
#                 sys.exit()
#         else:
#                 print('podales zle dane - sproboj jeszcze raz')

# liczby = [1, 2, 3, 4, 5, 6]
#
#
# potegi_dwojki = [e**2
#                  for e in liczby
#                  ]
# print(potegi_dwojki)
#
# liczbyparzyste = [e
#                   for e in liczby
#                   if (e % 2 == 0)
#                   ]
# print(liczbyparzyste)

# evennumbers = [num for num in range(400) if (num % 2==0)]
# print(f'{evennumbers}')
#
# evengennumbers = (num for num in range(400) if (num % 2==0))
# print(evengennumbers)
# print(sum(evengennumbers))
# print(sys.getsizeof(evennumbers))
# print(sys.getsizeof(evengennumbers))
# for item in evengennumbers:
#     print(item)

# names = {"Arkadiusz", "Wioletta", "Karol", "Bartłomiej", "Jakub", "Ania"}
#
# nameslenght = {
#     name: len(name)
#     for name in names
#     if name.startswith('A')
# }
#
# print(nameslenght)
#
# celsius = {'t1':-20,'t2':-15, 't3':0, 't4':12, 't5':24}
#
# fahrenheit = {
#     k : temp * 1.8 + 32
#     for k,temp in celsius.items()
#     if temp > -5
#     if temp < 20
# }
#
# print(fahrenheit)

# names = {"arkadiusz", "Wioletta", "karol", "bartłomiej", "Jakub", "Ania"}
#
# names_ = {
#     name.capitalize()
#     for name in names
# }
#
# print(names_)

# cleandoc(
#     """"
# liczby od 100 do 470 ktore sa podzielne przez 7 ale nie sa podzielne przez 5
# """""
# )
#
# numsgenerator = [
#     num
#     for num in range(100, 471)
#     if num % 7 == 0
#     if num % 5 != 0
# ]
# #
# # for num in numsgenerator:
# #     print(num)
#
# print(numsgenerator)
import math
cleandoc("""
Stwórz menu, z którego użytkownik, może wybrać opcje, aby policzyć powierzchnie figur:
1) prostokąta
2) kwadratu
3) trójkąta
4) trapezu
5) koła
Pamiętaj, by skorzystać z funkcji.
""")

# def pole_prostokąta(a,b):
#     return a * b
# def pole_kwadratu(a):
#     return a**2
# def pole_trojkata(a,h):
#     return 0.5* a * h
# def pole_kola(r):
#     return 3.14 * r ** 2
# def pole_trapezu(a,b,h):
#     return (0.5 * (a+b)) * h
#
#
# x= pole_trapezu(2,5,2)
# print(x)
# a = pole_kola(3)
# print(a)
# b =pole_trojkata(4,4)
# print(b)


"""
Napisz funkcję,
która jako argument przyjmuje listę liczb 
i zwraca sumę wszystkich liczb dodatnich na liście. 
Funkcja powinna ignorować wszelkie liczby ujemne lub zera na liście.
"""

# def suma_liczb(numbers):
#     return sum([num for num in numbers if num > 0])
#
# numbers = [1,-5,2,4,-10,20]
#
# x = suma_liczb(numbers)
# print(x)
import random
# x = 0
# while x < 100:
#     a = random.randint(0,100)
#     print(a)
#     x +=1

# def czy_uderzysz_przeciwnika(percent_probably_to_hit):
#     weapon_hit = random.randint(0,100)
#     if weapon_hit <= percent_probably_to_hit:
#         return 'hit'
#     else:
#         return 'not hit'
#
# # x = czy_uderzysz_przeciwnika(50)
# # print(x)
# listhit = []
# a=0
# while a < 100:
#     listhit.append(czy_uderzysz_przeciwnika(50))
#     a += 1
#
# # print(listhit)
# # print(listhit.count('hit'))
# # print(listhit.count('not hit'))
# from collections import Counter
#
# dicthit = Counter(listhit)
# print(dicthit)

# movieList = ["Tytuł1", "Tytuł2", "Tytuł3", "Tytuł4"]
# # print(random.choice(movieList))
# event = ['wygrana', 'smierc', 'przegrana', 'utratas zlota' , 'losowa rzecz']
# nagroda = ['zielona', 'pomaranczowa', 'purpurowa', 'legendarna']
# from collections import Counter
# print(Counter(random.choices(nagroda,[80,15,4,1], k=100)))
#
#
# cardList = [ "9", "9", "9", "9",
#              "10", "10", "10", "10",
#              "Jack", "Jack", "Jack", "Jack",
#              "King", "King", "King", "King",
#              "Queen", "Queen", "Queen", "Queen"
#              "Ace", "Ace", "Ace", "Ace",
#              "Joker", "Joker"
#            ]
#
# random.shuffle(cardList)
# print(cardList)

"""Napisz funkcję, która zasymuluje jak działa 
Lotto tzn. wybierze 6 unikalnych liczb z 49."""
# def lotto():
#     print(random.sample(range(1,50), 6))
#
# a = lotto()

# from enum import Enum
# event = Enum('Event', ['Skrzynia', 'Pusty'])
#
# eventDict = {
#             event.Skrzynia : 0.6,
#             event.Pusty : 0.4,
# }
# evenList = list(eventDict.keys())
# evenList_probability = list(eventDict.values())
#
# kolory = Enum('Kolory',{'Green': 'zielony',
#                         'Orange' : 'pomaranczowy',
#                         'Purple': 'fioletowy',
#                         'Gold' : 'zloty'
#                         }
#               )
#
# probability_kolory = {
#     kolory.Green : 0.60,
#     kolory.Orange : 0.20,
#     kolory.Purple : 0.15,
#     kolory.Gold : 0.05
# }
# coloursList = list(probability_kolory.keys())
# coloursList_probability = list(probability_kolory.values())
#
# nagrodazaskrzynke = {
#             coloursList[reward]: (reward+1) * (reward+1) * 1000
#             for reward in range(len(coloursList))
# }
#
# gameLenght = 5
#
# sumanagrodgracza = 0
# while gameLenght > 0:
#     gamer_response = input('Do you wanna move forward?')
#     if gamer_response == 'yes':
#         print('ok sprawdzmy co masz')
#         drawnEvent = random.choices(evenList,evenList_probability)[0]
#         if (drawnEvent == event.Skrzynia):
#             print('wylosowales skrzynke')
#             drawnkolor = random.choices(coloursList,coloursList_probability)[0]
#             print(drawnkolor.value)
#             nagrodagracza = nagrodazaskrzynke[drawnkolor]
#             print(f'w tej rundzie zdobyles {nagrodagracza}')
#             sumanagrodgracza = sumanagrodgracza+nagrodagracza
#         elif drawnEvent == event.Pusty:
#             print('wylosowales nic')
#     else:
#         print('mozesz chodzic tylko do prostu')
#         continue
#
#     gameLenght -= 1
#
# print(f'zdobyles {sumanagrodgracza} punktow')

"""

JSON

"""
# import json
#
# film = {
#     'title': 'Ale ja nie będę tego robil!',
#     'release_year' : 1969,
#     'won_oscar' : True,
#     'actors' : ('Michał','Marlena'),
#     'budget' : None,
#     'credits' : {
#         'director' : 'Michał',
#         'writer' : 'Marlena',
#         'animator' : 'marcin'
#     }
# }
#
# x = json.dumps(film, ensure_ascii=False, indent=4,)
#
# with open('przyklad.json', 'w', encoding='UTF-8') as file:
#     json.dump(film, file, ensure_ascii=False, indent=4)
# print(x)
#
# with open('file.json', encoding='UTF-8') as file:
#     x = json.load(file)
#
# # print(json.dumps(x,indent=4, sort_keys=True))
#
# import pprint
# pprint.pprint(x, indent=4)

# with open('oceany.txt', 'a', encoding="UTF-8") as file:
#     file.write('\ntest')
#     print(file.tell())

# x = []
# with open('imionanazwiska.txt', 'r',encoding="UTF-8" ) as file:
#         for line in file:
#                 x.append(tuple(line.replace('\n', "").split(' ')))
# print(x)
#
# with open('imiona.txt', 'w',encoding="UTF-8" ) as file:
#         for item in x:
#                 file.write(item[0] + '\n')
#
# with open('nazwiska.txt', 'w',encoding="UTF-8" ) as file:
#         for item in x:
#                 try:
#                         file.write(item[1] + '\n')
#                 except IndexError:
#                         file.write('\n')

cleandoc("""Stwórz funkcję, która obsługuje otwieranie pliku do wczytywania danych.
Zapytaj się użytkownika o nazwę pliku, który chce otworzyć do wczytania.
Jeśli plik nie istnieje wypisz mu odpowiedni komunikat.
Jeśli plik istnieje wczytaj całą jego zawartość i zwróć jako wynik funkcji.
Podpowiedź: skorzystaj z wiedzy dotyczącej obsługi wyjątków z poprzedniej lekcji:
except FileNotFoundError:""")

def open_file_to_read_data(path):
        try:
                with open(path, 'r',encoding="UTF-8") as file:
                        print(file.read())
        except FileNotFoundError:
                print('Nie znaleziono takiego pliku')

ask_about_name_file = input('Podaj nazwe pliku jaka cchesz otworzyc: ')

file_name = open_file_to_read_data(ask_about_name_file)

cleandoc("""
1) Napisz kod, który sprawdzi, jak często słowo "kot" występuje w pliku "tekst.txt".
Dane wejściowe:
Ścieżka do pliku: "tekst.txt"
Słowo do wyszukania: "kot"
Dane wyjściowe:
Liczba wystąpień słowa "kot" w pliku "tekst.txt":
Przykład:
Jeśli w pliku "tekst.txt" znajduje się tekst "Kot jest bardzo fajnym zwierzęciem", to kod powinien wyświetlić "Słowo 'kot' wystąpiło 1 razy w pliku 'tekst.txt'."
Wskazówki:
Otwórz plik w trybie odczytu i za pomocą metody count zlicz wystąpienia słowa w całym pliku.
Wyświetl wynik za pomocą instrukcji print.
2) Pamiętaj o obsłudze wyjątków!
FileNotFoundError występuje, gdy plik o podanej ścieżce nie zostanie znaleziony.
PermissionError występuje, gdy brak jest uprawnień do odczytu pliku.
3) Gdy wypiszesz dane skorzystaj z formatted stringa
Przykład:
imie = "Jan"
wiek = 30
print(f"Cześć, nazywam się {imie} i mam {wiek} lat.")  # wyświetli "Cześć, nazywam się Jan i mam 30 lat."
"f" na początku ciągu znaków oznacza, że jest to tzw. f-string (ang. formatted string).
F-string to nowa wersja ciągów znaków w Pythonie, która pozwala na szybkie i łatwe formatowanie ciągów znaków za pomocą zmiennych i wyrażeń.
F-string pozwala na oszczędzenie czasu i linii kodu, ponieważ nie trzeba już używać operatora "+" do połączenia ciągów znaków ze zmiennymi.
Uwaga: f-string dostępny jest od Python 3.6. Jeśli używasz starszej wersji Pythona, możesz użyć operatora "+" do formatowania ciągów znaków.
""")