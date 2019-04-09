class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
item1 = Item('clock', 175, 10)
item2 = Item('Painting', 90, 9)
item3 = Item('Radio', 20, 4)
item4 = Item('Vase', 50, 2)
item5 = Item('Book', 10, 1)
item6 = Item('Computer', 20, 10)

items = [item1, item2, item3, item4, item5, item6]
#20 agirlik miktarina kadar max degerde hirsizlik yap

def bombaci (items):
    items.sort(key=lambda item: item.value/item.weight)
    maxVal = items[-1].value
    calinan = []
    calinanAgirligi = 0
    for k in range(1,len(items)):
        for i in range (len(items)-1,-1,-1):
            weight = 20
            iterator = i
            val = 0
            calinanlar = []
            calinanAgirlikGecici = 0
            while iterator >=0:
                if weight - items[iterator].weight >= 0 :
                    weight -= items[iterator].weight
                    calinanAgirlikGecici += items[iterator].weight
                    val += items[iterator].value
                    calinanlar.append(items[iterator].name)
                    iterator -= k
                else:
                    iterator -= k
            if maxVal < val :
                maxVal = val
                calinan = calinanlar
                calinanAgirligi = calinanAgirlikGecici
    return(maxVal, calinanAgirligi, calinan)
bombaci(items)  
