#Inventory button and screen

#Images
image euro_coin= im.FactorScale("img/beatmeter/euro_coin.png", 0.35)
image heart= im.FactorScale("img/beatmeter/heart.png", 0.17)
image affinity= im.FactorScale("img/beatmeter/affinity.png", 0.17)

screen inventory_button:
    vbox xalign 0 yalign 0:
        textbutton "Pulsómetro" action ui.callsinnewcontext("aff_screen_label")
  
screen aff_screen:
 vbox:
  spacing 10
  xalign 0.5 yalign 0.5
  frame:
   hbox:
    text "{color=ffffff}Dinero: [c.me.money]{/color} "
    image("euro_coin")  
  frame:
   vbox:
    hbox:
     for friend in c.me.friendslist:
      if friend.isknown & friend.isfriend:
       vbox:
        text "{color=ffffff}[friend.name]{/color}" at center
        image("side [friend.name]_pulsometer") at center
        vbox:
         hbox:
          image("affinity")
          python:
            if friend.affinity>=60:
             color_affinity= "105e01"
            elif friend.affinity>=40 and friend.affinity<60:
             color_affinity= "eac168" 
            elif friend.affinity<40:
             color_affinity= "bd0b18"            
          text "{color=[color_affinity]}[friend.affinity]%{/color}"
         if friend.genre== Genre.Male:
          hbox:
           image("heart")
           text "[friend.love]%"
  frame:
   vbox:
    text "Inventario" at center
    hbox:
     for item in c.me.items:      
       vbox:
        image("[item.filename]") at center
        text "{size=-4}{color=ffffff}[item.name]{/color}{/size}" at center
  frame:
    vbox:
        textbutton "Volver":
            action Return()
            tooltip "Cierra el inventario"
        $tooltip= GetTooltip()
        if tooltip:
            text "[tooltip]"

label aff_screen_label:
 call screen aff_screen
 return