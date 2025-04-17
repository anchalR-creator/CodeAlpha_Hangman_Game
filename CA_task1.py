import random

name=input("Enter your name:")
print(f"Hello {name} ready to play a game..?")
print("GAME: ")
print("Theme of the game is : fruite kingdom")
print("You will have to keep guessing a letter each time to unlock a complete word .")
print("You will have five chances to guess the letter and unlock the word and win .")
print("LET'S START..! ")

words=['pineapple','blueberry','papaya','dragonfruite','guava','lychee','passionfruite','pomegranete','raspberry','kiwi']
word_choosen=random.choice(words)
letter_guess=[]
chances=5

print("_"*len(word_choosen))


while chances>0:
    guess=input("Guess a letter:").lower()

    if guess in letter_guess:
        print("you have already guessed that letter.")
        continue
    letter_guess.append(guess)
    
    if guess in word_choosen:
        print("correct")
    else:
        chances-=1
        print(f"WRONG! You have {chances} chances left .")
    display_word=[letter if letter in letter_guess else '_' for letter in word_choosen]
    print(" ".join(display_word))
    if '_' not in display_word:
        print("congratulations! you guessed the word!")
        print("YOU WIN!!")
        break
else:
     print(f"YOU LOST. The word was {word_choosen}.")
