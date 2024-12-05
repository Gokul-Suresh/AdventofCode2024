import re
import pathlib 


# Define file and folder
file = 'file4'
folder = 'Raetsel_Vier'

# Construct the file path
file_path = pathlib.Path.cwd() / folder /file

# Print current working directory for debugging
print("Current working directory:", pathlib.Path.cwd())

# Initialize file_content
data = []

# Check if the file exists
if file_path.exists():
    with file_path.open('r') as f:
        data = f.read()
else:
    print('File not found:', file_path)

print(data)
# Day 4 
   
def find_word(word, grid):
    # Convert to lowercase for case-insensitive search
    word = word.lower()
    word_length = len(word)
    count = 0

    # Define directions: (row_step, col_step)
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # down-right
        (-1, -1), # up-left
        (1, -1),  # down-left
        (-1, 1)   # up-right
    ]
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):  # Ensure you use len(grid[0]) for column length
            for dr, dc in directions:
                if all(0 <= r + dr*i < len(grid) and 0 <= c + dc*i < len(grid[0]) and grid[r + dr*i][c + dc*i].lower() == word[i] for i in range(word_length)):
                    count += 1

    return count


# Read the file content
grid = data

# Word to find
word_to_find = 'XMAS'

# Find XMAS occurrences
xmas_count = find_word(word_to_find, grid)
print(f"Total occurrences of '{word_to_find}':", xmas_count)