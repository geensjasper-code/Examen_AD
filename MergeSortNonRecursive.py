def sorteer(rij):

    # Helperfunctie om twee gesorteerde subrijen te mergen
    def merge(left, right):
        i = j = 0
        resultaat = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                resultaat.append(left[i])
                i += 1
            else:
                resultaat.append(right[j])
                j += 1
        resultaat.extend(left[i:])
        resultaat.extend(right[j:])
        return resultaat

    n = len(rij)
    grootte = 1  # begin met sublijsten van lengte 1

    # Elke iteratie verdubbelt de sublijstgrootte
    while grootte < n:
        for i in range(0, n, 2 * grootte):

            # splits in twee gesorteerde sublijsten
            left = rij[i : i + grootte]
            right = rij[i + grootte : i + 2 * grootte]

            # merge en zet resultaat terug
            rij[i : i + 2 * grootte] = merge(left, right)

        grootte *= 2
