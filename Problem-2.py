#  Problem 2: Count Vowels in a String

# Write a function that counts the number of vowels (a, e, i, o, u) in a string (case-insensitive).

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
        if char in vowels:
         count += 1
    return count
    
    #  Test cases

print(count_vowels("Python"))
print(count_vowels("suggestions"))
print(count_vowels("Agentic AI"))
print(count_vowels("Generative AI"))
    