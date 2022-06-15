def formatedlist(cart):
    rangenum = int(len(cart)/5)
    cart = list(cart)
    templist = []
    formatedlist = []
    
    for i in range(rangenum):
        templist.append(i)
        for j in range(0,5):
            
            templist.append(cart[j])
        for a in range(0,5):
            cart.pop(0)
        
        
        formatedlist.append(templist)
        templist = []

    return formatedlist