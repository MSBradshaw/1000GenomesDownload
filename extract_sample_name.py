import sys

# wget ftp://ftp.sra.ebi.ac.uk/vol1/run/ERR398/ERR3989317/NA12329.final.cram

for line in sys.stdin:
    sample = line.strip().split('/')[-1].split('.')[0]
    print(sample)
