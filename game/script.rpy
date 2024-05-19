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
        ypos 10
        xpos 4
        0.5
        "images/star2.png"
        zoom 0.28
        ypos 10
        xpos 4
        0.5
        repeat

transform e:
    ycenter 1000
    xcenter 960
    alpha 0.0

    ease .06 ycenter 916 alpha 0.2

    ease .05 ycenter 832 alpha 0.4

    ease .04 ycenter 748 alpha 0.6

    ease .04 ycenter 664 alpha 0.8

    ease .04 ycenter 580 alpha 1.0
    alpha 1.0
    ycenter 580
    
transform bar:
    alpha 0
    ease .06 xcenter -960
    alpha 1
    ease .05 xcenter -576
        
    ease .04 xcenter -192
        
    ease .04 xcenter 192
   
    ease .04 xcenter 576

    ease .04 xcenter 960


transform left:
    ease .06 xcenter 900
    ease .05 xcenter 800
    ease .04 xcenter 700
    ease .04 xcenter 600
    ease .04 xcenter 500

transform right:
    ease .06 xcenter 1000
    ease .05 xcenter 1100
    ease .04 xcenter 1200
    ease .04 xcenter 1300
    ease .04 xcenter 1400

transform centerL:
    ease .06 xcenter 500
    ease .05 xcenter 600
    ease .04 xcenter 700
    ease .04 xcenter 820
    ease .04 xcenter 960
    
