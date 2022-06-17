import glob

t="""aws s3 cp  --no-sign-request --recursive --exclude "*" --include "*.mapped*.bam" s3://1000genomes/phase3/data/{}/exome_alignment/ Bams/ """
t2="""aws s3 cp  --no-sign-request --recursive --exclude "*" --include "*.mapped*.bai" s3://1000genomes/phase3/data/{}/exome_alignment/ Bams/ """
for line in open('1000_genome_s3_ids.txt','r'):
    n = line.strip()
    if len(glob.glob('Bams/*{}*.bam*'.format(n))) == 0:
        print(t.format(n,n))
    if len(glob.glob('Bams/*{}*.bai*'.format(n))) == 0:
        print(t2.format(n,n))
