This dirrectory is dedicated to downloading the 1000 Genomes Exomes in the most efficient way possible.

**Warning**: all the bam and bai files for the ~3000 files totals ~30TB of data. Storing this much data may be expensive. I recommend not keeping it longer than necessary.


A few things are required to do this
1. 1000_genome_s3_ids.txt - a list of the 1000 Genomes ids to be downloaded
2. make_download_scripts.py - script that produces one aptly named script with the commands to download the bam and bai for a given sample
3. get_1000_genomes.snake - a snakemake pipeline for governing the downloading process, uses the previous 2 files


Example command of how to start the download pipeline
`rj -t 96:00:00 -n '1k_G_download' -T 64 -m 500G -p long -c 'snakemake -s get_1000_genomes.snake --cores 64'`


`check_downloads.py` is a usefull script to check and ensure everything was downloaded properly


`Sequence_Index_Exploration.ipynb` was created to selected a set of samples perfectly balanced by sex and demographics that all used the same capture technology. This is important so CNVkit can be used and fair comparisons can be made across callers.
