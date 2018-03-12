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
    text "{color=ffffff}Dinero: [me.money]{/color} "
    image("euro_coin")  
  frame:
   vbox:
    hbox:
     for x in me.friendslist:
      if x.isknown & x.isfriend:
       vbox:
        text "{color=ffffff}[x.name]{/color}" at center
        image("side [x.name]_pulsometer") at center
        vbox:
         hbox:
          image("affinity")
          python:
            if x.affinity>=60:
             color_affinity= "105e01"
            elif x.affinity>=40 and x.affinity<60:
             color_affinity= "eac168" 
            elif x.affinity<40:
             color_affinity= "bd0b18"            
          text "{color=[color_affinity]}[x.affinity]%{/color}"
         if x.genre== Genre.Male:
          hbox:
           image("heart")
           text "[x.love]%"
  frame:
   vbox:
    text "Inventario" at center
    hbox:
     for x in me.items:      
       vbox:
        image("[x.filename]") at center
        text "{size=-4}{color=ffffff}[x.name]{/color}{/size}" at center
  frame:
    vbox:
     textbutton "Volver" action Return()
 
label aff_screen_label:
 call screen aff_screen
 return