define ex = Dissolve(0.1)

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
    
    bgSong = "bgm_skipABeat.mp3"

    sfxBell = "hoshibucks_bell.mp3"
    hoshibucksSong = "bgm_hoshibucks.mp3"

    config.auto_voice = "voice/{id}.mp3"

    quizWords = ["Environment", "Tradition", "Influence"]
    quizAnswers = ["かんきょう", "でんとう", "えいきょう"] #quizAnswers = ["環境", "伝統", "影響"]
    quizWord = quizWords[renpy.random.randint(0,len(quizWords) - 1)]
    quizCorrect = quizAnswers[quizWords.index(quizWord)]
    quizGuess1 = quizAnswers[renpy.random.randint(0,len(quizAnswers) - 1)]
    quizAnswers.remove(quizGuess1)
    quizGuess2 = quizAnswers[renpy.random.randint(0,len(quizAnswers) - 1)]
    quizAnswers.remove(quizGuess2)
    quizGuess3 = quizAnswers[renpy.random.randint(0,len(quizAnswers) - 1)]

    projectScore = 0

    ririname = "..."
    mcname = "..."
    joename = "..."
    jtname = "..."
    sophianame = "..."
    maryamname = "..."
    mioname = "..."

    ririname_kanji = ""
    mcname_kanji = ""
    joename_kanji = ""
    jtname_kanji = ""
    sophianame_kanji = ""
    maryamname_kanji = ""
    mioname_kanji = ""

    metRiri = False
    metJoe = False
    metJt = False
    metSophia = False
    metMaryam = False
    metMio = False

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
    define mother = Character("Mom", show_name = "お母さん", ctc="ctc_blink", what_outlines = dialogue_outlines)
    define teacher_e = Character("Sensei", show_name = "先生", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define mio = Character("[mioname]", show_name = "[mioname_kanji]", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)

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

    define riri = Character("[ririname]", show_name = "リリ", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True) # define riri = Character("リリ")
    define mv = Character("Mysterious Voice", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define mi = Character("Mysterious ikemens", show_name = "イケメンたち", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)

    define ff = Character("Delinquent 1", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define d1 = Character("Delinquent 1", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define d2 = Character("Delinquent 2", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define d3 = Character("Delinquent 3", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define s1 = Character("Student 1", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define s2 = Character("Student 2", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define s3 = Character("Student 3", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define mg1 = Character("Mean girl 1", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define mg2 = Character("Mean girl 2", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    define sg = Character("Sullen Girl", ctc="ctc_blink", what_outlines = dialogue_outlines, bold = True)
    
    style character_text:
        outlines [
        (0, "#6529233d", 2, 2),
        (2, "#65292318", 3, 3),
        (1, "#6529230e", 4, 4)
    ]
        

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
    mother "PLACEHOLDER"
    return

label riri:
    show choice
    show riri normal at e
    if riris[10]:

        riri "Yay! You did it! I'm so proud of you Naninani. Okay... let's see your options..."

        riri "Your teacher is really mad right now. If you went to class you'd definitely receive that anger."

        riri "But... if you skip class you could find yourself in a battle for your very fate."

        riri "Ooooh spicy. You know which one I would choose. {i}Wink. Wink.{/i}"

        $ riris[10] = False
    elif riris[11]:

        riri "Hehehehe..."

        $ riris[11] = False
    elif riris[14]:

        riri "Follow your gut, Naninani!"

        $ riris[14] = False
    elif riris[15]:

        riri "You {i}have{/i} to go to that party Naninani! 'Kay?"

        $ riris[15] = False
    elif riris[26]:

        riri "Look at this cutie-patootie! Maybe you don't have to go to that party Naninani."

        riri "The choice is yours... though I am a fan of Chiba-kun myself... hehehehehe..."

        $ riris[26] = False
    elif riris[27]:

        na "{i}[[Riri shakes her head. It looks like she doesn't want to talk to you right now.]{/i}"

        $ riris[27] = False
    elif riris[28]:

        riri "The drama! As the main character, you {i}must{/i} pick at least one of them!"

        riri "Don't let the temptation of the forbidden fruit fool you!"

        $ riris[28] = False
    elif riris[24]:

        riri "Hey, Naninani, he's really asking you on a date!"

        riri "I never thought you'd make it this far... It truly brings tears to my eyes!"
        
        riri "Anyways, you HAVE to go with him! For me <3"

        $ riris[24] = False
    elif riris[44]:

        riri "Wow, did you really just ask him on a date?!?! All by yourself??"

        riri "I knew you could do it! They grow up so fast..."

        $ riris[44] = False
    elif riris[46]:

        riri "That's a tough one..."

        riri "Either way will bring you two closer, right? So, I'll let you decide this time..."

        $ riris[46] = False
    elif riris[29]:

        riri "If you go to the basketball game, Chiba-kun is totes falling for you!"

        riri "Partying is fine too though I guess..."

        $ riris[29] = False
    elif riris[33]:

        riri "Poor Chiba... Oh well, this means even more love routes!"

        $ riris[33] = False
    elif riris[35]:

        riri "Oooh, you like the bad ones, huh?"

        $ riris[35] = False
    elif riris[37]:
        
        riri "If you go get drinks with Isamu, you'll find yourself in a world of broken doors, crime, and... {i}cats?{/i}"

        riri "I mean, that's basically your only option... right? Right?"

        $ riris[37] = False
    elif riris[47]:

        riri "What an unexpected twist!"

        riri "Come on, Naninani! He's the love of your life, your soulmate! You must save him!"

        $ riris[47] = False
    elif riris[53]:

        riri "You need to be more explorative! Maybe this girl on the poster is actually your soulmate!"

        $ riris[53] = False
    elif riris[57]:

        riri "Maybe we should just give the, the benefit of the doubt? But why would they have your ring and not give it back? Hmmm..."

        $ riris[57] = False
    elif riris[60]:

        riri "How strange... let's test them to see if they know the password!"

        $ riris[60] = False
    elif riris[63]:

        riri "We can always just do the project another dayyy..."
        
        $ riris[63] = False
    elif riris[65]:

        riri "You could call the cops, but the culprit is already long gone..."

        $ riris[65] = False
    elif riris[34]:

        riri "CHIBA-KUN WANTS TO GO SOMEWHERE ELSE?!?! JUST THE TWO OF YOU?!?! AAAAAAAAAA GO NANINANI GOOO!"

        $ riris[34] = False
    elif riris[36]:

        riri "Look at you go!"

        $ riris[36] = False
    elif riris[75]:

        riri "A fight would be fun..."

        riri "But wait, no, Yutaka won't like it if you cause a huge fight!"

        riri "Think about his feelings, and just let this play out peacefully!"

        $ riris[75] = False
    elif riris[92]:

        riri "Dang it name, I told you he would be mad!"

        riri "But, he did seem pleased that you went that far for him... hehe!"

        riri "If you accept his forgiveness and change now, you can still have a chance!"

        riri "Come on now, what are you waiting for? Do it!"

        $ riris[92] = False
    elif riris[94]:

        riri "Why are you looking at me?"

        riri "This time it's your decision, okay?"

        $ riris[94] = False
    elif riris[30]:

        riri "{i}{color=#b0b0b0}{size=-6}{cps=10}*gasp*{/cps}{/size}{/color}{/i}"

        $ riris[30] = False
    elif riris[13]:

        riri "Follow your gut, [mcname]!"

        $ riris[13] = False
    elif riris[51]:

        riri "Hey, why are you looking at me?"

        riri "Come on now, you should know this..."

        $ riris[51] = False

    else:
        na "{i}[[It doesn't look like Riri has anything to say right now.]{/i}"

    python:
        for i in range(numscenes):
            del(riris[i])
            riris.insert(i, False)
    
    hide riri with ex
    #hide choice

    return
# -------------------------------------------------------------------------------------------------------------------
# s1 = start
# voice voice.mp3

label start:
    stop music

    pause 0.7
    na "Welcome. We're glad you could make it. Again. Weirdo. Who are you anyway?"

    $ mcname = renpy.input("What is your name?")
    $ mcname = mcname.strip()
    $ mcname = mcname[0:13]
    if mcname == "":
        $ mcname = "Naninani Nantoka"
        #何とか、何々

    na "Ah, got it. Hi, [mcname]. Welcome to Gwetome Academy, where this story-- your story-- is continuing into its second year of high school. A new year of love, lust, and violent tendencies."

    na "What route will you choose?"

    jump s51

    scene bedroom

    pjmc shy "{i}{color=#b0b0b0}{size=-6}{cps=10}*yawn*{/cps}{/size}{/color}{/i} I'm so tired... I stayed up all night playing otome games."
    
    pjmc ecstatic "It`s hard not to when you`re given so many choices, especially when you can punch the male leads. Hehehe!"

    pjmc scared "Oh wait! I forgot to introduce myself. My name is{u} [mcname]!{/u}"

    pjmc normal "I'm sixteen. Today is my first day of my second year at Gwetome Academy."

    pjmc normal "Ever since my family moved back to Shizuoka, I've been living my high-school life to the fullest."

    pjmc normal "During my time here, I've come to learn that love isn't the only important thing in life."

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
    show mother normal at e
    mother "Good morning! I made you breakfast since I knew you'd wake up late."

    mother "Dad's already left to go work on his new Food Network episode and I'm heading out now. Have fun at school! I'm off!"

    hide mother with ex

    #TODO: Door close noise

    mc ecstatic "Thanks, have a good day!"

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

    #TODO: Bed sheet noise
    scene black
    na "You crawl into your covers again and begin to sleep blissfully; everything is cozy, warm, and peaceful. You begin to dream."

    na "It's your first day of school at Gwetome Academy. Everyone is calling you Naninani Nantoka. 
        But why? You've always been [mcname] haven't you? How strange."

    na "Just as you are about to investigate this, you feel a sudden shake." with hpunch

    scene bedroom
    show mother angry at e
    mother "Hey!...Hey! Get up! How did I end up with such a lazy child?"

    show mother normal
    mother "[mcname], school's already started so you need to hurry! I'm off to work now, so I can't help you. I'm off!"

    hide mother with ex
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

    show joe normal at e
    joe "Ah sorry, I was walking kind of slow. Are you ok?"

    show joe ecstatic
    joe "A lot of people bump into me so my back muscles have become hard like metal. My doctor said it's because I tend to draw people in... I'm magnetic."

    show joe embarrassed
    joe "Heh. Sorry, I'm rambling. Anyways, I'll just uh... keep walking."

    hide joe with ex
    na "The mysterious ikemen runs his hand through his hair cooly and starts to saunter away."

    na "Your heart is beating fast; you don't know if it's because of his dazzling looks or possible metal poisoning."

    na "Either way, you should probably get to school. The question is: How?"

    menu:
        "{i}I'll take the journey alone!":
            jump s8
        "{i}Try to talk to the ikemen":
            jump s9

label s5:

    $ metRiri = False

    na "The TV has summoned you and you must answer its call. As you sit down on the couch, you see the familiar face of the main character, Kimura Takeshi."

    na "It looks like he's having a serious talk with the Kiss Kiss Love Power Team, a magical-girl group that saves the world from evil monsters."
    
    na "During the last episode, Takeshi was deciding whether or not to keep his office job or pursue his dream of becoming a full-time magical girl. 
        He must be discussing this with them now."

    mi1 "Takeshi... you must make a choice. If we wait any longer, the Dr. will find out your true identity. Either join us or leave us."

    pp "Pyun!"

    takeshi "But--{nw}"

    mi2 "Takeshi, we {i}meow{/i} it's a hard decision, but it's one that must be {i}mwade.{/i} {color=#b0b0b0}{size=-6}nya~{/size}{/color}"

    takeshi "But... but... what if I'm not cut out to be on the Kiss Kiss Love Power Team? 
        What if I'm not a real magical-girl? If I fail... I can't ever return. Please, give me more--{nw}"

    #explosion/crash + helicopter sounds
    #PyunPyun falls

    na "{color=#b0b0b0}{size=-6}*explosion noise*{/size}{/color}" with hpunch

    pp "Pyuuuuuuuuuuun~"

    mi1 "NO! PYUNPYUN!"

    #Through a megaphone:

    dr "HUEHUEHUEHUEHUE! I will defeat you all one by one!"

    na "Man, they kept the annoying mascot from season 1."

    na "Just as the Dr. begins to shoot his sadness missiles at the Kiss Kiss Love Power team, your phone buzzes."

    mc concerned "Huh?"

    na "Suddenly, a tiny sexy witch emerges out of your phone."

    mc scared "Mark Zuckerberg?!"

    
    $ ririname = "Riri"
    $ ririname_kanji = "リリ"
    riri "Wrong! I'm Riri. My boss told me there was a weeb here so I came to help."

    riri "Wait! Are you Naninani Nantoka!?!?"

    mc normal "Uh. No. I'm [mcname]."

    riri "Oh how the great have fallen. {i}{color=#b0b0b0}{size=-6}{cps=10}*sigh*{/cps}{/size}{/color}{/i} I used to always hear about you at work--"

    riri "you were determined to get a lover by the end of the school day. On your first day of school! You were my hero... But now... {i}{color=#b0b0b0}{size=-6}{cps=10}*cries*{/cps}{/size}{/color}{/i}"

    mc normal "Ummm..."

    riri "Well no matter Naninani! I'll help you get back on your feet and into the world of romance once again. Let's go!"

    mc normal "Ummmmmmmmm..."

    menu:
        "{i}Go to school... late":
            jump s10

label s6:

    mc scared "Ah! I've done it now!"

    na "You quickly throw on your uniform, grab a piece of toast, and run out the door."

    scene neighborhood
    mc scared "I'm gonna be late!"

    na "It isn't long before you find yourself turning a sharp corner... with toast... hmm..."

    mc flirtyjoke "Ah! It hurts!" with hpunch

    mc concerned "...?"

    mc concerned "Is no one... here?"

    na "Wow, you must be really off your game today [mcname]. You look around yourself, stunned... this has never happened before."

    na "How could you not bump into a hot ikemen while turning a corner with toast in your mouth?!?! Maybe you should try again."

    na "You pick up the toast and start walking back to where you started, when you hear a strange noise."

    joe "{i}Kyaa~!{/i} I'm gonna be late!"

    na "Ah, there it is. You look up and see a hot... pole? No wait! You shake your head to clear your vision."

    show joe concerned at e
    #TODO: Joe special scene
    joe "Sorry, are you ok? I don't know what came over me. I just felt a sudden need to run around that corner."

    mc shy "Yeah, I'm alright."

    na "The boy's eyes sparkle as you take his hand and he smoothly pulls you to your feet. Nice."

    $ joename = "Joe Kun"
    $ joename_kanji = "くん・ジョー"
    $ metJoe = True

    show joe ecstatic
    joe "The name's Joe. I'll see ya!"

    hide joe with ex
    na "After you both apologize you quickly continue on your way."

    jump s10

label s7:

    na "Heh... school. Who needs it? You're about to discover the answer to the greatest mystery yet: who is Naninani Nantoka?!"

    scene black
    na "You rustle back under your blankets, close your eyes, and start to dream again... but this time you are not at school."

    na "You are floating through an endless void. You can't move. You can't breathe. All is silent."

    na "Is this what it's like to be in a world with no love? No romance? No {i}ikemens?{/i}"

    na "Your mind succumbs to the darkness."

    mv "..."

    mv "You have failed your purpose, [mcname]."

    na "..."

    scene bedroom
    na "By the time you wake up, the school year has already ended. You now know your true duty but it is too late, and there is no one left to love you."

    na "Weeping, you succumb to the darkness of sleep once more."

    scene black
    jump e0 #Eternal Power Nap

label s8:

    scene gate
    na "You keep walking to school alone and eventually end up at the front of the school."

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
    mc normal "Oh... kay, sorry! I didn't see you there."

    show joe scared
    joe "Really? I'm quite hard to miss, you know..."
    
    mc normal "Is that so? Anyways, what is your name?"

    $ joename = "Joe Kun"
    $ joename_kanji = "くん・ジョー"
    $ metJoe = True

    show joe ecstatic
    joe "Oh right! The name's Joe-kun, but you can just call me Joe."

    na "His name is... kun?"

    mc normal "Well, nice to meet you! My name is [mcname]"

    show joe normal
    joe "Wow, what a cool name! I'm jealous."

    show joe ecstatic
    joe "I'm just an average Joe, you know? Hahaha!"

    na "Seriously, laughing at your own jokes? This guy..."

    mc concerned "Ha... well, which way are you heading?"

    show joe normal
    joe "Oh, I've got class this way. It was nice talking to you, see you around!"

    hide joe with ex

    menu:
        "{i}Walk to school":
            jump s8

label s10:

    $ metRiri = True
    scene gate
    
    na "You arrive at school... late of course."

    na "What did you expect? After all that you'd still be early? Hah."

    na "Now [mcname]...  you have two options..."

    if metRiri:
        
        show choice
        show riri surprised at e
        riri "What's this?! Two options of potential love and beauty?!?!"

        show riri ecstatic
        riri "Ahhhh I can't wait for you to turn back to your old self again!"

        show riri normal
        riri "Listen, Naninani, I have the power of insight."

        riri "I can help guide you through this love journey."

        riri "But... you need to be the one making the decisions. Got it?"

        show riri happy
        riri "I'll just be over here, and if you need my input just click on me."

        show riri normal
        riri "Hehe... hehehehehe..."
        hide riri with ex

        if metRiri:
            $ riris[10] = True
            

    menu:
        "{i}Go to class late":
            jump s11
        "{i}Skip!":
            jump s12

label s11:

    na "Skipping class? It looks like you value your education..."

    scene classroom1 day
    na "You walk to class and fling open the door."

    na "You're here in order to learn! You must study! You have your whole life ahead of you and you're not backing down!"

    mc ecstatic "Excuse me!"

    sensei "Detention!"

    if metRiri:
        $ riris[11] = True
    
    menu:
        "Go to detention":
            jump s13
        

label s12:

    na "Yea, who needs school anyways? If they really wanted you to be there, they'd make the start of school later than 8:30 AM."

    jump s18

label s13:

    scene detention day
    na "Ahhh... detention. A land of hopes and sorrows... youth and forgotten dreams."

    na "Somehow you always seem to find yourself here."

    na "You scan the room in order to find familiar faces, but suddenly your attention is caught by the piercing eyes of another student."

    na "They seem to be staring you down."

    na "Oh wait, now they're blinking at you. Or are they winking... with both eyes? Is that morse code?"

    na "Suddenly you hear the whispers of two delinquents a desk over."

    $ sophianame = "Isamu Takao"
    $ sophianame_kanji = "高尾・勇"
    $ metSophia = True

    show d1 happy at e
    d1 "Hey hey, is that Takao Isamu?"

    show d1 happy at left
    show d2 normal at e
    d2 "Takao... Isamu?"

    show d1 normal
    d1 "You don't know? Their family is yakuza! Apparently they transferred in this school year but haven't said more than two words to anyone. They're super cold."

    d2 "Ohhhh, yeah yeah I know them. {i}The Panther{/i}, huh? I heard they sleep with their eyes open because they have so many enemies."

    show d2 happy
    d2 "They're also rich, hot, have a six pack, and like to brood all the time."

    show d1 sad
    d1 "Wow... I wish I was that cool."

    hide d1 with ex
    hide d2 with ex
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

    na "You make a scene. How could you resist after all?"

    na "After throwing a few delinquents out the window with your super muscular muscles..."

    na "...Takao Isamu swaggers up to your desk."

    show sophia normal at e
    sophia "Yo."

    mc flirtyjoke "Oh, hey."

    sophia "You dropped this."

    na "Isamu hands you a small handkerchief with a small cute cat print on it."

    mc shy "Oh, that's not mi--{nw}"

    show sophia cocky
    sophia "Keep it."

    hide sophia with ex
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

    na "What a waste, they even winked at you!"

    na "Well, anyways... You decide to wait out detention. Maybe it was a bad idea to interact anyways."

    # After school

    scene hallway night
    na "Man, it was your first day and you got {i}detention{/i}. Honestly, I'm impressed."

    #TODO: Earthquake rumble

    na "Whoa! What was that?! It felt like an earthqua-{w=0.2}{nw}" with hpunch

    na "...Oh. It was you? Wow, you must be hungry."

    na "You happen to spot a Hoshibucks. It'll be a pretty penny, but a Caramel Ribbon Crunch Frappe sounds pretty good right about now."

    jump s24


label s17:

    na "Yutaka scolds you for skipping class."

    na "After some thinking, you decide that this treatment isn't fair in the slightest!"

    na "Maybe you want to skip class? He shouldn't be able to stop you! This is a free country!"

    mc angry "I refuse! {i}You{/i} shouldn't be able to send me back to class!"

    mc angry "What are you doing out of class, huh? I'll make {i}you{/i} go back!"

    show jt thinking
    na "Yutaka stares at you for a moment, then a small grin appears on his face."

    show jt calculating
    jt "Ah, people like you are my favorite!"

    jt "What {i}I{/i} do while at school does not matter to you, understand me? I am the president of the student council!"

    show jt cocky
    jt "{i}You{/i} have to listen to me, and {i}I{/i} am in charge. That is how it works, and how it always will."

    na "Who does this guy think he is?"

    mc sad "That's just not fair!"

    show jt normal
    jt "Oh, but my dear girl, {i}life{/i} is not fair. I am simply getting you ready for reality."

    na "I want to punch {i}\"reality\"{/i} into his face! It would have been better if you chose to fight him."

    show jt calculating
    jt "Anyways, I like you, so I will let you off easy this time."

    show jt cocky
    jt "Just detention. Consider yourself lucky."

    mc scared "Hey!"

    show jt normal
    jt "Don't make me angrier now. Welp, See you around!"

    na "Yutaka turns and walks away confidently. Man, what a prick!"

    na "You pick up the detention slip that he slid in your pocket and reluctantly read it."

    mc sad "Right after school? This is the worst! Whatever, I better go..."

    jump s13

label s18:

    scene hallway day
    na "As you're wandering the halls, you notice a student walking your way. He seems to be dressed very nicely, even for the prestigious Gwetome Academy."

    na "Wait, that's the student council president! You're in trouble if he finds you out here."

    menu:
        "{i}Hide behind a corner!":
            jump s18_1
        "{i}Pshh, what is he gonna do?":
            jump s18_2

    label s18_1:

        #TODO: Rose snap noise (?)
        na "As you tip-toe over to the corner of the hallway, you accidentally step on a very conveniently placed rose."

        jt "How'd a rose get in here?"

        na "Busted..."

        jump s18_3

    label s18_2:

        na "You stand confidently in the center of the hallway as he walks towards you."

        jump s18_3

    label s18_3:

        show jt amorous at e
        jt "What's a pretty looking girl such as yourself doing around these parts?"

        show jt concerned
        jt "Wait, what's a student doing in the halls? ...I'm terribly sorry, but you're gonna have to go back to class."

        mc scared "Nonono, I just--{nw}"

        show jt thinking
        jt "--Needed to go to the bathroom and got lost in the halls, I've been there."

        show jt ecstatic
        jt "Well, you're not going anywhere without a hall pass. How about we bring you back to class to get one?"

        menu:
            "{i}Sure, I should probably head back":
                jump s21
            "{i}No, I don't think I will!":
                jump s17
            "{i}This guy deserves a punch!":
                jump s18_4
                
    label s18_4:

        hide jt with ex
        na "As you start to turn around to walk back to class, you swiftly turn back and drive your fist into the student's face. Nice." with hpunch

        na "Uh oh, he got back up? Looks like it's time for a fight!"

        jump fight #TODO: Make sure fight scene works

label s19:

    scene hallway day
    na "You throw a powerful punch, flying him across the room. He won't be bringing you back to class again anytime soon." with hpunch

    na "You hear a feeble voice as you walk away."

    jt "Wait-- please... You don't need to do this!"

    mc cocky "Heh... I knew that CrossFit membership would pay off."

    jump s20

label s20:

    scene gate
    na "Word quickly spreads about how you punched the student council president and skipped class as you proudly walk out the front gates."

    mc normal "Man, that fight really took a lot out of me. I could really go for a Caramel Ribbon Crunch Frappe right about now."

    jump s24

label s21:

    mc shy "{i}Oh shoot, I forgot to grab one{/i}! Sure, let's head back."

    scene classroom1_day
    na "You walk back to class to get a hall pass, even though you never needed one. But right as you grab it, the bell rings."

    show jt cocky
    jt "Awww, well that's a shame. Well hey, at least we have the same class next period!"

    mc concerned "Oh, nice! Wait, how did you know that we had the same class?"

    show jt normal
    jt "I just checked the class roster! It's the job of the student council president to know their fellow students' names, after all."

    show jt ecstatic
    jt "C'mon, we have English class next. Let's go!"

    jump s51

label s22:

    scene hallway day
    na "You release a powerful punch aimed right at Yutaka!"

    na "...and miss. Well, that's embarrassing."

    mc shy "Oh... oops."

    show jt cocky at e
    $ jtname = "Yutaka Yanai"
    $ jtname_kanji = "柳井・豊"
    $ metJt = True
    jt "Ahahha, how cute! You really think you stand a chance against me? I am the one and only student council president, Yutaka!"

    mc shy "Uhm... okay?"

    show jt calculating
    jt "You've been naughty now, haven't you?"

    jt "You think you can walk free after trying  to hurt the most important student in the school?"

    show jt concerned
    jt "No! I will not let this stand! Off to counseling with you!"

    na "How dramatic can this kid get..."

    mc cocky "Alright fine, I'll go to counseling. Sorry for trying to punch you, but it was too hard to resist."

    show jt embarrassed
    jt "Hey! Wait, don't say that about me!"

    hide jt with ex
    na "You turn and go to counseling. You can feel Yutaka fuming behind you, but you keep walking without a care in the world."

    jump s25

label s23:

    scene black
    na "While Yutaka continues to monologue your heart begins to sink."

    na "You think of Mio... has everything she's felt, worked for, and loved... been for a persona?"

    na "Have hundreds of girls' feelings been manipulated just to move forward an agenda?"

    na "Your hands shake at the thought of it."

    #TODO: Shattered glass noise
    scene student_council
    na "In a frenzied panic you grab Mio's jacket and look for the nearest exit: the window, and before you know it you're flying through the air with shattered glass as your wings." with hpunch

    scene gate
    na "As soon as you double somersault handspring onto the grass you start sprinting."

    na "You can hear Yutaka yelling behind you but it doesn't matter-- you must tell Mio."

    #TODO: Check if this is right neighborhood for mio
    scene neighborhood
    na "As you turn onto the road of her family's restaurant you quickly spot her walking outside."

    mc scared "Mio!"

    show mio scared at e
    mio "[mcname]?! What are you doing here?"

    mc shy "I... I..."

    mc normal "I brought you your jacket."

    mio "B-but I said you could give it to me tomorrow!"

    mio "You didn't have to come all this way!"

    show mio embarrassed
    mio "...Huh? Why is there glass all over it?"

    mc concerned "Well. there's also this other thing."

    scene black
    na "You explain everything to Mio: finding the jacket, getting locked in the room with Yutaka, his true nature... everything. And jumping out the window. That too."

    scene neighborhood
    show mio scared at e
    mio "Wow... I can't believe it."

    show mio embarrassed
    mio "How could I be this silly, [mcname]."

    show mio sad
    mio "So I'm just... I'm just a tool to him?"

    mc concerned "I think we all are Mio..."

    hide mio with ex
    na "As Mio tries to hold back shaky sobs you pull her into a tight hug."

    show mio scared at e
    mio "T-thank you for t-telling me, [mcname]."

    show mio happy
    mio "You're the first good friend I've had in a w-while."

    mc shy "I'm sorry about all this..."

    show mio scared
    mio "D-don't be!"

    na "Mio hastily wipes her tears and looks into your eyes."

    show mio lecturing
    mio "Don't w-worry about me!"

    show mio normal
    mio "I'm sure I'll find my \"Prince Charming\" one day... hehe."

    mio "In the meantime, let's just enjoy highschool."

    mc ecstatic "Together!"

    show mio happy
    mio "Yes... Together!"

    scene black
    na "Soon after, the two of you quit the student council, and start a European culture club that studies the history, etiquette, fashion, and culture of the continent's nations."

    na "Although the club starts small, Mio's expert management skills and your creativity allow the club to thrive-- eventually warranting the attention of a news station and later a small European monarchy."

    na "After months of correspondence and negotiation, the club is eventually invited to visit the nation."

    na "It is there that Mio meets her real life \"Prince Charming\" and you discover your natural talent for riding horses. Lots of horses."

    na "The two of you fall so deeply in love with the nation that after graduating you both immediately move to its fairytale-like countryside."

    na "Mio marries the kind prince, and you are dubbed the palace's cavalry knight of honor."

    na "A new beginning in a beautiful kingdom-- together."

    na "Who needs the student council? Am I right?"

    jump e15


label s24:

    #In hoshibucks

    stop music
    play sound sfxBell
    pause 0.5
    scene hoshibucks
    play music hoshibucksSong

    na "You enter the Hoshibucks and step up to the bartender."
    
    show beckham hoshibucks normal at e
    mc ecstatic "I'll take your finest Caramel Ribbon Crunch Frappe, please."

    na "You felt like you've seen this kid before. Maybe from school?"

    show beckham hoshibucks ecstatic 
    beckham "that'll be 2,210¥."

    mc scared "Wh-{nw}"

    # Saying yen amount loudly
    na "-Wait, 2,210¥?? What has this world come to..."

    hide beckham with ex
    na "Failing to hold back spending one fourth of your monthly allowance on a single Frappe, you swipe your card and watch as the barista skillfully crafts your drink."

    scene hoshibucks
    na "You imagine what the flavor will be as you grab the cup and walk away from the front counter."

    mc normal "It looks so good! I'll worry about the cost later, because this is gonna be so worth i--{nw}"

    #TODO: Crash noise

    mc scared "NOOOO! MY CARAMEL RIBBON CRUNCH FRAPPE!!" with hpunch

    na "Well, that's rough. After you witness-- with pure agony--  the drink spill on the floor, you then look up to see... a pole? And an attractive one at that."

    na "Wait, who would put a pole in the middle of a Hoshibucks? The pole reaches out a hand to you."

    #TODO: Special shot with joe and his hand out towards camera in hoshibucks (?)

    show joe scared at e
    joe "Are you okay?! I'm so sorry, I didn't see where I was going."

    if metJoe:
        show joe ecstatic
        joe "Hey, I remember you!"
    
    show joe normal
    joe "Drinks from Hoshibucks are expensive nowadays."

    joe "Here, let me pay for it. It was my fault anyways."

    mc ecstatic "No, it's okay! Don't even worry about it, It didn't cost {i}that{/i} much."

    na "You're still a bit irritated due to the fact that it {i}did{/i} in fact cost that much."

    show joe ecstatic
    joe "No no no, please, let me! I'd feel bad if I didn't."

    show joe normal
    mc ecstatic "No no no no, I wasn't looking where I was going."

    joe "No no n-{nw}"

    #TODO: Rumble noise
    show joe scared
    na "{b}Enough with the “no no no” talk!{/b}" with hpunch

    $ joename = "Joe Kun"
    $ joename_kanji = "くん・ジョー"
    $ metJoe = True
    show joe normal
    joe "Well, anyways, my name's Joe. Nice to meet you! I'm gonna buy a drink for myself anyways, so I'll get us both one."

    mc normal "I'm [mcname], nice to meet you!"

    scene hoshibucks
    na "You let him buy you another Caramel Ribbon Crunch Frappe and have a nice chat at one of the tables."

    show joe ecstatic
    joe "Hahaha, you're so funny!"

    na "You didn't even say anything..."

    show joe normal
    joe "Well, anyways, It's getting kind of late. Mind if I take you home?"

    mc shy "Hmmm... It {i}is{/i} getting kind of dark out..."

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

    show beckham normal at e
    beckham "If you don't go to school, you won't find success. You need to try your best everyday."

    mc sad "Okay..."

    show beckham angry
    beckham "Why did you think punching a classmate was a good idea? Do you realize what could happen?"

    mc sad "He was being a bully, I needed to do something."

    show beckham confused
    beckham "That was a dumb thing to do. You were such a good student last year, I'm sorry that I have to do this..."

    mc scared "Wa--What?"

    show beckham angry
    beckham "{cps=6}{b}GO TO DETENTION!{b}{/cps}" with hpunch

    jump s13

label s26:

    na "Actually... does it even matter if it's a date? It's a party! Of course you're going!"

    na "You carefully put the handkerchief and note in your bag and begin to daydream."

    scene black
    mc normal "{i}I wonder who's going to be there... I'll have to make lots of friends! Maybe I should try something new to make a good impression...{/i}"

    #TODO: Door noise
    scene detention day
    mc scared "Eh? Akimitsu?!" with hpunch

    na "Chiba Akimitsu, your childhood friend since third grade appears at the desk next to yours."

    show kyle confident at e
    kyle "Hey [mcname]! Ahaha, did I surprise you?"

    mc normal "Mhm! Why are you also in detention?"

    show kyle loving
    kyle "I knew you'd be here on the first day so I came to keep you company."

    show kyle normal
    kyle "What were you thinking about before I interrupted you?"

    mc shy "Nothing much... just this party..."

    na "You take out the handkerchief and note and show Akimitsu."

    na "His eyebrows furrow into a look of concern."

    show kyle scared
    kyle "A party with... the {i}PANTHER{/i}??? TAKAO ISAMU???"

    show kyle concerned
    kyle "There's no way I'm letting you go alone, [mcname]. A party with yakuza attending? Absolutely not."

    mc concerned "What are you... my dad?"

    show kyle confused
    kyle "I'm just worried about you! Who knows what those people are like?"

    show kyle loving
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

    scene hallway night
    show d2 normal at e
    d2 "That's [mcname] isn't it?"

    show d2 normal at left
    show d3 normal at e
    d3 "Oh, you're right! I can't believe she'd reject Takao-sama's kind offer!"

    show d3 normal at right
    show d1 normal at e
    d1 "Weirdo..."

    show d2 sad
    d2 "Even after they used their special kitty handkerchief too!"

    show d1 sad
    d1 "{i}{color=#b0b0b0}{size=-6}{cps=10}*gasp*{/cps}{/size}{/color}{/i} No way!"

    show d3 angry
    d3 "It's true... I saw them outside weeping with it in their arms. It was their favorite handkerchief and it got dirty!"

    d1 "Poor Takao-sama..."

    hide d1 with ex
    hide d2 with ex
    hide d3 with ex
    na "You walk through the halls with shame. When you get home you can only find comfort in the soft light of your television."

    if metRiri:
        $ riris[27] = True
    
    jump s43
        

label s28:

    scene walkway
    na "Soon, night falls. You arrive at the party with Akimitsu and head inside."

    scene party
    na "The party is surprisingly classy. Everyone is dressed nicely, there's a live jazz band, and even an open apple juice bar. You make a mental note of the apple juice bar."

    na "You quickly see Takao Isamu spot you and even slightly move their lips upward."

    na "You can't tell if they're grimacing in pain or perhaps attempting a smile, but either way it's directed towards you."

    na "Akimitsu tenses up and steps closer to you."

    $ sophianame_kanji = "高尾・勇"
    $ sophianame = "Isamu Takao"
    $ metSophia = True
    
    show sophia party normal at e
    sophia "Hey. I've heard a lot about you, [mcname]. I'm Isamu Takao."

    show sophia party happy
    sophia "When I first saw you I wasn't sure the rumors were true, but now I know. You're incredible. What dojo did--{nw}"

    show sophia party happy at left
    show kyle party angry at e
    kyle "Youseikan. We trained at Youseikan."

    show sophia party concerned
    sophia "Ah... Who's this?"

    pmc normal "This is my childhood friend, Chiba Akimitsu."

    sophia "Is that so? Interesting."

    show sophia party flirty
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

    show kyle scared
    na "..." with hpunch

    kyle "Actually... wait..."

    mc concerned "Huh?"

    show kyle concerned
    kyle "Ahhh, sorry. I have a basketball game after school."

    show kyle confused
    kyle "He says, \"Hey, turns out we're in the finals now because some person with bleached blonde hair just showed up and beat up the team that we lost to.\""
    
    show kyle normal
    kyle "He was saying something about [mcname], you, and a party. Weird, huh?"

    mc shy "I wonder who that could be..."

    show kyle ecstatic
    kyle "Right? Well now I can't miss my basketball game... would you mind coming to watch instead?"

    if metRiri:
        $ riris[29] = True

    menu:
        "\"Sure, I'll watch\"":
            jump s14
        "\"I'd rather party\"":
            jump s33

label s30:

    smc normal "The party's good.{nw}"

    na "You say, proceeding to turn and face Akimitsu."

    smc concerned "Hey... should we get going?"

    show sophia party concerned
    sophia "Wait. Would you like to get drinks with me?"

    na "{i}{color=#b0b0b0}{size=-6}{cps=10}*Narrator gasps*{/cps}{/size}{/color}{/i}"

    if metRiri:
        $ riris[30] = True

    menu:
        "\"You know what? Sure.\"":
            jump s35
        "\"No, I have plans with Akimitsu\"":
            jump s36

label s31:

    pmc normal "The party's good.{nw}"

    na "...you say. And then you run and escape to the apple juice bar."

    #Bar scene

    scene party
    pmc flirty "Apple juice please~"

    show beckham bartender normal
    beckham "May I ask what type of apple you prefer? Honeycrisp? Fuji?"

    pmc shy "Umm... Gala please."

    show beckham bartender shake
    beckham "Coming right up."

    scene black
    na "Never before have you tasted such a sweet, succulent drink."

    na "You down glass after glass until your tummy can take it no longer. Delicious."

    na "Then you go home."

    if metRiri:
        $ riris[27] = True
        
    menu:
        "Go home":
            jump s43

label s32:

    pmc normal "The party's good."

    pmc shy "I just wish I was being escorted by someone since I've been so lonely by myself."

    show sophia party flirty
    sophia "Want me to help you?"

    show kyle party sad
    kyle "Hey, hey... wait. [mcname], please."

    show kyle party loving
    kyle "Don't do this... let's just get drinks. Just the two of us."

    na "{i}{color=#b0b0b0}{size=-6}{cps=10}*Narrator gasps*{/cps}{/size}{/color}{/i}"

    menu:
        "\"Sounds good to me!\"":
            jump s34
        "\"No thanks, I'm going with Isamu\"":
            jump s37

label s33:

    na "You shake your head solemnly"

    pmc concerned "Sorry, Akimitsu. I changed my mind. The party never stops."

    show kyle sad
    kyle "But you just said we would han--{nw}"

    # Door closes

    scene black
    na "You leave."

    scene hallway day
    show kyle scared at e
    kyle "Wait! Wait! If you're that determined to go to the party I'll go with you. I'll skip my game."

    show kyle loving
    kyle "Let's just go together, okay?"

    if metRiri:
        $ riris[33] = True
        
    jump s28

label s34:

    pmc normal "Ah, okay! Sounds good to me."
    
    show kyle party normal
    show sophia party sad
    na "Akimitsu lets out a deep breath as Isamu silently slips away into the crowd."

    hide sophia with ex
    kyle "Whew... I thought you were going to ditch me for a second."

    show kyle party ecstatic
    kyle "Wanna go find that open apple juice bar again?"

    scene party
    na "After finding the bar and getting your apple juice, the two of you begin to reminisce."

    na "You think about the dojo and your childhood."

    na "How Akimitsu has always been there for you, even writing letters to you after you moved away."

    na "He hasn't changed a bit has he? It's almost like this whole time he's been waiting for you..."

    show kyle party normal at e
    kyle "Hey... it's getting a little stuffy in here. Wanna go somewhere else?"

    if metRiri:
        $ riris[34] = True

    menu:
        "{i}Leave with Akimitsu":
            jump s40

label s35:

    pmc ecstatic "Sure!"

    show kyle party scared
    kyle "What?? Wait... what?!?!"

    show sophia party happy
    sophia "Heh. Let's go then."

    if metRiri:
        $ riris[35] = True
        
    menu:
        "{i}Go get drinks with Isamu":
            jump s38

label s36:

    pmc normal "I'm good. I was planning to spend time with Akimitsu tonight."

    show sophia party angry
    na "Isamu glares coldly at you both."

    sophia "Hmph."

    show kyle party loving
    kyle "I actually... was also thinking of getting drinks with you, [mcname]."

    if metRiri:
        $ riris[36] = True

    menu:
        "\"Sounds good to me!\"":
            jump s34

label s37:

    pmc normal "Sorry~ I've already got plans."

    pmc normal "I'll see you later Akimitsu!"

    show kyle party sad
    kyle "But..."

    show kyle party angry
    kyle "Actually, fine. Do what you want. I don't care."

    hide kyle with ex
    na "Akimitsu storms off. His hot fury combined with his blazing looks briefly set another guest on fire, but the flames are doused quickly with some apple juice."

    show sophia party flirty
    sophia "Heh. Let's drink something ourselves too."

    if metRiri:
        $ riris[37] = True
        
    menu:
        "{i}Go get drinks with Isamu":
            jump s38
        "Actually... I'm good":
            jump s39

label s38:

    scene party
    na "As you and Isamu start to go towards the bar you hear a brief shattering sound."

    # Shattering noise

    pmc normal "Ah. I think Akimitsu may have accidentally kicked the door down."

    pmc ecstatic "That's a bad habit of his. He tends to do it when he leaves houses."

    show sophia party happy at e
    sophia "Don't we all?"

    pmc cocky "Hey! Bartender! Get me your most appley apple juice."

    hide sophia with ex
    show beckham bartender shake at e
    beckham "Of course."

    scene black
    na "After hours of discussing fighting techniques and the best way to throw someone out a window, you run out of apple juice."

    scene party
    scene beckham bartender confused
    beckham "I'm sorry, we don't have any more apples to juice. It's a true tragedy for which I am very sorry Takao-sama."

    hide beckham with ex
    show sophia party normal
    sophia "Eh, whatever. Hey, [mcname], wanna take break outside? It stinks of granny apples here anyway."

    pmc normal "Sure."

    scene black
    na "The two of you step outside."

    scene balcony sophia
    na "You find yourself on a balcony overlooking Shizuoka."

    na "The wind softly blows through your hair and the lights of the city sparkle in the distance."

    show sophia party concerned
    sophia "To be honest... I didn't think you'd come with me."

    pmc scared "Huh? Why?"

    show sophia party normal
    sophia "My family is yakuza. Ordinary people are usually too afraid of getting hurt. But you're... different."

    show sophia party happy
    sophia "When you threw those three delinquents out the window you reminded me of my cat, Skull Crusher."

    show sophia party flirty
    sophia "And I love cats... and I love... you."

    pmc shy "I... I like you too."

    scene black
    na "Soon after Takao Isamu's confession the two of you start dating."

    na "It's a surprisingly healthy and loving relationship-- you meet {i}The Family{/i}|, go on lots of dates, and work through conflicts together."

    na "Eventually you decide to open a cat cafe together... but... it is no ordinary cat cafe."

    na "Through years of discipline and training, blood and tears, your cat cafe becomes the base for a new group of cat yakuza: {i}Nyanken{/i}."

    na "It is through Nyanken that you wage the Great Cat War, rise through the ranks, and become the most powerful yakuza couple in the nation."

    na "No one can stop your bulging muscles or your untouchable love!...  {i}{color=#b0b0b0}{size=-6}{cps=8}Nya~{/cps}{/size}{/color}{/i}"

    jump e5

    # not done

label s39:

    na "Romance? {i}{color=#b0b0b0}{size=-6}{cps=10}*scoff*{/cps}{/size}{/color}{/i} That's for weaklings."

    na "You don't need any of these weirdos, you just came for the party."

    na "But the party sucks so..."

    mc normal "Actually... I'm good."

    show sophia party embarrassed
    sophia "...Huh?"

    scene black
    na "You flip your hair and strut out the door."

    scene walkway
    na "As you walk you radiate power and confidence. Is this the power of self-worth?"

    na "In fact, the aura from your strut is so strong that it catches the attention of a modeling agent."

    show beckham agent normal at e
    beckham "Wait! I'm a modeling agent who also likes attending high school parties hosted by yakuza. You should join my agency! You're incredible!"

    mc normal "Okay."

    scene black
    na "And that was how your modeling career began."

    na "You dropped out of high school, moved to New York, and started your legacy by modeling for Elle, Versace, and Vogue."

    # Visual of "magazines pop up on screen"

    na "You became surrounded by fame and fortune, but soon it became too much."
    
    na "Burdened by the pressure of stardom, you started looking for a way to relieve the stress."

    scene party
    na "You thought back to that night... that party... and how you didn't get to try that apple juice."

    scene black
    na "Now you wanted it... you needed it... and eventually you succumbed to it."

    na "You spent all your money on apple juice, only drank apple juice, and only cared about apple juice."

    na "You threw away your career, friends, and life for apple juice."

    na "Everything you had... became apple juice."

    jump e11

label s40:

    scene black
    na "The two of you leave the party and walk to a nearby park."

    scene park night
    na "The air is chilly but the stars are shining clearly and brightly."

    show kyle party loving at e
    kyle "Let's sit down for a little bit. There's a bench over there."

    pmc ecstatic "Okay!"

    # Switch to bench

    scene park night
    show kyle party confused at e
    kyle "..."

    pmc shy "..."

    kyle "..."

    pmc normal "It's really cold out here."

    show kyle party concerned
    kyle "Maybe we shouldn't have sat down."

    pmc normal "Yeah, that was kind of stupid."

    show kyle party confused
    kyle "..."

    pmc shy "..."

    show kyle party confused
    kyle "Do you want my jacket?"

    pmc shy "No it's okay, you can keep it."

    show kyle party embarrassed
    kyle "Oh. Uh, okay."

    pmc shy "..."

    kyle "..."

    pmc shy "..."

    show kyle party concerned
    kyle "Have you ever wondered what the stars would say if they could talk?"

    pmc ecstatic "Haha, n--{nw}"

    show kyle party normal
    kyle "I think they'd tell us the world's secrets. Why we're here, what we're meant to become, and how we might get there."

    show kyle party concerned
    kyle "Sometimes I feel lost. Like I'm just falling through time with no real purpose."

    show kyle party happy
    kyle "But there are moments when this light reaches out to me."

    kyle "It tells me that I have something to give. That I have something to offer to this cold world."

    kyle "This light tells me to keep going, keep trying, and keep living."

    show kyle party loving
    kyle "And I've found [mcname], that it's when I'm with you that this light is most prevalent."

    kyle "You're like my star, [mcname]. And that's why... I love you."

    pmc shy "I..."

    jump e4

label s41:

    mc normal "No thanks, I can make it by myself. Nice meeting you though!"

    show joe sad
    joe "Oh okay... I guess I'll see you later then."

    hide joe with ex
    na "You had to get home quick anyways. You haven't been catching up on this season's anime!"

    scene neighborhood
    na "You dart out of the Hoshibucks, not even thanking him for buying your drink before leaving. Bold."

    jump s43
 
label s42:

    mc normal "Sure, why not? I live just 10 minutes down the road."

    show joe ecstatic
    joe "Perfect! I'm going the same direction. Come on, let's get moving!"

    scene black
    na "You leave the Hoshibucks with Joe."

    scene neighborhood
    na "It almost looks like you two are going on a date, hehe!"

    na "Alright now, what will you talk about for maximum romance?"

    menu:
        "{i}Talk about Hoshibucks":
            jump s44
        "{i}Talk about hobbies":
            jump s45
 
label s43:

    # At home

    scene kitchen
    na "You sit down in front of your television to watch anime."

    na "For some strange reason you feel empty and alone, like there is a dark hole in your heart."

    na "Maybe it's because Fanana Bish is on? You change the channel."

    pjmc normal "Ahh... that's better. Now I can go on with my day and never have to worry about romance agai- {i}{color=#b0b0b0}{size=-6}{cps=10}*yawn*{/cps}{/size}{/color}{/i}"

    pjmc shy "Suddenly... {color=#b0b0b0}I feel... {cps=15}{size=-6}very... {size=-8}{cps=5}sleepy.{/cps}"

    na "In the corner of your eye you see a tiny magic wand waving at you from behind the couch. Is that..."

    if metRiri:

        show choice
        show riri normal at e
        riri "It's me, Riri. Don't worry Naninani, I'm just making some minor adjustments to the fabric of time."

        show riri happy
        riri "You may have failed this time at romance, but I won't let you give up!"
    
    pjmc scared "Eh?! What's going on?"

    #TODO: Loading screen (?)

    jump start
 
label s44:

    mc normal "So, do you go to Hoshibucks often?"

    show joe ecstatic at e
    joe "Yes! In fact, I go almost every day after school! I live for Hoshibucks, haha!"

    mc ecstatic "Wow, that's cool! I like Hoshibucks, but I don't go very often because it's so expensive."

    show joe concerned
    joe "True..."

    show joe normal
    joe "Well, if you don't go to hoshibucks often, what do you do in your free time?"

    mc normal "Well, other than studying and extracurriculars, I like going to to the beach."

    show joe ecstatic
    joe "Really? Me too! It's such a nice way to unwind after a long day."

    na "I think this guy just wants something to do with you... he probably spends all day in Hoshibucks."

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

    show joe confused at e
    joe "Well, other than going to hoshibucks, I guess I go to the beach sometimes."

    mc ecstatic "Really? Me too! I love the beach."

    show joe enamoured
    joe "Is that so? It's such a nice way to unwind after a long day, right?"

    mc ecstatic "Right? The water feels so nice, especially in the summer."

    show joe ecstatic
    joe "Well, if you're ever free, we should go to the beach together."

    na "Wow, I didn't see that coming! What a slick way to ask you out..."

    mc ecstatic "Okay, sure! How does tomorrow sound?"

    show joe concerned
    joe "{color=#b0b0b0}{size=-5}I guess I can go one day without my caramel frappe... for [mcname]...{/size}{/color}"

    show joe ecstatic
    joe "Sounds good! I'll be looking forward to it! {i}{color=#b0b0b0}{size=-6}{cps=10}*wink*{/cps}{/size}{/color}{/i}"

    if metRiri:
        $ riris[44] = True

    menu:
        "Go to the beach!":
            jump s46
        
    
label s46:

    scene black
    na "The next day, you and Joe make plans to go to the beach together."

    na "The way he talks to you... I think he likes you, ya know!"

    na "Anyways... After school, you meet up with Joe at the beach."

    show joe suit ecstatic at e
    joe "Hey, [mcname]! It's nice to see you again. You look good!"

    na "Well, that was fast."

    smc ecstatic "Oh, thanks! Nice to see you too!"

    show joe suit concerned
    beckham "Ehem, lovebirds!"

    show joe suit confused
    joe "Excuse me?"

    show joe suit confused at left
    show beckham lifeguard normal at e
    beckham "Sorry to interrupt, but the currents are very strong today."

    na "This guy {i}again?{/i}"

    beckham "I recommend staying out of the water, for your own safety."

    show beckham lifeguard ecstatic
    beckham "Rest assured, I can save you, of course, but please be careful. Have a good day at the beach!"

    show joe suit normal
    hide beckham with ex
    joe "Oh, okay. What do you think, [mcname]? Should we still swim?"

    if metRiri:
        $ riris[46] = True
        
    menu:
        "{i}Go swimming! That lifeguard can't stop me!":
            jump s47
        "{i}Walk on the beach instead":
            jump s48
 
label s47:

    smc normal "Let's go swimming! That's what I came here for."

    show joe concerned
    joe "Alright, as long as you're careful. I don't want you to get hurt."

    smc ecstatic "Oh, I'll be fine! I'm more worried about you, hehe!"

    show joe suit embarrassed
    joe "Hey! I'm a great swimmer, I promise!"

    smc flirty "If you say so!"

    na "Enough flirting! I'm skipping to the part where you actually swim."

    # Switch to water

    scene beach
    na "Ahh, finally... but wait, is Joe okay?"

    show joe suit scared at e
    joe "Hey, I can't touch the ground here! I'm getting pulled out! Someone save me!!!" with hpunch

    joe "I'll admit it, I don't go to the beach very often! I prefer caramel frappes, okay!? {i}{color=#b0b0b0}{size=-6}{cps=10}*crying*{/cps}{/size}{/color}{/i}"
 
    if metRiri:
        $ riris[47] = True 
    
    menu:
        "{i}The lifeguard can deal with it":
            jump s49
        "\"Don't worry, I'll save you!!\"":
            jump s50

label s48:

    smc normal "Maybe we should just take a walk on the beach for today."

    show joe suit normal
    joe "Okay, sounds good. I'd love to take a walk together."

    # MC Blushes
    smc embarrassed "We'll have other opportunities to go swimming together anyways..."

    na "Aww, look at you two!"

    scene beach
    na "You take a nice walk and talk about various things, from hoshibucks, to school, to more hoshibucks, and eventually..."

    show joe suit embarrassed at e
    joe "You know, name, there's something I should tell you..."

    smc shy "Yes?"

    joe "Ever since I saw you in hoshibucks, I've thought you are the most beautiful person I've ever seen."

    # Whispering:
    show joe suit confused
    joe "{color=#b0b0b0}{size=-5}Maybe even more beautiful than a caramel frappe...{/color}{/size}"

    show joe suit concerned
    joe "But, anyways, I want you to know that..."

    show joe suit enamoured
    joe "I think... I love you."

    na "How adorable."

    smc shy "Joe... I think I love you too."

    show joe suit embarrassed
    joe "You've lightened up my life since we met..."

    na "As in yesterday?"

    show joe suit enamoured
    joe "And I want you to be the light in my life forever."

    # Gwyn giggles
    smc flirty "I can do that..."

    na "Aww, what a cute couple you make. Good job [mcname]!"

    jump e2

label s49:

    scene beach
    na "You wave your arms until the lifeguard notices Joe struggling."

    na "He rushes out to save Joe!"

    na "He doesn't seem to be paying attention to you though..."

    #TODO: Beckham and Joe Cutscene (if lucy finishes drawing)
    na "You manage to make it to shore safely, and see the lifeguard performing CPR on an unconscious Joe."

    smc shy "I've never seen someone perform CPR, but doesn't that seem a little... much?"

    na "Joe gasps and opens his eyes. He seems weirdly... happy to see the lifeguard above him."

    show joe suit enamoured at e
    joe "Thank you, you saved my life! I'll... do anything to repay you~"

    na "Joe and the lifeguard stare into each other's eyes for what seems like minutes..."

    na "Something is definitely off."

    show joe suit enamoured at left
    show beckham lifeguard normal at e
    beckham "Well, there's only one thing I want..."

    joe "What? I'll do anything!"

    show beckham lifeguard flirty
    beckham "All I want right now... is you."

    hide beckham with ex
    hide joe with ex
    na "The two close their eyes and engage in a long, drawn out kiss."

    na "Wow... really long... seriously, are they just trying to rub it in?"

    na "You sit there, utterly shocked. Really, is there anything else you can do?"

    smc normal "Is this what I get for not saving you, Joe?"

    show joe suit sad at e
    joe "I'm sorry, [mcname]..."

    na "Well, that's that, I suppose..."

    jump e1
 
label s50:

    smc scared "Don't worry Joe, I'll save you!"

    na "Despite your best efforts, you end up both getting swept away by the current."

    scene beach
    show joe suit sad at e
    joe "I'm so sorry, [mcname]. This is all my fault..."

    smc sad "It's okay... I don't want to live if it's without you."

    na "How romantic."

    show joe suit concerned
    joe "[mcname]"

    smc shy "...?"

    show joe suit enamoured
    joe "I... love you."

    show joe suit concerned
    joe "I need you. You are the light in my darkness, the sand on my beach, and..."

    show joe suit sad
    joe "The caramel crunch whipped cream on my caramel frappe."

    show joe suit enamoured
    joe "You are everything to me, [mcname]."

    na "Wow, this guy really has a way with words."

    show joe suit scared
    na "But, before, you can respond, you are knocked unconscious by a huge wave." with hpunch

    scene black
    na "Is this how you die?"

    na "..."

    na "Just kidding. You wake up on a deserted island with Joe laying by your side."

    # Opens eyes

    scene island
    show joe suit enamoured at e
    joe "[mcname]! You're awake! I got this coconut for you. Please, drink from it!"

    show joe suit normal
    joe "Apparently, Hoshibuck's pink drinks are made with coconut milk, so I thought it must help."

    na "You can feel your burnt skin and pain all over your body, but the coconut does help."

    smc shy "Thank you, I feel much better. Where are we?"

    show joe suit confused
    joe "It's been a few hours since we washed up on this island. I don't know if anyone will ever come for us."

    smc flirty "Oh... well, we have each other, don't we?"

    na "You take Joe's hand and look into his eyes."

    show joe suit enamoured
    joe "Maybe, if I have you by my side everyday, I can live without hoshibucks."

    smc flirty "Aw, Joe..."

    na "{i}{color=#b0b0b0}{size=-6}{cps=10}*sigh*{/cps}{/size}{/color}{/i} There he goes again."

    scene black
    na "You live the rest of your lives together, surviving on the island and its natural resources."

    na "What a happy ending..."
    
    jump e3
 
label s51:

    # English class scene

    scene classroom1 day
    na "You arrive at your English class. You could have had something fun, like Japanese. But {i}English?{/i}"

    #TODO: Sitting down noise(?)
    na "You take a seat and get ready to listen to the teacher's lecture."

    na "Right when they start talking, you start feeling very tired. Perhaps a nap wouldn't be too bad..."

    na "You fall into a deep slumber, and dream of a high school life where {i}you{/i} are the main character."

    # Dream scene
    # TODO: Fadeout?
    scene dream with fade

    na "As you walk to the front gates of the school in your dreams, you notice four ikemens waving at you from one of the classrooms. They seem to be trying to say something."

    mi "{i}Heeeeey!!!{/i}"

    scene black with fade
    na "Heyyy..." # mi line

    #TODO: smack sound effect
    teacher_e "Hey, [mcname]!" with hpunch

    # Back to classroom scene

    scene classroom1 day
    na "Suddenly, you feel a sharp pain on your forehead. A piece of chalk then drops onto your desk."

    show teacher_e angry at e
    teacher_e "Would you like to come up to the board and answer the question?"
    
    mc shy "Uhhh... What question?"

    show teacher_e sad
    # $ metRiri = True
    teacher_e "{i}{color=#b0b0b0}{size=-6}{cps=10}*sigh*...{/cps}{/size}{/color}{/i} I have it written right here. What is \"[quizWord]\" in Japanese?"

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

    scene student_council
    na "You look around and see a well dressed and quite handsome student sitting in an important looking chair."

    mc ecstatic "{i}He must be the leader of the student council! I should ask him about signing up!{/i}"

    mc shy "Excuse me, sir?"

    na "The student looks up with a puzzled expression on his face."

    show jt ecstatic at e
    jt "Me? Wow, sir is a new one... Do I really look that good?"

    mc embarrassed "Oh, you're just well dressed is all..."

    show jt normal
    jt "Anyways, what do you need?"

    mc normal "Well, I saw the poster looking for people to join the student council, and I decided to check it out. Can I sign up?"

    $ jtname = "Yutaka Yanai"
    $ jtname_kanji = "柳井・豊"
    $ metJt = True
    show jt ecstatic
    jt "Of course! I'd be delighted to have you on our student council team. My name is Yutaka Yanai, nice to meet you!"

    na "Yutaka pulls out a book's worth of papers from his cabinet."

    show jt normal
    jt "All you have to do is sign all these documents, and then you can get started."

    mc scared "Oh wow, alright."

    scene student_council
    na "It takes the whole school day, but you eventually finish filling out all the documents."

    na "Besides some documents mentioning that the student council will have complete ownership of your loved ones, prized possessions, free time, and soul, you aren't worried about what you're signing up for."

    na "When you are finally done, you hand them all back to Yutaka."

    show jt ecstatic at e
    jt "Congratulations! You are now an official member of the student council. I'm excited to work together~"

    mc ecstatic "Thank you! I'll do my best!"

    na "Suddenly, the door opens and a mouse-like girl enters the room."

    $ mioname = "Mio"
    $ mioname_kanji = "みお"
    $ metMio = True

    show jt normal at left
    show mio embarrassed at e
    mio "P-please excuse the intrusion!"

    jt "Ah! Mio, please meet our newest member, [mcname]."

    na "Upon seeing you Mio freezes up, but then quickly nods an awkward smile."

    show mio normal
    mio "H-hello! I'm Mio..."

    mc normal "I'm [mcname]! I look forward to working with you."

    show jt concerned
    jt "It's a little embarrassing, but up until now it's been just Mio and I... most of the student council graduated last year."

    show jt cocky
    jt "Mio's a hard worker though! Isn't that right Mio?"

    show mio embarrassed
    mio "Yeah..."

    show jt ecstatic
    jt "Hey! Why don't the two of you take a walk around the campus? Mio can show you our daily patrol routines and responsibilities-- plus you can hang a few posters while you're at it."

    na "Walking behind his desk, Yutaka shuffles through a drawer and grabs a stack of hand-painted posters."

    na "As he gently drops them into your hands, you notice they advertise an upcoming student council election."

    show jt normal
    jt "Hopefully we'll get a bit more busy soon."

    jump s74

label s53:

    na "You have no idea what you're doing as you scribble a random vocabulary word you remember onto the board."

    teacher_e "No... not quite, [mcname]. Maybe studying in the library will help you out."

    teacher_e "You'll need someone to help you on the English project we will have too. Details will be posted in Google Classroom."

    na "Well that's embarrassing. After getting laughed at by the entire class, you decide to go to the library to work on your English skills."

    na "As you are about to enter the library, you notice a flier posted next to the door."

    $ maryamname = "Haruka Kiyama"
    $ maryamname_kanji = "木山・遥花"
    $ metMaryam = True

    na "\"Come over to my house at address here if you need help with English words like [quizWord] and English project work. -Haruka Kiyama\". Huh, that sounds exactly like what you need! Maybe a little too exactly..."

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

    show teacher_e happy
    teacher_e "That's correct [mcname], good job. It wouldn't look good if you got that wrong, that was one of the easier ones."

    na "You proudly walk back to your seat and listen to the rest of the lesson."

    show teacher_e normal
    teacher_e "Alright everyone, we are going to be starting an English project using the vocabulary we learned. Please get with a partner and make a video by this Friday."

    hide teacher_e with ex
    na "You instantly realize that getting with a partner brings up a big issue..."

    na "...you have no friends."

    na "You notice someone sitting in the back of the classroom. Wanna try grouping with them?"
    menu:
        "{i}Ask to group with them":
            jump s56
        "{i}\"Nah, I'm good\"":
            jump s55
 
label s55:

    na "You're gonna have to group with somebody..."

    na "Hey, look, someone's walking up to you!"

    $ jtname = "Yutaka Yanai"
    $ jtname_kanji = "柳井・豊"
    $ metJt = True

    show jt normal at e
    jt "Hey cutie, I'm Yutaka. Why don't we work together? It seems like everyone is already paired up."

    na "It most definitely does not seem like everyone is paired up... in fact you're getting stared down quite intently by a group of slightly scary girls."

    na "You take a second look at Yutaka. He has a kind and princely appearance yet there's a slight snobbishness about him. Or maybe it's tiredness?"

    na "You wouldn't be surprised if this was his last-ditch attempt at \"escaping\" a certain group of girls."

    na "Either way, you don't have much to lose... probably."

    mc normal "Oh, sure-- I'm [mcname]! What should we do for the skit?"

    show jt thinking
    jt "I don't have any ideas right now... want to come over to my place after school and we can decide then?"

    mc ecstatic "Oh, okay!"

    show jt ecstatic
    jt "Alright, it's settled then! Meet me at my house after school to work on it."

    # At Yutaka's house

    scene house sophia
    na "That afternoon, you head over to Yutaka's house."

    na "Well, more like Yutaka's {i}castle.{/i} This place is massive!"

    show jt cocky at e
    jt "Hey [mcname], welcome in! Make yourself at home."

    show jt normal
    jt "So, do you have any ideas?"

    menu:
        mc shy "For the genre, let's do a..."
        "Action":
            $ projectScore += 0
        "Drama":
            $ projectScore += 1
        "Romance":
            $ projectScore += 2
    menu:
        mc shy "And we can film at..."
        "The beach":
            $ projectScore += 2
        "The park":
            $ projectScore += 0
        "Yutaka's house":
            $ projectScore += 1
    menu:
        mc shy "And the actors can be Yutaka and..."
        "Yutaka alone":
            $ projectScore += 0
        "Me":
            $ projectScore += 1
        "My Jungkook photocard":
            $ projectScore += 2
    menu:
        mc ecstatic "We'll make the film's underlying message about..."
        "Smartphone addiction":
            $ projectScore += 2
        "Immigration":
            $ projectScore += 1
        "Sustainable fashion":
            $ projectScore += 0
    menu:
        mc ecstatic "And the background music can be..."
        "A slow ballad":
            $ projectScore += 2
        "The Magical Ikemen Intro Song":
            $ projectScore += 0
        "Indie-rock":
            $ projectScore += 1
    menu:
        mc normal "Finally, we'll edit it with..."
        "Subtitles":
            $ projectScore += 0
        "Slo-mo shots":
            $ projectScore += 1
        "Flower special effects":
            $ projectScore += 2

    show jt ecstatic
    jt "Alright, sounds good! Let's do it!"

    scene house sophia
    na "You spend hours with Yutaka, and eventually finish the project."

    show jt ecstatic at e
    jt "Whew! That's the last scene!"

    mc ecstatic "Yes! We did it!"

    show jt concerned
    jt "Well, I guess you should start heading back soon..."

    show jt thinking
    jt "It was... really fun to work together."

    show jt normal
    jt "I feel like I really got to know you today, cutie."

    show jt ecstatic
    jt "I appreciate it."

    mc ecstatic "Yeah! I had a lot of fun too. Well, see you tomorrow!"

    hide jt with ex
    na "Well, although Yutaka initially presents as snobby, he really is nice on the inside."

    na "And it seems like he {i}really{/i} cares about you... hehe!"

    na "Ahem, anyways, the next day in class..."

    if projectScore >= 8:
        jump s100
    else:
        jump s99

label s56:

    na "You walk up to the student's desk."

    show maryam normal at e
    mc normal "Hey, do you have anyone to group with?"

    show maryam nervous
    maryam "N-no!"

    mc ecstatic "Would you like to work together on this project?"

    show maryam normal
    maryam "S-Sure!"

    na "You realize that your room is a mess, you probably wouldn't want them seeing that."

    mc normal "can I come over to your house tomorrow to work on it?"

    show maryam happy
    maryam "Okay, that works for me!"

    # Next Day
    
    scene neighborhood maryam
    na "You knock on the door, and Haruka answers."

    show maryam normal
    maryam "Welcome. Make yourself at home. Let's go to my room."

    na "You both go upstairs and enter their room."

    jump s57

label s57:

    scene room maryam
    show maryam nervous at e
    maryam "I'm going to go get my English work from downstairs... stay here for a little."

    hide maryam with ex
    na "You sit down and get under the kotatsu positioned in the middle of the room."

    # TODO: Under the sheets noise
    mc normal "Aaa~ It's so warm~"

    na "As you look around the room, you can see many pieces of hanging tape on the walls surrounding their bed. Did they take those down recently?"

    na "Looking a bit more, you notice a small shiny object on the floor near the other side of the kotatsu."

    # Gwyn talking to herself

    mc concerned "Ooo~ shiny! Hmmm... Isn't this my ring that I lost? I thought it was gone forever!"

    mc angry "They found it and never gave it back?! So rude!"

    mc scared "Hold on a minute..."

    if metRiri:
        $ riris[57] = True
        
    menu:
        "{i}Maybe they were planning to give it back":
            jump s61
        "{i}Something's fishy around here...":
            jump s60
 
label s58:

    na "You walk up to the door of the address posted on the flier with no worries in your mind."

    scene neighborhood maryam
    na "You then hear some noises coming from the house, like someone is frantically trying to clean up."

    show maryam normal at e
    maryam "H- Hello... Are you here for the English lessons?"

    mc normal "Yep! I saw your flier next to the library!"

    maryam "A- Alright... Come on in..."

    na "As you walk inside, you see Haruka running up the stairs ahead of you. You reach the second floor and see a door slam shut down the hallway."

    # Knock knock

    mc normal "Hey, is everything alright?"

    maryam "Just one minute...!"

    na "You give them a minute, and they eventually open the door, silently signaling you to enter the room."

    jump s57
 
label s59:

    na "Yeah, it sounds a little too risky."

    mc normal "I think I'll just study alone in the library today..."

    na "You spend all day studying English in the library, until you are fully satisfied that you have memorized that word."

    mc normal "Finally! Ahh, I'm exhausted. Time to head home and watch some anime..."

    jump s43
 
label s60:

    mc concerned "Hey, I noticed the ring in your room looks familiar, where did you get it?"

    na "You notice that Haruka starts looking a little nervous."

    show maryam nervous
    maryam "...From a shop."

    mc ecstatic "Oh, haha! I must be wrong."

    na "You put the ring back on the kotatsu. You start feeling a little uneasy. Maybe working in the safety of your home would be a better idea."

    mc normal "Do you think we could go to my house to work tomorrow?"

    show maryam normal
    maryam "Yeah, sure..."

    # New day, at MC house

    scene kitchen
    na "Haruka arrives at your house, ready to work on the English project."

    mc ecstatic "Alright, let's get to work!"

    na "Haruka takes their computer out and starts typing right away."

    na "Hmmm... Maybe they're using a Hotspot? You've never given them your Wi-Fi."

    mc normal "Hey, do you need my Wi-Fi password? You don't have to use data."

    show maryam scared
    maryam "No-- I mean yes! Yes please!"

    mc concerned "Right... Could I have the computer to put it in?"

    show maryam nervous
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

    #TODO: Door noise

    show maryam happy at e
    maryam "Hey, I'm back. Do you have everything?"

    mc concerned "Yep! But why is nobody else here? I even arrived thirty minutes late."

    show maryam nervous
    na "You notice their eyes starting to drift away from you as they respond."

    maryam "Yeah uh... The English problem was pretty specific. Maybe there was j-just nobody else that needed help."

    show maryam normal
    maryam "Anyways... do you want to-{nw}"

    na "Haruka glances to the floor next to you."

    hide maryam with ex
    na "They quickly walk over to the other side of the kotatsu and sit down, grabbing the ring."

    show maryam happy at e
    maryam "Would you like to start?"

    mc ecstatic "Okay!"

    scene room maryam
    na "You and Haruka work through your English for hours until you finally feel confident about your skills."

    #TODO: MC Stomach Rumble

    show maryam normal at e
    maryam "You want to finish up? We could go eat something after."

    mc normal "Sounds good!"

    na "You and Haruka clean up and start to walk out the door to go eat."

    jump s62
 
label s62: #TODO: Repetitive scene?

    scene neighborhood maryam
    show maryam normal at e
    mc normal "Where would you like to go?"

    maryam "Have you been to Hoshibucks before?"

    mc ecstatic "Yes! I love Hoshibucks!"

    # In Hoshibucks

    scene hoshibucks
    na "In the Hoshibucks line, Haruka notices that they forgot their wallet."

    show maryam scared at e
    maryam "Oh no! I forgot my wallet!"

    mc ecstatic "It's alright, I'll buy you a sweet treat because you helped me so much with the English project!"

    na "Haruka's eyes widen, they are entranced by your generosity and kindness."

    show maryam happy
    maryam "Thank you so much, [mcname]!"

    na "As you both order the sweet treats and sit down, Haruka seems nervous as if they something important to tell you."

    show maryam nervous
    maryam "uhm... [mcname]... I have something to tell you..."

    mc normal "Yes, Haruka?"

    show maryam embarrassed
    maryam "I've liked you ever since we had art together freshman year of highschool!"

    na "You guys went to the same freshman class? How do they even remem--{w=0.2}{nw}"

    show maryam normal
    maryam "When you gave me your extra pencil right before the final test, I knew you were the one for me! Would you like to go on a date with me?"

    mc ecstatic "I would love to!"

    jump e8
 
label s63:

    na "You decide to test Haruka."

    mc cocky "Alright then, the password is 123456."

    na "the real password is actually 1234567... They couldn't possibly figure it o--{w=0.2}{nw}"

    show maryam normal
    maryam "Perfect! I connected! L-let's get to work shall we?"

    na "You go silent. How could they possibly know your Wi-Fi password?!"

    show maryam concerned
    maryam "[mcname], are you a-alright? You're awfully quiet."

    na "Your heart starts to race, Haruka has noticed your changed demeanor."

    mc normal "Ahaha actually, I don't feel very well at the moment, maybe we could continue another day?"

    maryam "Oh, alright, I see."

    hide maryam with ex
    na "Haruka hastily grabs their stuff and goes home. Anxiety is rushing through your veins, how could they have known your wifi password?!"

    # New day at school

    scene classroom1 day
    na "You and Haruka plan on finishing the project later that day, but then you notice a handsome figure approaching..."

    show kyle normal at e
    kyle "Hey naninani, I was wondering if you would like to come hang out with me after school... if you're not busy of course."

    show kyle normal at left
    show maryam nervous at e
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

    show maryam ecstatic
    maryam "I'm in. Let's finish this project!"

    na "The two of you get the project done early and decide to go get a sweet treat together."

    jump s62
 
label s65:

    scene park night
    na "After school, you and Akimitsu get Hoshibucks. After you order your drinks, the two of you walk around the town and stop at a quaint park."

    na "The trees are thick and the sun has gone down, the two of you are seemingly alone."

    show kyle embarrassed at e
    kyle "Uhm... [mcname], there has been something on my mind that I have wanted to tell you for a really long time now..."

    na "You turn around and look at Akimitsu, his face is flushed red but you can't tell whether he is blushing or if it's the cold breeze."

    mc concerned "What is it?"

    show kyle loving
    kyle "I have loved you ever since we were kids..."

    #TODO: Leaf crackle and bushes noises
    na "Just as Akimitsu confesses his love, you hear a leaf crackle and the bushes shake as if someone is in them and are shocked to hear Akimitsu's love confession!" with hpunch

    show kyle scared
    kyle "Who's there!"

    #TODO: Bushes noise
    na "The person in the bushes scurries deeper into them. The two of you look over to find a photo of the two of you from Hoshibucks and a knife!"

    na "Whoever was in the bushes has been stalking you guys all day!"

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
    
    scene black
    na "You tried, I guess. Unfortunately you spend the rest of eternity in Haruka's basement, doomed to a life of no sunshine..."

    na "You never learn your lesson, do you?"

    jump e7
 
label s73:
 
label s74:

    scene hallway day
    na "You begin walking the halls with Mio, putting up posters and talking about club duties. Although Mio seems meek she speaks with openness and discipline."

    show mio normal at e
    mio "I-if you see students skipping class please tell them to return immediately."
    
    show mio lecturing
    mio "Some of them will try to use the \"restroom excuse\" but I'm sure you won't fall for that... it's a bit of an obvious lie."

    mc ecstatic "Ha... yeah... who would ever--{nw}"

    show mio scared
    #TODO: Thud noise
    mio "Aah!" with hpunch

    hide mio with ex
    na "Suddenly you find yourself in a stupor, standing above Mio who has face-planted onto the ground."

    na "After processing what just happened, you quickly put down the posters."

    show mio sad at e
    mc scared "Are you okay?"

    show mio embarrassed
    mio "Y-yeah! I-it's my fault, my mind has been a little... occupied."

    mc shy "Oh..."

    na "You follow Mio's line of sight to... a rose? She tripped on a {i}rose{/i}?"

    na "All of a sudden, Mio turns to face you with a surprising intensity in her eyes."

    show mio normal
    mio "[mcname], do you... do you..."

    show mio scared
    mio "Oh no! The posters!"

    na "Mio rushes to grab the posters off the ground, and brushes them off carefully."
    
    na "It isn't until now that you notice the intricate lettering and detailed visuals. It's clear that a lot of love was put into them."

    mc scared "Sorry! Did you make those?"

    show mio normal
    mio "Yeah..."

    mc ecstatic "They're beautiful! It sounds like you do a lot of work, but you must really love the student council."

    show mio embarrassed
    na "Mio blushes furiously and her eyes roam back to where the rose still sits."

    mio "It's not the student council... I... well, it's nothing."

    menu:
        "\"It's okay, you can talk to me\"":
            jump s93
        "{i}Don't push into it{/i}":
            jump s94

 
label s75:

    scene classroom1 day

    mc shy "Yesterday was so embarrassing! I hope no one says anything..."

    na "I'm sure it'll be fine..."

    na "Don't mind everybody's staring... I'm sure your outfit today is just... really cute!"

    mc embarrassed "Oh no, what should I do??"

    na "Ah, look out!"

    show mg1 happy at e
    mg1 "Oh look, it's [mcname]!"

    show mg1 happy at left
    show mg2 happy at e
    mg2 "Oh nooo, don't be late to class now! Yutaka might give you an {i}extra scolding!{/i}"

    na "The girls look at each other and snicker deviously... they really think they're soo funny, huh?"

    mc embarrassed "It wasn't all my choice that our project ended up like that! He wanted it that way!"

    mc concerned "But seriously, why do you all care so much??"

    show mg1 sad
    mg1 "Oh, please sweetie, everyone knows you wanted it."

    show mg2 angry
    mg2 "Yeah, and you never stopped to think about how we feel! The whole school wants to be with the student council president!"

    mc embarrassed "{i}Student council president?! No wonder he's so popular!{/i}"

    show mg2 sad
    mg2 "It's not fair for some random new girl to swoop in and get his attention!"

    show mg1 angry
    mg1 "I bet you only asked him to work together because you knew how rich and popular he is! You used him for his money!"

    show mg1 sad
    mc sad "But he asked me..."

    show mg2 angry
    mg2 "Oh shut up, you just wanted to make us jealous!"

    show mg1 angry
    mg1 "You don't love him as much as we do!"

    na "This is getting a little out of hand..."

    na "It's time to settle this... but how?"

    mc shy "{i}Let me think...{/i}"

    if metRiri:
        $ riris[75] = True

    menu:
        "{i}Don't let those girls walk all over you! Get physical and fight back!":
            jump s76
        "{i}Well, I'm sure Yutaka will be here any moment now to resolve this commotion... it'd be best to be silent and tough it out...":
            jump s77

label s76:

    na "With determined rage, you expertly sucker punch one of those annoying stuck up ******!"

    #TODO: Thud noise
    hide mg1 with ex
    na "Oooh, right in the face!"

    na "Wow, that's a lot of blood... Jeez, did you break her nose?!"

    na "Whatever, I guess she had it coming..."

    mc angry "Stay away from me! I don't care what you think, but I didn't ask for any of this!"

    show mg2 sad
    mg2 "Oh my god, are you insane?! Sierra, are you okay??"

    show mg2 angry at left
    show mg1 angry at e
    mg1 "Ow, that hurt! What is wrong with you!"

    show mg1 sad
    show mg2 sad
    na "Suddenly, the expressions on the two girls' faces dramatically change, and they seem to be staring at something looming above your shoulder..."

    show mg1 sad at right
    show jt concerned at e
    na "Caught literally red handed, you turn around to see Yutaka, looking down on you with disappointment."

    mc scared "Y-Yutaka! This isn't what it looks like... They were blaming me of using you, and-{nw}"

    show jt thinking
    jt "Quiet."

    show mg1 happy
    mg1 "Oh thank goodness! Yutaka-Senpai, please help me!"

    show mg2 angry
    mg2 "She attacked us for no reason! She's deranged! Get her out of this school!"

    jt "{i}{color=#b0b0b0}{size=-6}We'll see about that...{/color}{/size}{/i}"

    show jt concerned
    jt "Girls, please calm down. Sierra and Brynja, head to the office and give your account to the principal."

    show jt thinking
    jt "As for you, [mcname], come with me. I want to hear what happened from your point of view."

    scene black
    na "Yutaka leads you to the student council room and sits you down across from him, all alone..."

    jump s92

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

    scene student_council

    show jt thinking at e
    jt "Tell me what happened."

    na "You explain to him everything that they said that led up to you punching the girl."

    na "He seems disappointed by your story. But somehow... amused?"

    show jt concerned at e
    jt "Okay, look. I appreciate you looking out for me, and respect the intention of standing up for yourself."

    jt "But seriously, no matter what happens, you cannot be violent."

    show jt thinking
    jt "If you want to continue being my companion, you need to learn to control yourself."

    na "His companion? I wonder what that means..."

    na "You sheepishly look at the floor, not sure how to reply."

    jt "[mcname], look at me. Can you do that?"

    if metRiri:
        $ riris[92] = True

    menu:
        "{i}Accept his forgiveness and promise to be more careful":
            jump s102
        "{i}Tell him he's not the boss of you!":
            jump s103
    
label s93:

    mc normal "It's okay, you can talk to me."

    show mio embarrassed
    mio "I-- well..."

    show mio normal
    mio "Ever since I was little, I've dreamed of meeting my \"Prince Charming\"... and until recently I never thought I'd find him."

    mio "You know... someone handsome and kind who actually cares about me."

    mio "But when I met Yutaka it was almost like destiny."

    show mio lecturing
    mio "Of course, a lot of girls like him-- but for some reason I have this hope that one day he'll choose me."

    mio "And until then... I don't mind being \"Cinderella\"."

    mio "I believe that if I work hard in the student council and persist where others failed, he will someday return my feelings."

    show mio normal
    mio "I'll have someone to cherish and be cherished by."

    show mio embarrassed
    mio "...To be honest [mcname], you scare me."

    mio "Now that most of the student council has graduated and the election is coming up, more people will join. Yutaka won't have to rely on me anymore."

    show mio normal
    mio "I-I know we just met, but please tell me..."

    show mio happy
    mio "What should I do?"

    menu:
        "\"Tell him before it's too late!-- like right now!\"":
            jump s95
        "\"Wait and see how it plays out\"":
            jump s96
        "\"Uhh... I also like Yutaka\"":
            jump s97

label s94:

    na "You decide not to push into the matter."

    na "After all, the two of you just met-- it might be rude to ask anything too personal."

    hide mio with ex
    na "You continue to walk the halls with Mio, putting up posters and talking about the student council."

    show mio normal at e
    mio "By the way [mcname], I'm a little curious... what's your campaign plan for the student council election?"

    mc embarrassed "Huh?"

    show mio scared
    mio "Ah! N-not that you need to tell me anything!"

    show mio embarrassed
    mio "Sorry for being so presumptuous... you probably want to keep it a secret."

    mc concerned "What? I haven't signed up to run in the election."

    na "Mio suddenly turns to you with a puzzled expression."

    show mio scared
    mio "What are you talking about? Of course you have!"

    show mio lecturing
    mio "When you joined the student council you signed away your soul, didn't you?"

    mc shy "Yeah..."

    mio "So, you must run in the election. Student council members' souls are bound by contract."

    mc scared "What?! What happens if I break the contract?"

    show mio embarrassed
    mio "..."

    show mio sad
    mio "...B-bad things..."

    mc concerned "Oh uh... okay?"

    na "I guess you have no choice but to run then..."

    na "Well, if you're being forced into this, better go big or go home, right?"

    show mio lecturing
    mio "Don't worry though, [mcname]. It shouldn't be too hard as long as you're not running for student council president."

    mc "..."

    mio "Yutaka is basically guaranteed that position with the whole school already supporting him..."

    show mio scared
    mio "T-that's not to say he doesn't deserve it though! He's smart and kind and handsome, and um... um..."

    na "Second or nothing! Am I right?"

    na "To vice president stardom we go!"

    show mio lecturing
    mio "A-anyways! If you don't have a campaign plan I would start working on it right away-- it has a huge effect on how many votes you get."

    scene black
    na "After you and Mio finish hanging posters, you shortly part ways."

    na "You have a big decision to make after all..."

    na "What will be your campaign for student council vice president?"

    if metRiri:
        $ riris[92] = True

    menu:
        "{i}\"Improving Sports Programs\"":
            jump s105
        "{i}\"Pets Need Education Too\"":
            jump s106


label s95:

    mc ecstatic "Tell him your feelings of course!"

    mc normal "How do you expect anything to happen if you never let him know?"

    show mio scared
    mio "Wait! B-but--{nw}"

    mc ecstatic "In fact, let's go find him right now!"

    hide mio with ex
    na "You grab Mio's hand and sprint through the halls back to the student council room."

    show mio scared
    mio "R-running in the halls isn't allowed!"

    hide mio with ex
    #TODO: Thud noise
    na "As you and Mio are about to turn the last corner, you hear a sudden thud." with hpunch

    na "The two of you peek around the corner to find Yutaka talking to a girl slumped against the wall with a pink letter. Talk about bad timing."

    # Whispering
    show mio scared at e
    mio "Oh, it's the previous vice president! She graduated last year... what's she doing here?"

    show mio scared at left
    show jt thinking at e
    jt "Beautiful girls like you shouldn't cry... but I'm afraid I can't return your feelings."

    show jt thinking at right
    show sg sad at e
    sg "But... but you said you liked me! You even just said I was beautiful!"

    show sg angry
    sg "Ever since you entered Gwetome, I've liked you and worked my butt off for you. How could you say such a thing?!"

    show jt concerned
    jt "Ha! You claim to \"like\" me... {color=#b0b0b0}{size=-6}whatever that means...{/color}{/size} yet you know nothing about me, do you?"

    #TODO: Small thud
    mio "!!!" with hpunch

    show jt calculating
    jt "Whatever romance you had imagined is just a projection of your idiocracy."

    jt "I would never look twice at someone who decides to worship me just because of my looks."

    show sg sad
    sg "But--{nw}"

    show jt thinking
    jt "I'm sorry to tell you this Senpai... but you no longer have value to me now that you've graduated."

    show jt ecstatic
    jt "We had fun while it lasted though, didn't we?"

    sg "{i}{color=#b0b0b0}{size=-6}{cps=10}*sobs*{/cps}{/size}{/color}{/i}"

    hide sg with ex
    hide jt with ex
    na "As the girl bolts out of the hallway, you turn to look at Mio who seems to be... blushing?"

    # Whispering:
    show mio embarrassed at centerL
    mio "This whole time I never realized... how lonely Yutaka is."

    # Whispering (loudly)
    mc scared "HUH?!"

    show mio normal
    mio "Thanks for helping me find my courage, [mcname]."

    na "Before you can say anything, Mio steps around the corner and reveals herself to Yutaka."

    show mio happy
    mio "Yutaka!"

    show mio happy at left
    show jt concerned at e
    jt "Huh? Oh-- Mio."

    show jt thinking
    jt "I guess you saw all that, hm? That's too bad... you've been such a hard worker too."

    show jt normal
    jt "If you want to quit, the application fo--{nw}"

    show mio embarrassed
    mio "No! I-I don't care if you use me."

    show jt embarrassed
    jt "Huh?"

    show mio normal
    mio "I want to be by your side Yutaka! I know now that your actions, your words, have carried no weight..."

    show mio lecturing
    show jt thinking
    mio "...and I can't say I'm much different from the old Vice President... but I want to try!"

    show mio lecturing
    mio "Although this side of you is new to me, it does not deter me... or my feelings."

    mio "I want to know you for who you are!"

    show mio happy
    jt "..."

    show jt normal
    jt "I... I guess I wouldn't mind that."

    scene black
    na "Thanks to your dating expertise and fully intentional guidance, Mio and Yutaka start dating."

    na "Their unexpected yet beautiful romance quickly becomes the talk of the school, and your matchmaking skills make you a local celebrity."

    na "You become known as the \"Campus Cupid\"... a respectable title for a respectable matchmaker."

    na "You continue to help lonely hearts find love for the rest of your high school career, and even later become the godparent of Mio and Yutaka's child!"

    na "Who needs love when you're the one shooting the arrows?"

    jump e13

label s96:

    mc normal "You should wait and see how it plays out. You don't want to rush into anything."

    show mio normal
    mio "Ah... that's good, I was thinking the same thing."

    show mio embarrassed
    mio "I'm glad I got your advice [mcname]-- I was beginning to doubt myself a little bit..."

    show mio happy
    mio "W-why don't we finish hanging up these posters?"

    mio "I can keep telling you about the student council in the meantime."

    hide mio with ex
    na "As the two of you continue hanging the posters Mio opens up to you little by little."

    na "You learn about her first time running a school event, how the previous treasurer once embezzled the council's funds..."

    na "...and the time Yutaka ran an extra lap during the sports festival because a cat started chasing him."

    na "You even learn about some of Mio's personal life like how her family owns a restaurant and how her brother almost caught his middle school on fire."

    na "Time flies by, and eventually your spirited conversation comes to an end."

    show mio normal at e
    mio "That's the last poster! ...It's really gotten late hasn't it?"

    mio "Thanks for listening to me ramble-- at least now that you're in the student council, I'll have more time to work at--{nw}"

    stop music
    show mio scared
    mio "!!!" with hpunch

    mio "I'm late!"

    mio "Ahh, I'm sorry [mcname], I have to get to the restaurant right away!"

    show mio embarrassed
    mio "Would you mind grabbing my jacket for me?"

    show mio normal
    mio "It's in the student council room-- if you could give it to me tomorrow I would really appreciate it."

    mc ecstatic "Sure!"

    show mio happy
    mio "Thank you so much!"

    scene black
    #TODO: play school
    na "As Mio hurries away you make your way back to the student council room."

    scene student_council
    na "When you open the door Yutaka is hard at work, going through paperwork at his desk. As you come in he looks up at you with a coy smile."

    na "Or is it just a friendly smile? Cocky? Honestly, at this point you can't tell."

    show jt normal at e
    jt "Forget something?"

    mc normal "Mio had to leave right away so I'm getting her jacket for her."

    show jt concerned
    jt "Oh? I think I saw it earlier... let me help you look."

    hide jt with ex
    na "The two of you thoroughly search the room but the jacket is nowhere to be seen."

    show jt concerned at e
    jt "That's strange-- I could have sworn she left it here."

    show jt ecstatic
    jt "Hey why don't we do one more check of everything?"

    mc ecstatic "Okay!"

    scene black
    #TODO: Thud noise
    na "As you begin walking towards the cabinet to look for the jacket again, you suddenly trip on something and find yourself falling forward." with hpunch

    na "Closing your eyes, you brace for impact."

    jt "[mcname]!"

    na "You feel a hand grab your waist and pull you back."

    scene student_council
    na "When you open your eyes, instead of feeling the sweet embrace of the floor you find yourself in Yutaka's arms-- inches away from his face."

    show jt sad at e
    na "For a second you think you see a brief flash of worry in his expression, but it is soon overtaken by a full grin."

    show jt cocky
    na "This smile is definitely cocky."

    jt "Careful there. Don't want you hurting those lovely hands of yours-- we still have lots of posters to put up."

    na "You quickly look around for what you tripped over and see a cardboard box full of CDs. Something light blue seems to be peeking out from behind it on the ground."

    show jt ecstatic
    jt "Oh hey-- it's the jacket!"

    na "As you go to pick up the jacket, you hear a brief jingle of keys in the hallway and a click from the door."

    show jt embarrassed
    jt "Hey wait! There's still people in here!"

    na "Yutaka rushes to the door and tries to open it, but the handle doesn't budge."

    show jt concerned
    jt "Hey!!"

    mc shy "Was that the janitor?"

    show jt thinking
    jt "Yeah-- I heard they got a new hire recently so it was probably him."

    jt "Idiot doesn't know not to lock doors without checking the inside first..."

    show jt concerned
    jt "Is anyone out there?! Hey!"

    na "Yutaka pounds on the door but it is no use-- no one comes to help."

    mc shy "Hey we could call someone... I could use my phone?"

    jt "You don't have your phone anymore, remember?"

    mc concerned "Huh?"

    show jt thinking
    jt "It was one of your prized possessions, so when you signed it away it was sold for student council funds."

    na "That fast?! I guess the student council needs to be efficient when they only have three members."

    mc concerned "How about your phone?"

    show jt concerned
    jt "Don't have one. It's too much of a bother."

    mc shy "Really? But you're so popular... I'm sure people want to contact you?"

    show jt thinking
    jt "I can get along fine without it."

    show jt normal
    jt "More importantly, let's see if there's a way to get out of here..."

    #TODO: SpongeBob time card (?)
    scene black
    na "Three hours later..."

    scene student_council
    show jt thinking at e
    jt "There's no way to get out of here."

    mc shy "I mean... if we're going to be stuck here for the rest of the night, we can talk about something?"

    show jt cocky
    jt "Ha... talk."

    mc shy "..."

    show jt thinking
    jt "..."

    show jt concerned
    jt "Fine. About what?"

    mc concerned "I don't know... love?"

    show jt embarrassed
    na "Yutaka looks at you, stunned, and then breaks into a fit of laughter."

    show jt cocky
    na "You're not sure what's supposed to be funny."

    show jt calculating
    jt "God, I should have known."

    jt "You're all the same aren't you? You. Mio. Everyone."

    mc concerned "Excuse me?"

    show jt concerned
    jt "Is love all you think about? Is having a lover just the only thing that matters to you people?"

    na "Uh... he might have you figured out there."

    show jt calculating
    jt "Ha. Who needs something as shallow as love?"

    jt "All you people want is some pretty face to look at-- something to show off."

    show jt concerned
    jt "Doesn't matter what they're like, you'll already do anything for them. You're just tools to be used."

    mc concerned "..."

    show jt thinking
    jt "If people can't see me beyond my looks why should I try to change their mind? All I need to do is say a few sweet words and they're already wrapped around my finger."

    menu:
        "\"I don't see you that way Yutaka.\"":
            jump s98
        "{i}Escape and let Mio know Yutaka's true nature":
            jump s23
    

label s97:

    mc embarrassed "Uhh... I also like Yutaka."

    show mio embarrassed
    mio "That's what I was afraid of."

    hide mio with ex
    na "A sudden flush of red fills Mio's face as she darts away from you, dropping the posters back on the ground."

    na "Guess that wasn't something she wanted to hear."

    na "You look down at the mess-- you definitely have your work cut out for you now."

    na "As you begin picking up and hanging the rest of the posters, Yutaka spots you in the hallway and walks up to you."

    show jt cocky at e
    jt "Hey-- what are you doing all alone?"

    show jt thinking
    jt "Did Mio run off?"

    mc embarrassed "Um... well..."

    show jt normal
    jt "Ah, I bet I know what happened."

    show jt cocky
    jt "Did you two fight over a guy?"

    mc shy "How did you know?"

    show jt normal
    jt "It's just something I see a lot."

    hide jt with ex
    na "As Yutaka begins to walk away he winks at you, making your heart skip a beat."

    na "Is now the time? Should you tell him your feelings? Does he already know?!"
    
    show jt normal at e
    mc scared "Hey, wait! Yutaka I--{nw}"

    show jt cocky
    jt "Keep doing what you're doing, [mcname]!"

    jt "Maybe if you do a good job we could grab a coffee one day."

    na "Well... that gives you something to work towards, I guess."

    scene black
    na "In your flurry of love you go above and beyond-- hanging posters, cleaning Yutaka's desk, organizing all the council's paperwork..."

    na "It's all hard work but you're determined to do it."

    na "After all, if you continue to try your best you'll eventually win over his heart-- right?"

    na "...Right...?"

    na "As you continue fulfilling Yutaka's requests and supporting him in the student council, you help him become the most powerful student in the academy."

    na "Yet at what cost?"

    na "Your entire life begins to revolve around Yutaka-- you no longer have time for hobbies or friends."

    na "When you wake up you think of Yutaka."

    na "When you go to school you think of Yutaka."

    na "His love is something that feels so close yet is never in reach... and never will be."

    na "You spend the rest of high school in his shadow, unknown and forgotten, forever vying for his love and attention."

    na "But I mean... it's in the name of love, right?"

    jump e16



label s98:

    mc shy "I don't see you that way Yutaka."

    mc normal "I don't think that you're just some trophy to display, and I'm definitely not someone you can just manipulate."

    mc concerned "You're good looking, sure, but I don't love you."

    show jt thinking
    jt "..."

    mc concerned "That's not what love is..."

    mc normal "Love is getting to know someone-- their flaws, their quirks, and their stories."

    mc ecstatic "It's enjoying someone's company and taking the time to work through life, together."

    mc concerned "If you want someone to truly love you... you have to give them a chance first. Believe in them a little."

    mc concerned "I think if you assume everyone is already shallow and close yourself off it's a self-fulfilling prophecy."

    mc shy "Of course they won't \"love\" you for who you are-- you never gave them a chance to try in the first place."

    jt "..."

    show jt concerning
    jt "I see..."

    jt "I'm sorry for exploding on you, [mcname]... and assuming your intentions..."

    show jt thinking
    jt "That was wrong of me to do."

    jt "I've been saying that no one sees me for who I am as a person, but... I've been doing the same to others... haven't I?"

    mc normal "I think you just need a little time to change."

    show jt ecstatic
    jt "No kidding, huh?"

    show jt thinking
    na "Yutaka chuckles sadly."

    show jt concerned
    jt "If... it's alright with you... may I get to know you?"

    mc shy "Huh?"

    jt "I'm sure you think I'm a terrible person right now-- and you'd probably be right."

    show jt sad
    jt "But I want to become someone different."

    jt "I would like to get to know you as a person... and a friend if you'll let me."

    mc ecstatic "Of course!"

    mc normal "Let's be friends."

    show jt normal
    jt "Thank you."

    mc cocky "Anytime, babygirl."

    show jt ecstatic
    jt "I'm gonna pretend I didn't hear that."

    jump e14

label s99:

    scene classroom1 day

    show teacher_e normal at e
    teacher_e "Next we have... Yutaka and name's project."

    show teacher_e normal at left
    show jt ecstatic at e
    jt "Ah yes, our masterpiece is finally being shown!"

    mc shy "Here we go..."

    hide teacher_e with ex
    hide jt with ex
    na "As the teacher shows your project, you can hear your classmates murmuring."

    na "They're... suspicious. Your project seems a little too romantic..."

    show teacher_e normal at e
    teacher_e "Comments?"

    s1 "Thought it was very cute..."

    s2 "Wow, it almost felt like you two are {i}really{/i} in love!"

    #TODO: Whole class laughing noise (?)

    mc embarrassed "This is too embarrassing!"

    na "You grab your stuff and sprint out of class."

    jump s75

label s100:

    scene classroom1 day
    show teacher_e happy at e
    teacher_e "Next we have... Yutaka and [mcname]'s project."

    show teacher_e happy at left
    show jt ecstatic at e
    jt "Ah yes, our masterpiece is finally being shown!"

    mc shy "I hope everyone likes it..."

    scene classroom1 day
    na "As the teacher shows your project, smiles and nods of approval appear on your classmates' faces."

    na "Success! Everyone seemed to like it. Good job, [mcname]."

    show teacher_e happy at e
    teacher_e "Comments?"

    na "As kids' hands fly in the air to sing praise of your masterpiece, the door dramatically opens and a well dressed man with a camera around his neck enters the room..." with hpunch

    jump s101

label s101:

    show teacher_e sad at left
    show beckham agent normal at e
    beckham "Hello everyone, I am here from Kunkler Productions, and I would like to amend Ms. [mcname] on her wonderful project."

    mc shy "Oh, really? Thank you..."

    beckham "Yes, [mcname], this project excellently portrays your talent in filmmaking."

    show beckham agent happy
    beckham "Talent like yours is needed in my industry right now."

    beckham "What do you say to dropping this silly school business and becoming a full-time producer?"

    show beckham agent flirty
    beckham "Generous payment included, of course!"

    show teacher_e angry
    teacher_e "Hey, you can't just-{w=0.2}{nw}"

    show beckham agent happy
    show teacher_e sad
    beckham "Now I can. So what do you say, [mcname]?"

    show beckham agent flirty
    beckham "You could make millions. {i}{color=#b0b0b0}{size=-6}{cps=10}*wink*{/cps}{/size}{/color}{/i}"

    mc ecstatic "Wow, that sounds awesome! Sign me up!"

    jump e20

label s102:

    mc "I'm sorry, Yutaka. I shouldn't have gotten so worked up."

    mc "I like working with you... I promise I won't be violent ever again! Please forgive me!"

    jt "Good, that's more like it."

    jt "Don't you worry your little head about it! What's done is done."

    jt "Although, I might have to watch you a little {i}closer{/i} now... {color=#b0b0b0}{size=-6}*wink*{/color}{/size}"

    na "Anddd he's right back to normal. No surprise there."

    na "You and him spend some time chatting, when Yutaka suddenly remembers that he's got student council work to do."

    #TODO: Fix s102 (talk to maryam)

label s103:

    mc angry "Yutaka, you aren't the boss of me. I can and will do whatever I want."

    mc concerned "If you don't agree with my methods of cleaning up messes, then we can part ways."

    scene black

    na "You get up and leave the room without a second glance at your student council president."

    na "He seems dumbfounded, like no one has ever rejected him like that before."

    scene hallway day
    na "As you turn into the hallway, you see a nonchalant, delinquent-looking student leaned against the wall, seemingly waiting for you."

    show sophia normal at e
    sophia "Yo."

    mc shy "Hello?"

    show sophia flirty
    sophia "The way you handled that was pretty cool, you know. I love a good ol' fight, and you really showed it to that stuck up student council president of ours."

    mc embarrassed "Oh, you saw all that? Haha, yeah... I guess you could say it was pretty cool..."

    show sophia happy
    sophia "You've got some serious spunk, stepping up for yourself like that."

    show sophia flirty
    sophia "You know, I think you'd fit right into my family, if you catch my drift. {color=#b0b0b0}{size=-6}*wink*{/color}{/size}"

    mc embarrassed "Family? Wait... are you trying to recruit me to be a yakuza?!"

    show sophia normal
    sophia "You tell me."

    mc normal "That actually sounds pretty fun..."

    mc ecstatic "You know what, school is lame anyways! I'll do it, I'm in!"

    show sophia happy
    sophia "That's the spirit."

    na "Well that was a bold choice!"

    #TODO: Yakuza family headquarters background (?)
    na "Anyways, Isamu leads you to his Yakuza family headquarters for initiation."

    scene black
    na "After a long initiation process..."

    ff "By drinking this sake, you hereby dedicate your life to being a child under my protection. Is this your wish?"

    mc normal "Yes, Father."

    ff "Very well."

    na "As you drink the sake, a sense of relief washes over you, knowing you'll never be under the control of that bossy Yutaka ever again."

    jump e17

label s104:

label s105:

    na "You decide to make your campaign about improving the sports programs at Gwetome Academy."

    na "For too long this school's athletic prowess has been overlooked!"

    na "But, you're here to be the change Gwetome Academy needs!"

    na "...Or so you think"

    na "Shortly after launching your campaign you notice that your cause is overwhelmingly... underwhelming."

    na "Most of your competitors had the same idea, and after years of sports-centered campaigns the idea has become rather worn-out."

    na "Your campaign is completely disregarded by the student body, and after a humiliating loss you quickly fade into political obscurity."

    na "With your ego shattered and dreams crushed, you become just another face in the crowd… forever dragged down by your mediocrity."

    jump e18

label s106:

    na "As a firm believer in equality, you decide to make your campaign about allowing pets to enroll at Gwetome Academy."

    na "After all, shouldn't pets have the same right to education as humans?"

    na "After launching your campaign it immediately becomes a hit with the student body, and your progressive thinking draws numerous powerful financial supporters."

    na "One such supporter being the infamous yakuza, \"The Dark Prince of Shizuoka,\" and their cat, Skullcrusher."

    na "With your new huge (and slightly questionable) financial backing, you crush your opponents in the polls and easily win the election."

    na "After a few months, all pets are in classrooms and able to get a fair education-- a huge step forward for animal rights across Shizuoka."

    na "You even get your first pet staffmember, an important event that exposes the incompetence in the school's human management."

    na "This eventually leads to a complete change of staff in the district, and soon enough, the whole of Gwetome is taught and run by animals."

    na "A true revolution in education as we know it."

    jump e19

label e0:

label e1: # Joe falls in love with the lifeguard
    
label e2: # Date Joe (pending name)

label e3: # Castaway with Joe

label e4: # Love you too
    
label e5: # All is fair in Love and War

label e6:

label e7: # Death

label e8: # Date Maryam (pending name)

label e9:

label e10:
    
label e11: # Big Apple Juice

label e12: # Love in the Basket

label e13: # The Archer of Love

label e14: # First Love

label e15: # Happily Ever After

label e16: # Mio 2.0

label e17: # Yakuza

label e18: # The Safe Play

label e19: # The True High School Experience

label e20: # Famous Filmmaker


label dice_roll:
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d10 = renpy.random.randint(1, 10)
    $ d20 = renpy.random.randint(1, 20)
    return

label fight:

    $ player_hp = 20
    $ enemy_hp = 20
    $ player_attack_value = 3
    $ enemy_attack_value = 3

    $ player_max_hp = 20
    $ enemy_max_hp = 20

    scene hallway day
    show fight1 at bar
    show fight2 at bar
    show jt cocky at e
    

    

    while player_hp > 0 and enemy_hp > 0:

        # Player Turn - two choices!
        call dice_roll

        $ player_attack_value = 3
        $ enemy_attack_dec = 0

        menu:
            "Flirt":

                if d10 >= 8:                                                # 80%
                    show jt calculating
                    jt "...Well that's embarrassing." 
                    #TODO: add fight lines to script??
                    na "Your flirting had no effect!"          # 70%
                else:
                    $ enemy_attack_dec += d4
                    call flirt1
                    na "You successfully flirt with Yutaka and reduce his damage by [d4]!"
                    #mc scared "[d4] damage!"
            "Punch":
                #call camera_knight_attack                       
                if d10 >= 8:                                                # 20%
                    $ player_attack_value = (d6 + d4)*2
                    $ enemy_hp -= player_attack_value
                    na "Critical Hit! Yutaka took [player_attack_value] damage!" with hpunch
                elif d10 >= 3:                                              # 40%  
                    $ player_attack_value =  d6 + 2                                        
                    $ enemy_hp -= player_attack_value
                    na "That's a strong hit! Yutaka took [player_attack_value] hp!" with hpunch
                else:                                                       # 40% 
                    na "You miss!"   #:(    
            "Run":
                na "You run away."
                jump s22

        if enemy_hp <= 0:

            jump s19
            #jump harder_menu

        # Enemy Turn - Semi-randomized behavior!

        call dice_roll

        if d20 >= 17:                                            # 20%       
            if d10 - enemy_attack_dec <= 0:
                na "The Yutaka makes a wild attack, but does no damage!"
            else:
                $ newdmg = d10 - enemy_attack_dec
                $ player_hp -= newdmg
                na "The Yutaka makes a wild attack for [newdmg] damage!" with hpunch

        elif d20 <= 4:                                            # 20%
            
            if enemy_hp < (enemy_max_hp - d4):
                $ enemy_hp += d4
                na "The Yutaka heals itself, raising [d4] hp!"
                
            else:
                $ enemy_hp = enemy_max_hp
                na "The Yutaka fully heals itself back to full hp!"
        else:                                                    # 60%         
            if d4 - enemy_attack_dec <= 0:
                na "The Yutaka makes an attack, but does no damage!"
            else:
                $ newdmg = d4 - enemy_attack_dec
                $ player_hp -= newdmg
                na "The Yutaka attacks and does [newdmg] damage!" with hpunch

    #call camera_knight_died
    jump s22
    hide screen hp_bars_1v1


    menu harder_menu:
        "Play this level again?":
            $ player_hp = 20
            $ enemy_hp = 20
            jump fight
        "Back to Main Menu":
            jump start

    label flirt1:
        mc cocky "If I could rearrange the alphabet, I'd put 'U' and 'I' together."

        show jt flirty
        jt "Ohohohoho, you didn't..."

        





        














return