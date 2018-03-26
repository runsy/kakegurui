#Items
image rose= im.FactorScale("img/item/rose.png", 0.3)
image log= im.FactorScale("img/item/log.png", 0.3)

transform _show_item:    
    zoom 0.3
    linear 1.0 zoom 0.8

screen show_item(_item):
    modal True
    $change_cursor("hand64")
    imagebutton idle _show_item(_item)  xanchor 0.5 xpos 0.5 yanchor 0.5 ypos 0.65 action Return()