import random

def scoresAndGrades():

    for i in range(0,10):
        score = round(random.uniform(60,100))

        if(score >= 60 and score < 70):
            print 'Score:',score,'; Your grade is D'
        elif(score >= 70 and score < 80):
            print 'Score:',score,'; Your grade is C'
        elif(score >= 80 and score < 90):
            print 'Score:',score,'; Your grade is B'
        elif(score >= 90 and score <= 100):
            print 'Score:',score,'; Your grade is A'
scoresAndGrades()
