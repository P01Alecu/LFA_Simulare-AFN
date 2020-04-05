##in fisierul 'ad.txt' se gasesc datele de intrare
##fisierul este de forma:
##stare_initiala Stari_finale
##cuvant cuvant cuvant......
##litera starea_din_care_pleaca starea_in_care_ajunge
##...
##litera starea_din_care_pleaca starea_in_care_ajunge


def parcurgere(lista, sir):
    ok = True
    point = 0 #pointeaza litera pana la acare s-a parcurs sirul
    f = open("out.txt", "a")
    f.write('Cuvantul: ' + str(sir) + '\n')

    while (len(lista)!= [] and point<len(sir)):
        f.write(str(lista) + ' ' + str(sir[point:]) + "\n") #scrie in fisier
        print(str(lista) + ' ' + str(sir[point:]))  #scrie in consola
        lista = cautare(sir[point], lista, m)
        if(lista == []):
            ok = False
            break
        point = point+1

    if(ok): #verifica daca starea in care s-a ajuns dupa parcurgerea cuvantului este finala
        f.write(str(lista) + ' ' + "''\n") #scrie in fisier
        print(str(lista) + ' ' + "''")  #scrie in consola
        ok = verificare(lista, final)
    if(ok):
        f.write(str(lista) + ' ' + "''\n")
        print(str(lista) + ' ' + "''")
        f.write('Cuvantul este acceptat!\n')
        print('Cuvantul este acceptat!')
    else:
        f.write('Nu se poate!\n')
        print('Nu se poate!')
    f.write('\n')
    f.close()

def cautare(litera, starea, text):  #cauta starile a caror tranzitie accepta o litera anume
    lista = []
    for i in range(0, len(text.splitlines())):
        for j in range(0, len(starea)):
            if(text.splitlines()[i][0] == litera and text.splitlines()[i][2] == starea[j]):
                lista.append(text.splitlines()[i][4])
    return lista

def verificare(lista, final):   #verifica daca cel putin una din starile in care a ajuns este stare finala
    ok = False
    for i in range(0, len(final)):
        for j in range(0, len(lista)):
            if (final[i] == lista[j]):
                #print(str(final[i]) + ' == ' + str(lista[j] ))     #debug
                ok = True
    return ok

f = open("in.txt", "r")
final = []
m = f.read()

start = m[0]    #starea initiala
final = m.splitlines()[0][2:].split()   #vector cu starile finale
f.close()
#ok = True
sir = m.splitlines()[1].split()
lista = [start]

#print('Stare initiala: ' + str(lista))
#print('Stari finale: ' + str(final))

f = open("out.txt", "w")    #solutie simpla ptr a sterge un posibil vechi fisier "out.txt" si a creea unul nou in care se va face append
f.close()
for i in range(0, len(sir)):
    print()
    print(sir[i])
    parcurgere(lista, sir[i])