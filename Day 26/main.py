import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dic = {row.letter:row.code for (index,row) in data.iterrows()}

word = input("Enter a word : ").upper()
nato = [data_dic[letter] for letter in wordj]
print(nato)
