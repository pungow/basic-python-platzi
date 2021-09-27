def run():
    my_dictionary = {
        'key_1': 1,
        'key_2': 2,
        'key_3': 3,
    }
    # print(my_dictionary['key_1'])
    # print(my_dictionary['key_2'])
    # print(my_dictionary['key_3'])
    country_population = {
        'Arg': 44000000,
        'Bra': 210003245,
        'Col': 50402513
    }
    # print(country_population['Arg'])
    for key in country_population.keys():
        print(key)
    for value in country_population.values():
        print(value)
    for key, value in country_population.items():
        print(f'{key} tiene {value} habitantes')


if __name__ == '__main__':
    run()