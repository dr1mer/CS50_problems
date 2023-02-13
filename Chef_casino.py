# The game Chef is going to play in the casino consists of tossing a die with N faces twice
# There is a number written on each face of the die (these numbers are not necessarily distinct).
# In order to win, Chef must get the number A on the first toss and the number B on the second toss of the die

# eg input: 
# 2
# 5 1 1
# 1 1 1 1 1
# 2 1 1
# 1 2

t = int(input()) # number of test cases
for i in range(t):
    N, A, B = map(int, input().split()) # N - faces
    x=list(map(int, input().split())) # the numbers written on the faces of the die 
    p1=0 #prob of first toss
    p2=0 #prob of second
    for j in x: 
        if j==A: 
            p1+=1
        if j==B:
            p2+=1
    ans=(p1/N)*(p2/N)
    print(f"{ans:.10f}")
    
# output:
# 1.0000000000
# 0.2500000000
