#  Problem 3: Sum of Digits

# Write a function that takes a non-negative integer and returns the sum of its digits.


def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Test cases

print(sum_of_digits(1234))  
print(sum_of_digits(546))
print(sum_of_digits(108))