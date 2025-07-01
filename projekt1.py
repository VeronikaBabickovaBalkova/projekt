"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Veronika Balková
email: veronika.balkova@rohde-schwarz.com
"""

users = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}
user = input("username:")
password = input("password:")

if user in users:
    if users[user] == password:
        print("Welcome to he app, ", user)
        print("We have 3 texts to be analyzed.")
        print("-" * 40)
    else:
        print("unregistered user, terminating the program..")
        exit()
else:
    print("unregistered user, terminating the program..")
    exit()

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

vyber_text = input("Enter a number btw. 1 and 3 to select: ")
vybrany_text = []
slova_pocet = []
velka_slova = []
upper_slova = []
pocet_upper_slova = 0
lower_slova = []
digit = []
sumdigit = []
cetnosti = {}
vycistena_slova = []

print("-" * 40)

# kontrola, zda je volba číslem a vyber spravneho textu
if str(vyber_text).isdigit():
    for index, text in (enumerate(TEXTS, start = 1)):
        if index == int(vyber_text):

# tady tvorim z vybraneho textu list
            vybrany_text.append(text)
# rozdeleni vybraneho textu na jednotliva slova
            text_slova = text.split()

# 1 zjisteni poctu slov
            slova_pocet.append(len(vybrany_text[0].split()))
# 2 hledam pocet slov psanych velkymi pismeny
            for slovo in text_slova:
                if slovo.istitle():
                    velka_slova.append(slovo)
                    pocet_velka_slova = len(velka_slova)
# 3 počet slov psaných velkými písmeny
            for slovo in text_slova:
                if slovo.isupper():
                    upper_slova.append(slovo)
                    pocet_upper_slova += 1
# 4 pocet slov psanych malymi pismeny
            for slovo in text_slova:
                if slovo.islower():
                    lower_slova.append(slovo)
                    pocet_lower_slova = len(lower_slova)
# 5 počet čísel
            for slovo in text_slova:
                if slovo.isdigit():
                    digit.append(slovo)
                    pocet_digit = len(digit)
# suma všech čísel 
            for slovo in text_slova:
                if slovo.isdigit():
                    sumdigit.append(int(slovo))
                    sumalldigit = sum(sumdigit)
# graf
            for slovo in text_slova:
                vycistene_slovo = slovo.replace(" ", "").replace(",", "").replace(".", "")
                vycistena_slova.append(vycistene_slovo)
            delky_slov = [len(slovo) for slovo in vycistena_slova]
            for delka in delky_slov:
                if delka in cetnosti:
                    cetnosti[delka] = cetnosti[delka] +1
                else:
                    cetnosti[delka] = 1
            break
    else:
        print("unvalid choice, terminating the program...")
        exit()
else:
    print("uvlalid choice...not a number...terminating the program....")
    exit()

print("There are " + str(slova_pocet) + " words in the selected text." )
print("There are " + str(pocet_velka_slova) + " titelcase words.")
print("There are " + str(pocet_upper_slova) + " uppercase words.")
print("There are " + str(pocet_lower_slova) + " lowercase words.")
print("There are " + str(pocet_digit) + " numeric strings.")
print("The sum of all the numbers " + str(sumalldigit))
print("-" * 40)
print("LEN | OCCURENCES | NR.")
print("-" * 40)
for delka in sorted(cetnosti.keys()):
    cetnost = cetnosti[delka]
    print("{:<3}| {:<20} | {:<3}".format(delka, '*' * cetnost, cetnost))