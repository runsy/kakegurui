#-----------------------------------
screen back_button:
 zorder 1 #under the dialogue window
 vbox xalign 1.0 ypos 550:
  textbutton "<<" action Rollback()
#-----------------------------------
transform show_hide_dissolve:
    on show:
        alpha .0
        linear .5 alpha 1.0
    on hide:
        alpha 1.0
        linear .5 alpha .0
        
screen comment(comment_text, time= 3):
 frame:
  at show_hide_dissolve
  xcenter 0.5
  background RoundRect("#ae426f")
  hbox:
   timer time repeat False action [Hide('comment')]
   text "{size=-3}{color=ffffff}[comment_text]{/color}{/size}" 

screen comment2(comment_text, time= 3):
 frame:
  at show_hide_dissolve
  xcenter 0.2
  background RoundRect("#ae426f")
  hbox:
   timer time repeat False action [Hide('comment')]
   text "{size=-3}{color=ffffff}[comment_text]{/color}{/size}" 

screen comment3(comment_text, time= 3):
 frame:
  at show_hide_dissolve
  xcenter 0.8
  ycenter 0.5
  background RoundRect("#ae426f")
  hbox:
   timer time repeat False action [Hide('comment')]
   text "{size=-3}{color=ffffff}[comment_text]{/color}{/size}"
#-----------------------------------
screen today:
 vbox xalign 1.0:
  text "{size=-3}{color=fbf39b}[today.dayofweek], [today.day] de [today.month]{/color}{/size}"
#-----------------------------------
screen gameinfo(comment_text, _time= 1.5):
 frame:
  at show_hide_dissolve
  xcenter 0.5
  background RoundRect("#ae426f")
  hbox:
   timer _time repeat False action [Hide('gameinfo')]
   text "{size=-3}{color=ffffff}[comment_text]{/color}{/size}" 