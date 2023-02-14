file_name = 'cumparaturi.txt'


class Cumparaturi:
    def __init__(self, id_cumpar, id_produs1, cant1, id_produs2, cant2, id_produs3, cant3, sum):
        self.id_cumpar = id_cumpar
        self.id_produs1 = id_produs1
        self.cant1 = cant1
        self.id_produs2 = id_produs2
        self.cant2 = cant2
        self.id_produs3 = id_produs3
        self.cant3 = cant3
        self.sum = sum

    def __str__(self):
        return str(self.id_cumpar) + ' ' + str(self.id_produs1) + ' ' + str(self.cant1) + ' ' + str(self.id_produs2) + ' ' + str(self.cant2) + ' ' + str(self.id_produs3) + ' ' + str(self.cant3) + ' ' + str(self.sum)

    def __lt__(self, other):
        if self.sum > other.sum:
            return True
        else:
            return False


def citire_fis():
    list.clear()
    f = open(file_name)
    for line in f:
        sir = line.split(' ')
        cumpar = Cumparaturi(str(sir[0]), str(sir[1]), int(sir[2]), str(sir[3]), int(sir[4]), str(sir[5]), int(sir[6]), float(sir[7]))
        list.append(cumpar)
    print('Lista cumparaturilor a fost incarcata din fisier in program!')
    f.close()


def scriere_fis():
    f = open(file_name, 'w')
    for cumpar in list:
        f.write(str(cumpar.id_cumpar) + ' ' + cumpar.id_produs1 + ' ' + cumpar.cant1 + ' ' + str(cumpar.id_produs2) + ' ' + str(cumpar.cant2) + ' ' + str(cumpar.id_cumpar3) + ' ' + str(cumpar.cant3) + ' ' + str(cumpar.sum) + '\n')
    f.close()


def afis_fis():
    print(
        'Lista cumparaturilor (id_cumpar; id_produs1; cant1; id_produs2; cant2; id_produs3; cant3: ')
    for cumpar in list:
        print(cumpar)


def add_cumpar():
    f = open(file_name, 'a')
    id_cumpar = str(input('Introduceti id-ul cumparaturii: '))
    id_produs1 = input('Introduceti id-ul primului produs: ')
    cant1 = str(input('Introduceti cantitatea primului produs: '))
    id_produs2 = str(input('Introduceti id-ul produsului cu numarul 2: '))
    cant2 = int(input('Introduceti cantitatea produsului numarului 2: '))
    id_produs3 = str(input('Introduceti id-ul produsului cu numarul 3: '))
    cant3 = str(input('Introduceti cantitatea produsului cu numarul 3: '))
    sum = float(input('Introduceti suma totala a cumparaturii: '))
    f.write('\n' + str(id_cumpar) + ' ' + str(id_produs1) + ' ' + str(cant1) + ' ' + str(id_produs2) + ' ' + str(cant2) + ' ' + str(id_produs3) + ' ' + str(cant3) + ' ' + str(sum))
    f.close()
    print('Cumparatura a fost adaugat in fisier cu succes!')


def exista(id_cumpar):
    f = open(file_name)
    for line in f:
        sir = line.split(' ')
        if id_cumpar == str(sir[0]):
            f.close()
            return True
    f.close()
    return False


def elim_cumpar():
    f = open(file_name)
    g = open('temp.txt', 'w')
    id_cumpar = str(input('Introduceti id-ul cumparaturii, care va fi eliminat: '))
    if exista(id_cumpar):
        for line in f:
            sir = line.split(' ')
            if id_cumpar != str(sir[0]):
                g.write(line)
        f.close()
        g.close()
        f = open(file_name, 'w')
        g = open('temp.txt', 'r')
        for line in g:
            f.write(line)
        f.close()
        g.close()
        print('Produsul cu id-ul ', id_cumpar, ' a fost sters din fisier cu succes!')
    else:
        print('Asa student nu exista!')


def modif_cumpar():
    f = open(file_name)
    g = open('temp.txt', 'w')
    id_cumpar = str(input('Introduceti id-ul cumparaturii, datele caruia vor fi modificate: '))
    if exista(id_cumpar):
        for line in f:
            sir = line.split(' ')
            if id_cumpar != str(sir[0]):
                g.write(line)
            else:
                id_cumpar = str(input('Introduceti id-ul cumparaturii: '))
                id_produs1 = str(input('Introduceti id-ul produsului cu numarul 1: '))
                cant1 = int(input('Introduceti cantitatea produsului cu numarul 1: '))
                id_produs2 = str(input('Introduceti id-ul produsului cu numarul 2: '))
                cant2 = int(input('Introduceti cantitatea produsului cu numarul 2: '))
                id_produs3 = str(input('Introduceti id-ul produsului cu numarul 3: '))
                cant3 = int(input('Introduceti cantitatea produsului cu numarul 3: '))
                sum = float(input('Introduceti suma totala a cumparaturii: '))
                g.write(str(id_cumpar) + ' ' + str(id_produs1) + ' ' + str(cant1) + ' ' + str(id_produs2) + ' ' + str(cant2) + ' ' + str(id_produs3) + ' ' + str(cant3) + ' ' + str(sum) + '\n')
        f.close()
        g.close()
        f = open(file_name, 'w')
        g = open('temp.txt', 'r')
        for line in g:
            f.write(line)
        f.close()
        g.close()
        print('Datele studentului cu numarul ', id_cumpar, ' au fost actualizate in fisier cu succes!')
    else:
        print('Asa student nu exista!')


def sum_max():
    cumparSumMax = list[0]
    for cumpar in list:
        if cumpar.sum > cumparSumMax.sum:
            cumparSumMax = cumpar
    print('Cumparatura cu suma maxima are pretul', cumparSumMax.sum)


def sum_min():
    cumparSumMin = list[0]
    for cumpar in list:
        if cumpar.sum < cumparSumMin.sum:
            cumparSumMin = cumpar
    print('Cumparatura cu suma minima are pretul ', cumparSumMin.sum)


def menu():
    print('Citire din fisier..........1')
    print('Afisare cumparaturi...........2')
    print('Adaugare cumparaturi..........3')
    print('Eliminare cumparaturi..........4')
    print('Modificare cumparaturi..........5')
    print('Suma medie maxima..........6')
    print('Suma medie minima..........7')
    print('Inchiderea programului..........0')
    m = int(input())
    return m


m = 1
list = []
while m != 0:
    m = menu()
    if m == 1:
        citire_fis()
    elif m == 2:
        afis_fis()
    elif m == 3:
        add_cumpar()
    elif m == 4:
        elim_cumpar()
    elif m == 5:
        modif_cumpar()
    elif m == 6:
        sum_max()
    elif m == 7:
        sum_min()
    elif m == 0:
        print('Autorul programului este Fodorcea D.')
    else:
        print('Optiune incorecta. Mai incercati!')
