# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image vid = Movie(play="audio/5-6.webm", size=(1920,1080),loop=False, xalign=0.10, yalign=0.10)

init -2:
    # ---------- blinking arrow -------------------
    image ctc_blink:

        alpha 1.0
        "images/star1.png"
        zoom 0.28
        ypos 8
        xpos 4
        0.5
        "images/star2.png"
        zoom 0.28
        ypos 8
        xpos 4
        0.5
        repeat

    transform e:
        ycenter 1000
        xcenter 960
        alpha 0.0
        #ease .06 alpha 0.2
        ease .06 ycenter 900 alpha 0.2
        #ease .05 alpha 0.4
        ease .05 ycenter 800 alpha 0.4
        #ease .04 alpha 0.6
        ease .04 ycenter 700 alpha 0.6
        #ease .04 alpha 0.8
        ease .04 ycenter 600 alpha 0.8
        #ease .04 alpha 1.0
        ease .04 ycenter 500 alpha 1.0
        alpha 1.0
        ycenter 500
    
    define ex = Dissolve(0.1)

# transform jumper:
#     ease .04 yoffset 20
#     ease .03 yoffset 16
#     ease .02 yoffset 12
#     ease .01 yoffset 8
#     ease .01 yoffset 4
#     ease .01 yoffset 0

init python:

    numscenes = 101

    def slow_punctuation(str_to_test):
        return (str_to_test
            .replace(", ", ",{cps=5.0} {/cps}")
            .replace(". ", ".{cps=3.0} {/cps}")
            .replace("| ", "\n")
            .replace("! ", "!{cps=3.0} {/cps}")
            .replace("? ", "?{cps=3.0} {/cps}")
            .replace(": ", ":{cps=3.0} {/cps}")
            .replace("— ", "—{cps=3.0} {/cps}")
            .replace(" —", " —{cps=3.0} {/cps}")
            .replace("... ", "... {cps=3.0} {/cps}"))
    config.say_menu_text_filter = slow_punctuation
    gui.name = slow_punctuation
            


    #def display_character_names(english_name, japanese_name, x, y):
        #renpy.show(renpy.text(english_name, size=40, color="#ffffff"), x=x, y=y)
        #renpy.show(renpy.text(japanese_name, size=20, color="#ffffff"), x=x, y=y + 50)

    riris = []
    for i in range(numscenes):
        riris.append(False)

    char_left = Position(xpos=0.18, ypos=0.75)
    basketballSong = "bgm_basketball.mp3"
    sfxBell = "sfx_bell.mp3"
    bgSong = "bgm_skipABeat.mp3"
    config.auto_voice = "voice/{id}.mp3"

    quizWords = ["Hi", "Hello", "Hey"]
    quizAnswers = ["Hi2", "Hello2", "Hey2"]
    quizWord = quizWords[renpy.random.randint(0,len(quizWords) - 1)]
    quizCorrect = quizAnswers[quizWords.index(quizWord)]
    quizGuess1 = quizAnswers[renpy.random.randint(0,len(quizAnswers) - 1)]
    quizAnswers.remove(quizGuess1)
    quizGuess2 = quizAnswers[renpy.random.randint(0,len(quizAnswers) - 1)]
    quizAnswers.remove(quizGuess2)
    quizGuess3 = quizAnswers[renpy.random.randint(0,len(quizAnswers) - 1)]

    ririname = "..."
    mcname = "..."
    joename = "..."
    jtname = "..."
    sophianame = "..."
    maryamname = "..."

    ririname_kanji = ""
    mcname_kanji = ""
    joename_kanji = ""
    jtname_kanji = ""
    sophianame_kanji = ""
    maryamname_kanji = ""

    metRiri = False
    metJoe = False
    metJT = False
    metSophia = False
    metMaryam = False

    from game.images.Gwyn import *
    from game.images.NPCs import *
    from game.images.Riri import *
    from game.images.Beckham import *
    from game.images.Joe import *
    from game.images.Jt import *
    from game.images.Kyle import *
    from game.images.Maryam import *
    from game.images.Sophia import *
    from game.images.Backgrounds import *
    from game import *


