# Parallel-Concatenate-2-Structure-Files
Parallel concatenate 2 large Structure input files for population genetic analysis.

1. Combine two Structure input files that have different set of loci but have same individuals (or partially same). 
2. The program will find and output the common samples (individuals) in two Structure files. For example, if one file has sample id A, B, C, D, E, and the other has B, C, D, E, F, the concatenated file will have sample B, C, D, and E. Sample A and F will be excluded.
3. All the loci from two Structure files will be concatenated. Locus name will not be included. 
4. Your input Structure files should include one head line (usually locus names)

To run the script,

1. Download 'concatenateStructure.py' file and save it under the folder that has your Structure files. 
2. Open terminal or command prompt and change path to the folder (using 'cd your_path_to_folder').
3. Then enter 'python concatenateStructure.py' to execute the script.
4. It will then ask you to enter the Structure file names (R1 and R2). And hit enter.
5. The program will start concatenate two files and print out numbers of loci and individuals in the console.



