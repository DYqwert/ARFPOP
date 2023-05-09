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


### step 4: pairwise_distance.py is a program to caculated the distance between pairwise sequences based on the formula 

python3 pairwise_distance.py input corenumber 

input file is the k-mer matrix, and the output file is a input file for MEGA (input.meg). The NJ-tree can directly be constrcted using MEGA.

### step 5: PCA analyses is used the function of PCA in package sklearn.decomposition.


### step 6: prepare the input file for LD pruning and population structure analyses

#generation of unique k-mer matix 
python3 unique_kmermatrix.py input output 
input file is the output file of step 2, and the output file the matrix only containing the k-mer with two copy number (0 and 1).  

#slection of reference k-mers
python3 select_referece.py input column output
input file output file of above step, column is the position of reference in the matrix, output file is the matrix only containing the k-mer only present in reference.

#generation of .map file and .ped file 
python3 map.py input1 input2 output
input1 is the output file of above step, input2 in the output file of step 1, output is the .map file. In the .map file, the location of k-mer is its extracted order in the sequence.  
python3 ped.py input output
input1 is the output file of above step, output is the .ped file

#The following LD pruning is performed by PLINK.
#After LD pruning, the population structure analyses will be performed by ADMIXTURE.

### step 7: Caculated the genetic diversity in a group

python3 diversity.py input output

input is the k-mer matrix, output is the value of θπ

### step 8: Indentification of a large frament variants among genome

python3 identify_indel.py input output

The input file is the unique k-mer matrix, and the output is the assemble fragment using pairwise adjacant k-mers. The size of k-mer fragment is large than 2k-1 bp is the potential indel fragment.  