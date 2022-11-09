values=[]
def flatten(value):
    
    for i in value:
        if isinstance(i,list)==False:
            values.append(i)
        else:
            flatten(i)
    return values
