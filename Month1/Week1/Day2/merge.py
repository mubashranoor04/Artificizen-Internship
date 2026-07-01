#4. Merge two dictionaries (sum values)
dict1= {
    "x": 10,
    "y": 87
}
dict2= {
    "y" : 66,
    "z" : 7
}
merge= {}
for key in dict1:
    merge[key]=dict1[key]

for key in dict2:
    if key in merge:
        merge[key]+=dict2[key]
    else:
        merge[key]=dict2[key]
print(merge)