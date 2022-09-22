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

correct_number = 19
guess_number = int(input("Iveskite skaiciu: ")) 