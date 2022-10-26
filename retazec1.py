def pismeno(slovo,rad):
    if len(slovo)>=rad:
        print(slovo[rad-1])
    else:
        print("toľko písmen v slove nemáš")

pismeno("ahoj",3)