# Function to calculate the sum from the first and last digit of a string
def calculate_sum(s):
    first_last_digit = ''
    for character in s:
        if character.isdigit():
            first_last_digit += character
            break
    for character in s[::-1]:
        if character.isdigit():
            first_last_digit += character
            break
    return int(first_last_digit) if first_last_digit else 0

# Dictionary to map spelled out numbers to their equivalent digits
spelled_numbers_to_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

# Function to replace spelled out numbers in a string with their equivalent digits
def replace_spelled_numbers(input_string):
    positions = []
    temp_string = input_string
    for spelled_number in spelled_numbers_to_digits:
        if spelled_number in input_string:
            first_pos = input_string.find(spelled_number)
            last_pos = input_string.rfind(spelled_number)
            positions.append((spelled_number, first_pos, last_pos))
    if positions:
        first_spelled_number = min(positions, key=lambda x: x[1])
        last_spelled_number = max(positions, key=lambda x: x[2])
        temp_string = temp_string[:first_spelled_number[1]] + spelled_numbers_to_digits[first_spelled_number[0]] + temp_string[first_spelled_number[1]+len(first_spelled_number[0]):last_spelled_number[2]] + spelled_numbers_to_digits[last_spelled_number[0]] + temp_string[last_spelled_number[2]+len(last_spelled_number[0]):]
    return temp_string

# Main execution
file = 'input.txt'
total_sum = 0
with open(file, 'r') as file:
    for line in file:
        line = replace_spelled_numbers(line)
        total_sum += calculate_sum(line.strip())
print(total_sum)
