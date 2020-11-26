LO = [34, 32, 27, 15, 21, 23, 29, 40, 35, 31, 12, 26, 25, 33]

# exo 2
def minimum(liste):
    n = len(liste)
    a = liste[0]
    for i in range(1, n):
        if liste[i] < a:
            a = liste[i]
    return a

# exo 3
def moyenne(liste):
    return_moyenne = 0
    for i in liste:
        return_moyenne += i
    return return_moyenne / len(liste)

# exo 4
def ecart_type(liste):
    variance = 0
    moy = moyenne(liste)
    for i in liste:
        variance += (i - moy)**2
    variance = variance / len(liste)
    return variance**0.5

# exo 5
def nb_plus(liste, a):
    nombre_indices = 0
    for i in range(len(liste)):
        if liste[i] > a:
            nombre_indices +=1
    return nombre_indices

# exo 6
def ind_moins(liste, a):
    indices_liste = []
    for i in range(len(liste)):
        if liste[i] < a:
            indices_liste.append(i)
    return indices_liste
