def main():
    # Numerical
    # int
    number = 194756783839949944*858737372626278
    print(number)
    # float (är som en double)
    dec = 3.44565464466678574747373883
    print(dec)

    # Logiska
    # Boolean, skrivs med stor bokstav
    done = True
    done = False

    # String
    name = "Charlotte"

    # Sequence (listor)
    # List (dynamisk, som arrayList), uses [], kan take different types
    values = [1, 2, 3, 4, 5, "hej", True, 4.56]

    # Tuple - uses (), som vanlig array, ej dynamisk, kan dock blanda typer
    # Har färre metoder än Sequence
    tuple_values = (1, 2, 3 ,4, "hopp")

    # Indexing
    print(values[2])
    print(values.index("hej"))
    print(tuple_values[2])

    # Set - fungerar som men lista med har en särskild egenskap
    # Kan bara spara unika värden, skriver inte ut dubletter
    set_values = {1, 2, 3, 4, 5, 1, 2}
    print(set_values)
    list_values = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    #Denna omvandling tar bort dubletter
    list_values = list(set(list_values))
    print(list_values)

    # dictionary
    person = {
        'name': 'Pelle',
        'age': 34,
        'email': 'pelle@gmail.com'
    }
    print(person['email'])


if __name__ == '__main__':
    main()
