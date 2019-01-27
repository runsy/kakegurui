#Game script
#----------------

label start:        
    scene black
    stop music
    play sound effect.typing_PC
    centered "{color=#fff}{cps=20}Isla de Gran Canaria{/cps}{/color}"
    play sound effect.typing_PC
    centered "{color=#fff}{cps=20}15 de septiembre{/cps}{/color}"
    stop sound
label presentacion:
    play music music.farty_mcsty fadein 2 fadeout 2
    python:
        characts= {} #Dictionary of characters. They are accessed by: c.nameofthecharacter, ie.: c.violeta
        CreateCharacts() #create all the characters
        InitMe() #Init the Me character
        now_datetime= NowClass(2015, 9, 15, 7, 20) #Set the current datetime
    call LoadGUI
    show screen current_datetime
    #jump test
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

label primer_acto:
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
            vi triste "¿Eso es lo único que me tienes que decir?"
            vi chulesco "Ya veo lo que me has echado de menos..."
        "Pues muy bien. Me alegro de verte":
            pass
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
            vi neutral "Ya ves. Quiero mucho a Nacho —solo como amigo."
        "Oye, tía, te estás pasando tres pueblos.":
            play sound effect.golpe_dramatico
            $c.violeta.change_affinity(False,0)
            show screen comment("Violeta se indigna un poco")
            vi chulesco "A ver, tía, que Nacho es mi amigo...\n¿Acaso no puedo darle un beso después de no verlo en dos meses?"
        "¡Eres una zorrona!":
            vi sonriente "Por lo menos yo sí pillo cacho, jajaja."
    show nac neutral
    vi neutral "Y cambiando de tema. Nacho, ¿qué nos cuentas? ¿Qué hiciste en verano?"
    na "Pues nada, mucha playa, en el yate de mi padre, de fiesta. Nada del otro mundo."
    menu:
        "¿Y de tú novia qué de qué? ¿No nos hablas? Jejeje.":
            $cho_status= True
            play sound effect.golpe_dramatico
            $c.nacho.change_affinity(False,0)
            show screen comment("Nacho piensa que eres muy cotilla")
            na enfadado "¡¿Qué?! ¿Quién te ha contado eso?"
            na colorado "Ejem... prefiero no hablar. Lo siento."             
        "{=green_text}\[Ser discreta\]{/green_text} Ah, qué interesante.":
            $cho_status= False
    $c.me.choices[0]= Choice(cho_status, "Le preguntasté a nacho acerca de su nueva relación.")
    na neutral "Bueno, voy entrando. A ver si veo a más colegas. Ciao"
    hide nac with dissolve
    show vio neutral at center with move
    vi expectante "Oye, tía, ¿echamos unas cartas?\nHe practicado mucho este verano."
    $youwin= game_start(c.violeta, "Eres muy buena jugando a las cartas.", "Deberías practicar más, ja, ja, ja.")
    if youwin== True:
        show vio triste
        ma picaro "Si quieres, te doy clases para que mejores más.\nLo necesitas, ja, ja, ja."
    else:
        vi chulesco "Estás en baja forma, amiga, ja, ja, ja."
    vi expectante "Bueno, y tú, tía, ¿qué hiciste este verano?"
    show vio sonriente
    ma neutral "Nada, me pasó un poco como a ti, tuve que ir de vacaciones con mis padres y... hermanita.\nDe vacaciones a Roma."
    vi expectante "¡¿Eh?! ¿Me vas a comparar Roma con el chalet de mis padres?\nCuenta, cuenta..."
    ma picaro "¿Tengo otra opción...?\nVaaale, te cuento..."
    hide screen inventory_button
    hide screen current_datetime
    scene bg ruinas_romanas_sepia at atldissolve
    ma sonriente "Roma es una ciudad super chula. Aunque está muy sucia y hay piedras tiradas por todas partes, jeje."
    ma "Como te dije fui con mi madre y hermana, lo que era un tostón extra. Y hacía un calor que te cagas."
    scene bg ruinas_romanas with irisin
    show maru jeans preocupado at center:
       xzoom -1.0
    show mama feliz at right with dissolve
    pause
    ma preocupado "Uf, qué calor. Y qué cansada estoy. Llevamos todo el día de aquí para allá.\nEl Foro, el Colíseo, las Termas..."
    mama irritado "¡Maru! Empápate de la cultura de este país milenario y deja de quejarte, anda."
    show maru sorprendido at center
    ma sorprendido "Jo, mami, es que llevamos seis días aquí, y lo único que hemos hecho es andar y andar sólo para ver museos y cosas viejas y derruidas.\nMe aburro."
    show jes sonriente at left:
        xzoom -1.0
    with moveinleft
    play sound effect.pasar_zumbando
    je "Hey, ¡¿cómo estáis?!"
    mama irritado "¡Jesica! ¿Dónde te habías metido?\nA ver si te van a raptar..."    
    je neutral "¡Por ahí! A ver si encontraba un tesoro, jajaja."
    menu:
        "Tú eres tonta.":
            play sound effect.shock2  
            show maru alegre jeans
            je enfadado "¡¡¡LA TONTA ERES TÚ!!!" with Shake()
        "Cariño, haz caso a mamá...":
            show maru enfadado
            je neutral "Sí, el mismo caso que le haces tú... ¡Juas!"
    play sound effect.shock2 
    mama irritado "A ver niñas ¡¡¡Portaos bien!!!" with Shake()
    je alegre "He visto un carrito de los helados.\nMami, ¿me compras uno? Porfa..."
    mama "Bueno, pero espero que te portes bien..."
    hide mama with dissolve
    play sound effect.pedo
    je sonriente "Ja, ja, ja. Ya ves, siempre consigo lo que quiero."
    hide jes with dissolve
    ma enfadado " Si no tuviera tan solo cinco años, se iba a enterar de lo que vale un peine.\n¿Y ahora que hago yo? Ya he visto todo..."
    play sound effect.flash
    scene bg ruinas_romanas with flash     
    show maru sorprendido at left_to_right
    ma sorprendido "¡Hey! ¿Qué ha sido eso?"
    $c.me.AddFriend(c.paolo, True, True)
    show pao sonriente at right with moveinright
    pa "Ciao, bambina."
    menu:
        "¿Quién eres?":
            pass
        "¿Me has sacado una foto?":
            pa sorprendido "Si te dijera que sí, ¿te importaría?"
            menu:
                "...No":
                    pass                            
                "¡Pues claro que me importa, no te conozco!":
                    $c.paolo.change_love(True, 0)
                    show screen comment("Paolo piensa que eres guay.")    
                    pa sonriente "Me encantan las chicas con carácter, ja, ja, ja"  
        "¿Te quieres casar conmigo?":
            show pao sonrojado
            $c.paolo.change_love(True, 0)
            show screen comment("Paolo se siente halagado.")
            play sound effect.shock2 
            show heartbeat at atllove(0.85, 0.4) with dissolve
            pause
            hide heartbeat
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
            pass
        "¡Anda ya! ¡Si no me conoces de nada!":
            show pao sorprendido
            $c.paolo.change_love(False, 0)
            show heartbeat at atlbrokenheart(0.85, 0.4)
            play sound effect.romper
            $renpy.pause(2.0, hard=True)
            show screen comment("Lo has herido un poco en sus sentimientos.")
            pause
            hide heartbeat
    pa neutral "Bueno, y qué te cuentas bambina.\n¿Qué se te ha perdido por Roma?"
    ma alegre "Estoy de viaje con mi madre y hermana. Pasando unas vacaciones.\nSoy española."
    pa sonriente "¡Oh! ¡Espaniola! ¡Me flipan las bambinas espaniolas!\n¿Y te gusta Roma entonces?"
    ma normal "Buah, sí, pero ya nos quedan solo dos días. Lo hemos visto todo.\nMe aburro."
    pa expectante "Pues de eso nada. No puedo consentir que una bambina tan guapa se aburra."
    pa sonriente "¿Qué te parecería quedar cuando anochezca? Tú y yo solos.\nTe enseñaría los rincones más bonitos de Roma..."
    menu:
        "Vale. ¡Estupendo!":
            show maru colorado
            pa sonriente "¡Cuánto me alegro! No te arrepentirás.\nRoma tiene muchas cosas por descubrir y... amar."            
        "No sé yo...":
            pa sonrojado "A ver, bambina. No tienes nada que temer.\nConmigo estarás a salvo y en buena compañía."
            ma normal "¿Pues sabes qué te digo?"
    show heartbeat at atllove(0.5, 0.5) with dissolve
    ma alegre "Sí, quedo contigo esta noche. Pareces un buen chaval\nEso y que estoy súper aburrida, ja, ja, ja."
    pa sonriente "Ja, ja, ja. Lo vamos a pasar genial. Ya verás."
    ma alegre "Ja, ja, ja."
    hide heartbeat 
    pa sonriente "Toma... Un regalo.\nUna rosa para otra rosa."    
    show screen comment("Cógela", 1.0)
    call screen show_item("img/item/rose.png")
    #play sound effect.realizacion
    $change_cursor("hand32")
    show heartbeat at atllove(0.5, 0.5) with dissolve
    ma sonriente "¡¡¡Oooh!!! ¡¡¡Me encanta!!!\n¡Muchas gracias!"
    pa sonrojado "Ahora me tienes que regalar tú algo."
    hide heartbeat
    ma sorprendido "¡¿Yo?!\nPues... ejem... no tengo nada para darte."
    pa expectante "Regálame tu nombre.\nTodavía no sé cómo te llamas..."
    menu:
        "Me llamo Maru.":                        
            $cho_status= False
            $temp= "Maru"
        "{=red_text}\[Mentir\]{/red_text} Ein... Ups... Me llamo M-M-María...":            
            $cho_status= True
            $temp= "María"
    $c.me.choices[1]= Choice(cho_status, "Mentiste a Paolo sobre tu verdadero nombre.")
    pa sonriente "Oh, [temp]... ¡Qué bonito nombre!"
    pa sonriente "Pues entonces, quedamos a las nueve aquí mismo.\nEstaré ansioso hasta que sea la hora."
    ma preocupado "¡¿Aquí?!\n¿No estará esto muy solitario y oscuro a esas horas?"
    pa expectante "¡Qué va!\nAdemás llegaré yo un poco antes si así estás más tranquila.\n¿Vale?"
    ma picaro "OK, ji, ji, ji."
    pa sonrojado "Nos vemos entonces a esa hora, [temp].\nCiao."
    ma colorado "Ciao."
    hide pao with moveoutright
    pause
    ma sonriente "Oh, creo que..."
    ma colorado "¡Me he enamorado!"
    play sound effect.pasar_zumbando
    show jes alegre at right with moveinright
    show icecream:
        pos (800, 568)
    show maru enfadado
    show jes sonriente
    je "¡Hey, ¿con quién estabas hablando?\n¿Y por qué tienes esa cara de boba?"
    ma "No es asunto tuyo, niñata."
    je "Pues como no me lo digas, me chivo a mamá."
    menu:
        "Anda, no seas mala.":
            $cho_status= False
            je picaro "Te conozco, hermanita, algo estás tramando.\nY lo descubriré."
            je sonriente "Y cuando lo descubra, te haré chantaje.\nMe tendrás que comprar todas las gososinas del mundo, ji, ji, ji."
        "{=red_text}\[Ponerle el helado como sombrero\]{/red_text} ¡TE VAS A ENTERAR!":
            $cho_status= True
            show icecream:
                linear 0.8 pos (800,120)
                linear 0.8 pos (1000,120)
                yzoom -1
                pause 0.5
                linear 0.5 pos (1000,210)    
            $renpy.pause(2.6, hard=True)
            play sound effect.golpe_seco_2
            je lloroso "¡¡¡MAMÁ!!! ¡¡¡MAMÁ!!! ¡¡¡BUAHHH!!!"
            ma picaro "Ja, ja, ja.\nJÓ-DE-TE."
    $c.me.choices[2]= Choice(cho_status, "Le pusiste un helado a tu hermana Jesica en la cabeza.")   
    play sound effect.hacer_scroll    
    scene bg insti_puerta
    show screen inventory_button
    $now_datetime.UpdateDatetime(2015, 9, 15, 7, 29)
    show screen current_datetime
    show vio expectante at center
    with slideleft
    play music music.farty_mcsty fadein 2 fadeout 2
    vi "Oh, qué emocionante historia. Por favor, sigue."
    vi "Jo, ¿por qué a mí no me pasan esas cosas?\nMe parece súper injusto, ea."
    menu:
        "Quizá porque eres... ¿fea?":
            play sound effect.ups
            $c.violeta.change_affinity(False,0)
            show screen comment("Violeta piensa que eres demasiado cruel.")
            vi enfadado "Ah, la princesita piensa que las demás no podemos ligarnos a un tío buenorro, ¡juas!"    
        "{=green_text}\[Te muerdes la lengua\]{/green_text}":
            pass  
    show vio neutral
    vi expectante "A ver, ¿cómo acabó la historia con el italiano?\nMe muerdo las uñas para saber el final."
    play sound effect.alarma
    $renpy.pause(1.0, hard=True)
    ma neutral "Más tarde. Ha sonado la campana.\nVámonos para clase."
    vi chulesco "OK, pero en el recreo me vas a contar hasta el último detalle..."
    scene bg insti_edificio_manana
    $now_datetime.UpdateDatetime(2015, 9, 15, 7, 31)
    show screen current_datetime
    show nac sorprendido at center
    show ant sorprendido at right
    with dissolve
    play music music.burglars fadein 2 fadeout 2
    na " ..."
    an "..."
    $c.me.AddFriend(c.antia, True, True)
    ma alegre "Hey. ¡Hola, Antía! Nacho...\n¿De qué estabais hablando?"
    na asustado "Eh... No... Nada..."
    an timido "... ... ... Hola... Maru"    
    ma suspicaz "Mmm... No sé yo, estáis muy raros.\nY esas caras..."
    menu:
        "¿Os pasa algo?":
            na sorprendido "¿A nosotros? Nada.\nJa, qué cosas tienes..."
            an sorprendido "Maru, sólo charlabamos de lo que hicimos este verano."
        "¡¿Qué cojones estáis tramando?!":
            if c.me.choices[0].status== True:
                show screen comment("Nacho está harto de tus intromisiones.")
                na enfadado "Maru, no sé que mosca te ha picado este verano. Pero estás realmente INSOPORTABLE."
                $c.nacho.change_affinity(False, 0)        
                an engreido "Sí, la verdad, Maru, ¡sólo estabamos charlando amigablemente!\nLo que hay que escuchar a veces...\nEjem..." 
            else:
                na sorprendido "¿Eh? Nada. No sé porque te rayas."
                an enfadado "Maru, cariño, relajate. Solo le estaba contando lo bien que me lo pasé este verano."
    show nac neutral
    show ant neutral
    ma suspicaz "Y yo me lo tendré que creer, ¿no?"
    ma tierno "Bueno. Entonces Antía, ¿cómo te fue a ti?\nQue Nacho ya me contó de lo suyo."
    an sonriente "Oh. Fui un campamento de verano. En Estepona. Fue súper divertido.\nMe lo pasé bomba."
    na chulo "Ja, ja, ja, Antía. Los campamentos son para los niños pequeños."    
    play sound effect.shock2
    an cabreado "Agh, Nacho, cállate. Me lo va a decir alguien que todavía duerme con su oso de peluche de la infancia..." with Shake()
    na colorado "Jo, {i}Fofó{/i} no es un oso cualquiera.\nEs mi mejor amigo y me cuida por las noches para que duerma."
    an alegre "¡Ja, ja, ja!"
    ma sonriente "¡Ja, ja, ja!"
    show nac sonriente
    an sonriente "No era un campamento normal. Fue un campamento para jovenes artistas.\nAllí hicimos talleres de pintura, escritura... y compartimos experiencias."
    ma tierno "Qué guay. Se nota que eres la cerebrito del grupo. Aprovechaste el verano para formarte.\nNo como el resto, que estuvimos de jarana y fiesta."
    an colorado "Bueno... ejem.. tambien hubo tiempo para la diversión."
    na engreido "Bueno, chicas, vamos para clase. Que ya sonó el timbre hace un rato.\nNo podemos llegar tarde ya el primer día."
    hide nac with moveoutleft
    show ant at center with moveoutleft
    an engreido "Espera un momento, Maru. En el campamento nos pasabamos las noches jugando a los {i}8 Locos{/i} alrededor de la fogata.\nÉchemos una partida rápida. Ya verás lo que he mejorado."
    $youwin= game_start(c.antia, "Jo, al final, no soy tan buena como yo creía.", "Ya ves, he vuelto siendo toda una profesional.")
    if youwin== True:
        show ant triste
        ma picaro "Si quieres, te doy clases para que mejores más.\nLo necesitas, ja, ja, ja."
    else:
        an alegre "Estás en baja forma, amiga, ja, ja, ja."
    hide ant with moveoutleft
    show car at center with moveinright
    ca normal "Hola. ¿Me puedes ayudar?"
    ca alegre "Perdón, me presento. Me llamo Carmen. Y soy nueva en este instituto.\nEstoy buscando la clase de 3º B..."
    ca normal "Y me dije a mi misma: A ver, si esa simpática niña me puede ayudar, je, je."
    ma suspicaz "..."
    $c.me.AddFriend(c.carmen, True, True)
    menu:
        "Qué casualidad. Vamos a la misma clase.\nSi quieres, acompáñame.":
            $cho_status= True            
            show screen comment("Carmen cree que eres educada.")
            $c.carmen.change_affinity(True, 0)                        
            ca alegre "¡¿Oh, sí?! ¡Qué ilusión, podemos ser amigas, ¿verdad?"
            menu: 
                "Con el tiempo a lo mejor sí":
                    show screen comment("A Carmen le caes genial.")                    
                    $c.carmen.change_affinity(True, 1)
                    ca alegre "Claro. A mí me encantaría."
                "Bueno, tampoco te pases, eh.":
                    ca engreido "Claro, claro. Es que mis papis me dijeron que el primer día de clase había que hacer amigos.\nY me he embalado, ji, ji."
        "No me incordies y espabila, monina.":
            $cho_status= False
            play sound effect.golpe_dramatico
            show screen comment("Carmen opina que eres muy maleducada.")
            $c.carmen.change_affinity(False, 1)
            ca lloroso "..."
    $c.me.choices[3]= Choice(cho_status, "Te ofreciste a acompañar a Carmen a su/vuestra clase.") 
    scene bg insti_entrada_principal_manana
    show vio neutral at center
    show nac neutral at right
    with dissolve    
    pause
    play sound effect.golpe_dramatico
    vi enfadado "¡Maru! ¿Dónde te metiste?\n¡Qué vamos a llegar tarde el primer día de clase!" with Shake()
    na enfadado "Violeta, veo que tu caracter se agria más y más por momentos..."
    vi chulesco "¡Qué te den!\nTú como vives a todo trapo gracias a tus papis que te dan todo hecho..."
    play sound effect.ups
    show vio rabioso
    na enfadado "Serás puta..."
    ma emocionado "¡¡¡EH!!! ¡Tranquilos! Nada más empezar el curso no nos podemos pelear."
    ma emocionado "Recordad que somos amigos. Los cuatro mosqueteros: Violeta, Nacho, Antía y yo."
    show vio triste
    na sorprendido "Los mosqueteros eran tres, no cuatro."
    ma tierno "Que más da el número. Todos para uno y uno para todos.\n¿O ya no os acordáis?"    
    show nac neutral
    vi neutral "Tienes razón en la de líos que nos hemos metido desde que nos conocemos en preescolar. Y de juergas también."
    show vio sonriente
    na sonriente "Y las que nos quedan... ja, ja, ja."
    play sound effect.pasar_zumbando
    show car  alegre at left with moveinleft
    ca alegre "¡Hola, holita, chavalada! Ji, ji, ji."
    if c.me.choices[3].status== True:
        ca engreido "Eh, tía rubia, ¿me presentas a tus amigos?\nMe gustaría formar parte de vuestra cuchipandi."
        ma sorpendido "Ups, qué despiste el mío, no me había presentado. Yo, me llamo Maru, y estos son mis amigos."
        show car alegre
        show vio neutral
        ma normal "La del pelo rosa es Violeta. Es la cabeza loca del grupo. Pero tiene un fondo súper tierno."
        show nac chulo
        ma "El otro es Nacho. Que no te confundan las apariencias, tiene pinta de pijo, pero cuando le conoces es un cañero y un tío legal."
        ma "Y ella es Carmen, va a ir con nosotros en 3º B. Me ofrecí a guiarla por el instituto el primer día."      
    else:
        ca colorado "A ver si me podéis ayudar vosotros. Estoy buscando la clase de 3º B."
        ma encendido "Ya te he dicho que te des el piro, vampiro. Mira que eres pesadita."
        ca enfadado "Pero ellos tendrán algo que decir, digo yo. O hablas tú por ellos todo..."
        vi sonriente "Oh, qué mal rollo. Hola, yo me llamo Violeta. Si preguntas por mi en el insti, te dirán que soy un poco rarita.\nNo les hagas caso, son todos unos gilipollas."
        na chulo "Yo soy Nacho. El terror de las nenas. Si preguntas por mí en el insti, las niñas te dirán que soy irresistible y los tíos un tío guay."
        vi creido "Menos lobos, chavalote, juas."
        ca colorado "Encantada. Yo me llamo Carmen. Soy nueva."
        vi expectante "Maru, ¿y a ti qué puñetas te pasa con esta niña?\nParece que no te cae bien."
        menu:
            "Me cae como el culo, la verdad.":
                ca engreido "Pues qué pena, pero tú te lo pierdes..."
                ma encendido "Grrr..."
            "No sé, me da mala espina.":
                ca engreido "No tengo nada que esconder, soy limpia y transparente como el agua, ji, ji, ji."
                ma encendido "{i}{color=#b0b0b0}\[Hablas por lo bajini\]{/color}{/i} No te lo crees ni tú."
            "{=gray_text}\[Callarse\]{/gray_text} ...":
                pass
    show nac neutral
    show vio neutral
    ca normal "Mi papá es militar y lo destinaron a esta isla.\n¡Me encanta que aquí haga buen tiempo todo el año!"
    ca alegre "Me gusta ver pelis y hacer senderismo entre otras cosas. Me gustaría hacer nuevos amigos, ji, ji. ji."
    if c.me.choices[3].status== True:
        $cho_status= None
        ma sonriente "Qué guay. Podemos hacer muchas cosas juntos; quiero decir, todos juntos. ¿Verdad, chicos?"
        vi expectante "Pues claro, este año lo vamos a arrasar en el instituto."
        na asustado "¡Uf, qué peligro! Erais pocas las chicas y parió la abuela..."
        vi sonriente "¡Las mujeres al poder! Ja, ja, ja."
    else:
        menu:
            "Bueno, a lo mejor te doy una oportunidad...":
                $cho_status= True
                $c.carmen.change_affinity(True, 1)                
                ca alegre "¡Oh!, ¿en serio? Por mí estupendo.\nYa verás como tú y yo congeniamos a las mil maravillas."
                show screen comment("A Carmen le mola tu actitud positiva")
                vi sonriente "Carmen, ya verás como Maru es una buena tipa. Un poco tontaina a veces, pero de buen corazón." 
            "Ni de puta coña seré tu amiga nunca":
                $cho_status= False
                show car cabreado
                play sound effect.shock2
                vi rabioso "¡Maru! No sé porque eres tan mala con esta chica..." with Shake()
                ma encendido "No me parece trigo limpio. Seguro que es una mosquita muerta.\nA mí no me engaña."
                ca enfadado ".... ...."
                $c.carmen.change_affinity(False, 1)   
                show screen comment("Carmen te odia")
                ca normal "Bueno, allá tú... ji, ji, ji."
    $c.me.choices[4]= Choice(cho_status, "Le das a Carmen una nueva oportunidad.")
    show vio neutral
    show nac neutral
    show car engreido
    ma picaro "Hala, chicos, a clase."
    if (c.me.choices[3].status== False) and (c.me.choices[4].status== False):
        hide nac
        hide vio
        with moveoutright
        show car cabreado at center
        with moveinright
        play sound effect.shock2
        ca cabreado "A ver, Maru, cariño. Si me tocas los cojones, yo te los tocaré a ti." with Shake()
        ma enfadado "¡¿Me estás amenazando?! ¡¿A mí?!"
        ca enfadado "Tómalo como una advertencia, por el momento..."
        hide car with moveoutleft
        ma preocupado "¡Lo sabía! Voy a tener que tener mucho cuidado con esta lagarta."
        $cho_status= True
    else:
        $cho_status= False
    $c.me.choices[5]= Choice(cho_status, "Has descubierto que Carmen no es trigo limpio.") 
    pause
    #<--End of game
label end:
    return

label LoadGUI:
    show screen inventory_button #Show the button of the inventory
    show screen back_button #Show the button to rollback 
    return
    