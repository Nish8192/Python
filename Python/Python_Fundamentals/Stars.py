
def draw_stars(x):
    for i in range(0,len(x)):
        y=0
        str = ''

        while(y<x[i]):
            str += '*'
            y+=1
        print str

x=[4,6,1,3,5,7,25]
draw_stars(x)

def draw_stars2(x):

    for i in range(0,len(x)):
        y=0
        str = ''
        if(type(x[i]) is int):
            while(y<x[i]):
                str += '*'
                y+=1
            print str

        else:
            while(y<len(x[i])):
                str += x[i][0]
                y+=1
            print str
y=[4,'Tom',1,'Michael',5,7,'Jimmy Smith']
draw_stars2(y)
