input_file = "valid.mnemonicsb.txt"
output_file = "mnemonics.txt"

with open(input_file, 'r') as file:
    lines = file.readlines()

mnemonics = [line.split(':')[0].strip('{} \n"') for line in lines]

with open(output_file, 'w') as file:
    file.write('\n'.join(mnemonics))

print("Mnemonics extracted and saved to 'mnemonics.txt' file.")
