import random
def coinToss(x):
    heads = 0
    tails = 0
    for i in range(1,x+1):
        result = round(random.random())
        if(result == 1):
            heads+=1
            print 'Attempt #:',i,'Throwing a coin... It is heads!... Got',heads,'head(s) so far and',tails,'so far'
        else:
            tails+=1
            print 'Attempt #:',i,'Throwing a coin... It is tails!... Got',heads,'head(s) so far and',tails,'so far'

coinToss(5000)
