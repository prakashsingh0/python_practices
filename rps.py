# rock paper scissor

player1 = input("Please enter Player1's choice: ")

player2 = input("Please enter Player2's choice: ")
# if player1 == player2:
#     print("tie")
# elif (
#     (player1 == "rock" and player2 == "scissor")
#     or (player1 == "scissor" and player2 == "paper")
#     or (player2 == "rock" and player1 == "paper")
# ):
#     print("Player1 win!")
# elif( 
#     (player1 == "scissor" and player2 == "rock")
#     or (player1 == "paper" and player2 == "scissor")
#     or (player2 == "paper" and player1 == "rock")
# ):
#     print('player2 win!')


    #Refactor 1
# if player1 == 'rock' and player2 == 'scissor':
    # print('player1 win')
# elif player1 == 'paper' and player2 == 'rock':
    # print('Player1 win!')
# elif player1 == 'scissor' and player2 == 'paper':
    # print('Player1 win!')
# elif player2 == 'scissor' and player1 == 'paper':
    # print("Player2 win!")
# elif player2 == 'paper' and player1 == 'rock':
    # print("Player2 win!")
# elif player2 == 'rock' and player1 == 'scissor':
    # print("Player2 win!")

#Reractor 2
if player1 == 'rock':
    if player2 == 'scissor':
        print("Player1 win!")
    elif player2 == 'paper':
        print("Player2 win!")
elif player1 == 'paper':
    if player2 == 'rock':
        print("Player1 win!")
    elif player2 == 'scissor':
        print("Player2 win!")
elif player1 == 'scissor':
    if player2 == 'paper':
        print("Player1 win!")
    elif player2 == 'rock':
        print("Player2 win!")
