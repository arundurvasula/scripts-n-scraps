# This file will take a fasta file and generate fake reads from it
# read size is set to 36 base pairs
# overlap between reads is set to readsize-step (36 - 10)
from Bio import SeqIO
from Bio import Seq
from Bio.SeqRecord import SeqRecord

fragments = []
record = list(SeqIO.parse(open("../data/LR1-2014/GAP.txt"), "fasta"))
for i in record:
    sequence = '\n'.join(i.format('fasta').split('\n')[1:]) 
    sequence = sequence.replace("\n", "")
    start = 0
    step = 10
    readsize=36
    for i in range(0, len(sequence), step):
        fragments.append(sequence[i:i+readsize] + "\n")
final_output = []

fl = open("../data/LR1-2014/GAP-36-bp.txt", 'w')
for num,sequence in enumerate(fragments):
    out = '>fragment_%i' % (num) + "\n" + sequence
    fl.write(out)
