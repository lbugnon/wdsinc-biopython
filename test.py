from Bio import SeqIO
import tqdm
import os

seq = "guuucaaauuugggccaaaguuuggcaagaguugggugaaacuuggguuagacuuugguaaagcuugaauccaaguuuugccaaagucuugccuaacuuuugcccaaguuuagaca"
with open("tmp.fa", "w") as fout:
    fout.write(">seq_name\n%s\n" % (seq))

os.system("RNAfold --noPS --infile=tmp.fa --outfile=tmp.fold")


with open("tmp.fold") as fin:
    for line in fin:
        print(line)

print("all ok")
