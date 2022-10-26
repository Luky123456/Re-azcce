samohlasky=["a","e","i","y","o","u"]
def samoh(text):
    y= False
    for i in range (0,len(text)):
        if text[i] in samohlasky:
            y = True

        else:
            y = False
            break
    print(y)

samoh("aaeiyouaaa")
