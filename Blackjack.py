import random
import os




CARDS  =  [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
   '''return a random card to the deck'''
   RAND = random.choice(CARDS)
   return RAND
   


def calculate_card(CARDS):
    '''Take a list of card and calculate and add up the card in the list and give the out put of totla'''
   
    if sum(CARDS) == 21 and len(CARDS) == 2:
      return 0 
   
    if 11 in CARDS and sum(CARDS) > 21:
      CARDS.remove(11)
      CARDS.append(1)
      
    return sum(CARDS)
   


def compare(USER_SCORE, COMPUTER_SCORE):
    if  USER_SCORE == COMPUTER_SCORE:
        return "It a draw🥲"
    elif COMPUTER_SCORE  ==  0:
        return "Lose, opponent has Blackjack 😭"
    elif USER_SCORE  == 0:
        return "You won with a Blackjack 🥳"
    elif COMPUTER_SCORE >  21:
        return "Opponent went over: You won 🎆"
    elif USER_SCORE > 21:
        return "You went over: You lose 😱"
    elif USER_SCORE  >  COMPUTER_SCORE:
        return "You win 😁"
    else:
        return "You lose 😡"
    

def CONTIUNE():

    COMPUTER_CARD  =  []
    USER_CARD  =  [] 
    GAME_OVER  =  True  



    for card in range(2):
        '''it add random card to both players'''
        COMPUTER_CARD.append(deal_card())
        USER_CARD.append(deal_card())


    while GAME_OVER:

        '''for the user to contiunes taking card'''

        USER_SCORE  = calculate_card(USER_CARD)
        COMPUTER_SCORE  = calculate_card(COMPUTER_CARD)
        print(f"You card : {USER_CARD}, You current score : {USER_SCORE}")
        print(f"Computer card : {COMPUTER_CARD[0]}")
        

        if USER_SCORE == 0 or COMPUTER_SCORE == 0 or USER_SCORE > 21:
          GAME_OVER = False

        else:
            '''to check if the input was yes  then draw a card or if no exit the loop'''
            answer  =  input("Do you want to draw anthor card 'y' or 'n' \n: ").lower()
            if  answer  == "y":
                USER_CARD.append(deal_card())

            else:
                GAME_OVER  =  False


    while  COMPUTER_SCORE != 0 and   COMPUTER_SCORE < 17:
      '''for computer to follower the dealer strages'''
      COMPUTER_CARD.append(deal_card())
      COMPUTER_SCORE = calculate_card(COMPUTER_CARD)

    print(f"You final hand : {USER_CARD}, final score : {USER_SCORE}")
    print(f"Computer final hand : {COMPUTER_CARD}, final score : {COMPUTER_SCORE}")
    print(compare(USER_SCORE, COMPUTER_SCORE))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n' \n: ").lower() == 'y':
    '''This is to reset the game and os.system is to clear the screen '''
    os.system("cls")
    CONTIUNE()