def hanoi(n):
    """
    Lost de Torens van Hanoi op voor n schijven en print de stappen.
    """
    stappen = 0  # teller voor aantal stappen

    def verplaats(schijven, bron, doel, hulp):
        nonlocal stappen        #Zonder nonlocal stappen zou Python bij stappen += 1 een nieuwe lokale variabele stappen maken in verplaats,
                                # nonlocal vertelt Python dat we de variabele stappen van de omliggende functie (hanoi) willen gebruiken
                                #niet een nieuwe lokale variabele in verplaats
                                #Hierdoor werkt stappen += 1 correct: het verhoogt de teller in de buitenste functie
        if schijven == 1:
            print(f"Schijf 1 van {bron} naar {doel}")
            stappen += 1
        else:
            # verplaats de bovenste schijven naar de hulp-paal
            verplaats(schijven - 1, bron, hulp, doel)
            # verplaats de grootste schijf naar het doel
            print(f"Schijf {schijven} van {bron} naar {doel}")
            stappen += 1
            # verplaats de bovenste schijven van hulp naar doel
            verplaats(schijven - 1, hulp, doel, bron)

    # start de recursie van paal A naar C met B als hulp
    verplaats(n, "A", "C", "B")

    # print het aantal stappen
    print(f"{stappen} stappen gedaan")