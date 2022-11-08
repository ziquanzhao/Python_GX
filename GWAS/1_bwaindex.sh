#!/bin/bash
/mnt/storage/zhaoziquan/GWAS/software/Bwa/bwa index -a bwtsw -p xsoindex /mnt/storage/zhaoziquan/KCS/基因组文件/
/mnt/storage/zhaoziquan/GWAS/software/samtools-1.15.1/bin/samtools faidx /mnt/storage/zhaoziquan/KCS/基因组文件/
java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CreateSequenceDictionary -REFERENCE /mnt/storage/zhaoziquan/KCS/基因组文件/ -OUTPUT xso-gene.fa.dict