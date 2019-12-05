def editDistance(str1, str2, memo): 
    if len(str1) == 0:
        return len(str2)

    if len(str2) == 0: 
        memo[len(str1)][0]=len(str1)  
        return memo[len(str1)][0] 
  
    if memo[len(str1)-1][len(str2)-1] != None :
        return memo[len(str1)-1][len(str2)-1]

    if str1[-1]== str2[-1]: 
        memo[len(str1)-1][len(str2)-1] = editDistance(str1[:-1], str2[:-1],memo) 
        return memo[len(str1)-1][len(str2)-1]

    memo[len(str1)-1][len(str2)-1] =  1 + min(editDistance(str1, str2[:-1] , memo),    # Insert 
                editDistance(str1[:-1], str2, memo),    # Remove 
                editDistance(str1[:-1], str2[:-1], memo)    # Replace 
                )
    return memo[len(str1)-1][len(str2)-1]  

  
str1 = "ASWIN"
str2 = "HelloWORLDWIN"
memo=[[None for i in xrange(1000)] for k in xrange(len(str1)+1)]
print editDistance(str1, str2 , memo) 