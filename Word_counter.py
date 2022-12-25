# Word counter 
# d = {'a' : 1, 'h' : 2} 
# h = 2


# d =  {'S' : 2, "U" : 1}
# print(d)


def Word_Counter(s):
    count={}
    for char in s:
        count[char] = s.count(char)
    return count
print(Word_Counter("SuShant"))