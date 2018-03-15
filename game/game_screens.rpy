screen game_data():
    layer "game"
    frame xalign 0.5 ypos 0.1:
        python:
            if me.adversary.genre== "Male":
                pronoun= "Él"
            else:
                pronoun= "Ella"
            _adversary_cards= pronoun+" tiene "+str(len(me.adversary.deck))+" cartas."
            _cards=""
            for item2 in me.adversary.deck:
                _cards= _cards+str(item2[0])+str(item2[1])+", "
        background RoundRect("#00ae426f")  
        hbox:
            label _adversary_cards
            label _cards

screen my_hand(clickable):
        layer "game"
        python:
            MyHandLen= len(me.deck)
            i= 0            
        hbox spacing 0:
            for itemindex, item in enumerate(me.deck):    
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
                    imagebutton idle Transform(CardName, zoom=_zoom) xanchor 0.5 xpos _xpos ypos _ypos action Return([itemindex, item])
                else:
                    imagebutton idle Transform(CardName, zoom=_zoom) xanchor 0.5 xpos _xpos ypos _ypos
                $i= i+1

#Cards
#--------
#IMAGE ACTUALLY IN PLAY
#image card_img= At("[CardPath]", card_in_play_transform)
image card_img= "[CardPath]"

#RESTING DECK (BACK)
image deck_img= "img/cards/BACK.png"

transform card_in_play_transform:
    xpos 0.7
    ypos 0.38
    zoom 0.3

transform deck_transform:
    xpos 0.25
    ypos 0.38
    zoom 0.3

transform my_card_transform(_xpos, _ypos, _zoom):
    ypos _ypos
    xpos _xpos
    zoom _zoom