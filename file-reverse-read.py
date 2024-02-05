# Open the file in read mode
file_path = 'Misc.txt'  # Replace with your file path
with open(file_path, 'r') as file:
    # Read the content of the file into a list, splitting by lines
    lines = file.readlines()
    

# Reverse the list to read it in reverse order
lines.reverse()

# Iterate through the reversed lines and process them
for line in lines:
    print(line.strip())  # Print or process each line as needed

