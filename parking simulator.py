import heapq


class PriorityQueue:
    """
    Kleine wrapper rond heapq zodat we een PriorityQueue krijgen
    die tuples automatisch sorteert volgens Python's tuple-ordering.
    """

    def __init__(self):
        self.content = []

    def add(self, item):
        # Voeg een element toe in de priority queue
        heapq.heappush(self.content, item)

    def peek(self):
        return self.content[0] if self.content else None

    def poll(self):
        # Haal het element met de hoogste prioriteit eruit (kleinste tuple)
        return heapq.heappop(self.content) if self.content else None

    def is_empty(self):
        return len(self.content) == 0

    def __str__(self):
        return str(heapq.nsmallest(len(self.content), self.content))


def simuleer_parking(plaatsen, bloktijd, klanten):
    """
    Simuleer het parkeergedrag volgens:
      - plaatsen: totaal aantal beschikbare parkeerplaatsen
      - bloktijd: tijd die een klant nodig heeft om een rondje te rijden
      - klanten: lijst van tuples (aankomsttijd, winkellengte)

    De functie retourneert het tijdstip waarop de parking opnieuw leeg is.
    """

    # Aantal vrije plaatsen (wordt dynamisch aangepast)
    vrije_plaatsen = plaatsen

    # We houden bij wanneer de laatste klant vertrekt
    laatste_vertrek = 0

    # We plaatsen alle events in één priority queue
    # Een event is een tuple:
    #   (tijd, event_type, winkellengte, klant_id)
    #
    # Waar:
    #   tijd: moment van event
    #   event_type:
    #       0 = vertrek (moet altijd eerder uitgevoerd worden)
    #       1 = aankomst / terugkomst
    #   winkellengte: belangrijk voor het sorteren van arrivals
    #
    # Het sorteergedrag wordt volledig bepaald door deze tuple.
    events = PriorityQueue()

    # Voeg alle initiële aankomst-events toe
    for klant_id, (aankomst, winkellengte) in enumerate(klanten):
        # Let op:
        #   arrivals krijgen event_type = 1,
        #   en winkellengte blijft onderdeel van de tuple voor tie-breaking.
        events.add((aankomst, 1, winkellengte, klant_id))

    # De hoofdloop: werk events af in chronologische volgorde
    while not events.is_empty():

        tijd, event_type, winkellengte, klant_id = events.poll()

        # -----------------------------
        #  EVENT TYPE 0  => VERTREK
        # -----------------------------
        if event_type == 0:
            # Een klant vertrekt => parkeerplaats wordt vrij
            vrije_plaatsen += 1

            # Update het laatst gekende vertrek
            if tijd > laatste_vertrek:
                laatste_vertrek = tijd

        # -----------------------------
        #  EVENT TYPE 1  => AANKOMST
        # -----------------------------
        else:
            # Klant probeert te parkeren
            if vrije_plaatsen > 0:
                # Parkeren lukt
                vrije_plaatsen -= 1
                vertrektijd = tijd + winkellengte

                # Plan vertrek-event
                # Vertrek heeft event_type=0 en is dus belangrijker dan aankomst
                events.add((vertrektijd, 0, 0, klant_id))

            else:
                # Parking vol ⇒ klant rijdt rondje en komt later terug
                terugkomst = tijd + bloktijd

                # Ook terugkomst is een arrival (event_type=1)
                # Winkellengte blijft zodat gelijktijdige terugkeerders
                # juist geordend worden.
                events.add((terugkomst, 1, winkellengte, klant_id))

    return laatste_vertrek


# ---- TESTS ----
print(simuleer_parking(1, 5, [(0, 5), (4, 5), (5, 3), (10, 10)]))
# Verwacht: 25

print(simuleer_parking(2, 5, [(0, 5), (3, 4), (4, 5), (5, 3), (8, 9), (10, 3), (10, 10)]))
# Verwacht: 30
