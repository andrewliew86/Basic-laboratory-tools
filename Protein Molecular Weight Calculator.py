# this is an protein/peptide molecular weight calculator
from __future__ import division

# make a dictionary with each amino acid molecular weight
# amino acid weights taken from https://www.thermofisher.com/sg/en/home/references/ambion-tech-support/rna-tools-and-calculators/proteins-and-amino-acids.html
AA_list = {'A': 89.1, 'R': 174.2, 'N': 132.1,
           'D': 133.1, 'C': 121.2, 'E': 147.1,
           'Q': 146.2, 'G': 75.1, 'H': 155.2,
           'I': 131.2, 'L': 131.2, 'K': 146.2,
           'M': 149.2, 'F': 165.2, 'P': 115.1,
           'S': 105.1, 'T': 119.1, 'W': 204.2,
           'Y': 181.2, 'V': 117.1}

# input sequence of amino acids
sequence1 = '''
MIKATDRKLVVGLEIGTAKVAALVGEVLPDGMVNIIGVGSCPSRGMDKGGVNDLESVVKC
VQRAIDQAELMADCQISSVYLALSGKHISCQNEIGMVPISEEEVTQEDVENVVHTAKSVR
VRDEHRVLHVIPQEYAIDYQEGIKNPVGLSGVRMQAKVHLITCHNDMAKNIVKAVERCGL
KVDQLIFAGLASSYSVLTEDERELGVCVVDIGGGTMDIAVYTGGALRHTKVIPYAGNVVT
SDIAYAFGTPPSDAEAIKVRHGCALGSIVGKDESVEVPSVGGRPPRSLQRQTLAEVIEPR
YTELLNLVNEEILQLQEKLRQQGVKHHLAAGIVLTGGAAQIEGLAACAQRVFHTQVRIGA
PLNITGLTDYAQEPYYSTAVGLLHYGKESHLNGEAEVEKRVTASVGSWIKRLNSWLRKEF
'''
sequence_capital = sequence1.upper()  # capitalize all sequence inputs
sequence = list(sequence_capital.replace('\n', ''))  # split protein into a list of individual amino acids

# this loop counts all the molecular weights of the amino acids of the protein
MW_total = 0
for i in sequence:
    AA = AA_list.get(i)
    MW_total = MW_total+AA


# note: we have to take into account the loss of the water molecule during formation of peptide bonds.. which is why my initial MWs were wrong!!!
# see 'https://www.quora.com/What-is-the-approximate-molecular-weight-of-a-peptide-made-up-of-10-amino-acids-provided-the-molecular-weight-of-one-amino-acid-is-128' for more explanations

# calculating final molecular weight when taking into account loss of water molecule!
AA_length = len(sequence1.replace('\n', ''))  # length of the amino acid sequence input after removing whitespace etc..
waterMW = 18.015*(AA_length-1)  # number of peptide bonds and therefore the number of water molecules that were lost to form the protein. MW of water molecule is about 18.015 Da
MW_final = (MW_total-waterMW)/1000

print('Number of amino acids: '+str(AA_length))
print('MW: '+str(MW_final) + ' kDa')

# In the future, we can add other functionalities. For example, add a BLAST feature from Biopython

