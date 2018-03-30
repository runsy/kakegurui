#-----------------------------------
screen back_button:
    zorder 1 #under the dialogue window
    vbox xalign 1.0 ypos 550:
        textbutton "<<" action Rollback()
#-----------------------------------
style sty_current_datetime is text:
    font "fonts/Stamp.ttf"
    size 30
    color "#ffffff"
    justify True
#-----------------------------------
screen current_datetime:
    frame:
        background RoundRect("#ff666666")
        xalign 1.0
        vbox:
            text "[now_datetime.dayofweek], [now_datetime.day] de [now_datetime.month]" style "sty_current_datetime"
            text "[now_datetime.datetime.hour]:[now_datetime.datetime.minute]" style "sty_current_datetime"
#-----------------------------------
transform show_hide_dissolve:
    on show:
        alpha .0
        linear .5 alpha 1.0
    on hide:
        alpha 1.0
        linear .5 alpha .0
#-----------------------------------        
screen comment(comment_text, time= 3):
    frame:
        at show_hide_dissolve
        xcenter 0.5
        background RoundRect("#ae426f")
        hbox:
            timer time repeat False action [Hide('comment')]
            text "{size=-3}{color=ffffff}[comment_text]{/color}{/size}" 
#-----------------------------------
screen comment2(comment_text, time= 3):
    frame:
        at show_hide_dissolve
        xcenter 0.2
        background RoundRect("#ae426f")
        hbox:
            timer time repeat False action [Hide('comment')]
            text "{size=-3}{color=ffffff}[comment_text]{/color}{/size}" 
#-----------------------------------
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