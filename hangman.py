import random
death_count = 0
used = set()
word_list = ["people", "history", "world", "information", "family", "government", "health", "system", "computer", "meat", "year", "music", "person", "theory", "bird", "literature", "problem", "software"]
word = random.choice(word_list)
word_letters = set(word)
letter_count = 0

while (letter_count != len(word_letters)) and death_count < 10:
    
    guess = input("Guess a letter: ")
    print("")
    used.add(guess)

    if guess in word:
        print(f"Your letter {guess} is in the word!")
        letter_count += 1
    else:
        print(f"Your letter {guess} is not in the word")
        death_count += 1 
    
    current_word = [i if i in used else "-" for i in word]

    print(f"You have used these letters: ", "".join(used))
    print(f"Your tries: {death_count}/10")
    print(f"current word: ", "".join(current_word))
    print("")

    if letter_count == len(word_letters):
        print("Congratulations! You won!")
    if death_count == 10:
        print(f"Sorry! You lost. The word was: {word}")
