import random


def intro():
    print()
    print("WELCOME TO HANGMAN\n")
    print("Instructions:\nGuess a single letter")
    print("Letters are represented by dashes (-) and spaces are represented by underscores (_)")
    print("You lose after 7 incorrect guesses\nYou win once you guess the word\n")


def random_word():
    # count_file = open("f1drivers.txt", "r")  # change file here
    count_file = open("movies.txt", "r")  # change file here
    count = len(count_file.readlines())
    count_file.close()
    # word_file = open("f1drivers.txt", "r")  # change file here
    word_file = open("movies.txt", "r")  # change file here
    word = word_file.readlines()[random.randint(0, count)]
    word_file.close()
    word = word.rstrip("\n")
    word = word.replace(" ", "_")
    return word


def theme():
    return "Movies"
    # return "Formula 1 Drivers"  # change theme here



def secret_phrase(word):
    secret_word = ""
    abc = "abcdefghijklmnopqrstuvwxyz"
    for letter in word:
        if letter.lower() in abc:
            secret_word += "-"
        else:
            secret_word += "_"
    return secret_word


def check_guess(guess, answer, secret_word):
    secret_word = list(secret_word)
    index = 0
    for letter in answer:
        if guess.lower() == letter.lower():
            secret_word[index] = guess
            index += 1
        else:
            index += 1
    secret_word = str(secret_word)
    secret_word = secret_word.replace("[", "")
    secret_word = secret_word.replace("]", "")
    secret_word = secret_word.replace(",", "")
    secret_word = secret_word.replace("'", "")
    secret_word = secret_word.replace(" ", "")
    return secret_word


def alphabet(guess):
    return guess.lower() in "abcdefghijklmnopqrstuvwxyz"


def results(secret_word, answer, wrong_answer):
    print("Your final answer was " + secret_word)
    if secret_word.lower() == answer.lower():
        return "You won!!\nYou had " + str(wrong_answer) + " incorrect guess(es)"
    else:
        return "You lost.\nThe correct answer was " + answer

