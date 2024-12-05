import re
import pathlib 


# Define file and folder
file = 'file3'
folder = 'Raetsel_Drei'

# Construct the file path
file_path = pathlib.Path.cwd() / folder /file

# Print current working directory for debugging
print("Current working directory:", pathlib.Path.cwd())

# Initialize file_content
data = ''

# Check if the file exists
if file_path.exists():
    with file_path.open('r') as f:
        data = f.read()
else:
    print('File not found:', file_path)


def extract_valid_instructions(input_data):
    # Find all instances of 'mul(x, y)' pattern with exact syntax
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, input_data)
    return [(int(x), int(y)) for x, y in matches]

def solve_day3_updated(input_data):
    # Extract valid multiplication instructions using regex
    valid_instructions = extract_valid_instructions(input_data)
    results = []
    
    for x, y in valid_instructions:
        product = x * y
        results.append(product)
    
    # Aggregate the results by summing them
    final_result = sum(results)
    return final_result

# Example usage:
input_data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
#print(solve_day3_updated(input_data))  # Output will be 161
print(solve_day3_updated(data))