#5. Given a sentence,count the vowels and consonants separately
sentence =input("Enter a sentence: ")
vowels ="aeiou"
vowelcount =0
consonantcount =0

for char in sentence.lower():
    if char.isalpha():
        if char in vowels:
            vowelcount += 1
        else:
            consonan_count += 1

print("Vowels:", vowelcount)
print("Consonants:", consonantcount)