# 3 užduotis
# Parašyti programą, kuri nurodytų, ar vartotojo įvestas skaičius yra lyginis,
# ar nelyginis
# Hint’as - operatorius %, funkcijos input(), float(). Naudoti if sakinį.

skaicius = int(input("Ivesti skaicius: "))
print("lyginis") if skaicius % 2 == 0 else print("nelyginis")
