
while True:
    sentence = input("Enter a sentence: ")
    target_vowel = input("Enter a vowel to search for (A, E, I, O, U): ")

    found = False

    for character in sentence:
        if character.lower() == target_vowel.lower():
            found = True
            break
    if found:
        print("Vowel Found")
    else:
        print("Vowel not Found")

    again = input("Try again? (Y/N): ")

    if again.upper() != "Y":
        break

