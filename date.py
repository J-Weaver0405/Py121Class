
date1 = ' 05.05.2021 '
date2 = ' 10.05.2021 '
date3 = ' 05.10.2021 '
date4 = ' 30.05.2021 '
date5 = ' 05.30.2021 '


def date_checker(date_to_check):
    ambiguous_str = None
    date_to_check = date_to_check.strip()
    date_parts = date_to_check.split('.')

    date_as_ints = [int(part) for part in date_parts]

    if int(date_as_ints[0]) == int(date_as_ints[1]):
        return "non_ambiguous"

    counter = 0
    for x in date_as_ints[:2]:
        if x < 13:
            counter += 1
    

    if counter == 2:
        return "ambiguous"

    return "non-ambiguous"
    

print(date_checker(date1))
print(date_checker(date2))
print(date_checker(date3))
print(date_checker(date4))




