values=[]
def reverse(value):
    
    for i in range(len(value)-1,-1,-1):
        if isinstance(value[i],list)==False:
            values.append(value[i])
        else:
            deger=True
            for j in range(0,len(value[i])):
                if type(value[i][j])==int:deger=True
                else:deger=False
            if deger==True:values.append(value[i][::-1])
            else:reverse(value[i])
                
    return values
a=[[1, 2], [3, 4], [5, 6, 7]] #input
reverse(a)
