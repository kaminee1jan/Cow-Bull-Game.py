import random
rand=[]
i=0
while i<5:
    randint=random.randint(0,9)
    if randint not in rand:
        rand.append(randint)
        i=i+1
secret_word=rand
print(secret_word)
def game():
    cow=[]
    bull=[]
    i=1
    while True:
        guess=int(input("enter any number="))
        position=int(input("enter any position="))
        if guess in secret_word:
            if secret_word.index(guess)==position:
                bull.append(guess)
                print("you choice correct word and correct position")
            else:
                cow.append(guess)
                print("you choice correct words but position is wrong")
        else:
            print("guess is not in secret word")
        if bull==secret_word:
            print("*****you won the game******")
            break
        if i==10:
            print("ur loose the game.....!")
            print("***********************")
            break
        i=i+1
        print("***************************************")
    print("cow","=",cow)
    print("*************************")
    print("bull","=",bull)
game()