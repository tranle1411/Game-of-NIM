import AlphaBeta

#Inputs
n = int(input("Welcome to the game of NIM! Pick the total number of sticks (greater than 0): "))
while n<=0: n = int(input("Invalid number! Pick again: "))
x = int(input("Good! Now pick the maximum number of sticks to pick each turn (between 0 and  " + str(n) + "): "))
while x<=0 or x>n: n = int(input("Invalid number! Pick again: "))

#Game loop
while n>0:
    p = AlphaBeta.AlphaBeta(n, x)
    computer_pick = p.alphabeta()
    n -= computer_pick
    print("I'm going to pick ", computer_pick , " stick(s). The remaining number of stick is ", n, ".")
    if(n==0):
        print("Computer wins! Haha!")
        exit(0)
    else:
        human_pick = int(input("How many stick(s) are you picking?: "))
        while human_pick<=0 or human_pick>n: human_pick = int(input("Invalid number! Pick again: "))
        n -= human_pick
        if(n==0):
            print("You win! Are you happy now? :(")
            exit(0)
            
    