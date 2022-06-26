from card import *
from deck import *


def computer():
 global d,table, computer_hand, what_happened
 target_val=table[-1].value
 target_sym=table[-1].symbol
 while True:
  for c in computer_hand:
   if c.value==target_val or c.symbol==target_sym:
    print("The computer draws", c)
    computer_hand.remove(c)
    table.append(c)
    what_happened="computer_played"
    return 
  new_card=d.draw()
  if new_card=="empty":
   what_happened="deck_finished"
   return
  else:
   print("The computer draws a card")


def print_info():
 global d, table, computer_hand, human_hand
 print()
 print("The deck has the following number of cards", len(d.content), "cards")
 print("The computer has the following number of cards:", len(computer_hand), "cards")
 print("On the table there has been:", len(table), "cards")
 print("Your cards are the following ones:", len(human_hand))
 HHS=[str(x) for x in human_hand]
 print(HHS)
 print()
 print("Pick which one you shall like to draw")
 print("or press enter to draw from the deck")

def human_plays():
 global d, table, human_hand, what_happened
 while True:
  print_info()
  sel=input()
  if sel="":
   new_card=d.draw()
   if new_card="empty"
    what_happened="deck_finished"
    return
   else:
    human_hand.append(new_card)
  else:
   HHS=[str(x) for x in human_hand]
   if not (sel in HHS):
    print(sel. "??? You have got no card")
   else:
    t=table[-1]
    target_val = t.value
    target_sym=t.symbol
    if sel[0]!=target_val and sel[1]!=target_sym:
     print("It is not allowed to draw a card", sel)
    else:
     print("You draw", sel)
     ind=HHS.index(sel)
     selc=human_hand[ind]
     human_hand.remove(selc)
     table.append(selc)
     what_happened = "human_played"
     return


def initial():
 global d, table, computer_hand, human_hand, what_happened
 print("I pick up the cards")
 d.collect()
 table=[]
 computer_hand=[]
 human_hand=[]
 print("I shuffle the cards collected from the deck")
 d.shuffle()
 print("I share the cards to the players")
 table.append(d.draw())
 print("On the table, the following card has been dropped", table[-1])
 for i in range(7):
  human_hand.append(d.draw())
  computer_hand.append(d.draw())
 print("I toss a coin", end=" ")
 if random.random()<0.5:
  print(" You play first")
  what_happened="computer_played"
 else:
  print("The computer plays first")
  what_happened= "human_played"


def evaluate():
 global computer_hand, human_hand, what_happened
 if what_happened=="human_wins":print("Congratulations!You win")
 if what_happened=="computer_wins":print("Computer wins")
 if what_happened=="deck_finished":
  ch=len(computer_hand)
  hh=len(human_hand)
  print("The deck is over, computer has got", ch, "cards, and the player has got", hh, "cards")
  if ch>hh: print("Congratulations, you win")
  if ch<hh: print("computer winds")
  if ch==hh: print("even")

def next_turn():
 global wht_happened
 while True:
  if what_happened=="game_start":
   initial()
  elif what_happened=="human_played":
   if len(human_hand)==0:
    what_happened="human_wins"
    evaluate()
    break
  elif what_happened="computer_played":
   if len(computer_hand)==0:
    what_happened="computer_wins"
    evaluate()
    break
   print()
   print("--Player's turn--")
   human_playes()
 elif what_happened=="deck_finished":
  evaluate()
  break



print("Deck game")
print("===")
print()
d=deck()
table=[]
computer_hand=[]
human_hand=[]
what_happened=""
again="y"
while again="y":
 what_happened="game_start"
 next_turn()
 print("would you like to pkay again?")
 again=input("type y or n")
print("Programme ending")


