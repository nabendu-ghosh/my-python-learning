STARTING_LETTER_FILE = "Beginner/mail_merge/Input/Letters/starting_letter.txt"
NAME_FILE = "Beginner/mail_merge/Input/Names/invited_names.txt"
OUTPUT_LOCATION = "Beginner/mail_merge/Output"

with open(NAME_FILE, "r") as name_file:
        names = [name.strip() for name in name_file]

with open(STARTING_LETTER_FILE, "r") as starting_letter_file:
    starting_letter = starting_letter_file.read()

for name in names:
    new_letter = starting_letter.replace("[name]", name)
    final_file = f"{OUTPUT_LOCATION}/letter_for_{name}.txt"
    with open(final_file,"w") as final_letter:
         final_letter.write(new_letter)