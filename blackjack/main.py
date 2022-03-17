from art import logo

from replit import clear 



import random 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card() :
  """retuns a random card from the deck"""
  card = random.choice(cards)
  return card 

def compare(user_score,computer_score):
  if user_score == computer_score :
    return "draw🤔"
  elif computer_score == 0:
    return " LOSE , computer has a blackjack🤦‍♂️"
  elif user_score == 0:
    return " WIN with a Blackjack😎 "
  elif user_score > 21 :
    return " LOSE , you went over 🤦‍♂️"
  elif computer_score > 21:
    return " WIN, computer went over 👏"
  elif user_score>computer_score:
    return " you winn "
  else:
    return "you lose 🤦‍♂️"      

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    for _ in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())


    def calculate_score(cards):
      """calculates the sum of user and computer cards that are dealt"""
      if sum(cards) ==21 and len(cards)== 2:
        return 0
      if 11 in cards and  sum(cards) > 21:
        cards.remove(11)
        cards.append(1) 
      return sum(cards)  


    game_over = False
    while game_over == False:
      user_score =calculate_score(user_cards)
      computer_score = calculate_score(computer_cards)
      print(f" user cards: {user_cards} \n user score : {user_score} ")
      print(f" computer cards: {computer_cards} \n user score : {computer_score} ")
      

      if user_score == 0 or computer_score ==0 or user_score > 21:
        game_over = True
      else :
        user_should_deal = input("Type 'y' to get another card and 'n' to pass\n")  
        if user_should_deal == "y":
            user_cards.append(deal_card())  
        else:
          game_over = True  


    while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score =calculate_score(computer_cards  )
    print(f"Your final hand is {user_cards} and your score is {user_score}")
    print(compare(user_score,computer_score))  

    print(f"computer's final hand is {computer_cards} and your score is {computer_score}")


while input("Do You wanna play the game of blackjack? type 'y' for yess and 'n' for no ") == "y" : 
  clear()
  play_game()
 