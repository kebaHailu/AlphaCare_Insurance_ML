import csv 


# Input and Output paths 
input_txt = "../Data/MachineLearningRating_v3.txt"
output_csv = "../Data/dataset.csv"


# Read data from the output 
with open(input_txt, mode='r', encoding="utf-8") as file:
    lines = file.readlines()


# Process data
header = lines[0].strip().split('|') # extract header 
rows = [line.strip().split('|') for line in lines[1:]] # extract rows 


# write to csv file 
with open(output_csv, mode='w', newline="", encoding='utf-8') as file:
    writer = csv.writer(file) 
    writer.writerow(header)
    writer.writerows(rows)



print("Data Converted Successfully ")