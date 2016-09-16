# Parallel-Concatenate-2-Structure-Files
Parallel concatenate two STRUCTURE files for population genetic analysis.

This program written in Python allows you to concatenate two STRUCTURE format files that have common individuals (or partially common) but different loci to a single STRUCTURE file. The progam will identify and output identical (based on individual ID) individuals in two STRUCTURE files to the new concatenated file. Individuals that only exist in one of the files will be automatically disregarded. For example, if one file has individuals A, B, C, D, and the other file has individuals B, C, D, E, individuals A and E will not be included in the new concatenated file.

### Note: 
1. All the loci from two STRUCTURE files will be concatenated. Locus or marker name will not be printed in the new file.
2. Your input STRUCTURE files should include one head line (usually locus name)

### How to use:
1. Download 'concatenateStructure.py' file and save it under the folder that has your Structure files. 
2. Open terminal or command prompt and change path to the folder (using 'cd your_path_to_folder').
3. Then enter 'python concatenateStructure.py' to execute the script.
4. It will then ask you to enter the Structure file names (R1 and R2). And hit enter.
5. The program will start concatenating two files and print out numbers of loci and individuals in the console.
6. The out file will be saved as 'StructureInput_R1R2comb.txt' under the folder



