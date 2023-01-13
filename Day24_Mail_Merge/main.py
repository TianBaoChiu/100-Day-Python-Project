# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
names = []
with open("input/Names/invited_names.txt", mode='r') as f:
    name_list = f.readlines()
for name in name_list:
    name_strip = name.strip()
    names.append(name_strip)

print(names)

with open("input/Letters/starting_letter.txt", mode='r') as f:
    sample_letter = f.read()
print(sample_letter)

for name in names:
    customize = sample_letter.replace("[name]", name)
    print(customize)
    with open(f"Output/Letter_for_{name}.txt", mode='w') as f:
        f.write(customize)
