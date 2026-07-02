#3. Use filter() to extract all strings longer than 5 characters from a list.
str= ["channel","ysl", "jw pei","miu miu", "Prada", "Gucci"]
result= filter(lambda x: len(x)<5, str)
print(list(result))