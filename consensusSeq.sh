#!/bin/bash
#load path from .bash_profile
source /home/arun/.bash_profile
# given trimmed reads and a reference genome, extract a consensus sequence

set -e
set -u

refseq='/path/to/refseq'
trimmedreads='path/to/trimmed/reads.fasta'
alignmentsam='../results/alignment.sam'
alignmentbam='../results/alignment.bam'
alignmentsortedbam='../results/alignment.sorted.bam'
alignmentmappedsortedbam='../results/alignment.mapped.sorted.bam'
consensus='../results/consensusSeq.fastq'

bwa index -a bwtsw $refseq
bwa bwasw $refseq $trimmedreads > $alignmentsam
samtools view -bS $alignmentsam > $alignmentbam
samtools sort $alignmentbam $alignmentsortedbam
samtools view -b -F 4 $alignmentsortedbam > $alignmentmappedsortedbam
samtools index $alignmentmappedsortedbam
samtools mpileup -uf $refseq $alignmentmappedsortedbam | bcftools view -cg - | vcfutils.pl vcf2fq > $consensus
 
