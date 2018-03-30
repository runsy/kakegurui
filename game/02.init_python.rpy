init python:
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")

    #Procedures
    def change_cursor(type="default"):
        persistent.mouse = type
        if type == "default":
            setattr(config, "mouse", None)
        elif type == "hand32":
            setattr(config, "mouse", {"default": [("img/cursors/hand32.png", 0, 0)]})
        elif type == "hand64":
            setattr(config, "mouse", {"default": [("img/cursors/hand64.png", 0, 0)]})            
    if not hasattr(persistent, "mouse"):
        change_cursor()
    else:
        change_cursor(persistent.mouse)

    change_cursor("hand32")    

    def InitMe():
        global c
        #Append the friends
        c.me.friendslist.append(c.nacho)
        c.me.friendslist.append(c.violeta)
        #Append the items
        log= Item(1, "Diario", "log", 0.1, "Mi diario con mis vivencias personales.", True)
        c.me.items.append(log)
        rose= Item(1, "Rosa", "rose", "Una rosa regalo de Paolo", 5.0, True)
        c.me.items.append(rose)    

    def CreateCharact(_key, _name, _charobj, _genre, _money, _affinitty, _love, _isknown, _isfriend, _gamelevel, _gamecount):  
        #Create the instances of the characters in the dictionary
        global characts        
        characts[_key] = Charact(name=_name, charobj=_charobj, genre= _genre, money=_money, affinity=_affinitty, love=_love,  isknown= _isknown, isfriend= _isfriend, gamelevel= _gamelevel, gamecount= _gamecount)

    def CreateCharacts():
        global characts
        global c
        #Create the chars                
        CreateCharact("me", "Maru", ma, Genre.Female, 100.0, 0, 0, True, True, 1, 1)
        CreateCharact("violeta", "Violeta", vi, Genre.Female, 100.0, 90, 0, True, True, 1, 0)
        CreateCharact("nacho", "Nacho", na, Genre.Male, 100.0, 80, 0, True, True, 1, 0)
        CreateCharact("antia", "Antía", an, Genre.Female, 125.0, 65, 0, False, False, 2, 0)
        CreateCharact("paolo", "Paolo", pa, Genre.Male, 2000.0, 85, 60, False, False, 2, 0)
        CreateCharact("carmen", "Carmen", ca, Genre.Female, 500.0, 20, 0, False, False, 3, 0)
        #It's better use a variable 'c' object to access the items of the dictionary (c.key) rather than dictionary['key']
        c= Bunch(characts)
         
    #Card Game Implementation

    #Define the Game class
    class _Game():
        def __init__(self, deck=[], WholeDeck=[], DiscardedDeck=[], CardPath= "", CardInPlay= tuple, ForceSuit= False, ForcedSuit="", ForcedSuitStr="", PassCount=0, NumCards_FirstHand= 7, TurnCount=0, RoundCount=0, MeScore=0, AdversaryScore=0):
            self.deck= deck          
            self.WholeDeck= WholeDeck
            self.DiscardedDeck= DiscardedDeck
            self.CardPath= CardPath
            self.CardInPlay= CardInPlay
            self.ForceSuit= ForceSuit
            self.ForcedSuit= ForcedSuit
            self.ForcedSuitStr= ForcedSuitStr
            self.TurnCount= TurnCount
            self.RoundCount= RoundCount
            self.PassCount= PassCount
            self.MeScore= MeScore
            self.AdversaryScore= AdversaryScore
            self.NumCards_FirstHand= NumCards_FirstHand
    
    #Create the game

    game= _Game()    

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
        global game
        game.CardPath= "img/cards/"+ str(game.CardInPlay[0])+str(game.CardInPlay[1])+".png"
        renpy.transition(moveintop)
        renpy.show('card_img', at_list=[Transform(zoom=0.3, xpos=0.2, ypos=0.05)], layer="game")
        renpy.play(effect.card)
        renpy.pause(1.5)

    def PlayCard(whatdeck, item, itemindex):
        global game
        game.CardInPlay= item
        game.DiscardedDeck.append(item) #Put the car in the list of discarded cards
        whatdeck.pop(itemindex)
        if game.ForceSuit== True:
            game.ForceSuit= False        
        ResetPassCount()
        ShowCardInPlay()

    def NoSuitableCard(type):
        global game
        renpy.play(effect.squoink)
        if type==0:
            msg= "No es la carta adecuada.\nDebe de ser un "+str(game.CardInPlay[2])+" o el palo "+str(game.CardInPlay[3])
        else:
            msg= "No es la carta adecuada.\nDebe de ser del palo "+str(game.ForcedSuitStr)
        renpy.show_screen('comment', msg, 2)    
        return False

    def play_a_card(itemindex, item):
        global game
        if (game.ForceSuit== True) and (game.CardInPlay[0]=="8"):
            if (item[0]== "8") or (item[1]== game.ForcedSuit):
                PlayableCard= True
            else:
                PlayableCard= NoSuitableCard(1)
        elif (item[0]== "8") or (item[0]== game.CardInPlay[0]) or (item[1]==game.CardInPlay[1]):
                PlayableCard= True
        else:
                PlayableCard= NoSuitableCard(0)
        if (PlayableCard== True):
            PlayCard(c.me.deck, item, itemindex)
            #IF AN Eight YOU SHOULD CHOICE THE SUIT TO PLAY
            CheckIsEight(item)
            return True
        else:
            return False

    #Create a new brand deck to start playing cards
    def newdeck():
        global game
        deck_definition()  
        del game.deck[:]
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
                value= 1
            elif val== "8":
                val_lang= "8"
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
            game.deck.append(tuple([val, suit, val_lang, suit_lang, suit_color, suit_icon, value]))
            game.WholeDeck= game.deck
        import random
        random.shuffle(game.deck)
        del deck_tmp[:]

    def GetRandomNum(whatdeck):
        import random
        return random.randint(0,len(whatdeck)-1) 

    def firsthand_create():
        import random
        global game
        global c
        newdeck()
        del c.me.deck[:]
        del c.me.adversary.deck[:]
        for x in range(0, game.NumCards_FirstHand):
            RandomCard= game.deck.pop(GetRandomNum(game.deck))   
            c.me.deck.append(RandomCard)
        for x in range(0, game.NumCards_FirstHand):
            RandomCard= game.deck.pop(GetRandomNum(game.deck))   
            c.me.adversary.deck.append(RandomCard)

    def draw_a_card(Character):
        global game
        import random
        RandomCard= game.deck.pop(GetRandomNum(game.deck))   
        Character.deck.append(RandomCard)
        renpy.play(effect.card)
        if Character== c.me:
            renpy.show_screen('comment', "Has obtenido la carta "+ str(RandomCard[2])+" de "+str(RandomCard[3]), 2)        
        return True

    def CheckIsEight(item):
        global game
        if item[0]== "8":
            game.ForceSuit= True
            renpy.show_screen('comment', "¿Qué palo se debe jugar?", 1)  
            shift= menu([('Forzar ♠Picas', 'pikes'), ('Forzar ♣Tréboles', 'clubs'), ('Forzar ♥Corazones', 'hearts'), ('Forzar ♦Diamantes', 'diamonds')])
            if shift=="pikes":
                game.ForcedSuit= "P"
                game.ForcedSuitStr= "Picas"
            elif shift=="clubs":
                game.ForcedSuit= "C"
                game.ForcedSuitStr= "Tréboles"
            elif shift=="hearts":
                game.ForcedSuit= "H"
                game.ForcedSuitStr= "Corazones"
            else:
                game.ForcedSuit= "D"
                game.ForcedSuitStr= "Diamantes"

    def CheckIfForceSuit():
        global game
        if game.ForceSuit== True: #Important: If pass the turn, and the ForceSuit is enabled then the ForceSuit is disabled
            renpy.show_screen('comment', "Al pasar, el forzado a palo "+str(game.ForcedSuitStr)+" ya no tiene efecto.", 2)
            game.ForceSuit= False   

    #PassCount functions->

    def IncPassCount():
        global game
        game.PassCount+= 1

    def ResetPassCount():
        global game
        game.PassCount= 0

    #When you pass you turn:
    def PassYourTurn():
        IncPassCount() #<-Inc the PassCount
        CheckIfForceSuit() 
        return False 

    def calculate_score(Character):
        global c
        score= 0
        for item in Character.deck:
            score= score + item[6]
        return score

    def CalcFrequencyOfSuits(whatdeck, AvoidThisCard):
        global c
        PikesCount= 0
        ClubsCount= 0
        HeartsCount= 0
        DiamondsCount= 0 
        for item in whatdeck:
            if (AvoidThisCard is None) or (item!= AvoidThisCard):
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

    def game_start(Charact, YouWinMsg, YouLoseMsg):
        global c
        global game     
        renpy.hide_screen("current_datetime")  #Hide the time indicator
        renpy.block_rollback() #Block the Back dialogue button
        CurrentMusic= renpy.music.get_playing() #Save the current music filename
        renpy.music.play(music.dreaming_in_puzzles, loop=True, fadein=2, fadeout=2)
        c.me.adversary= Charact
        cards_to_play= []
        best_cards_to_play=[]
        even_more_best_cards_to_play=[]
        game.MeScore= 0
        game.AdversaryScore= 0
        game.RoundCount= 0
        MeWonRounds= 0
        AdversaryWonRounds= 0
        import random
        #Random turn
        me_turn= bool(random.getrandbits(1))
        #Save the previous me_turn value (True or False)
        previous_me_turn= me_turn
        while (game.MeScore<100) and (game.AdversaryScore<100):
            break
            firsthand_create()                            
            first_turn= True
            if game.RoundCount>0: #Switch the turn at each round
                me_turn= not previous_me_turn
                previous_me_turn= me_turn            
            game.RoundCount+= 1
            game.TurnCount=0
            renpy.show_screen("game_data")
            while (True): #----------------PLAY TIL ROUND ENDS------------------
                game.TurnCount+= 1
                if game.PassCount>=4: #Multiple passes do not allowed, CANNOT BE POSSIBLE, THIS ONLY CAN OCCUR IF THE ALGORIMTH BELOW FAILS, it's a prevention messure to avoid an eternal loop in the game of players ever passing
                    ResetPassCount() #PassCount= 0 | Important for avoid an eternal loop when a round ends at this point
                    break 
                renpy.show_screen("adversary_data")                                                    
                #---------- MY TURN ----------------------
                if me_turn: #---------- MY FIRST TURN ----------------------
                    if first_turn: 
                        renpy.show_screen('comment', "Empiezas tú", 2)    
                        while True:
                            #Show your first hand
                            itemindex, item= renpy.call_screen('my_hand', True)
                            renpy.show_screen('my_hand', False)
                            #Play a card
                            if item!= None: #If you click on a card not on the deck
                                PlayCard(c.me.deck, item, itemindex)
                                #Check if your card is an eight
                                CheckIsEight(item)
                                #Change the turn of the game
                                first_turn= False
                                me_turn= False
                                break     
                    else: #---------- MY TURN ----------------------
                        renpy.show_screen('comment', "Es tu turno", 1)        
                        #Show your cards
                        while True: #Loop til I got playable cards (til break with the 'break' stament)
                            if c.me.gamecount==0: #CHOICE MENU
                                #Show your hand
                                result= renpy.show_screen('my_hand', False)
                                #Choose some options to play
                                if len(game.deck)>0: #You cannot pass if there are cards in the deck
                                    shift= menu([('Coger una carta del mazo', 'draw'), ('Jugar una de tus cartas', 'play')])
                                else:
                                    shift= menu([('Pasar', 'pass'), ('Jugar', 'play')])
                                #The results of your choices
                                #DRAW A CARD FROM THE DECK
                                if (shift=='draw'):
                                    me_turn= draw_a_card(c.me)                                                                
                                #PLAY A A CARD
                                elif (shift=='play'):
                                    renpy.show_screen('comment', "Escoge una carta.", 1)  
                                    #SELECT A CARD FROM YOUR HAND
                                    itemindex, item= renpy.call_screen('my_hand', True)
                                    renpy.show_screen('my_hand', False) #<-Important if you don't want my hand screen dissapears after the interaction
                                    if item== None:
                                        me_turn= draw_a_card(c.me)
                                    else:                                
                                        #CHECK IF YOU CAN PLAY THE ELIGIBLE CARD
                                        if (play_a_card(itemindex, item)== True):
                                            me_turn= False
                                            break
                                #PASS YOUR TURN
                                elif (shift=='pass'):                                                           
                                    me_turn= PassYourTurn()
                                    break
                            else: #DYNAMIC PLAY (NOT CHOICE MENU)
                                itemindex, item= renpy.call_screen('my_hand', True) #SELECT A CARD FROM YOUR HAND
                                renpy.show_screen('my_hand', False) #<-Important if you don't want my hand screen dissapears after the interaction
                                if item== None:
                                    me_turn= draw_a_card(c.me)
                                elif item== False:
                                    me_turn= PassYourTurn()
                                    break
                                else:                                
                                    #CHECK IF YOU CAN PLAY THE ELIGIBLE CARD
                                    if (play_a_card(itemindex, item)== True):
                                        me_turn= False
                                        break
                        #End of the While loop
                        if len(c.me.deck)==0: #I HAVE NOT CARDS = LAST TURN FOR ME = I WIN!
                            break
                        #_window_hide()
                else:
                    #--------TURN OF THE ADVERSARY---------
                    if first_turn:
                        #-------IF ADVERSARY'S FIRST TURN
                        renpy.show_screen('my_hand', False)
                        RandomNumber= GetRandomNum(c.me.adversary.deck)
                        PlayCard(c.me.adversary.deck, c.me.adversary.deck[RandomNumber], RandomNumber)
                        PlayableCard= True
                        first_turn= False
                    else: #--------TURN OF THE ADVERSARY---------
                        #Calculate what card the adversary will play
                        #First what cards in this hand match with the Card in Play
                        drawed_cards= 0
                        has_a_eight= False
                        while True:      
                            del cards_to_play[:]
                            del best_cards_to_play[:]
                            #pcards_to_play is a list of an integer and a tuple: [index,(val,suit)]
                            for itemindex, item in enumerate(c.me.adversary.deck):
                                if (game.CardInPlay[0]== "8") and (game.ForceSuit== True): #If the playing card is an Eight
                                    if (item[0]=="8") or (item[1]==game.ForcedSuit): #If Eight or match the forced suit
                                        cards_to_play.append((itemindex, item)) #append in cards_to_play list, a tuple of (itemindex, item)
                                        if item[0]=="8": #mark that the adversary has a Eight at least
                                            has_a_eight= True
                                else: #IF THE PLAYIND CARD IS A COMMON CARD ->
                                    if (item[0]=="8") or ((item[0]==game.CardInPlay[0]) or (item[1]==game.CardInPlay[1])): #If Eight or match val or suit
                                        cards_to_play.append((itemindex, item))
                                        if item[0]=="8": #mark that the adversary has a Eight at least
                                            has_a_eight= True
                            #IF HE HAVE SOME CARD TO PLAY OR THERE ARE NO CARDS IN THE DECK
                            if (len(cards_to_play)>0) or (len(game.deck)==0):
                                break #EXIT LOOP
                            else: #IF HE DON'T HAVE ANY CARD TO PLAY THEN DRAW A CARD FROM THE DECK
                                draw_a_card(c.me.adversary)
                                drawed_cards+= drawed_cards
                        if (len(cards_to_play)>0):
                            if (drawed_cards>0):
                                renpy.show_screen('comment', c.me.adversary.name +" ha cogido "+ str(drawed_cards)+" cartas del mazo.")      
                            #HERE THE ADVERSARY AI ACCORDING HIS GAME LEVEL
                            if (c.me.adversary.gamelevel>1):   #STUDY SOME POSSIBILITIES          
                                #FIRSTLY STUDY THE POSSIBILITY OF PLAY AN Eight
                                if (has_a_eight== True):
                                    if (len(cards_to_play)==1):  #If the adversary has an Eight as his unique playable card then the adversary has 100% of possibility to play this 
                                        play_the_eight= True
                                    else:  #If the adversary has an Eight and other playable cards then the adversary has 50% of possibility to play the Eight
                                        play_the_eight= bool(random.getrandbits(1))
                                else: #if the adversary has not an Eight
                                    play_the_eight= False
                                #IF NOT AN Eight, PLAY A COMMON CARD
                                if play_the_eight== False:                                       
                                    dictionaryofsuits= CalcFrequencyOfSuits(c.me.adversary.deck, None) #In this level check the frequency of suits in his hand  
                                    import operator
                                    #Order the dictionary suits by its frequency in a decreasing order
                                    sorted_suit_frequencies= sorted(dictionaryofsuits.items(), key=operator.itemgetter(1), reverse= True)
                                    #Created an ordered list with the cards to play according its suit->
                                    #x= ""
                                    #for suit in sorted_suit_frequencies:
                                        #x=x+","+suit[0]
                                    #renpy.show_screen('comment3', x, 20)   
                                    #x= ""
                                    for suit in sorted_suit_frequencies:
                                        for item in cards_to_play:                                    
                                            if item[1][1]==  str(suit[0]):
                                                best_cards_to_play.append(item) 
                                                #x= x+", "+str(item[1][0])+str(item[1][1])
                                    #renpy.show_screen('comment', x, 20)   
                                    if c.me.adversary.gamelevel==1: #DEBUG, PUT A VALUE OF 2 WHEN DEBUG IS FINISHED
                                        #Now get the first card with the suit of max frequency from the best playable cards
                                        #Get the fist element and its index to play                                                                                                       
                                        PlayCard(c.me.adversary.deck, best_cards_to_play[0][1], best_cards_to_play[0][0])
                                    else: #if opponent has a level of master, he should play the card of high value (important in case of tie or he loss)
                                        #So first I select all the cards of the suit of max frequency
                                        BetterSuit= best_cards_to_play[0][1][1] #The suit of the first card of the list
                                        #renpy.watch(BetterSuit)  #DEBUG
                                        #x=""
                                        for item in best_cards_to_play: #get all the cards of this suit
                                            if item[1][1]== str(BetterSuit):
                                                even_more_best_cards_to_play.append(item)
                                                #x= x+", "+str(item[1][0])+str(item[1][1])
                                            else:
                                                break #No more cards of the better suit
                                        #renpy.show_screen('comment2', x, 20) 
                                        #And finally get the card with the highest value and play it
                                        import operator                                    
                                        BetterCard= max(even_more_best_cards_to_play, key=operator.itemgetter(1))
                                        PlayCard(c.me.adversary.deck, BetterCard[1], BetterCard[0])     
                                        del even_more_best_cards_to_play[:]                               
                                    #else:    
                                        #IF GAME.DECK= 0 THE ADVERSARY COULD TO KNOW WHAT CARDS YOU HAVE    
                                        #if len(game.deck==0): 
                                            #for item_adversary in best_cards_to_play:
                                                #for item_me in c.me.deck
                                                    #if (item_adversary[1][0]!= item_me[0]) and (item_adversary[1][1]!= item_me[1]): #If matche sin val or suit, discard it
                                                    #best_cards_to_play_2.append(item_adversary)
                                                    #break
                                else: #if play the Eight
                                    for item in cards_to_play: #Search the first Eight to play (don't care what suit because you can change it)
                                        if (item[1][0]==  "8"):                    
                                            PlayCard(c.me.adversary.deck, item[1], item[0])
                                            break #not more search for the Eight
                            else: #if the player level is =1 then choose a random card and do not care anything
                                RandomNumber= random.randint(0,len(cards_to_play)-1)
                                PlayCard(c.me.adversary.deck, cards_to_play[RandomNumber][1], cards_to_play[RandomNumber][0])      
                            PlayableCard= True #HE CAN PLAY THE CARD
                        else: 
                            PlayableCard= False #HE CANNOT PLAY ANY CARD
                    #--------------- DRAW A PLAYABLE CARD -------------
                    if (PlayableCard== True) and (len(c.me.adversary.deck)>0):
                        if game.CardInPlay[0]=="8": #IF CARD-IN-PLAY IS A Eight
                            game.ForceSuit= True
                            #If adversary level is expert or master->
                            if (c.me.adversary.gamelevel>1):
                                #Analyze what is the suitable suit to switch
                                dictionaryofsuits= CalcFrequencyOfSuits(c.me.adversary.deck, game.CardInPlay)
                                #Get the suit of max. frequency ->                           
                                game.ForcedSuit= max(dictionaryofsuits, key=dictionaryofsuits.get)
                                #Otra opción a la anterior sentencia: game.ForcedSuit= max(dictionaryofsuits, key=lambda key: dictionaryofsuits[key])
                                #renpy.show_screen('comment', game.ForcedSuit, 20) DEBUG
                            else: #if adversary has a game level of 1
                                #Force a random Suit
                                game.ForcedSuit= random.choice("PCHD")
                            #Set the ForcedSuit
                            if game.ForcedSuit== "P":
                                game.ForcedSuitStr= "Picas"
                            elif game.ForcedSuit== "C":
                                game.ForcedSuitStr= "Tréboles"
                            elif game.ForcedSuit== "H":
                                game.ForcedSuitStr= "Corazones"
                            else:
                                game.ForcedSuitStr= "Diamantes"
                            ResetPassCount() #PassCount= 0
                            renpy.say(c.me.adversary.charobj, "Mi carta es {color=#"+str(game.CardInPlay[4])+"}"+str(game.CardInPlay[2])+" de "+str(game.CardInPlay[5])+str(game.CardInPlay[3])+"{/color}.\nTe obligo a que eches un palo "+game.ForcedSuitStr+".")
                        else: #IF CARD-IN-PLAY IS A REGULAR CARD (NOT AN Eight)
                            if (c.me.gamecount==0):
                                renpy.say(c.me.adversary.charobj, "Mi carta es {color=#"+str(game.CardInPlay[4])+"}"+str(game.CardInPlay[2])+" de "+str(game.CardInPlay[5])+str(game.CardInPlay[3])+"{/color}.\nEcha una carta del mismo palo o número.")
                    #------IF ADVERSARY HAS NOT A PLAYABLE CARD ---------
                    else:
                        if (len(c.me.adversary.deck)>0):
                            IncPassCount() #<-Inc the PassCount
                            renpy.say(c.me.adversary.charobj, "Paso el turno.")
                            CheckIfForceSuit()   
                        else:                    
                            renpy.say(c.me.adversary.charobj, "Mi última carta es {color=#"+str(game.CardInPlay[4])+"}"+str(game.CardInPlay[2])+" de "+str(game.CardInPlay[5])+str(game.CardInPlay[3])+"{/color}.\n¡Ya no me quedan más!")
                            break
                    #------ ADVERSARY END OF TURN ------------------
                    renpy.block_rollback()
                    me_turn= True
            #-------------END OF while (True) = ROUND ENDS
            renpy.hide('card_img', layer="game")
            renpy.hide_screen("adversary_data")                        
            renpy.hide_screen("my_hand")
            if len(c.me.deck)==0:    
                #Calculate the score
                won_score= calculate_score(c.me.adversary)
                game.MeScore+= won_score
                MeWonRounds+= MeWonRounds
                renpy.show_screen('comment', "¡¡¡HAS GANADO ESTA RONDA y "+str(won_score)+" puntos!!!")  
                renpy.say(c.me.adversary.charobj, YouWinMsg)
            elif len(c.me.adversary.deck)==0:
                game.AdversaryScore+= calculate_score(c.me)
                AdversaryWonRounds+= AdversaryWonRounds
                renpy.show_screen('comment', "¡¡¡HAS PERDIDO ESTA RONDA!!!") 
                renpy.say(c.me.adversary.charobj, YouLoseMsg)
            else:                
                _mescore= calculate_score(c.me)
                _adversaryscore= calculate_score(c.me.adversary)
                #If tie occurs, the lowest score wins this round
                if (_mescore<_adversaryscore): #You win!
                    #The puntuation is the difference between the high and low score
                    won_score= _adversaryscore - _mescore
                    game.MeScore+= won_score
                    MeWonRounds+= MeWonRounds
                    renpy.show_screen('comment', "¡¡¡HAS GANADO ESTA RONDA y "+str(won_score)+" puntos!!!")  
                    renpy.say(c.me.adversary.charobj, YouWinMsg)
                elif (_mescore>_adversaryscore):
                    game.AdversaryScore+= _mescore - _adversaryscore
                    renpy.show_screen('comment', "¡¡¡HAS PERDIDO ESTA RONDA!!!") 
                    renpy.say(c.me.adversary.charobj, YouLoseMsg)
                else:
                    renpy.show_screen('comment', "Habéis empatado.") 
            renpy.pause(2.0)
        #-------------END OF GAME ()
        c.me.gamecount+= 1
        renpy.hide('card_img', layer="game")
        renpy.hide_screen("game_data")                        
        renpy.hide_screen("adversary_data")                        
        renpy.hide_screen("my_hand")
        renpy.show_screen("current_datetime") 
        if CurrentMusic!= None:
            renpy.music.play(CurrentMusic, loop=True, fadein=2, fadeout=2)
        if (game.MeScore>=100):
            c.me.victorycount+= 1            
            return True
        else:
            c.me.downcount+= 1
            return False