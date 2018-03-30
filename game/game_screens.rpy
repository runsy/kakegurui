screen gameinfo(comment_text, _time= 1.5):
 frame:
  at show_hide_dissolve
  xcenter 0.5
  background RoundRect("#ae426f")
  hbox:
   timer _time repeat False action [Hide('gameinfo')]
   text "{size=-3}{color=ffffff}[comment_text]{/color}{/size}" 
screen adversary_data():
    layer "game"
    frame xalign 0.5 ypos 0.1:
        python:
            if c.me.adversary.genre== "Male":
                pronoun= "Él"
            else:
                pronoun= "Ella"
            _adversary_cards= pronoun+" tiene "+str(len(c.me.adversary.deck))+" cartas."
            #_cards=""
            #for item2 in c.me.adversary.deck:
                #_cards= _cards+str(item2[0])+str(item2[1])+", "
        background RoundRect("#00ae426f")  
        hbox:
            label _adversary_cards
            #label _cards

screen game_data():
    layer "game"
    frame xalign 0.85 ypos 0.05:
        python:
            _roundcount= "Ronda= "+ str(game.RoundCount)
            _turncount= "Turno= "+ str(game.TurnCount)
            _mescore= "Mis puntos= "+str(game.MeScore)
            _adversaryscore= "Puntos de "+ c.me.adversary.name + "= " +str(game.AdversaryScore)
        background RoundRect("#00ae426f")  
        vbox:
            hbox:
                label _roundcount
            hbox:
                label _turncount
            hbox:
                label _mescore
            hbox:
                label _adversaryscore


transform fade_card:      
    zoom 0.3
    additive 0.15

screen my_hand(clickable):
        layer "game"
        python:
            MyHandLen= len(c.me.deck)
            i= 0             
        if game.ForceSuit== True:                 
            label game.ForcedSuitStr+" forzado." xpos 0.21 ypos 0.45 background RoundRect("#00ae426f")  
        if (clickable== True) and (c.me.gamecount>0) and (len(game.deck)==0): #Show the pass button
            textbutton "Pasar el turno" xanchor 0.5 xpos 0.5 ypos 0.58 action Return([False, False])
        #RESTING DECK (BACK)
        if len(game.deck)>0:
            if clickable== True:
                imagebutton idle Transform("img/cards/BACK.png", zoom=0.3)  hover fade_card("img/cards/BACK.png") xpos 0.72 ypos 0.25 action Return([None, None])
            else:
                imagebutton idle Transform("img/cards/BACK.png", zoom=0.3)  xpos 0.72 ypos 0.25
        hbox spacing 0:
            for itemindex, item in enumerate(c.me.deck):    
                $CardName= "img/cards/"+str(item[0])+str(item[1])+".png"
                python:
                    if MyHandLen<=7:
                        _zoom= 0.3
                    else:
                        zoom= 0.3 * (7.0/MyHandLen)
                        _zoom= (zoom - 0.044) / (2.1 - 0.044)
                        _zoom= _zoom+0.195     
                    c_dist= -90 #card distance 
                    middle_card= int(MyHandLen/2)
                    middle_card_xpos= int(720/2)
                    if MyHandLen % 2 == 0:        
                        middle_card_xpos+= int(c_dist/2)
                    # Math
                    _xpos= middle_card_xpos + (c_dist * (i - middle_card))
                    if MyHandLen>7:
                        _xpos= _xpos -(51*MyHandLen)
                    else:
                        _xpos= _xpos -(45*MyHandLen)
                    _ypos= config.screen_height-260
                if clickable== True:
                    imagebutton idle Transform(CardName, zoom=_zoom) hover fade_card(CardName) xanchor 0.5 xpos _xpos ypos _ypos action Return([itemindex, item])
                else:
                    imagebutton idle Transform(CardName, zoom=_zoom) xanchor 0.5 xpos _xpos ypos _ypos
                $i= i+1

#Cards
#--------
#IMAGE ACTUALLY IN PLAY
#image card_img= At("[game.CardPath]", card_in_play_transform)
image card_img= "[game.CardPath]"

transform card_in_play_transform:
    xpos 0.7
    ypos 0.38
    zoom 0.3

transform my_card_transform(_xpos, _ypos, _zoom):
    ypos _ypos
    xpos _xpos
    zoom _zoom