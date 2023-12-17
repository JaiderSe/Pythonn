def mysplit(strng):
    my_list=[]
    i=0
    word=''
    for caracter in strng:
        
        if caracter.isspace():
                if word!='':
                    my_list.insert(i, word)
                    word=''
                    i+=1
        if caracter.isalnum():
            word+=caracter
    
    if word!='':my_list.insert(i, word)        
    return my_list
            

print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
    
