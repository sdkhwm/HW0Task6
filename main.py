#This is the Task 8 of HW0
#this program reads a CSV file of bird names and randomly selects one
#list is from the american ornithological society website https://checklist.americanornithology.org/

import csv

with open('NACC_list_species.csv',mode='r') as csv_file:
    BirdFile = csv.reader(csv_file)




