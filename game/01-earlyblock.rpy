python early:
    
    #HERE I DEFINE SOME CLASSES

    #To assign an object to a dictionary
    class Bunch(object):
        def __init__(self, adict):
            self.__dict__.update(adict)

    #--------------------------------------------
    #Define the player's choices that affect the story
    class Choice:
        def __init__(self, status, description):
            self.status= status
            self.description= description       

    # LIST OF CHOICES ######################
    ##### YOUR CHOICES ###################
    # 0: Le preguntasté a Nacho acerca de su nueva relación.  
    # 1: Mentiste a Paolo sobre tu verdadero nombre (María)
    # 2: Le pusiste un helado a tu hermana Jesica en la cabeza.
    # 3: Te ofreciste a acompañar a Carmen a su/vuestra clase.
    #--------------------------------------------
    #Define the Today date
    #05/10/09 18:00
    class NowClass:   
    
        def __init__(self, year, month, day, hour, minute):
            import datetime
            #(2015, 9, 1, 7, 20)
            self.datetime= datetime.datetime(year, month, day, hour, minute)
            self.day= self.datetime.strftime("%d") 
            months= ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dec"]
            self.month= months[month-1]
            days= ["Lun","Mar","Mie","Jue","Vie","Sab","Dom"]
            self.dayofweek= days[self.datetime.weekday()]            
        
        def UpdateDatetime(self, year, month, day, hour, minute):
            import datetime
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
        def __init__(self, id, name, filename, value, important, tooltip):
            self.id= id
            self.name= name
            self.filename= filename
            self.value= value
            self.important= important
            self.tooltip= tooltip
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
    class Charact(object):
        def __init__(self, charobj= None, name="", genre= Genre.Male, money=0, affinity=90, love=0, score=0, adversary= None, isknown= False, isfriend= False, gamelevel=1, victorycount=0, downcount=0, gamecount=0):
            self.adversary= adversary
            self.affinity= affinity
            self.charobj= charobj
            self.choices= {}
            self.deck= []    
            self.friendslist= []
            self.items= []
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
            self.gamecount= gamecount

        #Add a new friend
        def AddFriend(self, Character, IsKnown, IsFriend):
            global c
            Character.isknown= IsKnown
            Character.isfriend= IsFriend
            self.friendslist.append(Character)

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
            if inc==False:
                amount= -amount
            self.love+= amount
            if self.love<0:
                self.love=0
            elif self.love>100:
                self.love=100