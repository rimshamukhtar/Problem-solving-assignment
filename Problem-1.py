#  Problem 1: Reverse a String
# Write a function that takes a string as input and returns the reversed string.

def reverse_string(s):
    return s[::-1]

# Test cases

input_string = "Hello Python"
output_string = reverse_string(input_string)
print("Original_string:", input_string)
print("Reverse_string:", output_string)

input_string = "Python plays a crucial role in Agentic AI"
output_string = reverse_string(input_string)
print("Original_string:", input_string)
print("Reverse_string:", output_string)