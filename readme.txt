# ARFPOP

ARFPOP is an alignment- and reference-free population genomics analyses program. 


ARFPOP requires Python >= 3.7.


### step 1: KNC.py is a program to count k-mers copy number in the genome.

python3 KNC.py input k output  

The input file is a .fa or .fna file, k is the k-mer length, and output file is a text file containing the k-mer, its copy number and its extracted order in the genome. In the pargram, the k-mers are extrated by a slide window approach with strip 1 bp, and the k-mer and its reverse complement sequences was count as the same k-mers to aviod the affected of the selection of the starting site and extracted direction.   

### step 2: Kmermatix.py is a program to merge output file that derived from different sample into a matrix.

python3 Kmermatrix.py input output

The input file is the output file of step1, and the output file is a m X n matrix. m is the number of all present k-mers. n is the number of genomes. The zero in the matrix stand for corresponding k-mer is missing in the genomes. 


### optional step 3: The user can based on filtering out some k-mer or not according to your own needs. The reason for filtering can consider our study or Fan et al. 2015.
python3 filtering.py input h1 n output 

The input file is the output file of step2, h1 is the copy number，a k-mer will be filtered out when the copy number of k-mer above h1, n is the number of sample，the output file only contained the k-mers that copy number less than h1. 

### step 4: pairwise_distance.py is a program to caculated the distance between pairwise sequences based on the formula 

python3 pairwise_distance.py input corenumber 

input file is the k-mer matrix, and the output file is a input file for MEGA (input.meg). The NJ-tree can directly be constrcted using MEGA.

### step 5: PCA analyses is used the function of PCA in package sklearn.decomposition.


### step 6: prepare the input file for LD pruning and population structure analyses

#generation of unique k-mer matix 
python3 filtering.py input 2 n output 
input file is the output file of step 2, h1 is set to 2, the output file the matrix only containing the k-mer with two copy number (0 and 1).  

#slection of reference k-mers
python3 select_referece.py input column output
input file output file of above step, column is the position of reference, output is the a matix of the k-mers that present in selected reference.

#added position information of k-mers

python3 loction.py input1 input2 output

input1 is the output file of step 1，this file contained the information of k-mer extracted order in genome. input2 is the k-mer matrix obtained from above step, output file is also a k-mer matrix.

#generated .ped and .maf file
python3 trans_pm.py input output

input is the file that obtained from above step, output is two file, one output.ped and the other is output.map

#the remaining step for LD pruning were performed by Plink, the structure was analyzed using admixture.

### step 7：cacualted genetic diversity

python3 Theta_calc.py input col1 col2 output

input file is k-mer matrix, col1 is begin of colum, and col2 is stop of colum, output is value of Theta.
