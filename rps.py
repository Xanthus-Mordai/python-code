RULES = {
  ('Scissors', 'Paper') : 'cut',
  ('Paper', 'Rock') : 'covers',
  ('Rock', 'Lizard') : 'crushes',
  ('Lizard', 'Spock') : 'poisons',
  ('Spock', 'Scissors') : 'melts',
  ('Scissors', 'Lizard') : 'decapitates',
  ('Lizard', 'Paper') : 'eats',
  ('Paper', 'Spock') : 'disproves',
  ('Spock', 'Rock') : 'vaporizes',
  ('Rock', 'Scissors') : 'breaks',
}

hand1 = str(input('Hand 1: '))
hand2 = str(input('Hand 2: '))
hand1 = hand1.capitalize()
hand2 = hand2.capitalize()
if hand1 == hand2:
  print('Tie')
elif RULES.get((hand1,hand2), False) :
  print(hand1, RULES[(hand1, hand2)] , hand2)
else:
  print(hand2, RULES[(hand2, hand1)] , hand1)
