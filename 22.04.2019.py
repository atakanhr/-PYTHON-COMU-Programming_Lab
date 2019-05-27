import random


def gaussion(x,mu,sigma):

  f_1=(1.0/(sigma*((2*pylab.pi)**0.5)))
  f_2=pylab.e**-(((x-mu)**2)/(2*sigma**2))

  return f_1*f_2

def rollDie():

  return random.choice([1,2,3,4,5,6])

def checkPascal(numTrials):

  numWins=0

  for i in range(numTrials):
    for j in range(24):

      d1=rollDie()
      d2=rollDie()
      if(d1==6 and d2==6):
        numWins+=1
        break  
  print(numWins/numTrials)

checkPascal(5)



class CrapsGame(object):
  def __init__(self):
    self.passWins,self.dpLosses,self.passLosses=0,0,0
    self.dpWins,self.dpLosses,self.dpPushes=0,0,0 
  
  def playHand(self):
  
    throw=rollDie()+rollDie()
    if(throw==7 or throw==11):
      self.passWins+=1
      self.dpLosses+=1

    elif(throw==2 or throw==3 or throw==12):
      self.passLosses+=1
      if (throw==12):
        self.dpPushes+=1
      else:
        self.dpWins+=1  
    else:
      point=throw
      while(True):
        throw=rollDie()+rollDie()
        if(throw==point):
          self.passWins+=1
          self.dpLosses+=1
          break
        elif(throw==7):
          self.passLosses+=1
          self.dpWins+=1  
          break         
    

c= CrapsGame()
döngü=100000
for i in range(döngü):
  c.playHand()

print(c.passWins/döngü)
