#Game script
#----------------
#Load other script files
jump layers
jump characters #Load the characters definitions & Images
jump backgrounds #Load the background images
jump sound #Load the sound functions
jump effects #Load the effect functions
jump inventory #Load the inventory
jump misc_screens
jump game_screens
jump init_python #Init the python

#----------------
#-->Start of game
#----------------

label start:
    #jump _010
    scene black
    stop music
    play sound effect.typing_PC
    centered "{color=#fff}{cps=20}Isla de Gran Canaria{/cps}{/color}"
    play sound effect.typing_PC
    centered "{color=#fff}{cps=20}15 de septiembre{/cps}{/color}"
    stop sound

label intro:
    play music music.farty_mcsty fadein 2 fadeout 2
    call LoadGUI
    call UpdateToday
    ma "Hola, me voy a presentar."
    ma "Me llamo Maruja, pero nadie me llama así. Todo el mundo me dice {b}Maru{/b}, a secas."
    ma "Tengo 15 años y estoy a punto de cumplir los dieciseis. ¡Voy a celebrar una súper fiesta!"
    scene bg insti_vista_pajaro at atldissolve
    ma tierna "Este es mi instituto, Campolargo. Aquí paso la mayoría de mi tiempo.\nEl resto del día ando por ahí con mis amigos, o estoy de compras, me chifla gastar pasta."
    ma "Hoy es el primer día de insti, después de las vacaciones de verano. Odio empezar el curso. Odio estudiar."
    ma sonriente "Pero, ¡eh!, no saco tan malas notas. No soy una chica de sobresaliente, pero tampoco apruebo por los pelos, jeje."
    ma triste "Estoy deseando ver a mi pandilla: Violeta, Nacho...\nHace dos meses que no los veo ¡Cómo los echo de menos!"
    ma side "Pero antes de empezar a contaros mi historia, vamos a aprender a jugar."
    ma "Arriba tienes el botón {b}{color=#041c96}Pulsómetro{/color}{/b}. Haz clic sobre él."
    ma "Ahí puedes ver el dinero que tienes en cualquier momento.\nTambién puedes ver los amigos que tienes."
    ma "Las opciones que puedas tomar en el juego influirán en tus amistades y novios.\nTen cuidado con las opciones que eliges. A veces las cosas no son lo que parecen..."
    ma "La afinidad indica el grado de amistad con esa persona.\nTambién podrás ver cuán enamorado está un chico de ti."
    ma "Y ahora me voy para el insti. Empieza mi aventura.\n{i}Si se le puede llamar a eso volver al cole.{/i}"

label _001:
    scene bg insti_puerta at atldissolve 
    ma sonriente "Querido insti... ¿A que parece una cárcel? Jijiji.\nBueno, no es para tanto, pero casi."
    ma preocupado "Pero... ¡¿DÓNDE ESTÁN?! Esto debería estar ya lleno de gente.\nMis amigos,\n*Snif*"
    ma "Esto me recuerda a cuando me dice mi madre que tengo que aprender a estar sola.\n¡Pero es que son mis amigos, jopé!"
    play sound effect.ups
    ma asustado "¿Me habré equivocado de día y no empieza aún hoy el insti?\n*Ups*"
    play sound effect.pasar_zumbando
    show vio expectante
    vi "¡HOLA! ¡Maru! ¡¿Cómo estás?!"
    menu:
        "¡Agh! Casi me matas del susto":
            jump _002
        "Pues muy bien. Me alegro de verte":
            jump _003

label _002:
    vi triste "¿Eso es lo único que me tienes que decir?"
    vi chulesco "Ya veo lo que me has echado de menos..."
