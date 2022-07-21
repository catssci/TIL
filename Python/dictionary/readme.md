## nitializing dictionary
```Python
keys = range(4)
new_dict = dict(zip(keys, ([] for _ in keys)))
  
print(new_dict)# performing append
# shows no error
new_dict[0].append('GeeksforGeeks')
      
# printing result
print ("New dictionary created : " + str(dict(new_dict)))
```
