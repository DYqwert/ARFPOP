# ARFPOP

ARFPOP is an alignment- and reference-free population genomics analyses program. 


ARFPOP requires Python >= 3.7.
The entire analysis required 6 parameters. Include the folder where the sequence file suffix 'fa' or 'fna' resides, k-mer length k, minimum copy number h1, sample size n, column start, column end col2. Then, the output file is the input file of MEGA (input.meg) for building the NJ tree, adimixture analysis results, which displays population structure, PCA results, and nucleic acid diversity results.

Users can modify ARFPOP.sh internal parameters for custom analysis.
