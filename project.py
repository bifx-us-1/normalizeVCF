import sys

if len(sys.argv) != 6:
    print("Usage: python script.py sequence_file.txt sequence2_file.txt Pos Ref Alt")
    sys.exit(1)

# Read sequence from the first command line argument
sequence_filename = sys.argv[1]
with open(sequence_filename, "r") as file:
    sequence = file.read().strip()

# Read sequence2 from the second command line argument
sequence2_filename = sys.argv[2]
with open(sequence2_filename, "r") as file:
    sequence2 = file.read().strip()

# Parse Pos, Ref, and Alt from command line arguments
Pos = int(sys.argv[3])
Ref = sys.argv[4]
Alt = sys.argv[5]

# code for updating Pos based on conditions
if sequence[Pos - 3:Pos - 1] != "CA":
    Pos = 8
else:
    if sequence[Pos - 5:Pos - 3] != "CA":
        Pos = 6
    else:
        if sequence[Pos - 7:Pos - 5] != "CA":
            Pos = 4
        else:
            Pos = 2

# code for updating Ref and Alt based on conditions
if Alt == "":
    Pos -= 1
    Ref = sequence[Pos - 1] + Ref
    Alt = sequence[Pos - 1] + Alt

# Print the updated values
print("Updated Pos:", Pos)
print("Updated Ref:", Ref)
print("Updated Alt:", Alt)



