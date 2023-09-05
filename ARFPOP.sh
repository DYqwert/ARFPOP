##!/bin/bash
##author: "Dai yi"
##date: "2023/8/1"
##ARFPOP
##ARFPOP is an alignment- and reference-free population genomics analyses program.
##ARFPOP requires Python >= 3.7.
ProjectDir=$1
k=$2
KNCDir=$3
h1=$4
n=$5
corenumber=$6
col1=$7
col2=$8

##echo "$0";
echo "working dir: $1";
echo "k: $2";
echo "KNCDir: $3";
echo "h1: $4";
echo "n: $5";
echo "cornumber: $6";
echo "col1: $7";
echo "col2: $8";

mkdir ${KNCDir}
for file_a in ${ProjectDir}/*
do
temp_file=`basename $file_a`
python3 KNC.py ${temp_file} ${k} ${KNCDir}${temp_file}.cv.txt
done
echo count k-mers copy number in the genome ...done

python3 Kmermatrix.py ${KNCDir} Kmermatrix
echo "merge output file that derived from different sample into a matrix ...done"

python3 filtering.py Kmermatrix ${h1} ${n} Kmermatrix_${h1}_${n}_filtering
echo "filtering out some k-mers ...done"

python3 pairwise_distance.py Kmermatrix_${h1}_${n}_filtering ${corenumber}
echo "caculated the distance between pairwise sequences based on the formula ...done"

python3 Theta_calc.py Kmermatrix_${h1}_${n}_filtering ${col1} ${col2} Theta
echo "cacualted genetic diversity ...done"

python3 trans_pm.py Kmermatrix_${h1}_${n}_filtering

plink --file Kmermatrix_${h1}_${n}_filtering --indep-pairwise 100 50 0.2 --out whole_genome_snp_LD --allow-extra-chr --make-bed --double-id
plink --file whole_genome_snp_LD --extract whole_genome_snp_LD.prune.in --out admixture --recode 12 --allow-extra-chr --double-id

for K in {2..22};
do 
echo "admixture --cv admixture.bed(admixture.ped) $K | tee log${K}.out" 
done >cmd.list

ParaFly -c cmd.list -CPU 21

## the best K = min(CV)
grep -h CV log*.out
echo "estimated population structure by ADMIXTURE ...done"

plink --allow-extra-chr --double-id \
  --threads 20 --file Kmermatrix_${h1}_${n}_filtering --pca 20 \
  --out pca 
echo "PPCA analysis ...done" 