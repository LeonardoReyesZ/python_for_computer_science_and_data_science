""" Program to test dictionary manipulations """

tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

# ~~~~~~~~~  Definition of Functions  ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
def show_abbreviation():
    country = input("Enter the name of the country: ")
    abbreviation = tlds.get(country, "Country not found")
    print(f"The abbreviation for {country} is {abbreviation}.")
# end show_abbreviation

def display_all_pairs():
    print(f"{'Country':<20}{'Abbreviation':<10}")

    for country, abbreviation in tlds.items():
        print(f"{country:<20}{abbreviation:<10}")
# end display_all_pairs

def add_or_change_pair():
    country = input("Enter the name of the country: ")
    abbreviation = input("Enter the abbreviation: ")
    tlds[country] = abbreviation # add or update country
    print(f"Added/Updated: {country} -> {abbreviation}")
# end add_or_change_pair

def invert_dictionary():
    inverted_tlds = {abbreviation: country for country, abbreviation in tlds.items()}
    print("Inverted dictionary:")
    for abbreviation, country in inverted_tlds.items():
        print(f"{abbreviation:<10}{country:<20}")
# end invert_dictionary

def abbreviations_to_uppercase():
    for country in tlds:
        tlds[country] = tlds[country].upper()

    print("All abbreviations converted to uppercase.")
# end abbreviations_to_upercase

def menu():
    while True:
        print("\nDictionary manipulations:")
        print("(a) show the abbreviation of a country")
        print("(b) Display all key-value pairs")
        print("(c) Add or Update a key-value pair")
        print("(d) Create a new dictionary with values as keys and keys as values")
        print("(e) Convert all abbreviations to uppercase")
        print("(f) Exit")

        choice = input("Enter you choice: ").strip().lower()

        if choice == 'a':
            show_abbreviation()
        elif choice == 'b':
            display_all_pairs()
        elif choice == 'c':
            add_or_change_pair()
        elif choice == 'd':
            invert_dictionary()
        elif choice == 'e':
            abbreviations_to_uppercase()
        elif choice == 'f':
            break
        else:
            print("Invalid choice, try again ... ")
# end menu


# ~~~~~~~~~  Program Execution     ~~ ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
# run menu
menu()
