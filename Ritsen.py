'schrijf een functie samenvoegen waaraan twee reeksen (list of tuple) moeten doorgegeven worden.'
'De functie moet een nieuwe lijst (list) teruggeven, waarin de elementen van de twee gegeven reeksen beurtelings en paarsgewijs samengevoegd worden.'
'Het samenvoegen moet stoppen van zodra alle elementen van de kortste reeks zijn toegevoegd aan de nieuwe lijst.'
'Schrijf een functie weven waaraan twee reeksen (list of tuple) moeten doorgegeven worden.'
'De functie moet een nieuwe lijst (list) teruggeven, waarin de elementen van de twee gegeven reeksen beurtelings en paarsgewijs samengevoegd worden.'
'Het samenvoegen moet stoppen van zodra alle elementen van de langste reeks zijn toegevoegd aan de nieuwe lijst.'
'Na het laatste element van de kortste reeks wordt terug het eerste element van die reeks toegevoegd, en daarna telkens terug het volgende elementen van de reeks.'

'Schrijf een functie ritsen waaraan twee reeksen (list of tuple) moeten doorgegeven worden.'
' De functie moet een nieuwe lijst (list) teruggeven met alle elementen van de twee gegeven reeksen.'
' De functie voegt in die nieuwe lijst eerst beurtelings en paarsgewijs de elementen van de twee gegeven reeksen samen, totdat alle elementen van de kortste reeks zijn toegevoegd.'
' Daarna worden nog de resterende elementen van de langste reeks aan de nieuwe lijst toegevoegd.'

def samenvoegen(reeks1, reeks2):
    combi_lijst = []
    kortste_lengte = min(len(reeks1), len(reeks2))
    for i in range(kortste_lengte):
        combi_lijst.append(reeks1[i])
        combi_lijst.append(reeks2[i])
    return combi_lijst

def weven(reeks1, reeks2):
    combi_lijst = []
    langste = max(len(reeks1), len(reeks2))
    for i in range(langste):
        combi_lijst.append(reeks1[i % len(reeks1)])
        combi_lijst.append(reeks2[i % len(reeks2)])
    return combi_lijst


def ritsen(reeks1, reeks2):
    combi_lijst = []
    kortste_len = min(len(reeks1), len(reeks2))

    # eerst weven tot de kortste lijst op is
    for i in range(kortste_len):
        combi_lijst.append(reeks1[i])
        combi_lijst.append(reeks2[i])

    # voeg de rest van de langere lijst toe
    if len(reeks1) > kortste_len:
        combi_lijst.extend(reeks1[kortste_len:])
    elif len(reeks2) > kortste_len:
        combi_lijst.extend(reeks2[kortste_len:])

    return combi_lijst
