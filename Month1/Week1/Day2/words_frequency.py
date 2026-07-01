#2.Count the frequency of each word in a sentence using a dictionary.
sentence= "stars are in sky sky has stars"
words= sentence.split()
freq= {}

for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)