init python:

 import sys
 reload(sys)
 sys.setdefaultencoding("utf-8")

#--------------------------------------------
#Define the player's choices that affect the story
 class Choice:
  def __init__(self, id, status, description):
   self.id= id
   self.status= status
   self.description= description       

# 1: Le preguntasté a nacho acerca de su nueva relación.   
#--------------------------------------------
#Define the Today date
#05/10/09 18:00
 class TodayClass:   
 
  def __init__(self, year, month, day, hour, minute):
   import datetime
   #(2015, 9, 1, 7, 20)
   self.datetime= datetime.datetime(year, month, day, hour, minute)
   self.day= self.datetime.strftime("%d") 
   months= ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dec"]
   self.month= months[month-1]
   days= ["Lun","Mar","Mie","Jue","Vie","Sab","Dom"]
   self.dayofweek= days[self.datetime.weekday()] 
   
  def IncDay(self):
   import datetime
   import timedelta
   self.datetime+= timedelta(days=10)
   self.day= self.datetime.strftime("%d") 
   months= ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dec"]
   self.month= "Pipo"
   days= ["Lun","Mar","Mie","Jue","Vie","Sab","Dom"]
   self.dayofweek= "Sab"
#--------------------------------------------   
#Define the item class
 class Item:
  def __init__(self, id, name, filename, value, important):
   self.id= id
   self.name= name
   self.filename= filename
   self.value= value
   self.important= important
#--------------------------------------------   
#Define the Friend class
 class Friend:
  def __init__(self, char):
   self.char= char  
#--------------------------------------------
#Define the Genre class (workaround because enumerations not supported in python 2.7)
#Use: Genre.Male or Genre.Female
 class Enum(set):
  def __getattr__(self, name):
   if name in self:
    return name
   raise AttributeError
   
 Genre= Enum(["Male", "Female"])
#-------------------------------------------- 
#Define the Char class
 class Charact:
  def __init__(self, charobj= None, name="", genre= Genre.Male, money=0, affinity=90, love=0, score=0, adversary= None, isknown= False, isfriend= False, gamelevel=1, victorycount=0, downcount=0 ):
   self.adversary= adversary
   self.affinity= affinity
   self.charobj= charobj
   self.choices= []
   self.deck= []    
   self.friendslist= []
   self.genre= genre
   self.isfriend= isfriend
   self.isknown= isknown
   self.love= love
   self.money= money
   self.name= name
   self.score= score
   self.gamelevel= gamelevel #there is three levels: 1=casual, 2=expert, 3=master
   self.victorycount= victorycount
   self.downcount= downcount
   self.items= []

  #Buy item 
  def buy(self, item):
   if self.money>= item.cost:
    self.money-= item.cost
    self.items.append(item)
    return True
   else:
    return False
  #earn Money
  def earn(self, amount):
   self.money+= amount
  #Check if the char has item
  def has_item(self, item):
   if item in self.items:
    return True
   else:
    return False
  #Add a item to char   
  def add_item(self, id, name, pic, value):
   self.items.append(id, name, pic, value)
  #Edit the affinitty meter
  def change_affinity(self, inc, level):
   if level==0:
    min_random= 1
    max_random= 3
   elif level==1:
    min_random= 3
    max_random= 10
   elif level==2:
    min_random= 10
    max_random= 20
   elif level==3:
    min_random= 20
    max_random= 50
   else:
    min_random= 3
    max_random= 15
   import random
   amount= random.randint(min_random, max_random)
   if inc==False:
    amount= -amount
   self.affinity+= amount
   if self.affinity<0:
    self.affinity=0
   elif self.affinity>100:
    self.affinity=100
   if self.affinity>=40:
    self.isfriend= True
   else:
    self.isfriend= False
  #Edit the love meter
  def change_love(self, inc, level):
   if level==0:
    min_random= 1
    max_random= 3
   elif level==1:
    min_random= 3
    max_random= 10
   elif level==2:
    min_random= 10
    max_random= 20
   elif level==3:
    min_random= 20
    max_random= 50
   else:
    min_random= 3
    max_random= 15
   import random
   amount= random.randint(min_random, max_random)
   self.love+= amount
   if self.love<0:
    self.love=0
   elif self.love>100:
    self.love=100
