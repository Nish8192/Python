def odd_even(x,y):
    for i in range(x,y+1):
        if(i%2 == 1):
            print 'Number is',i,'. This is an odd number.'
        else:
            print 'Number is',i,'. This is an even number.'
odd_even(1, 2000)
