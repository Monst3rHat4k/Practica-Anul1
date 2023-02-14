file_name = 'produse.txt'


class Produse:
    def __init__(self, id_produs, name, day_prod, month_prod, year_prod, day_ex, month_ex, year_ex, price_per_unit):
        self.id_produs = id_produs
        self.name = name
        self.day_prod = day_prod
        self.month_prod = month_prod
        self.year_prod = year_prod
        self.day_ex = day_ex
        self.month_ex = month_ex
        self.year_ex = year_ex
        self.price_per_unit = price_per_unit

    def __str__(self):
        return str(self.id_produs) + ' ' + self.name + ' ' + str(self.day_prod) + ' ' + str(self.month_prod) + ' ' + str(self.year_prod) + ' ' + str(self.day_ex) + ' ' + str(self.month_ex) + ' ' + str(self.year_ex) + ' ' + str(self.price_per_unit)

    def __lt__(self, other):
        if self.price_per_unit > other.price_per_unit:
            return True
        else:
            return False


def citire_fis():
    list.clear()
    f = open(file_name)
    for line in f:
        sir = line.split(' ')
        prod = Produse(sir[0], sir[1], int(sir[2]), int(sir[3]), int(sir[4]), int(sir[5]), int(sir[6]), int(sir[7]), float(sir[8]))
        list.append(prod)
    print('Lista studentilor a fost incarcata din fisier in lista!')
    f.close()


def scriere_fis():
    f = open(file_name, 'w')
    for prod in list:
        f.write(str(prod.id_produs)+' '+prod.name+' '+str(prod.day_prod)+' '+str(prod.month_prod)+' '+str(prod.year_prod)+' '+str(prod.day_ex)+' '+str(prod.month_ex)+' '+str(prod.year_ex)+' '+str(prod.price_per_unit)+'\n')
    f.close()


def afis_fis():
    print('Lista produselor (id_produs; name; day_prod; month_prod; year_prod; day_ex; month_ex; year_ex; price_per_unit): ')
    for prod in list:
        print(prod)


def add_prod():
    f = open(file_name, 'a')
    id_produs = str(input('Introduceti id-ul produsului: '))
    name = input('Introduceti numele produsului: ')
    day_prod = str(input('Introduceti data producerii: '))
    month_prod = str(input('Introduceti luna producerii: '))
    year_prod = int(input('Introduceti anul producerii: '))
    day_ex = str(input('Introduceti data expirarii: '))
    month_ex = str(input('Introduceti luna expirarii: '))
    year_ex = int(input('Introduceti anul expirarii: '))
    price_per_unit = float(input('Introduceti pretul per unitate: '))
    f.write('\n' + str(id_produs) + ' ' + name + ' ' + str(day_prod) + ' ' + str(month_prod) + ' ' + str(year_prod) + ' ' + str(day_ex) + ' ' + str(month_ex) + ' ' + str(year_ex) + ' ' + str(price_per_unit))
    f.close()
    print('Produsul a fost adaugat in fisier cu succes!')


def exista(id_produs):
    f = open(file_name)
    for line in f:
        sir = line.split(' ')
        if id_produs == str(sir[0]):
            f.close()
            return True
    f.close()
    return False


def elim_prod():
    f = open(file_name)
    g = open('temp.txt', 'w')
    id_produs = str(input('Introduceti numarul produsului, care va fi eliminat: '))
    if exista(id_produs):
        for line in f:
            sir = line.split(' ')
            if id_produs != str(sir[0]):
                g.write(line)
        f.close()
        g.close()
        f = open(file_name, 'w')
        g = open('temp.txt', 'r')
        for line in g:
            f.write(line)
        f.close()
        g.close()
        print('Produsul cu id-ul ', id_produs, ' a fost sters din fisier cu succes!')
    else:
        print('Asa student nu exista!')


def modif_prod():
    f = open(file_name)
    g = open('temp.txt', 'w')
    id_produs = str(input('Introduceti id-ul produsului, datele caruia vor fi modificate: '))
    if exista(id_produs):
        for line in f:
            sir = line.split(' ')
            if id_produs != str(sir[0]):
                g.write(line)
            else:
                id_produs = str(input('Introduceti id-ul produsului: '))
                name = input('Introduceti numele produsului: ')
                day_prod = input('Introduceti data producerii: ')
                month_prod = str(input('Introduceti luna producerii: '))
                year_prod = int(input('Introduceti anul producerii: '))
                day_ex = str(input('Introduceti data expirarii: '))
                month_ex = str(input('Introduceti luna expirarii: '))
                year_ex = int(input('Introduceti anul expirarii: '))
                price_per_unit = float(input('Introduceti pretul per unitate: '))
                g.write(str(id_produs) + ' ' + name + ' ' + str(day_prod) + ' ' + str(month_prod) + ' ' + str(year_prod) + ' ' + str(day_ex) + ' ' + str(month_ex) + ' ' + str(year_ex) + ' ' + str(price_per_unit) + '\n')
        f.close()
        g.close()
        f = open(file_name, 'w')
        g = open('temp.txt', 'r')
        for line in g:
            f.write(line)
        f.close()
        g.close()
        print('Datele studentului cu numarul ', id_produs, ' au fost actualizate in fisier cu succes!')
    else:
        print('Asa student nu exista!')


def sortByPrice_per_unit():
    citire_fis()
    list.sort()
    print('Lista produselor in ordine descrescatoare a pretului: ')
    for prod in list:
        print(prod)
    scriere_fis()


def menu():
    print('Citire din fisier..........1')
    print('Afisare produse...........2')
    print('Adaugare produs...........3')
    print('Eliminare produs..........4')
    print('Modificare produs.........5')
    print('Sortare dupa pret desc....6')
    print('Iesire din program.........7')
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
        add_prod()
    elif m == 4:
        elim_prod()
    elif m == 5:
        modif_prod()
    elif m == 6:
        sortByPrice_per_unit()
    elif m == 0:
        print('Autorul programului este Fodorcea D.')
    else:
        print('Optiune incorecta. Mai incercati!')
