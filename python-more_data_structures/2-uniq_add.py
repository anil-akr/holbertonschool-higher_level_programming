#!/usr/bin/python3

def uniq_add(my_list=[]):
    resultat = 0
    uniques = []
    for x in my_list:
        if x not in uniques:
            resultat = resultat + x
            uniques.append(x)
    return resultat