#--------------------------------------------    
#Create the instances of the characters:
 #Create the chars
 me= Charact(name= "Maru", charobj=ma, genre= Genre.Female, money=100.0)
 violeta= Charact(name="Violeta", charobj=vi, genre= Genre.Female, money=100.0, affinity=90, love=0,  isknown= True, isfriend= True, gamelevel=2)
 nacho= Charact(name="Nacho", charobj=na, genre= Genre.Male, money=100.0, affinity=75, love=5,  isknown= True, isfriend= True, gamelevel=1)
 #Append the friends
 me.friendslist.append(nacho)
 me.friendslist.append(violeta)
 #Append the items
 log= Item(1, "Diario", "log", 0.1, True)
 me.items.append(log)
 rose= Item(1, "Rosa", "rose", 5.0, True)
 me.items.append(rose)

 #Today date:
 today= TodayClass(2015, 9, 15, 7, 20)

 #Card Game Implementation
 
 deck= []
 CardPath= str
 CardInPlay= tuple
 ForceSuit= False
 ForcedSuit= str
 ForcedSuitStr= str
 PassCount= 0

 firsthand_numcards= 7 # set the number of cards in the first hand

 AwaitClick= False

 def deck_definition():
  vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
  suits = ['P', 'C', 'H', 'D']
  import itertools
  deck_tmp= list(itertools.product(vals, suits))
  #Also add two Black&Red Jokers
  #deck_tmp.append(tuple(['Jo', 'B']))
  #deck_tmp.append(tuple(['Jo', 'R']))
  return deck_tmp
  del deck_tmp[:]

 def ShowCardInPlay():
  global CardPath
  CardPath= "img/cards/"+ str(CardInPlay[0])+str(CardInPlay[1])+".png"
  renpy.transition(moveintop)
  renpy.show('card_img', at_list=[Transform(zoom=0.3, xpos=0.7, ypos=0.05)], layer="game")
  renpy.pause(1.5)

 def PlayCard(item, itemindex):
  global CardInPlay
  CardInPlay= item
  me.deck.pop(itemindex)
  ShowCardInPlay()
  ResetPassCount()

 def play_a_card(itemindex, item):
  global CardInPlay
  global CardPath
  global ForceSuit
  global ForcedSuit
  global ForcedSuitStr
  if (ForceSuit== True) and (CardInPlay[0]=="A"):
   if (item[0]== "A") or (item[1]== ForcedSuit):
    ForceSuit= False
    PlayableCard= True
   else:
    renpy.show_screen('comment', "No es la carta adecuada.\nDebe de ser del palo "+str(ForcedSuitStr))
    PlayableCard= False
  elif (item[0]== "A") or (item[0]== CardInPlay[0]) or (item[1]==CardInPlay[1]):
    PlayableCard= True
  else:
    renpy.show_screen('comment', "No es la carta adecuada.\nDebe de ser un "+str(CardInPlay[2])+" o el palo "+str(CardInPlay[3]))
    PlayableCard= False
  if (PlayableCard== True):
   PlayCard(item, itemindex)
   return True
  else:
   return False

 #Create a new brand deck to start playing cards
 def newdeck():
  global deck
  deck_definition()  
  del deck[:]
  deck_tmp= deck_definition()
  for val,suit in deck_tmp:
   if val== "J":
    val_lang= "Comodín"
    value= 11
   elif val== "Q":
    val_lang= "Reina"
    value= 12
   elif val== "K":
    val_lang= "Rey"
    value= 13
   elif val== "A":
    val_lang= "As"
    value= 50
   else:
    val_lang= val
    value= int(val)
   if suit== "P":
    suit_lang= "Picas"
    suit_color= "000000"
    suit_icon= "♠"
   elif suit== "C":
    suit_lang= "Tréboles" 
    suit_color= "000000"
    suit_icon= "♣"
   elif suit== "H":
    suit_lang= "Corazones"
    suit_color= "ff0000"
    suit_icon= "♥"
   elif suit== "D":
    suit_lang= "Diamantes"
    suit_color= "ff0000"
    suit_icon= "♦"
   deck.append(tuple([val, suit, val_lang, suit_lang, suit_color, suit_icon, value]))
  import random
  random.shuffle(deck)
  del deck_tmp[:]

 def firsthand_create():
  import random
  global firsthand_numcards
  global me
  newdeck()
  del me.deck[:]
  del me.adversary.deck[:]
  for x in range(0, firsthand_numcards):
   RandomNumber= random.randint(0,len(deck)-1)
   RandomCard= deck.pop(RandomNumber)   
   me.deck.append(RandomCard)
  for x in range(0, firsthand_numcards):
   RandomNumber= random.randint(0,len(deck)-1)
   RandomCard= deck.pop(RandomNumber)   
   me.adversary.deck.append(RandomCard)

 def draw_a_card(Charact):
  global deck
  import random
  RandomNumber= random.randint(0,len(deck)-1)
  RandomCard= deck.pop(RandomNumber)   
  Charact.deck.append(RandomCard)
  if len(deck)==0:
   renpy.transition(dissolve)
   renpy.hide('deck_img', layer="game")
  return RandomCard

 def CheckIsAce(item):
  global ForceSuit
  global ForcedSuit
  global ForcedSuitStr
  if item[0]== "A":
   ForceSuit= True
   shift= menu([('Forzar ♠Picas', 'pikes'), ('Forzar ♣Tréboles', 'clubs'), ('Forzar ♥Corazones', 'hearts'), ('Forzar ♦Diamantes', 'diamonds')])
   if shift=="pikes":
    ForcedSuit= "P"
   elif shift=="clubs":
    ForcedSuit= "C"
   elif shift=="hearts":
    ForcedSuit= "H"
   else:
    ForcedSuit= "D"

 #PassCount functions->

 def PassTurn():
  global PassCount
  PassCount+= 1

 def ResetPassCount():
  global PassCount
  PassCount= 0

 def calculate_score(Charact):
  score= 0
  for item in Charact.deck:
   score= score + item[6]
  return score

 def CalcFrequencyOfSuits(deck, AvoidThisCard):
  global me
  PikesCount= 0
  ClubsCount= 0
  HeartsCount= 0
  DiamondsCount= 0 
  for item in deck:
   if (AvoidThisCard is None) or (item[0]!= AvoidThisCard):
    if item[1]=="P":
     PikesCount+= 1
    elif item[1]=="C":
     ClubsCount+= 1
    elif item[1]=="H":
     HeartsCount+= 1
    else:
     DiamondsCount+= 1   
  dictionaryofsuits= {"P": PikesCount, "C": ClubsCount, "H": HeartsCount, "D": DiamondsCount}
  #debug= ""
  #for suit, val in dictionaryofsuits.iteritems():
   #debug= debug+str(suit)+str(val)+", "
  #renpy.show_screen('comment', debug, 20)
  return dictionaryofsuits

 def game_start(Charact):
  global me
  global CardPath
  global CardInPlay
  global ForceSuit
  global ForcedSuit
  global ForcedSuitStr
  global PassCount
  global firsthand_numcards
  me.adversary= Charact
  renpy.block_rollback()
  firsthand_create()
  import random
  me_turn= bool(random.getrandbits(1))
  first_turn= True
  cards_to_play= []
  TurnCount=0
  while (True): #----------------PLAY TIL GAME ENDS------------------
   TurnCount+= 1
   if PassCount>=4: #Multiple passes do not allowed
    break 
   renpy.show_screen("game_data")
   if first_turn== True:
    renpy.transition(dissolve)
    renpy.show('deck_img', at_list=[Transform(zoom=0.3, xpos=0.2, ypos=0.05)], layer="game")
   #---------- MY TURN ----------------------
   if me_turn: #---------- MY FIRST TURN ----------------------
    if first_turn: 
     renpy.show_screen('comment', "Empiezas tú", 2)    
     while True:
      itemindex, item= renpy.call_screen('my_hand', True)
      PlayCard(item, itemindex)
      CheckIsAce(item)
      first_turn= False
      me_turn= False
      break     
    else: #---------- MY TURN ----------------------
     renpy.show_screen('comment', "Es tu turno", 1)        
     #Show your cards
     while True:
      result= renpy.show_screen('my_hand', False)
      if len(deck)>0:
       shift= menu([('Robar una carta', 'draw'), ('Jugar', 'play')])
      else:
       shift= menu([('Pasar', 'pass'), ('Jugar', 'play')])
      if (shift=='draw'):
       DrawedCard= draw_a_card(me)
       renpy.show_screen('comment', "Has obtenido la carta "+ str(DrawedCard[2])+" de "+str(DrawedCard[3]), 2)
       me_turn= True
      elif (shift=='play'):
       itemindex, item= renpy.call_screen('my_hand', True)
       if (play_a_card(itemindex, item)== True):
        CheckIsAce(item)
        me_turn= False
        break
      elif (shift=='pass'):
       PassTurn()
       if ForceSuit== True: #Important: If pass the turn, and the ForceSuit is enabled then the ForceSuit is disabled
        renpy.show_screen('comment', "Al pasar, el forzado a palo "+ForcedSuitStr+" ya no tiene efecto.", 2)
        ForceSuit= False      
       me_turn= False
       break
     if len(me.deck)==0: #I HAVE NOT CARDS = LAST TURN FOR ME = I WIN!
      break
     #_window_hide()
   else:
    #--------TURN OF THE ADVERSARY---------
    if first_turn:
     #-------IF ADVERSARY'S FIRST TURN
     RandomNumber= random.randint(0,len(me.adversary.deck)-1)
     CardInPlay= me.adversary.deck[RandomNumber]
     me.adversary.deck.pop(RandomNumber)
     PlayableCard= True
     first_turn= False
    else: #--------TURN OF THE ADVERSARY---------
     #Calculate what card the adversary will play
     #First what cards in this hand match with the Card in Play
     drawed_cards= 0
     has_a_ace= False
     while True:      
      del cards_to_play[:]
      for item in me.adversary.deck:
       if (CardInPlay[0]== "A") and (ForceSuit== True): #If the playing card is an ACE
        if (item[0]=="A") or (item[1]==ForcedSuit): #If Ace or match the forced suit
         cards_to_play.append(item)
         if item[0]=="A": #mark that the adversary has a Ace
          has_a_ace= True
       else: #For common cards ->
        if (item[0]=="A") or ((item[0]==CardInPlay[0]) or (item[1]==CardInPlay[1])): #If Ace or match val or suit
         cards_to_play.append(item)
         if item[0]=="A": #mark that the adversary has a Ace
          has_a_ace= True
      if (len(cards_to_play)>0) or (len(deck)==0):
       break
      else:
       draw_a_card(me.adversary)
       drawed_cards= drawed_cards + 1
     if (len(cards_to_play)>0):
      if (drawed_cards>0):
       renpy.show_screen('comment', me.adversary.name +" ha cogido "+ str(drawed_cards)+" cartas del mazo.")      
      #HERE THE ADVERSARY AI ACCORDING HIS GAME LEVEL
      if me.adversary.gamelevel>1:             
       if (has_a_ace== True) and (len(cards_to_play)==1):  #If the adversary has an Ace of the same suit as his unique playable card then the adversary has 100% of possibility to play this 
        play_the_ace= True
       if (has_a_ace== True):  #If the adversary has an Ace of the same suit then the adversary has 50% of possibility to play this 
        play_the_ace= bool(random.getrandbits(1))
       else:
        play_the_ace= False
       if play_the_ace== False:
        #In this level check the frequency of suits in his hand         
         dictionaryofsuits= CalcFrequencyOfSuits(me.adversary.deck, None)
         import operator
         #Order the dictionary suits by its frequency in a decreasing order
         sorted_suit_frequencies= sorted(dictionaryofsuits.items(), key=operator.itemgetter(1), reverse= True)
         #Now get the first card with the suit of max frequency from the playable cards
         for item in cards_to_play:
          for suit in sorted_suit_frequencies: #iterate all the max frequency suits
           if item[1]==  str(suit[0]): #get the first ocurrence
            CardInPlay= item
            break #not seach for other suitable card      
          else:
           continue  # executed if the loop ended normally (no break)
          break  # executed if 'continue' was skipped (break)        
       else: #if play the ace
        for item in cards_to_play: #Search the ace to play
         if item[0]==  "A":                    
          CardInPlay= item
          if ForceSuit== True:
           ForceSuit== False
          break #not more search for the Ace
      else: #if the player level is =1 then choose a random card
       RandomNumber= random.randint(0,len(cards_to_play)-1)
       CardInPlay= cards_to_play[RandomNumber]             
      #Quit that card form his/her deck
      for itemindex, item in enumerate(me.adversary.deck):
       if (item[0]==CardInPlay[0]) and (item[1]==CardInPlay[1]):
        me.adversary.deck.pop(itemindex)
        break
      PlayableCard= True
     else: 
      PlayableCard= False
    #--------------- DRAW A PLAYABLE CARD -------------
    if (PlayableCard== True) and (len(me.adversary.deck)>0):
     ShowCardInPlay()
     if CardInPlay[0]=="A": #IF CARD-IN-PLAY IS A ACE
      ForceSuit= True
      if me.adversary.gamelevel>1: #If adversary level is expert or master
       #Analyze what is the suitable suit to switch
       dictionaryofsuits= CalcFrequencyOfSuits(me.adversary.deck, CardInPlay)
       #Get the suit of max. frequency
       #ForcedSuit= max(dictionaryofsuits, key=lambda key: dictionaryofsuits[key])
       ForcedSuit= max(dictionaryofsuits, key=dictionaryofsuits.get)
       #renpy.show_screen('comment', ForcedSuit, 20) DEBUG
      else: #if adversary has a game level of 1
       #Force Random Suit
       ForcedSuit= random.choice("PCHD")
      #Set the ForcedSuit
      if ForcedSuit== "P":
       ForcedSuitStr= "Picas"
      elif ForcedSuit== "C":
       ForcedSuitStr= "Tréboles"
      elif ForcedSuit== "H":
       ForcedSuitStr= "Corazones"
      else:
       ForcedSuitStr= "Diamantes"
      ResetPassCount()
      renpy.say(me.adversary.charobj, "Mi carta es {color=#"+str(CardInPlay[4])+"}"+str(CardInPlay[2])+" de "+str(CardInPlay[5])+str(CardInPlay[3])+"{/color}.\nTe obligo a que eches un palo "+ForcedSuitStr+".")
     else: #IF CARD-IN-PLAY IS A REGULAR CARD (NOT A ACE)
      renpy.say(me.adversary.charobj, "Mi carta es {color=#"+str(CardInPlay[4])+"}"+str(CardInPlay[2])+" de "+str(CardInPlay[5])+str(CardInPlay[3])+"{/color}.\nEcha una carta del mismo palo o número.")
    #------IF ADVERSARY HAS NOT A PLAYABLE CARD ---------
    else:
     if (len(me.adversary.deck)>0):
      PassTurn()
      renpy.say(me.adversary.charobj, "Paso el turno.")
      if ForceSuit== True: #Important: If pass the turn, and the ForceSuit is enabled then the ForceSuit is disabled
       renpy.show_screen('comment', "Al pasar, el forzado a palo "+ForcedSuitStr+" ya no tiene efecto.", 2)
       ForceSuit= False      
     else:
       renpy.say(me.adversary.charobj, "Mi última carta es {color=#"+str(CardInPlay[4])+"}"+str(CardInPlay[2])+" de "+str(CardInPlay[5])+str(CardInPlay[3])+"{/color}.\n¡Ya no me quedan más!")
       break
    #------ ADVERSARY END OF TURN ------------------
    renpy.block_rollback()
    me_turn= True
  #-------------END OF while (True) = GAME ENDS
  renpy.hide('card_img', layer="game")
  renpy.hide('deck_img', layer="game")
  renpy.hide_screen("game_data")
  renpy.hide_screen("my_hand")
  if len(me.deck)==0:    
   #Calculate the score
   won_score= calculate_score(me.adversary)
   me.score+= won_score
   me.victorycount+= 1
   me.adversary.downcount+= 1
   renpy.show_screen('comment', "¡¡¡HAS GANADO "+str(won_score)+" puntos!!!")  
   return 1
  elif len(me.adversary.deck)==0:
   renpy.show_screen('comment', "¡¡¡HAS PERDIDO!!!") 
   me.adversary.score+= calculate_score(me)
   me.adversary.victorycount+= 1
   me.downcount+= 1
   return 2
  else:
   renpy.show_screen('comment', "Habéis empatado.") 
   return 3
  renpy.pause(2.0, hard=True)