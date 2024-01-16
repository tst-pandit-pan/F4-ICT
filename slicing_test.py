FOUND = False
POS = -1
WORD = "pineapple"
SHORT = input("Input PLZ:")
LWORD = len(WORD)
LSHORT = len(SHORT)
for i in range(0, LWORD - LSHORT + 1):
    if WORD[i : LSHORT + i] == SHORT:
        FOUND = True
        POS = i

if POS == -1:
    print("Not found!")
else:
    print("The word", WORD, "starts from index", POS)
