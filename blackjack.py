import random

### Input checks
def check_int(num):
  try:
    int(num)
    return True
  except ValueError:
    return False

def check_action(act):
  if act.lower() == 'h' or act.lower() == 's':
    return True
  return False

def check_verbosity(vb):
  if vb.lower() == 'a' or vb.lower() == 'v':
    return True
  return False

### Return the value of a card
def card_value(card, soft_ace = True):
  rank = card[0]
  if check_int(rank):
    return int(rank)
  elif rank == 'Ace':
    return 11 if soft_ace else 1
  else:
    return 10

### Return the value of a hand
def hand_value(list_cards):
  value = sum(list(map(card_value, list_cards)))
  if value > 21:
    value = sum(list(map(lambda x: card_value(x, False), list_cards)))
  return value

### String format of a card
def card_string(card, verbosity = 'v'):
  if verbosity == 'a':
    rank_abbrev = card[0][:2] if card[0] == '10' else card[0][0]
    return rank_abbrev + card[1][0]
  else:
    return card[0] + ' of ' + card[1]

### String format of a hand
def hand_string(list_cards, verbosity = 'v'):
  s = ''
  for card in list_cards:
    s += card_string(card, verbosity) + ', '
  return s[:-2]

### Deal card intelligently during hits
def deal_card(card_pool):
  if len(card_pool) <= 0:
    return None
  else:
    return card_pool.pop()

### Play one round of the game; returns result of the round (either the winner)
### or a game termination message
def play_round(pool, rd, card_verbosity):
  player_hand, dealer_hand = [], []
  ## Simulate alternate dealing of cards
  for i in range(4):
    if i % 2 == 0:
      player_hand.append(pool.pop())
    else:
      dealer_hand.append(pool.pop())

  print('ROUND', rd, '\n')
  print('You have been dealt the hand:', hand_string(player_hand, card_verbosity))
  print('The dealer has the', card_string(pool[-2], card_verbosity), 'and 1 card face-down.')

  ## Check for terminal results upon initial deal
  if hand_value(player_hand) == 21 and hand_value(dealer_hand) != 21:
    print('You got a blackjack!!')
    return 'Player'
  elif hand_value(player_hand) == 21 and hand_value(dealer_hand) == 21:
    print('You got a blackjack, but the dealer did too.')
    return 'Tie'
  elif hand_value(player_hand) > 21:
    print('Sorry, that\'s a bust!')
    return 'Dealer'

  ## Player's turn to play
  action = ''
  while action != 's':
    action = input('Would you like to hit [h] or stand [s]? ')
    while not check_action(action):
      action = input('Please enter a valid action. Would you like to hit [h] or stand [s]? ')

    if action == 'h':
      next_card = deal_card(pool)
      if not next_card:
        return 'Empty Pool'
      else:
        player_hand.append(next_card)
      print('Your hand:', hand_string(player_hand, card_verbosity))

      if hand_value(player_hand) > 21:
        print('Sorry, that\'s a bust!')
        return 'Dealer'
    else:
      print('Your final hand is', hand_string(player_hand, card_verbosity), 'with a value of', hand_value(player_hand), '\n')

  print('Now it\'s the dealer\'s turn.\n')

  ### Dealer plays deterministically
  while hand_value(dealer_hand) < 17:
    next_card = deal_card(pool)
    if not next_card:
      return 'Empty Pool'
    else:
      dealer_hand.append(next_card)

  print('The dealer\'s final hand is', hand_string(dealer_hand, card_verbosity), 'with a value of', hand_value(dealer_hand))
  if hand_value(dealer_hand) > 21:
    print('The dealer busted!')
    return 'Player'
  elif hand_value(dealer_hand) > hand_value(player_hand):
    return 'Dealer'
  elif hand_value(dealer_hand) == hand_value(player_hand):
    return 'Tie'
  else:
    return 'Player'


### Main game simulation
def main():
  ### Input parameters: card display mode, number of decks to play with
  print('Welcome to Blackjack!')
  verbosity = input('Please choose a card display mode (abbreviated [a] / verbose [v]): ')
  while not check_verbosity(verbosity):
    verbosity = input('Please enter a valid mode (abbreviated [a] / verbose [v]): ')
  decks = input('Please enter the number of standard card decks you\'d like to play with: ')
  while not check_int(decks) or int(decks) <= 0:
    decks = input('Plese enter a postive integer (non-integers will be floored): ')
  print()

  ### Prepare simulated pool of cards
  ranks = ['Ace'] + [str(i) for i in range(2, 11)] + ['Jack', 'Queen', 'King']
  suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
  deck = [(rank, suit) for rank in ranks for suit in suits]

  pool = sum([deck for i in range(int(decks))], [])
  random.shuffle(pool)

  ### Gameplay
  round_no = 1

  player_wins, dealer_wins = 0, 0

  while len(pool) >= 4:
    result = play_round(pool, round_no, verbosity)
    if result == 'Player':
      player_wins += 1
      print('You win this round!')
    elif result == 'Dealer':
      dealer_wins += 1
      print('The dealer wins this round!')
    elif result == 'Tie':
      print('Tie! No one wins.')
    elif result == 'Empty Pool':
      break

    round_no += 1
    print('The score is {}-{}.\n'.format(player_wins, dealer_wins))

  ### Summarize game results
  print('There are not enough cards to continue playing.')
  print('You won {} rounds and the dealer won {} out of {} completed rounds. Thanks for playing blackjack!'.format(player_wins, dealer_wins, round_no - 1))

if __name__ == '__main__':
  main()
