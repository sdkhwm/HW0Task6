#This is the Task 8 of HW0
#this program reads a CSV file of bird names and randomly selects one
#list is from the american ornithological society website https://checklist.americanornithology.org/

import numpy as np
import pandas as pd

N=np.random.randint(0,2201)


BirdData = pd.read_csv('NACC_list_species.csv')


print(BirdData.common_name[N])
#testing merging