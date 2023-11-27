def count_vowels(input_string):
    vowel_counts = {}
    input_string = input_string.lower()
    for char in input_string:
        if char in 'aeiou':
            vowel_counts[char] = vowel_counts.get(char, 0) + 1
    return vowel_counts
print("SJC22MCA-2027 - Georgekutty Biju\nS3MCA")
input_string = input("Enter a string: ")
vowel_counts = count_vowels(input_string)
for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")
