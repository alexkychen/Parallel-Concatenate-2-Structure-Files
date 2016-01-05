#Concatenate R1 and R2 results for Structure files
from itertools import izip
#Enter files
R1_input = raw_input('Enter R1 file: ')
R2_input = raw_input('Enter R2 file: ')
R1_open = open(R1_input, 'r')
R2_open = open(R2_input, 'r')
#create an empty list to include all,including duplicates, for R1 and R2 files
R1R2_sample_pool = []
#create an empty list to store samples from R1 or R2 file
R1_samples = []
R2_samples = []

#for loop to find sample ID in R1 and R2 files, and append to lists
count = 0
for R1_line in R1_open:
	count = count + 1
	R1_sample = R1_line.split()[0]
	if count % 2 == 0:
		R1R2_sample_pool.append(R1_sample)
		R1_samples.append(R1_sample)
	else:
		continue

count1 = 0
for R2_line in R2_open:
	count1 = count1 + 1
	R2_sample = R2_line.split()[0]
	if count1 % 2 == 0:
		R1R2_sample_pool.append(R2_sample)
		R2_samples.append(R2_sample)
	else:
		continue
#print (R1R2_sample_pool)
#print (len(R1R2_sample_pool))

#create a list to store all samples either in R1 or R2 files
count2 = 0
R1R2_uniqueSamples = []
for each_sample in R1R2_sample_pool:
	if each_sample not in R1R2_uniqueSamples:
		count2 = count2 + 1
		R1R2_uniqueSamples.append(each_sample)
#print (R1R2_uniqueSamples)
#print (len(R1R2_uniqueSamples))

#Create a list that has common samples from R1 and R2
count3 = 0
R1R2_commonSamples = []
for one_sample in R1R2_uniqueSamples:
	if one_sample in R1_samples and one_sample in R2_samples:
		count3 = count3 + 1
		R1R2_commonSamples.append(one_sample)
#print (R1R2_commonSamples)
total_no_sample = len(R1R2_commonSamples)

#Create temporary files to write
commonSamples_R1 = open('tempFileR1.txt', 'w')
commonSamples_R2 = open('tempFileR2.txt', 'w')

R1_open = open(R1_input, 'r')
R1_temp_list = []
for R1_line in R1_open:
	if R1_line.split()[0] in R1R2_commonSamples:
		R1_temp_list.append(R1_line)
R1_temp_list = sorted(R1_temp_list)
for R1_item in R1_temp_list:
	commonSamples_R1.write(R1_item)
commonSamples_R1.close()

R2_open = open(R2_input, 'r')
R2_temp_list = []
for R2_line in R2_open:
	if R2_line.split()[0] in R1R2_commonSamples:
		R2_temp_list.append(R2_line)
R2_temp_list = sorted(R2_temp_list)
for R2_item in R2_temp_list:
	commonSamples_R2.write(R2_item)
commonSamples_R2.close()

#Merge R1 and R2 temporary files
with open('tempFileR1.txt', 'r') as f1, open('tempFileR2.txt', 'r') as f2, open('StructureInput_R1R2comb.txt','w') as res:
	for line1, line2 in izip(f1,f2):
		temp_list = []
		#split a line into a list
		line1_ls = line1.split()
		line2_ls = line2.split()
		#count total number of loci
		R1_no_loci = len(line1_ls) - 1
		R2_no_loci = len(line2_ls) - 1
		total_no_loci =  R1_no_loci + R2_no_loci
		#append item into temporary list
		temp_list = line1_ls #take a line of R1 to the list
		temp_list[len(line1_ls):] = line2_ls[1:] #take a line of R2 (remove sample id) to the list
		res.write(temp_list[0])#write sample id to file
		for i in temp_list[1:]:
			res.write('\t')
			res.write(i.rstrip())
		res.write('\n')

print ('R1 has %d loci' %R1_no_loci)
print ('R2 has %d loci' %R2_no_loci)
print ('Total number of loci is %d' %total_no_loci)
print ('Total number of individuals is %d' %total_no_sample)
