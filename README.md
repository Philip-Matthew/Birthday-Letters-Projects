# Personalized Letter Generator

This script generates personalized letters by replacing a placeholder in a template letter with names from a text file.

## Directory Structure

```
./Input/
   ├── People/
   │   └── people.txt    # Contains list of names
   └── Letter/
       └── letter.docx   # Template letter with [name] placeholder

./Output/
   └── EditedLetters/    # Personalized letters will be saved here
```

## Input Files

1. **people.txt**: A text file containing names (one name per line).
2. **letter.docx**: A template letter with the placeholder `[name]` for inserting the names.

## Output

Personalized `.docx` letters will be saved in the `./Output/EditedLetters/` directory, with filenames in the format `letter_for_[name].docx`.

## Script

```python
PLACEHOLDER = "[name]"

with open("./Input/People/people.txt") as people:
    people_names = people.readlines()  # readlines() creates a list

with open("./Input/Letter/letter.docx") as letter:
    letter_contents = letter.read()

    for name in people_names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        
        with open(f"./Output/EditedLetters/letter_for_{stripped_name}.docx", mode='w') as completed_letter:
            completed_letter.write(new_letter)
```

## Example

### `people.txt`
```
Alice
Bob
Charlie
```

### `letter.docx`
```
Dear [name],

We are pleased to invite you to our event.

Best regards,
The Team
```

### Output Files
- `letter_for_Alice.docx`
- `letter_for_Bob.docx`
- `letter_for_Charlie.docx`
```
