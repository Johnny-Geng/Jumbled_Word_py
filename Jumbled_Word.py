# Johnny Geng, johnnyge@usc.edu

# Description:
# This program asks a person to figure out the right spelling for a randomly jumbled word.
#   If the player fail to come up the right answer 3 times,
#   a hint will automatically appear starting the 4th time forward. Also, if the player figure out the jumbled word
#   without the hint, he or she will score 5 points higher than if the player uses a hint.
import random

def main():

    fruit = ["apple","banana","peach","orange","watermelon","strawberry"]
    selection = random.choice(fruit)
    word_list = list(selection)
    new_list = []
    for letter in word_list:
        while len(word_list) != 0:
            random_letter = random.choice(word_list)
            letter = random_letter
            word_list.remove(letter)
            new_list.append(letter)
    word = "".join(new_list)
    print("The jumbled word is \"" + word +"\"")

    guess = input("Please enter your guess: ")
    count = 1
    while guess != selection:
        if count < 3:
            print("Try again.")
            guess = input("Please enter your guess: ")
            count = count + 1
        else:
            print("Try again.")
            print("(Hint: the word is a fruit name)")
            guess = input("Please enter your guess: ")
            count = count + 1
    print("You got it!")

    if count == 1:
        print("It took you " + str(count) + " try.")
    else:
        print("It took you " + str(count) + " tries.")

    if count < 4:
        print("Since you figure out the word without a hint, you get 10 points! (5 extra points) :)")
    else:
        print("Since you figure out the word with a hint, you only get 5 points.")

main()