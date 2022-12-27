from art import logo
import random
from emoji import emojize

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The˳ Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

should_continue = True
while should_continue:
    is_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if is_play.lower() == 'y':
        print(logo)
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        user_cards = random.choices(cards, k=2)
        dealer_cards = random.choices(cards, k=2)
        user_total = 0
        dealer_total = 0
        for i in user_cards:
            user_total += i
        for i in dealer_cards:
            dealer_total += i
        print(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_total}")
        print(dealer_cards, dealer_total)
        if user_total == 21 or dealer_total == 21:
            if user_total == 21 and dealer_total != 21:
                print("You won with BlackJack \U0001F601")
            elif user_total != 21 and dealer_total == 21:
                print(f"Dealer won with BlackJack {emojize(':loudly_crying_face:')}")
            else:
                print("Both Dealer's total and User's total is 21, it's a PUSH!")
        print(f"Dealer's first card: {dealer_cards[0]}")
        # while user_total <= 21 or dealer_total <= 21:
        user_draw = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_draw.lower() == 'y':
            user_cards.append(random.choice(cards))
        print(user_cards)
        user_total = 0
        for i in user_cards:
            user_total += i
        while dealer_total < 17:
            dealer_cards.append(random.choice(cards))
            dealer_total = 0
            for i in dealer_cards:
                dealer_total += i
        print("dealer cards", dealer_cards, dealer_total)
        print("user cards", user_cards, user_total)
        if user_total > 21 or dealer_total > 21:
            if (user_total > 21 >= dealer_total) or (user_total > 21 and dealer_total > 21):
                print("You went over. You lose 😭")
            elif dealer_total > 21 >= user_total:
                print("Dealer went over. You won 😁")
        else:
            print("still building")


    elif is_play.lower() == 'n':
        should_continue = False
    else:
        print("Invalid input please try again.")
