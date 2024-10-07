PLACEHOLDER = "[name]"

with open("./Input/People/people.txt") as people :
    people_names = people.readlines() #readlines() creates a list
    # print(people_names)

with open("./Input/Letter/letter.docx") as letter:
    letter_contents = letter.read()
    # print(letter_content)
    for name in people_names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/EditedLetters/letter_for_{stripped_name}.docx", mode='w') as completed_letter:
            completed_letter.write(new_letter)