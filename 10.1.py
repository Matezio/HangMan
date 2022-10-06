import random


def hangman(word):
    wrong=0
    stages = ["",
             "_____________   ",
             "|            |  ",
             "|            |  ",
             "|            O  ",
             "|           /|\ ",
             "|           / \ ",
             "|               ",
             "|               ",
              ]
    letters=list(word)
    space=["_"]*len(word)
    win=False
    print ("Welcome to the club body!")
    while wrong < len(stages)-1:
        print("\n")
        player2=str(input("Введите букву:"))
        if player2 in letters:
            index=letters.index(player2)
            space[index]=player2
            letters[index]='$'
        else:
            wrong+=1
        print(("".join(space)))
        e=wrong+1
        print("\n".join(stages[0:e]))

        if "_" not in space:
            print("NICE SHOT!")
            print(" ".join(space))
            win=True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("STUPID FUCKING NIGGA,BITCH! Было загаданно слово:{}".format(word))
            
words = ("ниггер", "белый","черный","оранжевый","синий","лермонтчерт","солнце","звездопад", "холодильник", "сметана", "циклоп", "циклон", "телефон", "звездочет", "карта", "атмосфера", "клоун", "смех", "трава", "утюг", "мороженое", "чернила", "кальмар", "каракатица", "луна", "ночь", "день", "космос")
hangman(random.choice(words))