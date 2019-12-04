def editDistance(str1, str2): 
    if len(str1) == 0: 
         return len(str2) 

    if len(str2) == 0: 
        return len(str1)
  
    if str1[-1]== str2[-1]: 
        return editDistance(str1[:-1], str2[:-1]) 
  
    return 1 + min(editDistance(str1, str2[:-1]),    # Insert 
                   editDistance(str1[:-1], str2),    # Remove 
                   editDistance(str1[:-1], str2[:-1])    # Replace 
                   ) 
  
str1 = "ASWIN"
str2 = "NIWSABaby"
print editDistance(str1, str2) 