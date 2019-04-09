#Size verilen bozukluk listesi ve para ustu degiskenleriyle en az sayida madeni para ile verilebilecek para ustunu hesaplayan kodu yaziniz

bozukluklar = [1,5,10,21,25,50]
def recMC(coinValueList,change,knownResults):
    minCoins = change
    
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else :
        for i in [c for c in coinValueList if c<= change]:#bozuk para listesi olustur
            numCoins = 1 + recMC(coinValueList, change-i,knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins
recMC(bozukluklar, 40,[0]*41)
recMC(bozukluklar,99,[0]*124)
