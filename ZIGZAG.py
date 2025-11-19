#Schrijf een functie iszigzag waaraan een reeks (list of tuple) van gehele getallen (int) moet doorgegeven worden.
# De functie moet een Booleaanse waarde (bool) teruggeven die aangeeft of de gegeven reeks getallen zigzag-gesorteerd is.

#Schrijf een functie zigzag_traag waaraan een lijst (list) van gehele getallen (int) moet doorgegeven worden.
# De functie moet de gegeven lijst van getallen zigzag-sorteren op basis van de trage methode die hierboven werd omschreven.
# De functie moet geen resultaat teruggeven (lees: moet de waarde None teruggeven), maar moet de gegeven lijst in place bijwerken.

#Schrijf een functie zigzag_snel waaraan een lijst (list) van gehele getallen (int) moet doorgegeven worden.
# De functie moet de gegeven lijst van getallen zigzag-sorteren op basis van de snelle methode die hierboven werd omschreven.
# De functie moet geen resultaat teruggeven (lees: moet de waarde None teruggeven), maar moet de gegeven lijst in place bijwerken.

def iszigzag(lst):
    if len(lst) < 2:
        return True  # 0 or 1 element is trivially zigzag

    for i in range(len(lst) - 1):
        if i % 2 == 0:
            if lst[i] < lst[i + 1]:  # even index should be >= next
                return False
        else:
            if lst[i] > lst[i + 1]:  # odd index should be <= next
                return False
    return True

def zigzag_traag(lst):
    lst.sort()  # sorteert in-place, geen nieuwe lijst nodig
    for i in range(0, len(lst) - 1, 2): #vertrekken van index 0, tot voorlaatste index (index error vermijden) in stappen van 2
        lst[i], lst[i + 1] = lst[i + 1], lst[i]  # wissel buurparen
    # geen return -> standaard returnt de functie None

def zigzag_snel(lst):
    n = len(lst)
    for i in range(0, n, 2):  # alleen even indices: 0,2,4,...
        # check met vorige oneven positie
        if i > 0 and lst[i] < lst[i-1]:
            lst[i], lst[i-1] = lst[i-1], lst[i]
        # check met volgende oneven positie
        if i < n - 1 and lst[i] < lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
    # geen return → functie werkt in-place en geeft None

