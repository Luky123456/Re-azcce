def cisla(text):
    x=text
    y=0
    for i in range (0,len(text)):
        if x[i].isnumeric():
            y+=1
        else:
            y=y
    print(y)
cisla("176ghgh65")
