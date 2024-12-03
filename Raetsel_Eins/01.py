# Date: 2024/12/04

# Advent of code 2024
# Raetsel Eins

#import os
import pathlib 


# Define file and folder
file = 'file.txt'
folder = 'Raetsel_Eins'

# Construct the file path
file_path = pathlib.Path.cwd() / folder /file

# Print current working directory for debugging
print("Current working directory:", pathlib.Path.cwd())

# Initialize file_content
file_content = ''

# Check if the file exists
if file_path.exists():
    with file_path.open('r') as f:
        file_content = f.read()
else:
    print('File not found:', file_path)

# Initialize lists for storing columns
listA = []
listB = []

# Split each line into two columns and store them in listA and listB
for line in file_content.splitlines():
    parts = line.split()
    if len(parts) >= 2:  # Ensure there are at least two elements
        listA.append(int(parts[0]))  # First column
        listB.append(int(parts[1]))  # Second column

#print(listA)


#Challenge 01
def listsort(list):
    '''Sorts the list in ascending order'''
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] < list[j]:
                list[i],list[j]=list[j],list[i]
    return list

def listdistance(lista,listb):
    '''Sorts the list using listsort function 
    and then calculate the difference between the first element of list a and 
    first element of list b and returns the sum'''

    #sort the lists
    lista = listsort(lista)
    listb = listsort(listb)

    # counter to store the difference
    difference_list = 0
    for i in range(len(lista)):
        difference_list += abs(lista[i]-listb[i])
    return difference_list

print(listdistance(listA,listB))

#Challenge 02
def similarityscore(lista,listb):
    ''' Sorts the list using list sort function
        Calculate the similarity score by checking how many time element in list a appears in list b
        and multplies the element with the number of times it appears in list b
        and return the sum of the product'''
    
    #sort the lists
    lista = listsort(lista)
    listb = listsort(listb)

    # counter to store the similarity score
    similarity_score = 0
    for i in range(len(lista)):
        similarity_score += lista[i]*listb.count(lista[i])
    return similarity_score


print(similarityscore(listA,listB))

#end