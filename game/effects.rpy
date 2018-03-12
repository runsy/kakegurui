#------------------------------------------------
#Dissolve & text at the same time
init:
 transform atldissolve:
  alpha 0 # makes image transparent
  linear 0.5 alpha 1.0 # takes 0.5 seconds to make image fully opaque. adjust as needed.
#------------------------------------------------
#Rain & Lightning effect
init:
  image rev_lightning = im.Flip("img/weather/lightning.png", horizontal=True)
  image rain:
    "img/weather/rain1.png"
    0.2
    "img/weather/rain2.png"
    0.2
    "img/weather/rain3.png"
    0.2
    repeat      
  image lightning:
    choice: #weight of choice is 1
      "img/weather/lightning.png"
      alpha  0.0
      0.5 # show nothing for 0.5 seconds      
    choice 0.1: #weight of choice is 0.1
      "img/weather/lightning.png"
      alpha  0.0
      linear 0.3 alpha  1.0
      linear 0.3 alpha  0.0           
    choice 0.1:
      "rev_lightning"
      alpha  0.0
      linear 0.3 alpha  1.0
      linear 0.3 alpha  0.0
    repeat
#------------------------------------------------
#Shake effect
init:
 python:        
        import math
        class Shaker(object):          
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }     
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x
                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
                xpos = xpos - xanchor
                ypos = ypos - yanchor                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                return (int(nx), int(ny), 0, 0)
        def _Shake(start, time, child=None, dist=100.0, **properties):            
            SoundShock
            move = Shaker(start, child, dist=dist)        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties) 
        def SoundShock(self):
            renpy.sound.play("sound/effects/shock2.ogg") 
        Shake= renpy.curry(_Shake)
#------------------------------------------------