import csv

# Open the input file
with open('test.txt', 'r') as input_file:
    # Read the entire contents of the file
    contents = input_file.read()

# Split the contents by the line breaks to get individual lines
lines = contents.split('\n')

# Create a list to hold the questions and options
questions = []

# Loop through each line
for line in lines:
    # Strip any leading or trailing whitespace
    line = line.strip()

    # If the line starts with a number and a period, it's a question
    if len(line) >= 2 and line[0].isdigit() and line[1] == '.':
        # rest of your code here

        # Add a new question to the list
        questions.append([line])
    # Otherwise, it's an option for the current question
    elif len(questions) > 0:
        # Add the option to the current question
        questions[-1].append(line)

# Open a CSV file for writing
with open('questions.csv', 'w', newline='') as output_file:
    # Create a CSV writer object
    writer = csv.writer(output_file)

    # Loop through each question
    for question in questions:
        # Write the question and each option as a separate row in the CSV
        writer.writerow(question)
