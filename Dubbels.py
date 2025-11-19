#Schrijf een functie dubbel die een lijst van getallen als argument neemt, en het element van de lijst teruggeeft dat tweemaal voorkomt.
# De functie moet de waarde None teruggeven als er geen enkel getal meer dan één keer voorkomt in de lijst.
# Er is hoogstens één getal dat tweemaal voorkomt.

#Schrijf een functie dubbels die een lijst van getallen als argument neemt, en twee verzamelingen teruggeeft.
# De eerste verzameling bevat alle elementen die slechts eenmaal voorkomen in de lijst en de tweede verzameling bevat alle elementen die meer dan eenmaal voorkomen in de lijst.

def dubbel(elmntlijst):
    for i in range(len(elmntlijst) - 1):
        controle = i + 1
        for controle in range(i + 1, len(elmntlijst)):
            if elmntlijst[i] == elmntlijst[controle]:
                return elmntlijst[i]
    return None


def dubbels(elmntlijst):
    single = set()
    double = set()

    for item in elmntlijst:
        if item in single:
            single.remove(item)
            double.add(item)
        elif item not in double:
            single.add(item)

    return single, double