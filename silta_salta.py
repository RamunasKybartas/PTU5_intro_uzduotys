# ## 1. Žaidimas šilta-šalta.
# * Programa įsimena skaičių į kintamąjį `teisingas`.
# * Programa leidžia žaidėjui spėti skaičių:
#   * iš žaidėjo skaičių gauname per `input()` funkciją.
#   * nepamirškite konvertuoti į skaičių gautos iš žaidėjo įvesties, ir patikrinti ar tai yra įmanoma padaryti.
# * Įsimenamas absoliutus `skirtumas` tarp spėjimo ir teisingo atsakymo.
# * Kaskart spėjant, lyginti ar naujas skirtumas yra mažesnis už buvusį:
#   * jei taip, spausdinti "šilta..."
#   * kitu atveju, spausdinti "šalta..."
# * Programą kartoti, kol būna atspėtas skaičius. Atspėjus, išpsausdinti sveikinimus ir teisingą atsakymą.
# * BONUS 1: teisingas skaičius parenkamas atsitiktiniu būdu, įskaitant neigiamus skaičius. Pradžiai vistiek siūlyčiau gan mažą imtį.
# * BONUS 2: skaičiuokite kiek kartų buvo spėta
from random import randint

old_difference = 0
correct_number = randint(-20, 50)
guess_count = 0
while True:
    try:
        guess_number = int(input("Iveskite skaiciu: "))
    except ValueError:
        print("Ivestis turi buti sveikasis skaicius")
    guess_count += 1
    if guess_number == correct_number:
        print(f"Sveikiname!, laimingas skaicius {correct_number} atspeta is {guess_count} kartu")
        break
    difference = abs(correct_number - guess_number)
    if difference < old_difference:
        old_difference = difference
        print("silta")
    else:
        print("salta")
        old_difference = difference


# from random import randint
# teisingas = randint(-2**15, 2**15) # 777
# spejimas = None
# skirtumas = 0
# kartai = 0
# while spejimas is None or spejimas != teisingas:
#     try:
#         spejimas = int(input("Spėkite skaičių: "))
#     except ValueError:
#         print("įvestas ne skaičius")
#     else:
#         if teisingas != spejimas:
#             kartai += 1
#             if abs(teisingas - spejimas) < skirtumas:
#                 print(spejimas, "šilta...")
#             else:
#                 print(spejimas, "šalta...")
#             skirtumas = abs(teisingas - spejimas)
# else:
#     print(f"!!! Atspėjai iš {kartai} karto. Teisingas atsakymas: {teisingas}")