label _003:
    vi expectante "Tengo tantas cosas que contarte..."
    vi "Me lo he pasado genial este verano.\n¡Mira qué morenita estoy! ¿Te lo puedes creer?"
    vi enfadado "Ya sabes que mis papás me obligaron a ir con ellos a la casa de la playa. Qué coñazo..."
    vi rabioso "Pero lo bueno es que se abrió ante mí un mundo nuevo.\n¡Los locales de marcha!\nYa que ya tengo 15 años, me dejaron salir hasta las tantas."
    show vio sonriente
    ma triste "Jo, qué envidia, a ver cuando me dejan mis padres hacer esas cosas..."
    vi "Tú tranqui, colega, te queda poco para cumplir 16 años.\nEse día la vamos a liar, ya verás, jeje."
    vi "Además, te tengo que contar los últimos cotilleos...\n¿Sabes que Nacho se echó novieta?"
    ma sorprendido "¡¿Qué me dices?! ¿Nacho, ¿nuestro Nacho?"
    vi creido "Así te lo digo. Pero no sólo eso, lo más fuerte es que..."
    vi expectante "Se lió con una tía de nuestro insti. Que tú y yo conocemos..."
    ma sorprendido "Super fuerte, tía. ¡Ya me vas diciendo quién es!"
    vi neutral "Ups, por ahí se acerca Nacho, ya te contará él. Si quiere..."
    show vio neutral at right with move
    show nac sonriente at center with moveinleft
    na sonriente "Hola, mis niñas. Qué lindas que os veo. ¡Preciosas!"
    ma sonriente "Ay, Nachito. Eres un sol, de verdad. Qué cuqui eres."
    vi creido "Puaj, lo dirá por ti, Maru, que eres guapa.\nDe mí pasa mogollón."
    show vio colorado
    na chulo "Os quiero a las dos por igual, tontas. No sabéis lo mucho que os eché de menos...\nEstaba deseando veros."
    play sound effect.besucon
    vi "Maru tiene razón, eres lo más. ¡Ven que te como a besos!"
    ma picaro "Hay que ver, Violeta, lo que haces por un beso..."
    show nac asustado
    play sound effect.shock2
    vi rabioso "Mira quién habla, la que no se come un rosco." with Shake()
    menu:
        "Hay que ver como eres, jijiji.":
            jump _004
        "Oye, tía, te estás pasando tres pueblos.":
            jump _005
        "¡Eres una zorrona!":
            jump _006
label _004:
    vi neutral "Ya ves. Quiero mucho a Nacho —solo como amigo."
    jump _007
label _005:
    play sound effect.golpe_dramatico
    $violeta.change_affinity(False,0)
    show screen comment("Violeta se indigna un poco")
    vi chulesco "A ver, tía, que Nacho es mi amigo...\n¿Acaso no puedo darle un beso después de no verlo en dos meses?"
    jump _007
label _006:
    vi sonriente "Por lo menos yo sí pillo cacho, jajaja."
    jump _007
label _007:
    show nac neutral
    vi neutral "Y cambiando de tema. Nacho, ¿qué nos cuentas? ¿Qué hiciste en verano?"
    na "Pues nada, mucha playa, en el yate de mi padre, de fiesta. Nada del otro mundo."
    menu:
        "¿Y de tú novia qué de qué? ¿No nos hablas? Jejeje.":
            jump _008
        "{i}{color=#5bd53f}\[Ser discreta\]{/color}{/i} Ah, qué interesante.":
            jump _009 
label _008:
    play sound effect.golpe_dramatico
    $nacho.change_affinity(False,0)
    show screen comment("Nacho piensa que eres muy cotilla")
    na enfadado "¡¿Qué?! ¿Quién te ha contado eso?"
    na colorado "Ejem... prefiero no hablar. Lo siento." 
    $cho_status= True
    jump _010
label _009:
    $cho_status= False 
