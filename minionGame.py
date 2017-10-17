def minion_game(string):
    # your code goes here
    
    
    vowels = 'AEIOU'

    player1 = 0
    player2 = 0
    for i in range(len(string)):
        if string[i] in vowels:
            player1 += (len(string)-i)
        else:
            player2 += (len(string)-i)

    if player1 > player2:
        print "Player1", player1
    elif player1 < player2:
        print "Player2", player2
    else:
        print "Draw"


string = raw_input()
minion_game(string)