# ----------------------------------------------------------------------------------------------------------
init:
    
    $ dialogue_outlines = ((0, "#6529231e", -1, 1), (0, "#65292317", -1, 2), (0, "#65292311", -1, 3), (0, "#6529230c", -1, 4), (0, "#65292307", -1, 5), (0, "#65292303", -1, 6), 
    (0, "#6529231e", 1, 1), (0, "#65292317", 1, 2), (0, "#65292311", 1, 3), (0, "#6529230c", 1, 4), (0, "#65292307", 1, 5), (0, "#65292303", 1, 6), 
    (0, "#6529231e", 0, 1), (0, "#65292317", 0, 2), (0, "#65292311", 0, 3), (0, "#6529230c", 0, 4), (0, "#65292307", 0, 5), (0, "#65292303", 0, 6))

    define pjmc = Character("[mcname]", show_name = "You", ctc="ctc_blink", image="gwyn_pajamas", window_background="gui/textbox2.png", what_outlines = dialogue_outlines, what_style = "say_dialogue_mc")
    define pmc = Character("[mcname]", show_name = "You", ctc="ctc_blink", image="gwyn_party", window_background="gui/textbox2.png", what_outlines = dialogue_outlines, what_style = "say_dialogue_mc")
    define smc = Character("[mcname]", show_name = "You", ctc="ctc_blink", image="gwyn_suit", window_background="gui/textbox2.png", what_outlines = dialogue_outlines, what_style = "say_dialogue_mc")
    define mc = Character("[mcname]", show_name = "You", ctc="ctc_blink", image="gwyn", window_background="gui/textbox2.png", what_outlines = dialogue_outlines, what_style = "say_dialogue_mc")

    #define daniel = Character("ダニエル", show_name = "beast of osaka", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define na = Character(name=None, ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define mom = Character("Mom", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define teacher_e = Character("Sensei", show_name = "先生", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define mio = Character("Mio", show_name = "みお", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)

    define beckham = Character("Mario", show_name = "マリオ", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define joe = Character("[joename]", show_name = "[joename_kanji]", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True) # Joe
    define kyle = Character("Akimitsu Chiba", show_name = "千葉・昭光", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True) # Akimitsu Chiba
    define jt = Character("[jtname]", show_name = "[jtname_kanji]", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True) # Yutaka Yanai
    define sophia = Character("[sophianame]", show_name = "[sophianame_kanji]", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True) # Isamu Takao
    define maryam = Character("[maryamname]", show_name = "[maryamname_kanji]", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True) # Haruka Kiyama

    define mi1 = Character("Magical Ikemen 1", show_name = "魔法イケメン１", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define mi2 = Character("Meowgical Ikemen 2", show_name = "魔法イケミェン２",ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define pp = Character("PyunPyun", show_name = "ピュンピュン", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define takeshi = Character("Takeshi", show_name = "たけし", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define dr = Character("Dr.", show_name = "ダクター", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)

    define riri = Character("[ririname]", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True) # define riri = Character("リリ")
    define mv = Character("Mysterious Voice", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define mi = Character("Mysterious ikemens", show_name = "イケメンたち", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)

    define d1 = Character("Deliquent 1", ctc="ctc_blink", what_outlines = dialogue_outlines)
    define d2 = Character("Deliquent 2", ctc="ctc_blink", what_outlines = dialogue_outlines)
    define d3 = Character("Deliquent 3", ctc="ctc_blink", what_outlines = dialogue_outlines)
    define sg = Character("Sullen Girl", ctc="ctc_blink", what_outlines = dialogue_outlines)
    
    style character_text:
        outlines [
        (0, "#6529233d", 2, 2),
        (2, "#65292318", 3, 3),
        (1, "#6529230e", 4, 4)
    ]
        
    #default say = character_text

    # image beckham agent normal = "/images/Zeil/ph.png"
    # image beckham agent ecstatic = "/images/Zeil/ph.png"
    # image beckham bartender normal = "/images/Zeil/ph.png"
    # image beckham bartender angry = "/images/Zeil/ph.png"
    # image beckham bartender sad = "/images/Zeil/ph.png"
    # image beckham fan normal = "/images/Zeil/ph.png"
    # image beckham fan ecstatic = "/images/Zeil/ph.png"

# --------------------------------------------------------
label pro:
    pause 0.2
    stop music
    show vid
    pause 2
    #play music bgSong
    pause 0.2
    scene gym with Pixellate(0.5,3)

    queue music basketballSong
    "During gym..."
    show zeil normal at char_left with vpunch
    mc normal "{b}Hi!{/b} I'm {u}mc!{/u} {size=+10}This{/size} is my \"Project\"!"
    mc normal "Man, is it just me, or am I... {color=#b0b0b0}getting... {size=-6}a {nw}"
    mc normal "little sleepy...{/size}{/color}"
    return

label DefaultQuestion:
    mc normal "What?!"
    menu:
        "Nothing!":
            jump Questions_mc.Answer_Nothing
        "Hi.":
            jump Questions_mc.Answer_Hi
        "Play a game with me!":
            $ renpy.dynamic("randumNum","answer") #To make variables local
            $ randomNum = renpy.random.randint(1,4)
            mc normal "Anyways... OMG! It's a [randomNum]!"
            if randomNum >= 1 or randomNum <= 2:
                $ answer = "What?"
            elif randomNum == 3:
                $ answer = "Say that again?"
            else:
                $ answer = "Huh?"
            mc normal "[answer]"
            # $ repeatQuestion = renpy.random.choice(["What?", "Say that again?", "Huh?"])
            return
    
label Questions_mc:
    label .Question_What:
        label .Answer_Nothing:
            mc normal "Oh."
            return
        label .Answer_Hi:
            mc normal "Hi!"
            return


# --------------------------------------------------------
# p = placeholder label
# s = scene
label p:
    mom "PLACEHOLDER"
    return

label riri:
    if riris[10]:

        riri "Yay! You did it! I'm so proud of you Naninani. Okay... let's see your options..."

        riri "Your teacher is really mad right now. If you went to class you'd definitely receive that anger."

        riri "But... if you skip class you could find yourself in a battle for your very fate."

        riri "Ooooh spicy. You know which one I would choose. {i}Wink. Wink.{/i}"

        $ riris[10] = False
    if riris[11]:

        riri "Hehehehe..."

        $ riris[11] = False
    if riris[14]:

        riri "Follow your gut, Naninani!"

        $ riris[14] = False
    if riris[15]:

        riri "You {i}have{/i} to go to that party Naninani! 'Kay?"

        $ riris[15] = False
    if riris[26]:

        riri "Look at this cutie-patootie! Maybe you don't have to go to that party Naninani."

        riri "The choice is yours... though I am a fan of Chiba-kun myself... hehehehehe..."

        $ riris[26] = False
    if riris[27]:

        na "{i}[[Riri shakes her head. It looks like she doesn't want to talk to you right now.]{/i}"

        $ riris[27] = False
    if riris[28]:

        riri "The drama! As the main character, you {i}must{/i} pick at least one of them!"

        riri "Don't let the temptation of the forbidden fruit fool you!"

        $ riris[28] = False
    if riris[24]:

        riri "Hey, Naninani, he's really asking you on a date!"

        riri "I never thought you'd make it this far... It truly brings tears to my eyes!"
        
        riri "Anyways, you HAVE to go with him! For me <3"

        $ riris[24] = False
    if riris[44]:

        riri "Wow, did you really just ask him on a date?!?! All by yourself??"

        riri "I knew you could do it! They grow up so fast..."

        $ riris[44] = False
    if riris[46]:

        riri "That's a tough one..."

        riri "Either way will bring you two closer, right? So, I'll let you decide this time..."

        $ riris[46] = False
    if riris[29]:

        riri "If you go to the basketball game, Chiba-kun is totes falling for you!"

        riri "Partying is fine too though I guess..."

        $ riris[29] = False
    if riris[33]:

        riri "Poor Chiba... Oh well, this means even more love routes!"

        $ riris[33] = False
    if riris[35]:

        riri "Oooh, you like the bad ones, huh?"

        $ riris[35] = False
    if riris[37]:
        
        riri "If you go get drinks with Isamu, you'll find yourself in a world of broken doors, crime, and... {i}cats?{/i}"

        riri "I mean, that's basically your only option... right? Right?"

        $ riris[37] = False
    if riris[47]:

        riri "What an unexpected twist!"

        riri "Come on, Naninani! He's the love of your life, your soulmate! You must save him!"

        $ riris[47] = False
    if riris[53]:

        riri "You need to be more explorative! Maybe this girl on the poster is actually your soulmate!"

        $ riris[53] = False
    if riris[57]:

        riri "Maybe we should just give the, the benefit of the doubt? But why would they have your ring and not give it back? Hmmm..."

        $ riris[57] = False
    if riris[60]:

        riri "How strange... let's test them to see if they know the password!"

        $ riris[60] = False
    if riris[63]:

        riri "We can always just do the project another dayyy..."
        
        $ riris[63] = False
    if riris[65]:

        riri "You could call the cops, but the culprit is already long gone..."

        $ riris[65] = False
    if riris[34]:

        riri "CHIBA-KUN WANTS TO GO SOMEWHERE ELSE?!?! JUST THE TWO OF YOU?!?! AAAAAAAAAA GO NANINANI GOOO!"

        $ riris[34] = False
    if riris[36]:

        riri "Look at you go!"

        $ riris[36] = False
    if riris[51]:

        riri "yo test!"

        $ riris[51] = False

    else:
        na "{i}[[It doesn't look like Riri has anything to say right now.]{/i}"

    python:
        for i in range(numscenes):
            del(riris[i])
            riris.insert(i, False)

    return
# -------------------------------------------------------------------------------------------------------------------
# s1 = start
# voice voice.mp3
label start:
    #show beckham agent ecstatic at topright
    #with moveinright
    #show gwyn party normal at topleft
    $ mcname = renpy.input("What is your name?")
    $ mcname = mcname.strip()
    $ mcname = mcname[0:13]
    if mcname == "":
        $ mcname = "Naninani Nantoka"
        #何とか、何々

    stop music

    jump s51

    # show screen character_name("Hana Kobayashi", "小林・花")

    scene bedroom

    #jump s74

    pjmc normal "I'm so tired... I stayed up all night playing otome games."
    
    pjmc ecstatic "It`s hard not to when you`re given so many choices, especially when you can punch the male leads. Hehehe!"

    pjmc scared "Oh wait! I forgot to introduce myself. My name is {u}[mcname]{/u}!"

    pjmc normal "I'm sixteen. Today is my first day of my second year at Gwetome Academy."

    pjmc normal "Ever since my family moved back to Shizuoka, I've been living my high-school life to the fullest."

    pjmc normal "During my time here, I've come to learn that love isn't the only important thing in life. {w=2}{nw}"

    pjmc ecstatic "I'm my own person, with my own goals and dreams, and I'm proud of that. I am independent and strong!"

    pjmc embarrassed "...and I'm late for school."

    menu:
        "{i}Go downstairs and get ready for school":
            jump s2
        "{i}Sleep in just a liiitle longer":
            jump s3

label s2:

    na "You put on your uniform and go downstairs."

    scene kitchen
    show mom normal
    mom "Good morning! I made you breakfast since I knew you'd wake up late."

    mom "Dad's already left to go work on his new Food Network episode and I'm heading out now. Have fun at school! I'm off!"

    hide mom

    #TODO: Door close noise

    mc normal "Thanks, have a good day!"

    na "You happily munch on the breakfast your mother made and pat your belly in satisfaction. 
        Suddenly, the TV turns on, as if it's beckoning you to watch it."

    #TODO: Show TV / Magical Ikemen

    na "Wait! Is that... the new season of Magical Ikemen?!? It's been a whole year since the last episode!"

    na "But... you have school. If you leave now, you still might be able to make it in time."

    menu:
        "{i}Head off to school":
            jump s4
        "{i}Watch Magical Ikemen":
            jump s5

label s3:

    na "You crawl into your covers again and begin to sleep blissfully; everything is cozy, warm, and peaceful. You begin to dream."

    na "It's your first day of school at Gwetome Academy. Everyone is calling you Naninani Nantoka. 
        But why? You've always been [mcname] haven't you? How strange."

    na "Just as you are about to investigate this, you feel a sudden shake."

    mom "Hey!...Hey! Get up! How did I end up with such a lazy child?"

    mom "[mcname], school's already started so you need to hurry! I'm off to work now, so I can't help you. I'm off!"

    menu:
        "{i}Wake up and go go go!":
            jump s6
        "{i}Nahh, I'm sleeping more":
            jump s7

label s4:

    na "Wow, look at you all responsible! You discard the temptation of Magical Ikemen and start your trek to school."

    scene neighborhood
    na "You check your phone and see you have more time than you realized. Maybe you'll just quickly look up the information about 
        Magical Ikemen's new season while you walk... you have the time after all."

    na "Plus, you need to know whether or not Takeshi finally leaves his office job to pursue his dream
        of becoming a full-time magical girl in the Kiss Kiss Love Power Team."

    na "As you scroll through the wonderland that is the Magical Ikemen online forum, you bump into a pole. Ouch." with hpunch

    na "Wow, that's a strangely attractive pole. And it's wearing a... Gwetome Academy uniform!? The pole turns around."

    show joe normal
    joe "Ah sorry, I was walking kind of slow. Are you ok?"

    show joe ecstatic
    joe "A lot of people bump into me so my back muscles have become hard like metal. My doctor said it's because I tend to draw people in... I'm magnetic."

    show joe embarrassed
    joe "Heh. Sorry, I'm rambling. Anyways, I'll just uh... keep walking."

    hide joe
    na "The mysterious ikemen runs his hand through his hair cooly and starts to saunter away."

    na "Your heart is beating fast; you don't know if it's because of his dazzling looks or possible metal poisoning."

    na "Either way, you should probably get to school. The question is: How?"

    menu:
        "{i}I'll take the journey alone!":
            jump s8
        "{i}Try to talk to the ikemen":
            jump s9

label s5:

    na "The TV has summoned you and you must answer its call. As you sit down on the couch, you see the familiar face of the main character, Kimura Takeshi."

    na "It looks like he's having a serious talk with the Kiss Kiss Love Power Team, a magical-girl group that saves the world from evil monsters."
    
    na "During the last episode, Takeshi was deciding whether or not to keep his office job or pursue his dream of becoming a full-time magical girl. 
        He must be discussing this with them now."

    mi1 "Takeshi... you must make a choice. If we wait any longer, the Dr. will find out your true identity. Either join us or leave us."

    pp "Pyun!"

    takeshi "But--{nw}"

    mi2 "Takeshi, we {i}meow{/i} it's a hard decision, but it's one that must be {i}mwade.{/i} {color=#b0b0b0}{size=-6}nya~{/size}{/color}"

    takeshi "But... but... what if I'm not cut out to be on the Kiss Kiss Love Power Team? 
        What if I'm not a real magical-girl? If I fail... I can't ever return. Please, give me more--"

    #explosion/crash + helicopter sounds
    #PyunPyun falls

    pp "Pyuuuuuuuuuuun~"

    mi1 "NO! PYUNPYUN!"

    #Through a megaphone:

    dr "HUEHUEHUEHUEHUE! I will defeat you all one by one!"

    na "Man, they kept the annoying mascot from season 1."

    na "Just as the Dr. begins to shoot his sadness missiles at the Kiss Kiss Love Power team, your phone buzzes."

    mc normal "Huh?"

    na "Suddenly, a tiny sexy witch emerges out of your phone."

    mc normal "Mark Zuckerberg?!"

    $ metRiri = True
    $ ririname = "Riri"
    $ ririname_kanji = "リリ"
    riri "Wrong! I'm Riri. My boss told me there was a weeb here so I came to help."

    riri "Wait! Are you Naninani Nantoka!?!?"

    mc normal "Uh. No. I'm [mcname]."

    riri "Oh how the great have fallen. {i}{color=#b0b0b0}{size=-6}{cps=10}*sigh*{/cps}{/size}{/color}{/i} I used to always hear about you at work--"

    riri "you were determined to get a lover by the end of the school day. On your first day of school! You were my hero... But now... {i}*cries*{/i}"

    mc normal "Ummm..."

    riri "Well no matter Naninani! I'll help you get back on your feet and into the world of romance once again. Let's go!"

    mc normal "Ummmmmmmmm..."

    menu:
        "{i}Go to school... late":
            jump s10

label s6:

    mc normal "Ah! I've done it now!"

    na "You quickly throw on your uniform, grab a piece of toast, and run out the door."

    mc normal "I'm gonna be late!"

    na "It isn't long before you find yourself turning a sharp corner... with toast... hmm..."

    mc normal "Ah! It hurts!"

    #Background bird caw noises
    mc normal "...?"

    mc normal "Is no one... here?"

    na "Wow, you must be really off your game today *name*. You look around yourself, stunned... this has never happened before."

    na "How could you not bump into a hot ikemen while turning a corner with toast in your mouth?!?! Maybe you should try again."

    na "You pick up the toast and start walking back to where you started, when you hear a strange noise."

    joe "Kyaa~! I'm gonna be late!"

    na "Ah, there it is. You look up and see a hot... pole? No wait! You shake your head to clear your vision."

    joe "Sorry, are you ok? I don't know what came over me. I just felt a sudden need to run around that corner."

    mc normal "Yeah, I'm alright."

    na "The boy's eyes sparkle as you take his hand and he smoothly pulls you to your feet. Nice."

    na "After you both apologize you quickly continue on your way."

    jump s10

label s7:

    na "Heh... school. Who needs it? You're about to discover the answer to the greatest mystery yet: who is Naninani Nantoka?!"

    na "You rustle back under your blankets, close your eyes, and start to dream again... but this time you are not at school."

    na "You are floating through an endless void. You can't move. You can't breathe. All is silent."

    na "Is this what it's like to be in a world with no love? No romance? No {i}ikemens?{/i}"

    na "Your mind succumbs to the darkness."

    mv "You have failed your purpose, [mcname]."

    na "By the time you wake up, the school year has already ended. You now know your true duty but it is too late, and there is no one left to love you."

    na "Weeping, you succumb to the darkness of sleep once more."

    jump e0 #Eternal Power Nap

label s8:

    na "You keep walking to school alone and eventually end up at the front of the school."

    scene gate
    na "You notice a poster near the entrance, offering students to join the Student Council"

    na "Hmmm... It'd look pretty good on college applications. How hard could it be?"

    menu:
        "{i}Go to class":
            jump s51
        "{i}Sign up and go to the Student Council room":
            jump s52

label s9:

    na "His looks are too much to resist... you must talk to him now that you have the chance and time."

    na "Looks like being responsible pays off."

    show joe normal
    mc normal "Oh.. kay, sorry! I didn't see you there."

    show joe scared
    joe "Really? I'm quite hard to miss, you know..."
    
    mc normal "Is that so? Anyways, what is your name?"

    $ joename = "Joe Kun"
    $ joename_kanji = "くん・ジョー"

    show joe ecstatic
    joe "Oh right! The name's Joe-kun, but you can just call me Joe."

    na "Is that even a name?"

    mc normal "Well, nice to meet you! My name is [mcname]"

    show joe normal
    joe "Wow, what a cool name! I'm jealous."

    show joe ecstatic
    joe "I'm just an average Joe, you know? Hahaha!"

    na "Seriously, laughing at your own jokes? This guy..."

    mc normal "Ha... well, which way are you heading?"

    show joe normal
    joe "Oh, I've got class this way. It was nice talking to you, see you around!"

    hide joe

    menu:
        "{i}Walk to school":
            jump s8

label s10:

    na "You arrive at school... late of course."

    na "What did you expect? After all that you'd still be early? Hah."

    na "Now [mcname]...  you have two options..."

    if metRiri:
        
        riri "What's this?! Two options of potential love and beauty?!?!"

        riri "Ahhhh I can't wait for you to turn back to your old self again!"

        riri "Listen, Naninani, I have the power of insight."

        riri "I can help guide you through this love journey."

        riri "But... you need to be the one making the decisions. Got it?"

        riri "I'll just be over here, and if you need my input just click on me."

        riri "Hehe... hehehehehe..."

        if metRiri:
            $ riris[10] = True
            

    menu:
        "{i}Go to class late":
            jump s11
        "{i}Skip!":
            jump s12

label s11:

    na "Skipping class? It looks like you value your education..."

    na "You walk to class and fling open the door."

    na "You're here in order to learn! You must study! You have your whole life ahead of you and you're not backing down!"

    mc normal "Excuse me!"

    sensei "Detention!"

    
    if metRiri:
        $ riris[11] = True
    
    jump s13
        

label s12:

    na "Yea, who needs school anyways? If they really wanted you to be there, they'd make the start of school later than 8:30 AM."

    jump s18

label s13:

    na "Ahhh... detention. A land of hopes and sorrows... youth and forgotten dreams."

    na "Somehow you always seem to find yourself here."

    na "You scan the room in order to find familiar faces, but suddenly your attention is caught by the piercing eyes of another student."

    na "They seem to be staring you down."

    na "Oh wait, now they're blinking at you. Or are they winking... with both eyes? Is that morse code?"

    na "Suddenly you hear the whispers of two delinquents a desk over."

    d1 "Hey hey, is that Takao Isamu?"

    d2 "Takao... Isamu?"

    d1 "You don't know? Their family is yakuza! Apparently they transferred in this school year but haven't said more than two words to anyone. They're super cold."

    d2 "Ohhhh yeah yeah I know them. {i}The Panther{/i}, huh? I heard they sleep with their eyes open because they have so many enemies."

    d2 "They're also rich, hot, have a six pack, and like to brood all the time."

    d1 "Wow... I wish I was that cool."

    na "As you look back over to the yakuza student you notice a majestic tear rolling down their cheek. Wow. What an emotionally conflicted and vulnerable young adult."

    na "You should totally cause a scene and show them your physical prowess."

    if metRiri:
        $ riris[13] = True
        
    menu:
        "{i}Make a scene!":
            jump s15
        "{i}Wait for detention to end and leave":
            jump s16

label s14:

    na "You agree to go and watch Akimitsu's basketball game after school."

    na "How could you not? You've known Akimitsu since you were tiny and basketball has always been really important to him."

    na "Maybe one day you'll be important to him too."

    na "After a short walk out of school the two of you arrive at a small run-down gym."

    scene gym
    show kyle jersey normal
    mc normal "The final is... here?"

    show kyle jersey flirty
    kyle "Yeah! It's just a small local tournament. Nothing to get too excited about."

    mc normal "Oh, got it."

    na "The two of you slowly open the door to the gym."

    na "Immediately you are blinded by colorful spotlights and music blasts throughout a ginormous stadium."

    na "The stands are packed with cheering onlookers, their voices roaring like thunder."

    na "There must be hundreds, no-- thousands of people here!"

    na "A basketball court stands in the center."

    mc normal "Is this... THE B. LEAGUE FINALS?"

    kyle "Mhm! That's why I didn't want to miss it."

    kyle "Why don't you grab a seat? I need to get warmed up."

    mc normal "Uhuh..."

    na "Your heart races. Sometimes Akimitsu is a little too humble."

    na "You grab a seat and the game begins. You don't even know what's going on because you keep staring at the Akimitsu fan section."

    beckham "YAAAAAAY AKIMITSU!"

    na "Impressive."

    na "Soon after, Akimitsu scores a touchdown which is {i}even more{/i} impressive because he's playing basketball."

    na "He glances your way and flashes a coy smile."

    beckham "KYAAAAAAAAAA~ AKIMITSUUUU!!"

    na "Maybe you should move away from the fan section."

    na "The game goes by quickly and Akimitsu's team wins by a landslide."

    na "You feel a sense of pride, but also distance."

    na "The boy you grew up with is a basketball star, and you're just... well... [mcname]."

    na "Suddenly a voice from the loudspeakers snaps you out of your thoughts."

    #In speakers
    kyle "In honor of this victory, I would like to sing a song. It's dedicated to my favorite person in the world, [mcname]. I love you. {i}{color=#b0b0b0}{size=-6}{cps=10}*ahem*{/cps}{/size}{/color}{/i}"
    
    #kyle song

    jump e12



label s15:
    scene classroom day
    na "You make a scene. How could you resist after all?"

    na "After throwing a few delinquents out the window with your super muscular muscles...{nw}"

    # Sound effects

    na "...Takao Isamu swaggers up to your desk."
    
    show sophia normal
    sophia "Yo."

    mc normal "Oh, hey."

    sophia "You dropped this."

    na "Isamu hands you a small handkerchief with a small cute cat print on it."

    mc normal "Oh, that's not mi--"

    sophia "Keep it."

    na "Isamu coolly grabs their jacket and leaves the room. You can't help but notice a slight blush on their face."

    mc normal "Huh..."

    na "You unfold the handkerchief to find a piece of paper with a message:"

    #Sophia's voice / piece of paper with words on it
    na "{i}You. Me. Rager party. Tonight? Yes? No? Plz yes. :3 Thank you.{color=#b0b0b0} - The Panther{/i}{/color}"

    na "Despite \"The Panther\"'s horrible grammar, your heart skips a beat. Are they asking you... on a date?"

    if metRiri:
        $ riris[15] = True
        

    menu:
        "{i}I'm going to that party!":
            jump s26
        "{i}Absolutely not":
            jump s27

label s16:

    na "What a waste, they even blinked at you!"

    na "Well, anyways... You decide to wait out detention. Maybe it was a bad idea to interact anyways."

    # After school

    na "Man, it was your first day and you got {i}detention{/i}. Honestly, I'm impressed."

    # Stomach rumbles and screen shakes

    na "Whoa! What was that?! It felt like an earthqua-{nw}"

    na "...Oh. It was you? Wow, you must be hungry."

    na "You happen to spot a Hoshibucks{size=-12}©{/size}. It'll be a pretty penny, but a Caramel Ribbon Crunch Frappe sounds pretty good right about now."

    jump s24


label s17:

    na "Yukata scolds you for skipping class."

    na "After some thinking, you decide that this treatment isn't fair in the slightest!"

    na "Maybe you want to skip class? He shouldn't be able to stop you! This is a free country!"

    mc normal "I refuse! {i}You{/i} shouldn't be able to send me back to class!"

    mc normal "What are you doing out of class, huh? I'll make {i}you{/i} go back!"

    na "Yukata stares at you for a moment, then a small grin appears on his face."

    jt "Ah, people like you are my favorite!"

    jt "What {i}I{/i} do while at school does not matter to you, understand me? I am the president of the student council!"

    jt "{i}You{/i} have to listen to me, and {i}I{/i} am in charge. That is how it works, and how it always will."

    na "Who does this guy think he is?"

    mc normal "That's just not fair!"

    jt "Oh, but my dear girl, {i}life{/i} is not fair. I am simply getting you ready for reality."

    na "I want to punch \"reality\" into his face! It would have been better if you chose to fight him."

    jt "Anyways, I like you, so I will let you off easy this time."

    jt "Just detention. Consider yourself lucky."

    mc normal "Hey!"

    jt "Don't make me angrier now. Welp, See you around!"

    na "Yukata turns and walks away confidently. Man, what a prick!"

    na "You pick up the detention slip that he slid in your pocket and reluctantly read it."

    mc normal "Right after school? This is the worst! Whatever, I better go..."

label s18:

    na "As you're wandering the halls, you notice a student walking your way. He seems to be dressed very nicely, even for the prestigious Gwetome Academy."

    na "Wait, that's the student council president! You're in trouble if he finds you out here."

    menu:
        "{i}Hide behind a corner!":
            jump s18_1
        "{i}Pshh, what is he gonna do?":
            jump s18_2

    label s18_1:

        na "As you tip-toe over to the corner of the hallway, you accidentally step on a very conveniently placed rose."

        jt "How'd a rose get in here?"

        na "Busted..."

        jump s18_3

    label s18_2:

        na "You stand confidently in the center of the hallway as he walks towards you."

        jump s18_3


    label s18_3:

        jt "What's a pretty looking girl such as yourself doing around these parts?"

        jt "Wait, what's a student doing in the halls? ...I'm terribly sorry, but you're gonna have to go back to class."

        mc normal "Nonono, I just--{nw}"

        jt "--Needed to go to the bathroom and got lost in the halls, I've been there."

        jt "Well, you're not going anywhere without a hall pass. How about we bring you back to class to get one?"

        menu:
            "{i}Sure, I should probably head back":
                jump s21
            "{i}This guy deserves a punch!":
                jump s18_4
                
    label s18_4:

        na "As you start to turn around to walk back to class, you swiftly turn back and drive your fist into the student's face. Nice."

        na "Uh oh, he got back up? Looks like it's time for a fight!"

        jump ph

label s19:

    na "You throw a powerful punch, flying him across the room. He won't be bringing you back to class again anytime soon."

    na "You hear a feeble voice as you walk away."

    jt "Wait-- please... You don't need to do this!"

    mc normal "Heh... I knew that CrossFit membership would pay off."

    jump s20

label s20:

    na "Word quickly spreads about how you punched the student council president and skipped class as you proudly walk out the front gates."

    mc normal "Man, that fight really took a lot out of me. I could really go for a Caramel Ribbon Crunch Frappe right about now."

    jump s24

label s21:

    mc normal "{i}Oh shoot, I forgot to grab one{/i}! Sure, let's head back."

    na "You walk back to class to get a hall pass, even though you never needed one. But right as you grab it, the bell rings."

    jt "Awww, well that's a shame. Well hey, at least we have the same class next period!"

    mc normal "Oh, nice! Wait, how did you know that we had the same class?"

    jt "I just checked the Google Classroom! It's the job of the student council president to know their fellow students' names, after all."

    jt "C'mon, we have English class next. Let's go!"

label s22:

    na "You release a powerful punch aimed right at Yukata!"

    na "...and miss. Well, that's embarrassing."

    mc normal "Oh... oops."

    jt "Ahahha, how cute! You really think you stand a chance against me? I am the one and only student council president, Yukata!"

    mc normal "Uhm... okay?"

    jt "You've been naughty now, haven't you?"

    jt "You think you can walk free after trying to hurt the most important student in the school?"

    jt "No! I will not let this stand! Off to counseling with you!"

    na "How dramatic can this kid get..."

    mc normal "Alright fine, I'll go to counseling. Sorry for trying to punch you, but it was too hard to resist."

    jt "Hey! Wait, don't say that about me!"

    na "You turn and go to counseling. You can feel Yukata fuming behind you, but you keep walking without a care in the world."

    jump s25

label s23: # Free space

label s24:

    #In starbucks

    mc normal "I'll take your finest Caramel Ribbon Crunch Frappe, please."

    na "You felt like you've seen this kid before. Maybe from school?"

    beckham "that'll be 2,210¥."

    mc normal "Wh-{nw}"

    # Saying yen amount loudly
    na "-Wait, 2,210¥?? What has this world come to..."

    na "Failing to hold back spending one fourth of your monthly allowance on a single Frappe, you swipe your card and watch as the barista skillfully crafts your drink."

    na "You imagine what the flavor will be as you grab the cup and walk away from the front counter."

    mc normal "It looks so good! I'll worry about the cost later, because this is gonna be so worth i-"

    #Drink spill noise, crash

    mc normal "NO! MY CARAMEL RIBBON CRUNCH FRAPPE!!"

    na "Well, that's rough. After you witness-- with pure agony--  the drink spill, you then look up to see… a pole? And an attractive one at that."

    na "Wait, who would put a pole in the middle of a Hoshibucks{size=-12}©{/size}? The pole reaches out a hand to you."

    # Shot with joe and his hand out towards camera in hoshibucks

    joe "Are you okay?! I'm so sorry, I didn't see where I was going."

    if metJoe == True:
        joe "Hey, I remember you! We met at the [metJoeLocation]."
    
    joe "Drinks from Hoshibucks{size=-12}©{/size} are expensive nowadays."

    joe "Here, let me pay for it. It was my fault anyways."

    mc normal "No, it's okay! Don't even worry about it, It didn't cost {i}that{/i} much."

    na "You're still a bit irritated due to the fact that it {i}did{/i} in fact cost that much."

    joe "No no no, please, let me! I'd feel bad if I didn't."

    mc normal "No no no no, I wasn't looking where I was going."

    joe "No no n-"

    na "{b}Enough with the “no no no” talk!{/b}"

    $ joename = "ジョ～・くん"
    joe "Well, anyways, my name's Joe. Nice to meet you! I'm gonna buy a drink for myself anyways, so I'll get us both one."

    mc normal "I'm [mcname], nice to meet you!"

    na "You let him buy you another Caramel Ribbon Crunch Frappe and have a nice chat at one of the tables."

    joe "Hahaha, you're so funny!"

    joe "Well, anyways, It's getting kind of late. Mind if I take you home?"

    mc normal "Hmmm... It {i}is{/i} getting kind of dark out..."

    if metRiri:
        $ riris[24] = True
        
    menu:
        "\"No, leave me alone!\"":
            jump s41
        "\"Sure, why not?\"":
            jump s42

label s25:

    scene counseling

    na "You enter the counseling office with Yutaka to find... another student?"

    na "I guess the school's low on staff..."

    na "After Yutaka angrily explains the situation to the student \"student counselor\", you soon find yourself in a one-on-one counseling session to address your... issues..."

    beckham "If you don't go to school, you won't find success. You need to try your best everyday."

    mc normal "Okay..."

    beckham "Why did you think punching a classmate was a good idea? Do you realize what could happen?"

    mc normal "He was being a bully, I needed to do something."

    beckham "That was a dumb thing to do. You were such a good student last year, I'm sorry that I have to do this..."

    mc normal "Wa--What?"

    beckham "{cps=6}{b}GO TO DETENTION!{b}{/cps}"

    jump s13

label s26:

    na "Actually... does it even matter if it's a date? It's a party! Of course you're going!"

    na "You carefully put the handkerchief and note in your bag and begin to daydream."

    mc normal "{i}I wonder who's going to be there... I'll have to make lots of friends! Maybe I should try something new to make a good impression...{/i}"

    # Door sounds

    mc normal "Eh? Akimitsu?!"

    na "Chiba Akimitsu, your childhood friend since third grade appears at the desk next to yours."

    kyle "Hey [mcname]! Ahaha, did I surprise you?"

    mc normal "Mhm! Why are you also in detention?"

    kyle "I knew you'd be here on the first day so I came to keep you company."

    kyle "What were you thinking about before I interrupted you?"

    mc normal "Nothing much... just this party..."

    na "You take out the handkerchief and note and show Akimitsu."

    na "His eyebrows furrow into a look of concern."

    kyle "A party with... the {i}PANTHER{/i}??? TAKAO ISAMU???"

    kyle "There's no way I'm letting you go alone, [mcname]. A party with yakuza attending? Absolutely not."

    mc normal "What are you... my dad?"

    kyle "I'm just worried about you! Who knows what those people are like?"

    kyle "Please, let me go with you. Or better yet, don't go at all and we can just hang out."

    if metRiri:
        $ riris[26] = True
        
    menu:
        "{i}Go to the party with Akimitsu":
            jump s28
        "{i}Ditch the party and hang out":
            jump s29

label s27:

    na "Date or not, you're not going. You toss the handkerchief and note out the window and wait for the school day to end. Soon enough, word gets around of your rejection."

    d2 "That's [mcname] isn't it?"

    d3 "Oh, you're right! I can't believe she'd reject Takao-sama's kind offer!"

    d1 "Weirdo..."

    d2 "Even after they used their special kitty handkerchief too!"

    d1 "{i}{color=#b0b0b0}{size=-6}{cps=10}*gasp*{/cps}{/size}{/color}{/i} No way!"

    d3 "It's true... I saw them outside weeping with it in their arms. It was their favorite handkerchief and it got dirty!"

    d1 "Poor Takao-sama..."

    na "You walk through the halls with shame. When you get home you can only find comfort in the soft light of your television."

    if metRiri:
        $ riris[27] = True
    
    jump s43
        

label s28:

    scene city_night
    na "Soon, night falls. You arrive at the party with Akimitsu and head inside."

    scene party
    na "The party is surprisingly classy. Everyone is dressed nicely, there's a live jazz band, and even an open apple juice bar. You make a mental note of the apple juice bar."

    na "You quickly see Takao Isamu spot you and even slightly move their lips upward."

    na "You can't tell if they're grimacing in pain or perhaps attempting a smile, but either way it's directed towards you."

    na "Akimitsu tenses up and steps closer to you."

    $ sophianame_kanji = "高尾・勇"
    $ sophianame = "Isamu Takao"
    sophia "Hey. I've heard a lot about you, [mcname]. I'm Isamu Takao."

    sophia "When I first saw you I wasn't sure the rumors were true, but now I know. You're incredible. What dojo did--"

    kyle "Youseikan. We trained at Youseikan."

    sophia "Ah... Who's this?"

    mc normal "This is my childhood friend, Chiba Akimitsu."

    sophia "Is that so? Interesting."

    sophia "Anyways, how is the party?"

    na "You start to get the feeling that these two aren't getting along."

    na "So, you must do what any reasonable person would do: ignore one of them."

    if metRiri:
        $ riris[28] = True
        
    
    menu:
        "{i}Ignore Isamu":
            jump s30
        "{i}Ignore Akimitsu":
            jump s32
        "{i}Ditch both for apple juice":
            jump s31

label s29:

    mc normal "Actually, hanging out sounds fun."

    na "Akimitsu flashes a smile."

    kyle "That's a relief. After school let's go to my pla--{nw}"

    # *phone buzz sounds*

    kyle "Actually... wait..."

    mc normal "Huh?"

    kyle "Ahhh, sorry. I have a basketball game after school."

    kyle "He says, \"Hey, turns out we're in the finals now because some person with bleached blonde hair just showed up and beat up the team that we lost to. {w=2}{nw}"
    
    kyle "He was saying something about [mcname], you, and a party. Weird, huh?"

    mc normal "I wonder who that could be..."

    kyle "Right? Well now I can't miss my basketball game... would you mind coming to watch instead?"

    if metRiri:
        $ riris[29] = True
        

    menu:
        "\"Sure, I'll watch\"":
            jump s14
        "\"I'd rather party\"":
            jump s33

label s30:

    mc normal "The party's good.{nw}"

    na "You say, proceeding to turn and face Akimitsu."

    mc normal "Hey... should we get going?"

    sophia "Wait. Would you like to get drinks with me?"

    na "{i}{color=#b0b0b0}{size=-6}{cps=10}*Narrator gasps*{/cps}{/size}{/color}{/i}"

    menu:
        "\"You know what? Sure.\"":
            jump s35
        "\"No, I have plans with Akimitsu\"":
            jump s36

label s31:

    mc normal "The party's good.{nw}"

    na "You say. And then you run and escape to the apple juice bar."

    #Bar scene

    mc normal "Apple juice please~"

    beckham "May I ask what type of apple you prefer? Honeycrisp? Fuji?"

    mc normal "Umm... Gala please."

    beckham "Coming right up."

    na "Never before have you tasted such a sweet, succulent drink."

    na "You down glass after glass until your tummy can take it no longer. Delicious."

    na "Then you go home."

    if metRiri:
        $ riris[27] = True
        
    jump s43

label s32:

    mc normal "The party's good."

    mc normal "I just wish I was being escorted by someone since I've been so lonely by myself."

    sophia "Want me to help you?"

    kyle "Hey, hey... wait. [mcname], please."

    kyle "Don't do this... let's just get drinks. Just the two of us."

    na "{i}{color=#b0b0b0}{size=-6}{cps=10}*Narrator gasps*{/cps}{/size}{/color}{/i}"

    menu:
        "\"Sounds good to me!\"":
            jump s34
        "\"No thanks, I'm going with Isamu\"":
            jump s37

label s33:

    na "You shake your head solemnly"

    mc normal "Sorry, Akimitsu. I changed my mind. The party never stops."

    kyle "But you just said we would han--{nw}"

    # Door closes

    na "You leave."

    kyle "Wait! Wait! If you're that determined to go to the party I'll go with you. I'll skip my game."

    kyle "Let's just go together, okay?"

    if metRiri:
        $ riris[33] = True
        
    jump s28

label s34:

    mc normal "Ah, okay! Sounds good to me."

    na "Akimitsu lets out a deep breath as Isamu silently slips away into the crowd."

    kyle "Whew... I thought you were going to ditch me for a second."

    kyle "Wanna go find that open apple juice bar again?"

    na "After finding the bar and getting your apple juice, the two of you begin to reminisce."

    na "You think about the dojo and your childhood."

    na "How Akimitsu has always been there for you, even writing letters to you after you moved away."

    na "He hasn't changed a bit has he? It's almost like this whole time he's been waiting for you..."

    kyle "Hey... it's getting a little stuffy in here. Wanna go somewhere else?"

    if metRiri:
        $ riris[34] = True

    jump s40

label s35:

    mc normal "Sure!"

    kyle "What?? Wait... what?!?!"

    sophia "Heh. Let's go then."

    if metRiri:
        $ riris[35] = True
        
    menu:
        "{i}Go get drinks with Isamu":
            jump s38

label s36:

    mc normal "I'm good. I was planning to spend time with Akimitsu tonight."

    na "Isamu glares coldly at you both."

    sophia "Hmph."

    kyle "I actually... was also thinking of getting drinks with you, [mcname]."

    if metRiri:
        $ riris[36] = True

    menu:
        "\"Sounds good to me!\"":
            jump s34

label s37:

    mc normal "Sorry~ I've already got plans."

    mc normal "I'll see you later Akimitsu!"

    kyle "But..."

    kyle "Actually, fine. Do what you want. I don't care."

    na "Akimitsu storms off. His hot fury combined with his blazing looks briefly set another guest on fire, but the flames are doused quickly with some apple juice."

    sophia "Heh. Let's drink something ourselves too."

    if metRiri:
        $ riris[37] = True
        
    menu:
        "{i}Go get drinks with Isamu":
            jump s38
        "Actually... I'm good":
            jump s39

label s38:

    na "As you and Isamu start to go towards the bar you hear a brief shattering sound."

    # Shattering noise

    mc normal "Ah. I think Akimitsu may have accidentally kicked the door down."

    mc normal "That's a bad habit of his. He tends to do it when he leaves houses."

    sophia "Don't we all?"

    mc normal "Hey! Bartender! Get me your most appley apple juice."

    beckham "Of course."

    na "After hours of discussing fighting techniques and the best way to throw someone out a window, you run out of apple juice."

    beckham "I'm sorry, we don't have any more apples to juice. It's a true tragedy for which I am very sorry Takao-sama."

    sophia "Eh, whatever. Hey, [mcname], wanna take break outside? It stinks of granny apples here anyway."

    mc normal "Sure."

    na "The two of you step outside."

    scene city_night
    na "You find yourself on a balcony overlooking Shizuoka."

    na "The wind softly blows through your hair and the lights of the city sparkle in the distance."

    show sophia party normal
    sophia "To be honest... I didn't think you'd come with me."

    mc normal "Huh? Why?"

    sophia "My family is yakuza. Ordinary people are usually too afraid of getting hurt. But you're... different."

    sophia "When you threw those three delinquents out the window you reminded me of my cat, Skull Crusher."

    sophia "And I love cats... and I love... you."

    mc normal "I... I like you too."

    na "Soon after Takao Isamu's confession the two of you start dating."

    na "It's a surprisingly healthy and loving relationship-- you meet {i}The Family{/i}|, go on lots of dates, and work through conflicts together."

    na "Eventually you decide to open a cat cafe together... but... it is no ordinary cat cafe."

    na "Through years of discipline and training, blood and tears, your cat cafe becomes the base for a new group of cat yakuza: {i}Nyanken{/i}."

    na "It is through Nyanken that you wage the Great Cat War, rise through the ranks, and become the most powerful yakuza couple in the nation."

    na "No one can stop your bulging muscles or your untouchable love!...  {i}{color=#b0b0b0}{size=-6}{cps=10}Nya~{/cps}{/size}{/color}{/i}"

    jump e5

    # not done

label s39:

    na "Romance? {i}{color=#b0b0b0}{size=-6}{cps=10}*scoff*{/cps}{/size}{/color}{/i} That's for weaklings."

    na "You don't need any of these weirdos, you just came for the party."

    na "But the party sucks so..."

    mc normal "Actually... I'm good."

    sophia "...Huh?"

    na "You flip your hair and strut out the door."

    scene city night
    na "As you walk you radiate power and confidence. Is this the power of self-worth?"

    na "In fact, the aura from your strut is so strong that it catches the attention of a modeling agent."

    show beckham agent normal
    beckham "Wait! I'm a modeling agent who also likes attending high school parties hosted by yakuza. You should join my agency! You're incredible!"

    mc normal "Okay."

    na "And that was how your modeling career began."

    hide beckham
    na "You dropped out of high school, moved to New York, and started your legacy by modeling for Elle, Versace, and Vogue."

    # Visual of "magazines pop up on screen"

    na "You became surrounded by fame and fortune, but soon it became too much."
    
    na "Burdened by the pressure of stardom, you started looking for a way to relieve the stress."

    na "You thought back to that night... that party... and how you didn't get to try that apple juice."

    na "Now you wanted it... you needed it... and eventually you succumbed to it."

    na "You spent all your money on apple juice, only drank apple juice, and only cared about apple juice."

    na "You threw away your career, friends, and life for apple juice."

    na "Everything you had... became apple juice."

    jump e11

label s40:

    na "The two of you leave the party and walk to a nearby park."

    na "The air is chilly but the stars are shining clearly and brightly."

    kyle "Let's sit down for a little bit. There's a bench over there."

    mc normal "Okay!"

    # Switch to bench

    kyle "..."

    mc normal "..."

    kyle "..."

    mc normal "It's really cold out here."

    kyle "Maybe we shouldn't have sat down."

    mc normal "Yeah, that was kind of stupid."

    kyle "Do you want my jacket?"

    mc normal "No it's okay, you can keep it."

    kyle "Oh. Uh, okay."

    mc normal "..."

    kyle "..."

    mc normal "..."

    kyle "Have you ever wondered what the stars would say if they could talk?"

    mc normal "Haha, n--{nw}"

    kyle "I think they'd tell us the world's secrets. Why we're here, what we're meant to become, and how we might get there."

    kyle "Sometimes I feel lost. Like I'm just falling through time with no real purpose."

    kyle "But there are moments when this light reaches out to me."

    kyle "It tells me that I have something to give. That I have something to offer to this cold world."

    kyle "This light tells me to keep going, keep trying, and keep living."

    kyle "And I've found [mcname], that it's when I'm with you that this light is most prevalent."

    kyle "You're like my star, [mcname]. And that's why... I love you."

    mc normal "I..."

    jump e4

label s41:

    mc normal "No thanks, I can make it by myself. Nice meeting you though!"

    joe "Oh okay... I guess I'll see you later then."

    na "You had to get home quick anyways. You haven't been catching up on this season's anime!"

    na "You dart out of the Hoshibucks, not even thanking him for buying your drink before leaving. Bold."

    jump s43
 
label s42:

    mc normal "Sure, why not? I live just 10 minutes down the road."

    joe "Perfect! I'm going the same direction. Come on, let's get moving!"

    na "You leave the Hoshibucks with Joe."

    na "It almost looks like you two are going on a date, hehe!"

    na "Alright now, what will you talk about for maximum romance?"

    menu:
        "{i}Talk about Hoshibucks":
            jump s44
        "{i}Talk about hobbies":
            jump s45
 
label s43:

    # At home

    na "You sit down in front of your television to watch anime."

    na "For some strange reason you feel empty and alone, like there is a dark hole in your heart."

    na "Maybe it's because Fanana Bish is on? You change the channel."

    mc normal "Ahh... that's better. Now I can go on with my day and never have to worry about romance agai- {i}{color=#b0b0b0}{size=-6}{cps=10}*yawn*{/cps}{/size}{/color}{/i}"

    mc normal "Suddenly... {color=#b0b0b0}I feel... {cps=15}{size=-6}very... {size=-8}{cps=5}sleepy.{/cps}"

    na "In the corner of your eye you see a tiny magic wand waving at you from behind the couch. Is that..."

    show riri normal
    riri "It's me, Riri. Don't worry Naninani, I'm just making some minor adjustments to the fabric of time."

    show riri happy
    riri "You may have failed this time at romance, but I won't let you give up!"
    
    mc normal "Eh?! What's going on?"

    #Reset with loading screen or something

    jump start
 
label s44:

    mc normal "So, do you go to Hoshibucks often?"

    joe "Yes! In fact, I go almost every day after school! I live for Hoshibucks, haha!"

    mc normal "Wow, that's cool! I like Hoshibucks, but I don't go very often because it's so expensive."

    joe "True..."

    joe "Well, if you don't go to hoshibucks often, what do you do in your free time?"

    mc normal "Well, other than studying and extracurriculars, I like going to to the beach."

    joe "Really? Me too! It's such a nice way to unwind after a long day."

    na "I think this guy just wants something to do with you… he probably spends all day in Hoshibucks."

    joe "Well, if you're ever free, we should go to the beach together."

    mc normal "Okay, sure! How does tomorrow sound?"

    joe "{color=#b0b0b0}{size=-5}I guess I can go one day without my caramel frappe... for [mcname]...{/size}{/color}"

    joe "Sounds good! I'll be looking forward to it! {i}{color=#b0b0b0}{size=-6}{cps=10}*wink*{/cps}{/size}{/color}{/i}"

    if metRiri:
        $ riris[44] = True
        
    menu:
        "{i}Go to the beach with Joe":
            jump s46
 
label s45:

    mc normal "So, what do you like to do in your free time?"

    joe "Well, other than going to hoshibucks, I guess I go to the beach sometimes."

    mc normal "Really? Me too! I love the beach."

    joe "Is that so? It's such a nice way to unwind after a long day, right?"

    mc normal "Right? The water feels so nice, especially in the summer."

    joe "Well, if you're ever free, we should go to the beach together."

    na "Wow, I didn't see that coming! What a slick way to ask you out..."

    gwyn "Okay, sure! How does tomorrow sound?"

    joe "{color=#b0b0b0}{size=-5}I guess I can go one day without my caramel frappe... for [mcname]...{/size}{/color}"

    joe "Sounds good! I'll be looking forward to it! {i}{color=#b0b0b0}{size=-6}{cps=10}*wink*{/cps}{/size}{/color}{/i}"

    if metRiri:
        $ riris[44] = True

    jump s46
        
    
label s46:

    na "The next day, you and Joe make plans to go to the beach together."

    na "The way he talks to you... I think he likes you, ya know!"

    na "Anyways... After school, you meet up with Joe at the beach."

    joe "Hey, [mcname]! It's nice to see you again. You look good!"

    na "Well, that was fast."

    mc normal "Oh, thanks! Nice to see you too!"

    beckham "Ehem, lovebirds!"

    joe "Excuse me?"

    beckham "Sorry to interrupt, but the currents are very strong today."

    na "This guy {i}again?{/i}"

    beckham "I recommend staying out of the water, for your own safety."

    beckham "Rest assured, I can save you, of course, but please be careful. Have a good day at the beach!"

    joe "Oh, okay. What do you think, [mcname]? Should we still swim?"

    if metRiri:
        $ riris[46] = True
        
    menu:
        "{i}Go swimming! That lifeguard can't stop me!":
            jump s47
        "{i}Walk on the beach instead":
            jump s48
 
label s47:

    mc normal "Let's go swimming! That's what I came here for."

    joe "Alright, as long as you're careful. I don't want you to get hurt."

    mc normal "Oh, I'll be fine! I'm more worried about you, hehe!"

    joe "Hey! I'm a great swimmer, I promise!"

    mc normal "If you say so!"

    na "Enough flirting! I'm skipping to the part where you actually swim."

    # Switch to water

    na "Ahh, finally... but wait, is Joe okay?"

    joe "Hey, I can't touch the ground here! I'm getting pulled out! Someone save me!!!"

    joe "I'll admit it, I don't go to the beach very often! I prefer caramel frappes, okay!? {i}{color=#b0b0b0}{size=-6}{cps=10}*crying*{/cps}{/size}{/color}{/i}"
 
    if metRiri:
        $ riris[47] = True
        
    
    menu:
        "{i}The lifeguard can deal with it":
            jump s49
        "\"Don't worry, I'll save you!!\"":
            jump s50

label s48:

    mc normal "Maybe we should just take a walk on the beach for today."

    joe "Okay, sounds good. I'd love to take a walk together."

    # MC Blushes
    mc normal "We'll have other opportunities to go swimming together anyways..."

    na "Aww, look at you two!"

    na "You take a nice walk and talk about various things, from hoshibucks, to school, to more hoshibucks, and eventually..."

    joe "You know, name, there's something I should tell you..."

    mc normal "Yes?"

    joe "Ever since I saw you in hoshibucks, I've thought you are the most beautiful person I've ever seen."

    # Whispering:
    joe "Maybe even more beautiful than a caramel frappe..."

    joe "But, anyways, I want you to know that..."

    joe "I think... I love you."

    na "How adorable."

    mc normal "Joe... I think I love you too."

    joe "You've lightened up my life since we met..."

    na "As in yesterday?"

    joe "And I want you to be the light in my life forever."

    # Gwyn giggles
    mc normal "I can do that..."

    na "Aww, what a cute couple you make. Good job [mcname]!"

    jump e2

label s49:

    na "You wave your arms until the lifeguard notices Joe struggling."

    na "He rushes out to save Joe!"

    na "He doesn't seem to be paying attention to you though..."

    na "You manage to make it to shore safely, and see the lifeguard performing CPR on an unconscious Joe."

    mc normal "I've never seen someone perform CPR, but doesn't that seem a little... much?"

    na "Joe gasps and opens his eyes. He seems weirdly... happy to see the lifeguard above him."

    joe "Thank you, you saved my life! I'll... do anything to repay you~"

    na "Joe and the lifeguard stare into each other's eyes for what seems like minutes..."

    na "Something is definitely off."

    beckham "Well, there's only one thing I want..."

    joe "What? I'll do anything!"

    beckham "All I want right now... is you."

    na "The two close their eyes and engage in a long, drawn out kiss."

    na "Wow... really long... seriously, are they just trying to rub it in?"

    na "You sit there, utterly shocked. Really, is there anything else you can do?"

    mc normal "Is this what I get for not saving you, Joe?"

    joe "I'm sorry, [mcname]..."

    na "Well, that's that, I suppose..."

    jump e1
 
label s50:

    smc normal "Don't worry Joe, I'll save you!"

    na "Despite your best efforts, you end up both getting swept away by the current."

    joe "I'm so sorry, [mcname]. This is all my fault..."

    smc normal "It's okay... I don't want to live if it's without you."

    na "How romantic."

    joe "[mcname]"

    smc normal "...?"

    joe "I... love you."

    joe "I need you. You are the light in my darkness, the sand on my beach, and..."

    joe "The caramel crunch whipped cream on my caramel frappe."

    joe "You are everything to me, [mcname]."

    na "Wow, this guy really has a way with words."

    na "But, before, you can respond, you are knocked unconscious by a huge wave."

    na "Is this how you die?"

    na "..."

    na "Just kidding. You wake up on a deserted island with Joe laying by your side."

    # Opens eyes

    joe "[mcname]! You're awake! I got this coconut for you. Please, drink from it!"

    joe "Apparently, Hoshibuck's pink drinks are made with coconut milk, so I thought it must help."

    na "You can feel your burnt skin and pain all over your body, but the coconut does help."

    smc normal "Thank you, I feel much better. Where are we?"

    joe "It's been a few hours since we washed up on this island. I don't know if anyone will ever come for us."

    smc normal "Oh... well, we have each other, don't we?"

    na "You take Joe's hand and look into his eyes."

    joe "Maybe, if I have you by my side everyday, I can live without hoshibucks."

    smc normal "Aw, Joe..."

    na "{i}{color=#b0b0b0}{size=-6}{cps=10}*sigh*{/cps}{/size}{/color}{/i} There he goes again."

    na "You live the rest of your lives together, surviving on the island and its natural resources."

    na "What a happy ending..."
    
    jump e3
 
label s51:

    # English class scene

    scene classroom day
    na "You arrive at your English class. You could have had something fun, like Japanese. But {i}English?{/i}"

    #TODO: Sitting down noise(?)
    na "You take a seat and get ready to listen to the teacher's lecture."

    na "Right when they start talking, you start feeling very tired. Perhaps a nap wouldn't be too bad..."

    na "You fall into a deep slumber, and dream of a high school life where {i}you{/i} are the main character."

    # Dream scene
    scene dream

    na "As you walk to the front gates of the school in your dreams, you notice four ikemens waving at you from one of the classrooms. They seem to be trying to say something."

    mi "{i}Heeeeey!!!{/i}"

    scene black
    na "Heyyy..." # mi line

    #TODO: smack sound effect
    teacher_e "Hey, [mcname]!" with hpunch

    # Back to classroom scene

    scene classroom day
    na "Suddenly, you feel a sharp pain on your forehead. A piece of chalk then drops onto your desk."

    # define e = MoveTransition(
    #             delay = 0.3,
    #             enter = offscreenbottom,
    #             leave = offscreenbottom,
    #             old = False,
    #             layers = ['master'],
    #             time_warp = ease,
    #             enter_time_warp = None,
    #             leave_time_warp = None)

    show teacher_e angry at e
    teacher_e "Would you like to come up to the board and answer the question?"
    
    # hide teacher_e with ex
    mc normal "Uhhh... What question?"

    teacher_e "{i}{color=#b0b0b0}{size=-6}{cps=10}*sigh*...{/cps}{/size}{/color}{/i} I have it written right here. What is [quizWord] in Japanese?"

    # $ metRiri = True
    if metRiri:
        $ riris[51] = True

    menu:
        "[quizGuess1]":
            if quizGuess1 == quizCorrect:
                jump s54
            else:
                jump s53
        "[quizGuess2]":
            if quizGuess2 == quizCorrect:
                jump s54
            else:
                jump s53
        "[quizGuess3]":
            if quizGuess3 == quizCorrect:
                jump s54
            else:
                jump s53

label s52:

    na "Going to class won't get you into college! Instead, you go to the student council office to do something useful instead of rotting in class."

    na "You look around and see a well dressed and quite handsome student sitting in an important looking chair."

    mc normal "He must be the leader of the student council! I should ask him about signing up!"

    mc normal "Excuse me, sir?"

    na "The student looks up with a puzzled expression on his face."

    jt "Me? Wow, sir is a new one... Do I really look that good?"

    mc normal "Oh, you're just well dressed is all..."

    jt "Anyways, what do you need?"

    mc normal "Well, I saw the poster looking for people to join the student council, and I decided to check it out. Can I sign up?"

    $ jtname = "Yutaka Yanai"
    jt "Of course! I'd be delighted to have you on our student council team. My name is Yutaka Yanai, nice to meet you!"

    na "Yutaka pulls out a book's worth off papers from his cabinet."

    jt "All you have to do is sign all these documents, and then you can get started."

    mc normal "Oh wow, alright."

    na "It takes the whole school day, but you eventually finish filling out all the documents."

    na "Besides some documents mentioning that the student council will have complete ownership of your loved ones, prized possessions, free time, and soul, you aren't worried about what you are signing up for."

    na "When you are finally done, you hand them all back to Yutaka."

    jt "Congratulations! You are now an official member of the student council. I'm excited to work together~"

    mc normal "Thank you! I'll do my best!"

    # Continue

    jump s74

label s53:

    na "You have no idea what you're doing as you scribble a random vocabulary word you remember onto the board."

    teacher_e "No... not quite, [mcname]. Maybe studying in the library will help you out."

    teacher_e "You'll need someone to help you on the English project we will have too. Details will be posted in Google Classroom."

    na "Well that's embarrassing. After getting laughed at by the entire class, you decide to go to the library to work on your English skills."

    na "As you are about to enter the library, you notice a flier posted next to the door."

    na "\"Come over to my house at address here if you need help with English words like [quizWord] and English project work. –遥花\". Huh, that sounds exactly like what you need! Maybe a little too exactly... Sounds like stalker behavior..."

    na "Pshh...  Let's be realistic here! It's just a coincidence!"

    if metRiri:
        $ riris[53] = True
        
    
    menu:
        "{i}Go to the address":
            jump s58
        "{i}Study alone in the library":
            jump s59
 
label s54:

    na "You swiftly write the answer up on the chalkboard."

    teacher_e "That's correct [mcname], good job. It wouldn't look good if you got that wrong, that was one of the easier ones."

    na "You proudly walk back to your seat and listen to the rest of the lesson."

    teacher_e "Alright everyone, we are going to be starting an English project using the vocabulary we learned. Please get with a partner and make a video by this Friday."

    na "You instantly realize that getting with a partner brings up a big issue..."

    na "...you have no friends."

    na "You notice someone sitting in the back of the classroom. Wanna try grouping with them?"

    menu:
        "{i}Ask to group with them":
            jump s56
        "{i}Nah, I'm good":
            jump s55
 
label s55:

    na "You're gonna have to group with somebody..."

    na "Hey, look, someone's walking up to you!"

    jt "Hey, I'm Yukata! You seem pretty cool, want to work together?"

    mc normal "Oh, sure! What should we do?"

    jt "I was thinking a love story could be pretty fun..."

    na "Something is fishy here..."

    mc normal "Oh, uh, sure, that could be fun!"

    jt "Alright, it's settled then! Meet me at my house after school to work on it."

    # At Yutaka's house

    na "That night, you head over to Yukata's house."

    na "Well, more like Yukata's castle. This thing is massive!"

    na "Anyways, you spend hours with Yukata, and eventually finish the project."

    jt "Whew! That's the last scene!"

    mc normal "Yes! We did it!"

    jt "Well, I guess you should start heading back soon..."

    jt "It was... really fun to work together."

    mc normal "Yeah! I had a lot of fun too. Well, see you tomorrow!"

    na "Well, although Yuata presents as snobby, he really is nice on the inside."

    na "And it seems like he really cares about you... hehe!"

    na "Ahem, anyways, the next day in class..."

    # In class the next day

    teacher_e "Next we have... Yukata and [mcname]'s project."

    jt "Ah yes, our masterpiece is finally being shown!"

    mc normal "Here we go..."

    na "As the teacher shows your project, you can here your classmates murmuring."

    na "As you thought, they're suspicious. Your project seems a little too romantic..."

    teacher_e "Comments?"

    #TODO: Finish Scene 55

label s56:

    na "You walk up to the student's desk."

    mc normal "Hey, do you have anyone to group with?"

    maryam "N-no!"

    mc normal "Would you like to work together on this project?"

    maryam "S-Sure!"

    na "You realize that your room is a mess, you probably wouldn't want them seeing that."

    mc normal "can I come over to your house tomorrow to work on it?"

    maryam "Okay, that works for me!"

    na "You knock on the door, and Haruka answers."

    maryam "Welcome. Make yourself at home. Let's go to my room."

    na "You both go upstairs and enter their room."

    jump s57

label s57:

    maryam "I'm going to go get my English work from downstairs... stay here for a little."

    na "You sit down and get under the kotatsu positioned in the middle of the room."

    mc normal "Aaa~ It's so warm~"

    na "As you look around the room, you can see many pieces of hanging tape on the walls surrounding their bed. Did they take those down recently?"

    na "Looking a bit more, you notice a small shiny object on the floor near the other side of the kotatsu."

    # Gwyn talking to herself

    mc normal "Ooo~ shiny! Hmmm... Isn't this my ring that I lost? I thought it was gone forever!"

    mc normal "They found it and never gave it back?! So rude!"

    mc normal "Hold on a minute..."

    if metRiri:
        $ riris[57] = True
        
    
    menu:
        "{i}Maybe they were planning to give it back":
            jump s61
        "{i}Something's fishy around here...":
            jump s60
 
label s58:

    na "You walk up to the door of the address posted on the flier with no worries in your mind."

    scene door
    na "You then hear some noises coming from the house, like someone is frantically trying to clean up."

    show maryam normal
    maryam "H- Hello... Are you here for the English lessons?"

    mc normal "Yep! I saw your flier next to the library!"

    maryam "A- Alright... Come on in..."

    na "As you walk inside, you see Haruka running up the stairs ahead of you. You reach the second floor and see a door slam shut down the hallway."

    # Knock knock

    mc normal "Hey, is everything alright?"

    maryam "Just one minute...!"

    na "You give they a minute, and they eventually opens the door, silently signaling you to enter the room."

    jump s57
 
label s59:

    na "Yeah, it sounds a little too risky."

    mc normal "I think I'll just study alone in the library today..."

    na "You spend all day studying English in the library, until you are fully satisfied that you have memorized that word."

    mc normal "Finally! Ahh, I'm exhausted. Time to head home and watch some anime..."

    jump s43
 
label s60:

    mc normal "Hey, I noticed the ring in your room looks familiar, where did you get it?"

    na "You notice that Haruka starts looking a little nervous."

    maryam "...From a shop."

    mc normal "Oh, haha! I must be wrong."

    na "You put the ring back on the kotatsu. You start feeling a little uneasy. Maybe working in the safety of your home would be a better idea."

    mc normal "Do you think we could go to my house to work tomorrow?"

    maryam "Yeah, sure..."

    # New day, at MC house

    na "Haruka arrives at your house, ready to work on the English project."

    mc normal "Alright, let's get to work!"

    na "Haruka takes their computer out and starts typing right away."

    na "Hmmm... Maybe they're using a Hotspot? You've never given them your Wi-Fi."

    mc normal "Hey, do you need my Wi-Fi password? You don't have to use data."

    maryam "No-- I mean yes! Yes please!"

    mc normal "Right... Could I have the computer to put it in?"

    maryam "No! ...I can put it in it myself."

    na "they're acting like they already have your Wi-Fi password. With this and the ring that you found, things are getting awfully suspicious..."

    if metRiri:
        $ riris[60] = True
        
    menu:
        "{i}Test them to see if they know the password":
            jump s63
        "{i}Pshh, it's probably fine!":
            jump s64
 
label s61:

    na "You decide not to think too much of it and start to take out your English work."

    # Door noise

    maryam "Hey, I'm back. Do you have everything?"

    mc normal "Yep! But why is nobody else here? I even arrived thirty minutes late."

    na "You notice their eyes starting to drift away from you as they respond."

    maryam "Yeah uh... The English problem was pretty specific. Maybe there was j-just nobody else that needed help."

    maryam "Anyways... do you want to-{nw}"

    na "Haruka glances to the floor next to you."

    na "They quickly walk over to the other side of the kotatsu and sit down, grabbing the ring."

    maryam "Would you like to start?"

    mc normal "Okay!"

    na "You and Haruka work through your English for hours until you finally feel confident about your skills."

    # MC stomach rumbles

    maryam "You want to finish up? We could go eat something after."

    mc normal "Sounds good!"

    na "You and Haruka clean up and start to walk out the door to go eat."

    jump s62
 
label s62:

    mc normal "Where would you like to go?"

    maryam "Have you been to Hoshibucks before?"

    mc normal "Yes! I love Hoshibucks!"

    # In Hoshibucks

    na "In the Hoshibucks line, Haruka notices that they forgot their wallet."

    maryam "Oh no! I forgot my wallet!"

    mc normal "It's alright, I'll buy you a sweet treat because you helped me so much with the English project!"

    na "Haruka's eyes widen, they are entranced by your generosity and kindness."

    maryam "Thank you so much, [mcname]!"

    na "As you both order the sweet treats and sit down, Haruka seems nervous as if they something important to tell you."

    maryam "uhm... [mcname]... I have something to tell you..."

    mc normal "Yes, Haruka?"

    maryam "I've liked you ever since we had art together freshman year of highschool!"

    na "You guys went to the same freshman class? How do they even--{nw}"

    maryam "When you gave me your extra pencil right before the final test, I knew you were the one for me! Would you like to go on a date with me?"

    mc normal "I would love to!"

    jump e8
 
label s63:

    na "You decide to test Haruka."

    mc normal "Alright then, the password is 123456."

    na "the real password is actually 1234567..."

    maryam "Perfect! I connected! L-let's get to work shall we?"

    na "You go silent, how could they possibly know your wifi password?!"

    maryam "[mcname], are you a-alright? You're awfully quiet."

    na "Your heart starts to race, Haruka has noticed your changed demeanor."

    mc normal "Ahaha actually, I don't feel very well at the moment, maybe we could continue another day?"

    maryam "Oh, alright, I see."

    na "Haruka hastily grabs their stuff and goes home. Anxiety is rushing through your veins, how could they have known your wifi password?!"

    # New day at school

    scene classroom day
    na "You and Haruka plan on finishing the project later that day, but then you notice a handsome figure approaching..."

    kyle "Hey naninani, I was wondering if you would like to come hang out with me after school... if you're not busy of course."

    na "Haruka's demeanor suddenly changes."

    na "Hmm, you were originally going to wrap up that project with Haruka though..."

    if metRiri:
        $ riris[63] = True
        
    menu:
        "{i}That project can wait! Hang out with Akimitsu instead":
            jump s65
        "{i}Nah, we have to finish this project.":
            jump s66
 
label s64:

    mc normal "Alright then, the password is 1234567."

    maryam "I'm in. Let's finish this project!"

    na "The two of you get the project done early and decide to go get a sweet treat together."

    jump s62
 
label s65:

    na "After school, you and Akimitsu get Hoshibucks. After you order your drinks, the two of you walk around the town and stop at a quaint park."

    na "The trees are thick and the sun has gone down, the two of you are seemingly alone."

    kyle "Uhm... [mcname], there has been something on my mind that I have wanted to tell you for a really long time now..."

    na "You turn around and look at Akimitsu, his face is flushed red but you can't tell whether he is blushing or if it's the cold breeze."

    mc  "What is it?"

    kyle "I have loved you ever since we were kids..."

    na "Just as Akimitsu confesses his love, you hear a leaf crackle and the bushes shake as if someone is in them and are shocked to hear Akimitsu's love confession!"

    kyle "Who's there!"

    na "The person in the bushes scurries deeper into them. The two of you look over to find a photo of the two of you from Hoshibucks and a knife! Whoever was in the bushes has been stalking you guys all day!"

    if metRiri:
        $ riris[65] = True

    menu:
        "{i}Call the cops!":
            jump s69
        "{i}Don't call the cops":
            jump s68
 
label s66:
 
label s67:
 
label s68:
 
label s69:
 
label s70:
 
label s71:
 
label s72:
 
label s73:
 
label s74:

    na "You begin walking the halls with Mio, putting up posters and talking about club duties. Although Mio seems meek she speaks with openness and discipline."

    mio "I-if you see students skipping class please tell them to return immediately. Some of them will try to use the “restroom excuse” but I'm sure you won't fall for that... it's a bit of an obvious lie."

    mc normal "Ha... yeah... who would ever--"

    mio "Aah!"

    na "Suddenly you find yourself in a stupor, standing above Mio who has face-planted onto the ground."

    na "After processing what just happened, you quickly put down the posters."

    mc normal "Are you okay?"

    mio "Y-yeah! I-it's my fault, my mind has been a little... occupied."

    mc normal "Oh..."

    na "You follow Mio's line of sight to… a rose? She tripped on a rose?"

    na "All of a sudden, Mio turns to face you with a surprising intensity in her eyes."

    mio "[mcname], do you... do you..."

    mio "Oh no! The posters!"

    na "Mio rushes to grab the posters off the ground, and brushes them off carefully. It isn't until now that you notice the intricate lettering and detailed visuals. It's clear that a lot of love was put into them."

    mc normal "Sorry! Did you make those?"

    mio "Yeah..."

    mc normal "They're beautiful! It sounds like you do a lot of work, but you must really love the student council."

    na "Mio blushes furiously and her eyes roam back to where the rose still sits."

    mio "It's not the student council… I… well, it's nothing."

    menu:
        "\"It's okay, you can talk to me\"":
            jump s93
        "{i}Don't push into it{/i}":
            jump s94

 
label s75:
 
label s76:
 
label s77:

label s78:

label s79:

label s80:

label s81:

label s82:

label s83:

label s84:

label s85:

label s86:

label s87:

label s88:

label s89:

label s90:

label s91:

label s92:
    
label s93:

    mc normal "It's okay, you can talk to me."

    mio "I-- well..."

    mio "Ever since I was little, I've dreamed of meeting my “Prince Charming”… and until recently I never thought I'd find him."

    mio "You know... someone handsome and kind who actually cares about me."

    mio "But when I met Yutaka it was almost like destiny."

    mio "Of course, a lot of girls like him-- but for some reason I have this hope that one day he'll choose me."

    mio "And until then... I don't mind being \"Cinderella\"."

    mio "I believe that if I work hard in the student council and persist where others failed, he will someday return my feelings."

    mio "I'll have someone to cherish and be cherished by."

    mio "...To be honest [mcname], you scare me."

    mio "Now that most of the student council has graduated and the election is coming up, more people will join. Yutaka won't have to rely on me anymore."

    mio "I-I know we just met, but please tell me..."

    mio "What should I do?"

    menu:
        "\"Tell him before it's too late!-- like right now!\"":
            jump s95
        "\"Wait and see how it plays out\"":
            jump s96
        "\"Uhh... I also like Yutaka\"":
            jump s97

label s94:

label s95:

    mc normal "Tell him your feelings of course!"

    mc normal "How do you expect anything to happen if you never let him know?"

    mio "Wait! B-but--{nw}"

    mc normal "In fact, let's go find him right now!"

    na "You grab Mio's hand and sprint through the halls back to the student council room."

    mio "R-running in the halls isn't allowed!"

    na "As you and Mio are about to turn the last corner, you hear a sudden thud.  The two of you peek around the corner 
        to find Yutaka talking to a girl slumped against the wall with a pink letter. Talk about bad timing."

    # Whispering
    mio "Oh, it's the previous vice president! She graduated last year... what's she doing here?"

    jt "Beautiful girls like you shouldn't cry... but I'm afraid I can't return your feelings."

    sg "But... but you said you liked me! You even just said I was beautiful! Ever since you entered Gwetome, I've liked you and worked my butt off for you. How could you say such a thing?!"

    jt "Ha! You claim to \"like\" me... {color=#b0b0b0}{size=-6}whatever that means...{/color}{/size} yet you know nothing about me, do you?"

    mio "!!!"

    jt "Whatever romance you had imagined is just a projection of your idiocracy."

    jt "I would never look twice at someone who decides to worship me just because of my looks."

    sg "But--{nw}"

    jt "I'm sorry to tell you this Senpai… but you no longer have value to me now that you've graduated."

    jt "We had fun while it lasted though, didn't we?"

    sg "{i}{color=#b0b0b0}{size=-6}{cps=10}*sobs*{/cps}{/size}{/color}{/i}"

    na "As the girl bolts out of the hallway, you turn to look at Mio who seems to be... blushing?"

    # Whispering:
    mio "This whole time I never realized... how lonely Yutaka is."

    # Whispering (loudly)
    mc normal "HUH?!"

    mio "Thanks for helping me find my courage, [mcname]."

    na "Before you can say anything, Mio steps around the corner and reveals herself to Yutaka."

    mio "Yutaka!"

    jt "Huh? Oh-- Mio."

    jt "I guess you saw all that, hm? That's too bad... you've been such a hard worker too."

    jt "If you want to quit, the application fo--{nw}"

    mio "No! I-I don't care if you use me."

    jt "Huh?"

    mio "I want to be by your side Yutaka! I know now that your actions, your words, have carried no weight… and I can't say I'm much different from the old Vice President... but I want to try!"

    mio "Although this side of you is new to me, it does not deter me... or my feelings."

    mio "I want to know you for who you are!"

    jt "..."

    jt "I... I guess I wouldn't mind that."

    na "Thanks to your dating expertise and fully intentional guidance, Mio and Yutaka start dating."

    na "Their unexpected yet beautiful romance quickly becomes the talk of the school, and your matchmaking skills make you a local celebrity."

    na "You become known as the \"Campus Cupid\"... a respectable title for a respectable matchmaker."

    na "You continue to help lonely hearts find love for the rest of your high school career, and even later become the godparent of Mio and Yutaka's child!"

    na "Who needs love when you're the one shooting the arrows?"

    jump e13

label s96:

label s97:

label s98:

label s99:

label s100:

label s101:

label e0:

label e1: # Joe falls in love with the lifeguard
    
label e2: # Date Joe (pending name)

label e3: # Castaway with Joe

label e4: # Love you too
    
label e5: # All is fair in Love and War

label e6:

label e7:

label e8: # Date Maryam (pending name)

label e9:

label e10:
    
label e11: # Big Apple Juice

label e12: # Love in the Basket

label e13: # The Archer of Love

label dice_roll:
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d10 = renpy.random.randint(1, 10)
    $ d20 = renpy.random.randint(1, 20)
    return

label fight:

    $ player_hp = 10
    $ enemy_hp = 10
    $ player_attack_value = 0
    $ enemy_attack_value = 3
    $ enemy_attack_value -= 1

    scene bedroom
    show jt cocky

    while player_hp > 0 and enemy_hp > 0:

        # Player Turn - two choices!
        call dice_roll

        menu:
            "Flirt":
                #call camera_knight_attack
                if d10 >= 8:                                                # 30%
                    $ player_attack_value = d4 + d6
                    $ enemy_hp -= player_attack_value
                    mc scared "That's scary!" with hpunch
                    #TODO: add to script??
                    "Yutaka took [player_attack_value] damage!"          # 70%
                else:
                    $ enemy_hp -= d4
                    #show side gwyn suit scared 
                    mc scared "[d4] damage!" with hpunch
            "Punch":
                #call camera_knight_attack                       
                if d10 >= 9:                                                # 20%
                    $ player_attack_value = (d6 + d4)*2
                    $ enemy_hp -= player_attack_value
                    "Critical Hit! Yutaka took [player_attack_value] damage!"
                elif d10 >= 5:                                              # 40%  
                    $ player_attack_value =  d6 + 2                                        
                    $ enemy_hp -= player_attack_value
                    "That's a strong hit! Yutaka took [player_attack_value] hp!"
                else:                                                       # 40% 
                    "You miss!"                                      
        
        if enemy_hp <= 0:
            #call camera_knight_win
            "You win the combat encounter!"
            #jump harder_menu

        # Enemy Turn - Semi-randomized behavior!

        call dice_roll

        if d20 >= 19:                                            # 20%       
            #call camera_skeleton_attack                                                                                
            $ player_hp -= d10
            "The Yutaka makes a wild attack for [d10] damage!"
        elif d20 <=2:                                            # 20%
            $ enemy_hp += d4
            if enemy_hp < enemy_max_hp:
                "The Yutaka heals itself, raising [d4] hp!"
            else:
                $ enemy_hp = enemy_max_hp
                "The Yutaka fully heals itself back to full hp!"
        else:                                                    # 60%
            #call camera_skeleton_attack                                                                                
            $ player_hp -= d4
            "The Yukata attacks for [d4] damage!"

    #call camera_knight_died
    "You died..."
    hide screen hp_bars_1v1

    menu harder_menu:
        "Play this level again?":
            $ player_hp = player_max_hp
            $ enemy_hp = enemy_max_hp
            jump harder_battle
        "Back to Main Menu":
            jump start

        





        










return