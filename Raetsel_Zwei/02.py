# 02/12/24

#Raetsel_Zwei
import pathlib

# Define file and folder
file = 'file2.txt'

# Construct the file path
file_path = pathlib.Path.cwd() / file

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

# Split each line into rows and store them in listA
if file_content:
    for line in file_content.splitlines():
        parts = line.split()
        if len(parts) >= 1:  # Ensure there is at least one element
            listA.append([int(i) for i in parts])  # Append all elements in line


def safeorunsafe(puzzle_input):
    ''' Checks if elements in the list are safe or unsafe based on two rules:
        1, All the element in rows are either in ascending or descending order
        2. Any two element in the same row differ by atleas 1 and atmost 3
        '''
    saferow = 0
    # Check each row in the puzzle input
    for row in puzzle_input:
        # Check if the row is sorted in ascending or descending order
        if row == sorted(row) or row == sorted(row, reverse=True):
            # Check if all consecutive elements differ by at least 1 and at most 3
            if all(1 <= abs(row[i] - row[i+1]) <= 3 for i in range(len(row) - 1)):
                saferow += 1
        else:
            print('Row is unsafe:', row)

    return saferow

print(safeorunsafe(listA))