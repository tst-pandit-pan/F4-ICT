puzzle = ["GYGGNTOVTKTNACJ", "ZIGRAVYNTNAILID", "ZAROREGITYKULHY", "TGGAZUFLVTRGIGP", "CNEGFMORGOENGTO", "XBALUFSPOLEEASL", "ZAGHDQEMIGMPTRA", "BIBEPTIOKOYOOHR", "JZWGZENTWKRKRKB", "NNOSNVLGTKUEJAE", "IRSDYHYEKNOMJMA", "NEPSVQZLUCCASVR", "DECPGUOYTOADUXB", "BQHDAVDXLULXBEZ", "WPANDASALZMMUWR"]
word = input()
found = False
for i in range(15):
    for j in range(15):
        if puzzle[i][j] == word[0] and found == False:
            found = True
            for k in range(len(word)):
                if j+k >15 or word[k] != puzzle[i][j+k]:
                    found = False
if found == True:
    print("True")