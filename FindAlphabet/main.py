import pandas as pd
"""
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass
"""
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary
data = pd.read_csv("./nato_phonetic_alphabet.csv")

alphabet_list = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.


def generate_list():
    user_asked = input("Type a word: ").upper()
    try:
        words = [alphabet_list[item] for item in user_asked]
    except KeyError:
        print("An illegal word was entered.")
        generate_list()
    else:
        print(words)

        
generate_list()
