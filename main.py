import random

suits = ["♠♠", "♥♥", "♦♦", "♣♣"]*2
cards = ["TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "KING", "QUEEN", "JACK", "ACE"]*2
values = {"TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5, "SIX": 6, "SEVEN": 7, "EIGHT": 8, "NINE": 9, "TEN": 10,
          "KING": 10, "QUEEN": 10, "JACK": 10, "ACE": 11}
LOWEST_AMOUNT = 50
HIGHEST_AMOUNT = 100000
LOWEST_BET = 50
player_hand = []
dealer_hand = []


def create_deck():
    deck = []
    for suit in suits:
        for card in cards:
            deck.append(f"{card} OF {suit}")
    return deck


def deal_cards(deck, hand):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)
    return hand


def deal_both_hands(deck):
    global player_hand, dealer_hand
    for _ in range(2):
        deal_cards(deck, player_hand)
        deal_cards(deck, dealer_hand)
    return player_hand, dealer_hand


def total_of_hand(hand):
    hand_value = 0
    aces = 0
    for card in hand:
        value = card.split()[0]
        if value == 'ACE':
            aces += 1
            hand_value += 11
        else:
            hand_value += values[value]
    while hand_value > 21 and aces > 0:
        hand_value -= 10
        aces -= 1
    return hand_value


def amount():
    while True:
        add_chips = input("HOW MUCH  CHIPS YOU WANT TO BUY: ")
        if add_chips.isnumeric():
            add_chips = int(add_chips)
            if add_chips > HIGHEST_AMOUNT:
                print(f"PLEASE BUY IN IN OUR CASINO LIMIT WHICH IS{HIGHEST_AMOUNT}: ")
            elif add_chips <= LOWEST_AMOUNT:
                print(f"BALANCE MUST BE HIGHER THAN{LOWEST_AMOUNT}$ ")
                continue
            elif add_chips > LOWEST_AMOUNT:
                break
    return add_chips


def bet_round():
    while True:
        bet = input("WHATS YOUR BET FOR THIS ROUND? ")
        if bet.isnumeric():
            bet = int(bet)
            if bet <= LOWEST_BET:
                print(f"BET MUST BE HIGHER THAN |{LOWEST_BET}")
                continue
            elif bet > LOWEST_BET:
                break
    return bet


def main(name):
    global chips, player_hand, dealer_hand
    while True:
        round_bet = bet_round()
        double_bet = (round_bet * 2)
        deck = create_deck()
        if round_bet > chips:
            print("YOU DON't HAVE ENOUGH CHIPS")
            continue
        player_hand, dealer_hand = deal_both_hands(deck)
        print("_______________________INITIAL_HANDS_________________________________________")
        print(f"HI {name} YOUR HANDS IS {player_hand}\n"
              f"WHILE DEALER HAVE {dealer_hand[0]} AND ONE CARD FACE DOWN XXX")
        print("__________________________________________________________________")
        if total_of_hand(dealer_hand) == 21 and total_of_hand(player_hand) != 21:
            print("DEALER GOT BLACK JACK")
            chips -= round_bet
            break
        elif total_of_hand(player_hand) == 21 and total_of_hand(dealer_hand) != 21:
            chips += (round_bet * 3.25)
            print(f"{name} GOT BLACK JACK")
            break

        player_in = True
        while player_in:
            play = input("WHATS YOUR PLAY HIT(1) or stand(2) or DOUBLE_bet(3)? ").strip()
            if play.isnumeric():
                play = int(play)
                if play == 1:
                    deal_cards(deck, player_hand)
                    print(player_hand)
                elif play == 2:
                    player_in = False
                elif play == 3 and double_bet <= chips and len(player_hand) == 2:
                    deal_cards(deck, player_hand)
                    round_bet += round_bet
                    print(player_hand)
                    player_in = False

            else:
                print("WRONG COMMAND! OR  YOU DON'T Have Enough Chips TO MAKE DOUBLE BET ")
        print("____________________WINNER______________________________________________")
        while total_of_hand(dealer_hand) <= 16:
            deal_cards(deck, dealer_hand)
        if total_of_hand(player_hand) > 21:
            print(f"{name} GOT BUSTED")
            chips -= round_bet
            break
        elif total_of_hand(dealer_hand) > 21:
            print(f"DEALER GOT BUSTED")
            chips += round_bet
            break
        elif total_of_hand(player_hand) == total_of_hand(dealer_hand):
            print("TIE TIE")
            break
        elif total_of_hand(player_hand) > total_of_hand(dealer_hand):
            print(f"{name}  WINS!")
            chips += round_bet
            break
        elif total_of_hand(dealer_hand) > total_of_hand(player_hand):
            print(f"DEALER WINS!")
            chips -= round_bet
            break
        else:
            print("ERROR")
            break
    print("______________________HANDS____________________________________________")
    print(f"{name} YOUR HANDS WAS>>>\n{player_hand}  ('{total_of_hand(player_hand)}')\nAND DEALER HAND WAS>>>\n"
          f"{dealer_hand} ('{total_of_hand(dealer_hand)}')")
    print("______________________BALANCE____________________________________________")
    print(f"YOUR HAVE {chips}$ CHIPS")
    print("__________________________________________________________________")

    if chips < LOWEST_AMOUNT:
        reload = input("DO YOU WANT TO RELOAD? YES OR NO").strip().upper()
        if reload == "YES":
            chips = chips + amount()
        elif reload == "NO":
            quit()


if __name__ == "__main__":
    welcome = "__________________________WELCOME TO BLACK JACK TABLE____________________________"
    print(welcome.center(100))
    user_name = input("PLEASE STATE YOUR NAME: ").title()
    chips = amount()
    while True:
        main(user_name)
        choice = input(f"ANOTHER ROUND {user_name}? YOU HAVE {chips}$  YES OR NO").upper().strip()
        if chips < LOWEST_AMOUNT:
            print(f"SEE YOU SOON YOUR REMAINING CHIPS ARE {chips}$")
            break
        elif choice == "YES":
            continue
        else:
            print("INVALID Command!")
            continue
