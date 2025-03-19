with open("Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    lines = starting_letter.read()

with open("Input/Names/invited_names.txt", mode="r") as invited_names:
    names = invited_names.readlines()
    for name in names:
        stripped_name = name.strip()
        new_letter = lines.replace("[name]", stripped_name)
        output = open(f"Output/ReadyToSend/{stripped_name} letter", mode="w")
        output.write(new_letter)
        output.close()
