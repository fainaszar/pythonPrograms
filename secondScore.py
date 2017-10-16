students = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    students.append([name,score])

    print "Student List is :\n %r" % students
    
    minScore = 999.99
    for student in students:
        if student[1] < minScore:
            minScore= student[1]


    print "Minimum Score is: %r" % minScore
          
    diff = 999
    names=[]
    for student in students:
        if (student[1] - minScore < diff) and (student[1]-minScore!= 0):
            diff = student[1]-minScore
            score = student[1]

    print "Second smallest score is: %r" % score
    for student in students:
        if student[1] == score:
            if names.count([students[0]]) == 0:
                names.append(student[0])
            
    names.sort()

    print names
    for name in names:
        print name
            
    
