
import pandas as pd

df = pd.read_csv("Day26_NATO_Alphabet_project/nato_phonetic_alphabet.csv")

df_dic = {row.letter: row.code for (index, row) in df.iterrows()}
print(df_dic)

user_input = input("Type a word: ").upper()
for char in user_input:
    print(df_dic[char])
