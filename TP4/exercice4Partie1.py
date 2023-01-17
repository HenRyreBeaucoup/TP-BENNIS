L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6, 6, 6]

def leplus_frequent(ARR):
    Element_Voulu = None
    Nbr = 0
    for i in range(len(ARR)):
        el_actu = ARR[i]
        freq_actu = ARR.count(el_actu)
        if freq_actu > Nbr:
            Nbr = freq_actu
            Element_Voulu = el_actu
    return Element_Voulu, Nbr

print(leplus_frequent(L1))