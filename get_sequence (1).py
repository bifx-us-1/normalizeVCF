import requests

#Adam's edit

def retrieve_sequence_from_ucsc(genome, chrom, start, end):
    base_url = "https://api.genome.ucsc.edu/"
    endpoint = f"/getData/sequence?genome={genome};chrom={chrom};start={start};end={end}"

    try:
        response = requests.get(base_url + endpoint)
        response_json = response.json()
        
        if 'dna' in response_json:
            return response_json['dna']
        else:
            print("Error: DNA sequence not found in the response.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to retrieve sequence - {e}")
        return None

# Specify the region of interest
genome = "hg38"  # Genome assembly version
chrom = "chr17"  # Chromosome
start = 7571720  # Start position
end = 7578562    # End position

# Retrieve the DNA sequence
sequence = retrieve_sequence_from_ucsc(genome, chrom, start, end)

# Display the sequence if available
if sequence:
    print("DNA sequence for the region:")
    print(sequence)
