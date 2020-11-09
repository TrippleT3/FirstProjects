import random
print('hello welcome to RPS tournament, where the winner gets nothing and the looser looses his dignity')
print('what is your name, for record keeping purposes')
name = input()
print('how many games of RPS do you want to play?')
gamesToPlay = int(input())
gamesplayed = 0
gamesWon = 0
gamesLost = 0
print('to make sure there is no issues with your choice, please use "r" for Rock, "p" for Paper, and "s" Scissors')

while gamesplayed < gamesToPlay:
    print('Round: '+ str(gamesplayed + 1))
    print('rock, paper, scissors, SHOOT')
    Playerchoice = input()
    ComputerChoice = random.randint(1,3)

    if Playerchoice == 'r':
        if ComputerChoice == 1:
            print ('you won this round')
            gamesWon = gamesWon + 1
        elif ComputerChoice == 2:
            print ('you tied this round')
        elif ComputerChoice == 3:
            print ('you lost this round')
            gamesLost = gamesLost + 1
    elif Playerchoice == 'p':
        if ComputerChoice == 1:
            print ('you tied this round')
        elif ComputerChoice == 2:
            print ('you lost this round')
            gamesLost = gamesLost + 1 
        elif ComputerChoice == 3:
            print ('you won this round')
            gamesWon = gamesWon + 1
    elif Playerchoice == 's':
        if ComputerChoice == 1:
            print ('you lost this round')
            gamesLost = gamesLost + 1
        elif ComputerChoice == 2:
            print ('you won this round')
            gamesWon = gamesWon + 1
        elif ComputerChoice == 3:
           print ('you tied this round')  
    else:
        print('you may have not noticed, but I did ask to use "r", "p", or "s", which you did not do, good job dingbat.')
    
    gamesplayed = gamesplayed + 1

    if gamesplayed == gamesToPlay:
        print('congrats on making it through the meat grinder, your win/loss:ratio is:')
        if gamesLost == 0:
            gamesLost = 0.0001
        print(str(gamesWon) + '/' + str(gamesLost) + ':' + str(gamesWon/gamesLost))
        if gamesWon/gamesLost < 1:
            print('wow ' + name + ' you suck. you wanna redeem yourself, or you just goanna go home with that sad look on your face (y for yes, n for no)')
            answer = str(input())
            if answer == 'y':
                print('ok, how many more rounds do you want to play?')
                answer = int(input())
                gamesToPlay = gamesToPlay + answer
            else:
                print('figures, you weekling, now get off my lawn before you make me throw up from your smell')
        else: 
            print('well look at that, I guess you arent the worst person at RPS Ive seen. go get your self a cofee or something.')

