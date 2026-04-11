import pandas

file_path = "Beginner/nato_alphabets/nato_phonetic_alphabet.csv"
nato_alphabets_data = pandas.read_csv(file_path)
nato_alphabets_dict = {row.letter:row.code for (index, row) in nato_alphabets_data.iterrows()}
end = False

while not end:
    user_input = [letter for letter in input("Enter a word: ").upper()]
    try:
        output_nato_alphabet = [nato_alphabets_dict[letter] for letter in user_input]
    except KeyError:
        print("Please only include letters in alphabets")
    else:
        print(output_nato_alphabet)
        end = True