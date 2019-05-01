# Bibliotecas #
import random

# Geração da senha #
key = random.randint(10000, 99999)

# Fatiamento da senha #
number1 = (int(str(key)[0]))
number2 = (int(str(key)[1]))
number3 = (int(str(key)[2]))
number4 = (int(str(key)[3]))
number5 = (int(str(key)[4]))
keyparts = (number1, number2, number3, number4, number5)

# Tentativa do usuário #
guess = int(input("Type the key (remember that the key never starts with 0): "))
while len(str(guess)) < 5:
    guess = int(input("Type the key (remember that the key never starts with 0): "))

# Fatiamento da tentativa #
guessn1 = (int(str(guess)[0]))
guessn2 = (int(str(guess)[1]))
guessn3 = (int(str(guess)[2]))
guessn4 = (int(str(guess)[3]))
guessn5 = (int(str(guess)[4]))
guessesparts = (guessn1, guessn2, guessn3, guessn4, guessn5)

# Gerando dicas #
play = 0
while guess != key and play < 10:
    if guessn1 not in keyparts:
        print (-1)
    if guessn1 != number1 and guessn1 in keyparts:
        print ( 0)
    if guessn1 == number1:
        print ( 1)
    if guessn2 not in keyparts:
        print (-1)
    if guessn2 != number2 and guessn2 in keyparts:
        print ( 0)
    if guessn2 == number2:
        print ( 1)
    if guessn3 not in keyparts:
        print (-1)
    if guessn3 != number3 and guessn3 in keyparts:
        print ( 0)
    if guessn3 == number3:
        print ( 1)
    if guessn4 not in keyparts:
        print (-1)
    if guessn4 != number4 and guessn4 in keyparts:
        print ( 0)
    if guessn4 == number4:
        print ( 1)
    if guessn5 not in keyparts:
        print (-1)
    if guessn5 != number5 and guessn5 in keyparts:
        print ( 0)
    if guessn5 == number5:
        print ( 1)
    play = (play) + 1

    guess = int(input("Type the key (remember that the key never starts with 0): "))
    while len(str(guess)) < 5:
        guess = int(input("Type the key (remember that the key never starts with 0): "))

    # Atualizando variáveis #
    number1 = (int(str(key)[0]))
    number2 = (int(str(key)[1]))
    number3 = (int(str(key)[2]))
    number4 = (int(str(key)[3]))
    number5 = (int(str(key)[4]))
    keyparts = (number1, number2, number3, number4, number5)
    guessn1 = (int(str(guess)[0]))
    guessn2 = (int(str(guess)[1]))
    guessn3 = (int(str(guess)[2]))
    guessn4 = (int(str(guess)[3]))
    guessn5 = (int(str(guess)[4]))
    guessesparts = (guessn1, guessn2, guessn3, guessn4, guessn5)

if play == 10:
    print ("You have used all your chances!")
if guess == key:
    print ("Congrats! You typed the corret key!")
    print (key)
  
    