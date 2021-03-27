import sys
!{sys.executable} -m pip install pysam

import pysam
AlignmentFile = pysam.AlignmentFile("merged-tumor.bam", "rb")

#Number of unmapped reads
num_of_unmapped = AlignmentFile.unmapped
print("Number of unmapped: " + str(num_of_unmapped))

#Total number of reads
number_of_reads = AlignmentFile.count()
print("Number of reads: " + str(number_of_reads))

#list_of_shit = ["hello" for fr in AlignmentFile.fetch() if fr.mapping_quality == 0]
#print("NOVI Number of reads with mapping quality 0: " + str(len(list_of_shit)))

number_of_reads_map_quality_zero = 0
number_of_reads_without_zero_map_quality = 0
mapping_quality_sum = 0
filtered_mapping_quality_sum = 0

for fr in AlignmentFile.fetch():
    if(fr.mapping_quality == 0):
        number_of_reads_map_quality_zero = number_of_reads_map_quality_zero + 1
    else:
        number_of_reads_without_zero_map_quality = number_of_reads_without_zero_map_quality + 1
        filtered_mapping_quality_sum = filtered_mapping_quality_sum + fr.mapping_quality
    mapping_quality_sum = mapping_quality_sum + fr.mapping_quality 

print("Number of reads with mapping quality 0: " + str(number_of_reads_map_quality_zero))
    
average_mapping_quality = mapping_quality_sum/number_of_reads
print("Average mapping quality: " + str(average_mapping_quality))

filtered_mapping_quality = filtered_mapping_quality_sum/number_of_reads_without_zero_map_quality
print("Filtered mapping quality: " + str(filtered_mapping_quality))

AlignmentFile.close()
