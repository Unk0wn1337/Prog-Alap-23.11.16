def szovegkezelesElsoFeladat(szoveg):
    szokozDb = 0
    index = 0
    while index < len(szoveg):
        if szoveg[index] == ' ':
            szokozDb += 1
        index += 1
    return szokozDb

def szovegkezelesMasodikFeladat(szoveg):
    index = 0
    szokozNelkul = ""
    while index < len(szoveg):
        if szoveg[index] != ' ':
           szokozNelkul += szoveg[index]
        index+=1
    print(szokozNelkul)

def szovegkezelesHarmadikFeladat(szoveg):
    kisSzoveg = szoveg.lower()
    print("a. feladat",kisSzoveg)
    kisSzoveg = kisSzoveg.replace('é','e')
    kisSzoveg = kisSzoveg.replace('á','a')
    kisSzoveg = kisSzoveg.replace('ő','o')
    kisSzoveg = kisSzoveg.replace('ö','o')
    kisSzoveg = kisSzoveg.replace('ű','u')
    kisSzoveg = kisSzoveg.replace('ü','u')
    print(kisSzoveg[::-1])





