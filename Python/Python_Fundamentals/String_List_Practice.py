str = 'If monkeys like bananas, then I must be a monkey!'
print str.find('monkey')
print str.find('monkey',str.find('monkey')+1)

strNew = str.replace('monkey', 'alligator')
print strNew

x = [2,54,-2,7,12,98]
print max(x)
print min(x)

y = ['hello',2,54,-2,7,12,98,'world']
print y[0]
print y[len(y)-1]