label _010:
    $me.choices.append(Choice(1, cho_status, "Le preguntasté a nacho acerca de su nueva relación."))
    na neutral "Bueno, voy entrando. A ver si veo a más colegas. Ciao"
    hide nac with dissolve
    show vio neutral at center with move
    vi expectante "Oye, tía, ¿echamos unas cartas?\nHe practicado mucho este verano."
    $whowins= game_start(violeta, "Eres muy buena jugando a las cartas.", "Deberías practicar más, ja, ja, ja.")
    vi expectante "Bueno, y tú, tía, ¿qué hiciste este verano?"
    show vio sonriente
    ma neutral "Nada, me pasó un poco como a ti, tuve que ir de vacaciones con mis padres y... hermanita.\nDe vacaciones a Roma."
    vi expectante "¡¿Eh?! ¿Me vas a comparar Roma con el chalet de mis padres?\nCuenta, cuenta..."
    ma picaro "¿Tengo otra opción...?\nVaaale, te cuento..."
label _011:
    hide screen inventory_button
    scene bg ruinas_romanas_sepia at atldissolve
    ma sonriente "Roma es una ciudad super chula. Aunque está muy sucia y hay piedras tiradas por todas partes, jeje."
    ma "Como te dije fui con mi madre y hermana, lo que era un tostón extra. Y hacía un calor que te cagas."
    scene bg ruinas_romanas with irisin
    show maru preocupado at center:
       xzoom -1.0
    show mama feliz at right with dissolve
    ma preocupado "Uf, qué calor. Y qué cansada estoy. Llevamos todo el día de aquí para allá.\nEl Foro, el Colíseo, las Termas..."
    mama irritado "¡Maru! Empápate de la cultura de este país milenario y deja de quejarte, anda."
    show maru sorprendido at center
    ma sorprendido "Jo, mami, es que llevamos seis días aquí, y lo único que hemos hecho es andar y andar sólo para ver museos y cosas viejas y derruidas.\nMe aburro."
    show je sonriente at left:
        xzoom -1.0
    with moveinleft
    play sound effect.pasar_zumbando
    jes "Hey, ¡¿cómo estáis?!"
    mama irritado "¡Jesica! ¿Dónde te habías metido?\nA ver si te van a raptar..."    
    jes neutral "¡Por ahí! A ver si encontraba un tesoro, jajaja."
    menu:
        "Tú eres tonta.":
            jump _012
        "Cariño, haz caso a mamá...":
            jump _013 
label _012:
    play sound effect.shock2  
    show maru alegre
    jes enfadado "¡¡¡LA TONTA ERES TÚ!!!" with Shake()
    jump _014
label _013:
    show maru enfadado
    jes neutral "Sí, el mismo caso que le haces tú... ¡Juas!"
    jump _014
label _014:
    play sound effect.shock2 
    mama irritado "A ver niñas ¡¡¡Portaos bien!!!" with Shake()
    jes alegre "He visto un carrito de los helados.\nMami, ¿me compras uno? Porfa..."
    mama "Bueno, pero espero que te portes bien..."
    hide mama with moveinright
    play sound effect.pedo
    jes sonriente "Ja, ja, ja. Ya ves, siempre consigo lo que quiero."
    hide je with moveinleft
    ma enfadado " Si no tuviera tan solo cinco años, se iba a enterar de lo que vale un peine.\n¿Y ahora que hago yo? Ya he visto todo..."
    play sound effect.flash
    scene bg ruinas_romanas with flash     
    show maru sorprendido at left_to_right
    ma sorprendido "¡Hey! ¿Qué ha sido eso?"
    python:
        paolo.isknown= True
        paolo.isfriend= True
        me.friendslist.append(paolo)
    show pao sonriente at right with moveinright
    pa "Ciao, bambina."
    menu:
        "¿Quién eres?":
            jump _017
        "¿Me has sacado una foto?":
            jump _015
        "¿Te quieres casar conmigo?":
            jump _016

label _015:
    pa sorprendido "Si te dijera que sí, ¿te importaría?"
    menu:
        "...No":
            jump _017                            
        "¡Pues claro que me importa, no te conozco!":
            jump _015_2
