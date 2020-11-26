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

# exo 7
def moyenne_jour(liste):
    n = len(liste)
    liste_moyenne_jour = []
    for i in range(7):
        liste_moyenne_jour.append(moyenne(liste[i:n:7]))
    return liste_moyenne_jour

# exo 8
def maximum(liste):
    """
    Renvoie la valeur du maximum puis l'indice du maxium
    """
    n = len(liste)
    maxi = liste[0]
    indice_max = 0
    for i in range(1, n):
        if liste[i] > maxi:
            maxi = liste[i]
            indice_max = i
    return maxi, indice_max


jours = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"]
def jour_max(liste):
    # indice_max est l'indice du jour qui a la plus grande moyenne de réservation
    indice_max = maximum(moyenne_jour(liste))[1]
    return jours[indice_max]

# exo 16
arriveesO = [495, 562, 740, 841, 920, 1264]
departO = [624, 803, 950, 1047, 1133, 1320]
def nb_quais(arrivees, departs):
    nb_quais_neccessaires = 0
    max_nb_quais_neccessaires = 0
    for i in range(arrivees[0], departs[-1]+1):
        if i in arrivees:
            nb_quais_neccessaires +=1
        elif i in departO:
            nb_quais_neccessaires -= 1
        if nb_quais_neccessaires > max_nb_quais_neccessaires:
            max_nb_quais_neccessaires = nb_quais_neccessaires
    return max_nb_quais_neccessaires
