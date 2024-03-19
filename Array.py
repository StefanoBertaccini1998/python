import math
import math as mt
import numpy as np
import pandas as pd

matrix = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]

mat_array = np.array(matrix)

# print("Index", mat_array[0, :])

# print("Seconda riga", mat_array[-2, :])

# print("Step di 2", mat_array[-2, 0::2])
# print("Step di 2 senza numpy", matrix[-2][::2])

# .sin() .cos() .factorial()
# .pi
# narray = np.array(matrix)
# print(mt.sin(90))
# print("SIN di 90",mt.sin(math.pi/2),"COS di 90",mt.cos(math.pi/2),"SIN di 180",mt.sin(math.pi),"COS di 180",mt.cos(math.pi))
# factorial
# print(mt.factorial(9))
# print(math.degrees(math.pi))

lst = [2000, 5500, 7200, 4320, 1280, 1900, 2500, 3900, 6410, 8150, 7100, 5350]

lst = np.array(lst)

# qual è stata la vendita massima mensile?
# print("Max:", lst.max())

# E quella minima?
# print("min:", lst.min())

# quali sono le vendite mensili maggiori di 4999 oggetti?

filter_4999 = lst[lst > 4999]

# print("Maggiori di 4999", filter_4999)

# E quante ne sono?

# print("Quanti sono:", len(filter_4999))

# quali sono le vendite minori di 3000 oggetti?

filter_3000 = lst[lst < 3000]

# print("Minori di 3000", filter_3000)

# E quante ne sono?

# print("Quanti sono:", len(filter_3000))

# E quella media?
# print("Media al mese arrotondata a 2 cifre", round(lst.mean(), 2))

# Dizionario
fatturati_dict = {1997: 12_000, 1998: 15_000, 1999: 20_000, 2000: 23_000, 2001: 25_000, 2002: 17_000, 2003: 14_000,
                  2004: 21_000}

# Serie Pandas
fatturati_series = pd.Series([12_000, 15_000, 20_000, 23_000, 25_000, 17_000, 14_000, 21_000], index=range(1997, 2005))

# Accesso tramite chiave x, restituisce y {x:y}
# print("Tipo di valore del dizionario", type(fatturati_dict[1997]))

# print("Tipo di valore della serie pandas", type(fatturati_series[1997]))

# print("Massimo della serie", fatturati_series.max())
# print("Between\n", fatturati_series[fatturati_series.between(15_000, 20_000)])

stipendi = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])

# print(stipendi)

# Raddoppiare gli stipendi tramite un ciclo for
lista_stipendi_raddoppiati = []
lista_stipendi_raddoppiati_numpy = []

# print(stipendi[1])

for stipendio in stipendi:
    lista_stipendi_raddoppiati.append(stipendio * 2)

# List comprehension
# lista_stipendi_raddoppiati_com = [stipendio * 2 for stipendio in stipendi]

# print("Lista stipendi raddoppiati for\t\t", lista_stipendi_raddoppiati)
# print("Lista stipendi raddoppiati", lista_stipendi_raddoppiati_com)

lista_stipendi_raddoppiati_numpy = stipendi * 2

# print("Lista stipendi raddoppiati masking\t", lista_stipendi_raddoppiati_numpy)

# Ciclo for in range

for x in range(0, 10, 2):
    print(list(range(x, 0, -1)))

libri = ["enciclopedia", "atlante", "dizionario", "enciclopedia"]

for libro in libri:
    print(libro)

for contatore, libro in enumerate(libri):
    print(contatore, libro)

alunni = ["Lucio", "Silvio", "Michela", "Natalia"]
corsi = ["ingegneria", "medicina", "cinema", "giurisprudenza"]
anni = [19, 22, 25, 21]

for alunno, corso, eta in zip(alunni, corsi, anni):
    print(alunno, "frequenta", corso, "e ha", eta, "anni.\n")

nomi = ['Anna', 'Bruno', 'Carla']
eta = [28, 34, 29]

persone = zip(nomi, eta)
# Converti l'iteratore in una lista di tuple
lista_persone = list(persone)
print(lista_persone)

for nome, eta in zip(nomi, eta):
    print(f"{nome} ha {eta} anni.")

