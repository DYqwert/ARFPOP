# ARFPOP

ARFPOP is an alignment- and reference-free population genomics analyses program. 


ARFPOP requires Python >= 3.7.
The entire analysis is done by executing ARFPOP.sh. 6 parameters were required, including the folder where the sequence file suffix 'fa' or 'fna' resides, k-mer length k, minimum copy number h1, sample size n, column start, column end col2. Then, the output file is the input file of MEGA (input.meg) for building the NJ tree, adimixture analysis results, which displays population structure, PCA results, and nucleic acid diversity results.

For example, I put 10 sample sequence files in the folder ./sampledata/ and set k value to 4, filtering minimum kmer copy number to 0, and set CPU number to 10.
Just run the code:

sh ARFPOP.sh ./sampledata/ 4 KNCDir 0 10 10

The output file will then be generated under the current folder. The KNCDir folder holds the original file of the kmers copy of each sample in *.cv.txt.

Users can modify ARFPOP.sh internal parameters for custom analysis.
