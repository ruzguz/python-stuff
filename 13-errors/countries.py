countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

while True:
    country = input('Write the name of a country: ').lower()

    try:    
        print('{} have {} people'.format(country, countries[country]))
    except KeyError:
        print('We don\'t have the information of population of {}'.format(country))
