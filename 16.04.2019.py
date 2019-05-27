def maxVal(toConsider, avail):

    """Assumes toConsider a list of items, avail a weight
    Returns a tuple of the total value of a solution to the
    0/1 knapsack problem and the items of that solution"""


    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0][2] > avail:
        #Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],avail - nextItem[2])
        withVal += nextItem[1]
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result
    
item_1 = ['a',6,3]
item_2 = ['b',7,3]
item_3 = ['c',8,2]
item_4 = ['d',9,5]
items =[item_1,item_2,item_3,item_4]


maxVal(items,5)
