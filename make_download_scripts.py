t="""aws s3 cp  --no-sign-request --recursive --exclude "*" --include "*.mapped*.bam" s3://1000genomes/phase3/data/{}/exome_alignment/ Bams/ """
t2="""aws s3 cp  --no-sign-request --recursive --exclude "*" --include "*.mapped*.bai" s3://1000genomes/phase3/data/{}/exome_alignment/ Bams/ """
for line in open('1000_genome_s3_ids.txt','r'):
    n = line.strip()
    with open('DownloadScripts/{}_download.sh'.format(n),'w') as outfile:
        outfile.write(t.format(n,n) + '\n')
        outfile.write(t2.format(n,n))
    print(t.format(n,n))
    print(t2.format(n,n))