label _015_2:
    $paolo.change_love(True, 0)
    show screen comment("Paolo piensa que eres guay.")    
    pa sonriente "Me encantan las chicas con carácter, ja, ja, ja"            
    jump _017
label _016:
    show pao sonrojado
    $paolo.change_love(True, 0)
    show screen comment("Paolo se siente halagado.")
    play sound effect.shock2 
    show heartbeat at atllove(0.85, 0.4) with dissolve
    pause
    hide heartbeat
    jump _017
label _017:
    pa sonriente "Me ciamo Paolo. He venido a visitar las ruinas.\nY sacar fotos. Me gusta la historia."
    show maru colorado
    show heartbeat at atllove(0.5, 0.5) with dissolve
    play music music.calmer_times fadein 2 fadeout 2
    pa sonriente "Pero hasta ahora no había fotografiado un \"monumento\" tan bello como... {b}¡TÚ!{/b}"
    hide heartbeat
    pa sonriente "La verdad es que suelo ser un cortado con las chicas,\npero tú tienes algo especial no sé..."
    pa expectante "Tu mirada, tu pose, tu forma de ser... quizás."
    menu:
        "Gracias, qué bonitas palabras...":
            jump _019
        "¡Anda ya! ¡Si no me conoces de nada!":
            jump _018
label _018:        
    show pao sorprendido
    $paolo.change_love(False, 0)
    show heartbeat at atlbrokenheart(0.85, 0.4)
    play sound effect.romper
    show screen comment("Lo has herido un poco en sus sentimientos.")
    pause
    hide heartbeat
label _019:
    pa neutral "Bueno, y qué te cuentas bambina.\n¿Qué se te ha perdido por Roma?"
    ma alegre "Estoy de viaje con mi madre y hermana. Pasando unas vacaciones.\nSoy española."
    pa sonriente "¡Oh! ¡Espaniola! ¡Me flipan las bambinas espaniolas!\n¿Y te gusta Roma entonces?"
    ma normal "Buah, sí, pero ya nos quedan solo dos días. Lo hemos visto todo.\nMe aburro."
    pa expectante "Pues de eso nada. No puedo consentir que una bambina tan guapa se aburra."
    pa sonriente "¿Qué te parecería quedar cuando anochezca? Tú y yo solos.\nTe enseñaría los rincones más bonitos de Roma..."
    menu:
        "Vale. ¡Estupendo!":
            jump _20
        "No sé yo...":
            jump _21
label _20:
    show maru colorado
    pa sonriente "¡Cuánto me alegro! No te arrepentirás.\nRoma tiene muchas cosas por descubrir y... amar."
    jump _22
label _21:
    pa sonrojado "A ver, bambina. No tienes nada que temer.\nConmigo estarás a salvo y en buena compañía."
    ma normal "¿Pues sabes qué te digo?"
label _22:
    show heartbeat at atllove(0.5, 0.5) with dissolve
    ma alegre "Sí, quedo contigo esta noche. Pareces un buen chaval\nEso y que estoy súper aburrida, ja, ja, ja."
    pa sonriente "Ja, ja, ja. Lo vamos a pasar genial. Ya verás."
    ma alegre "Ja, ja, ja."
    hide heartbeat 
    pa sonriente "Toma... Un regalo.\nUna rosa para otra rosa."    
    show screen comment("Cógela", 1.0)
    call screen show_item("img/item/rose.png")
    play sound effect.realizacion
    $change_cursor("hand32")
    show heartbeat at atllove(0.5, 0.5) with dissolve
    ma sonriente "¡¡¡Oooh!!! ¡¡¡Me encanta!!!\n¡Muchas gracias!"
    #<--End of game
label end:
    return

label LoadGUI:
    show screen inventory_button #Show the button of the inventory
    show screen back_button #Show the button to rollback 
label UpdateToday:
    show screen today
    