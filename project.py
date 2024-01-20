import argparse

def left_justify_variant_calls(sequence, Pos, Ref, Alt):
    # Code for updating Pos based on conditions
    if sequence[Pos - 3:Pos - 1] != "CA":
        Pos = 8
    elif sequence[Pos - 5:Pos - 3] != "CA":
        Pos = 6
    elif sequence[Pos - 7:Pos - 5] != "CA":
        Pos = 4
    else:
        Pos = 2

    # Code for updating Ref and Alt based on conditions
    if Alt == "":
        Pos -= 1
        Ref = sequence[Pos - 1] + Ref
        Alt = sequence[Pos - 1] + Alt

    return Pos, Ref, Alt

def main():
    parser = argparse.ArgumentParser(description='Perform left justification of variant calls.')
    parser.add_argument('sequence_file', type=str, help='Path to the sequence file')
    parser.add_argument('Pos', type=int, help='Position (integer) for the variant call')
    parser.add_argument('Ref', type=str, help='Reference sequence')
    parser.add_argument('Alt', type=str, help='Alternate sequence')

    args = parser.parse_args()

    # Read sequence from the first command line argument
    with open(args.sequence_file, "r") as file:
        sequence = file.read().strip()

    # Call the function to perform left justification
    updated_Pos, updated_Ref, updated_Alt = left_justify_variant_calls(sequence, args.Pos, args.Ref, args.Alt)

    # Print the updated values
    print("Updated Pos:", updated_Pos)
    print("Updated Ref:", updated_Ref)
    print("Updated Alt:", updated_Alt)

if __name__ == "__main__":
    main()

