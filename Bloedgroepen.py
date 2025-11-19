#Schrijf een functie bloedgroep_kind waaraan twee strings als argument moeten doorgegeven worden.
# Deze stellen respectievelijk de bloedgroep van een vader en van een moeder voor.
# De functie moet als resultaat een verzameling (van strings) teruggeven die alle mogelijke bloedgroepen bevat die kinderen van deze twee ouders kunnen hebben.

#Schrijf een functie bloedgroep_ouder waaraan twee strings als argument moeten doorgegeven worden.
# Deze stellen respectievelijk de bloedgroep van een ouder en één van diens kinderen voor.
# De functie moet als resultaat een verzameling (van strings) teruggeven die alle mogelijke bloedgroepen bevat die de andere ouder van het kind kan hebben.
# Merk op dat in dit geval de verzameling bloedgroepen ook leeg kan zijn.

from itertools import product

# Alle mogelijke combinaties van genotypen
ABO_MAP = {
    'A': [('A', 'A'), ('A', 'O')],
    'B': [('B', 'B'), ('B', 'O')],
    'AB': [('A', 'B')],
    'O': [('O', 'O')]
}

RH_MAP = {
    '+': [('+', '+'), ('+', '-')],
    '-': [('-', '-')]
}


def combine_ABO(a1, a2):
    """Bepaalt bloedgroep op basis van twee ABO allelen."""
    s = {a1, a2}
    if s == {'A', 'B'}:
        return 'AB'
    if 'A' in s and 'B' not in s and 'O' in s or s == {'A'}:
        return 'A'
    if 'B' in s and 'A' not in s and 'O' in s or s == {'B'}:
        return 'B'
    if s == {'O'}:
        return 'O'


def combine_RH(r1, r2):
    """Bepaalt rhesusfactor op basis van twee RH allelen."""
    if '+' in (r1, r2):
        return '+'
    return '-'


def bloedgroep_kind(vader, moeder):
    """Geeft alle mogelijke bloedgroepen van de kinderen."""
    vader_ABO, vader_RH = vader[:-1], vader[-1]
    moeder_ABO, moeder_RH = moeder[:-1], moeder[-1]

    result = set()
    for v_ABO, m_ABO in product(ABO_MAP[vader_ABO], ABO_MAP[moeder_ABO]):
        for v_a, m_a in product(v_ABO, m_ABO):
            child_ABO = combine_ABO(v_a, m_a)
            for v_RH, m_RH in product(RH_MAP[vader_RH], RH_MAP[moeder_RH]):
                for r1, r2 in product(v_RH, m_RH):
                    child_RH = combine_RH(r1, r2)
                    result.add(child_ABO + child_RH)
    return result


def bloedgroep_ouder(ouder, kind):
    """Geeft alle mogelijke bloedgroepen voor de andere ouder."""
    kind_ABO, kind_RH = kind[:-1], kind[-1]
    mogelijke = {'A', 'B', 'AB', 'O'}
    rh_tekens = ['+', '-']
    mogelijke_bloedgroepen = {a + r for a in mogelijke for r in rh_tekens}

    res = set()
    for bg in mogelijke_bloedgroepen:
        if kind in bloedgroep_kind(ouder, bg) or kind in bloedgroep_kind(bg, ouder):
            res.add(bg)
    return res
