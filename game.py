import hangmantools
import extras

hangmantools.intro()
print("The theme is " + hangmantools.theme() + "\n")

answer = hangmantools.random_word()
# print(answer)

secret_word = hangmantools.secret_phrase(answer)
print(secret_word)

wrong_answer = 0
letters_guessed = ""

while secret_word.lower() != answer.lower() and wrong_answer != 7:
    guess = input("Enter a letter: ")
    if guess in letters_guessed:
        print("You have already guessed this letter.\nPlease try again.")
        print("\nGuessed Letters: " + letters_guessed + "      Lives Remaining: " + str((7 - wrong_answer)) + "\n")
        print(secret_word + "\n")
        extras.gallows(wrong_answer)
    elif hangmantools.alphabet(guess):
        print("You guessed " + guess)
        temp_word = secret_word
        secret_word = hangmantools.check_guess(guess, answer, secret_word)

        if temp_word == secret_word:
            wrong_answer += 1
            print("Your guess is incorrect.\n")
        else:
            print("Your guess is correct!\n")
        letters_guessed += guess
        extras.gallows(wrong_answer)
        print("\nGuessed Letters: " + letters_guessed + "      Lives Remaining: " + str((7 - wrong_answer)))
        print("\n" + secret_word + "\n")
    else:
        print("You entered an illegitimate character.\nPlease try again.\n")
        print(secret_word + "\n")
        extras.gallows(wrong_answer)
print(hangmantools.results(secret_word, answer, wrong_answer))
