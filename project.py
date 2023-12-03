with open("sequence_file.txt", "r") as file:
    sequence = file.read().strip()

# Read sequence2 from text file
with open("sequence2_file.txt", "r") as file:
    sequence2 = file.read().strip()

# sequence="GGGCACACACAGGG"
# sequence2="GGGCACACAGGG"

Pos=8
Ref="CA"
Alt=""
#look at 6 and 7 in sequence, if 67 is not ca, position=8 else look at 45 if 45 is not ca, position=6 else look at 23 if 23 is not ca, position =4, else position=2
#if Alt="", postion -1, add character at the postion to prefix of ref, add character at the posotion to prefix of alt. 

if sequence[Pos-3:Pos-1] != "CA":
    Pos = 8
else: 
    if sequence[Pos-5:Pos-3] != "CA":
        Pos = 6
    else:
        if sequence[Pos-7:Pos-5] != "CA":
            Pos = 4
        else: Pos = 2

#print(Pos)
if Alt == "":
    Pos -= 1
    Ref = sequence[Pos-1] + Ref
    Alt = sequence[Pos-1] + Alt

# Print the updated values
print("Updated Pos:", Pos)
print("Updated Ref:", Ref)
print("Updated Alt:", Alt)



