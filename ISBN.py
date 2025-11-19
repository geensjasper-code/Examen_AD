def codecorrect(ISBN):
    chars = list(ISBN) #make list of char
    int_chars = [int(x) for x in chars]
    even_indices = int_chars[1:12:2] #sequence[start:stop:step], index 0 == x1 => x2 == index 1
    odd_indices = int_chars[0:11:2]
    control_char = int_chars[-1]
    sum_even = sum(even_indices)
    sum_odd = sum(odd_indices)
    if control_char == (10 - ((sum_odd + 3*sum_even) % 10)) % 10 and (int_chars[0:3] == [9, 7, 8] or int_chars[0:3] == [9, 7, 9]):
        return True
    else:
        return False

def overzicht(codes):
    groepen = ['Engelstalige landen', 'Franstalige landen', 'Duitstalige landen', 'Japan', 'Russischtalige landen', 'China', 'Overige landen', 'Fouten']
    overzicht_dict = {group: 0 for group in groepen}
    for code in codes:
        if codecorrect(code) == False:
            overzicht_dict['Fouten'] += 1
        else:
            chars = list(code)  # make list of char
            int_chars = [int(x) for x in chars]
            if (int_chars[3] == 0 or int_chars[3] == 1):
                overzicht_dict['Engelstalige landen'] += 1
            elif int_chars[3] == 2:
                overzicht_dict['Franstalige landen'] += 1
            elif int_chars[3] == 3:
                overzicht_dict['Duitstalige landen'] += 1
            elif int_chars[3] == 4:
                overzicht_dict['Japan'] += 1
            elif int_chars[3] == 5:
                overzicht_dict['Russischtalige landen'] += 1
            elif int_chars[3] == 7:
                overzicht_dict['China'] += 1
            else:
                overzicht_dict['Overige landen'] += 1
    for group in groepen:
        print(f"{group}: {overzicht_dict[group]}")