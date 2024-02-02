# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image vid = Movie(play="audio/5-6.webm", size=(1920,1080),loop=False, xalign=0.10, yalign=0.10)

init -2:
    # ---------- blinking arrow -------------------
    image ctc_blink:

        alpha 1.0
        "images/star1.png"
        zoom 0.22
        ypos -5
        xpos 4
        0.5
        "images/star2.png"
        zoom 0.22
        ypos -5
        xpos 4
        0.5
        repeat

transform jumper:
    ease .04 yoffset 20
    ease .03 yoffset 16
    ease .02 yoffset 12
    ease .01 yoffset 8
    ease .01 yoffset 4
    ease .01 yoffset 0

#--------------
image zeil normal:
    "images/zeil normal.png"
    zoom 0.8

init python:

    riris = []
    for i in range(100):
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


    


    # quizAnswers = ["hi2, hello2, hey2"]
    

    ririname = "..."
    mcname = "..."
    joename = "..."
    jtname = "..."
    sophianame = "..."
    maryamname = "..."

    metRiri = False
    metJoe = False
    metJT = False
    metSophia = False
    metMaryam = False

    from game.images.Gwyn import *
    from game.images.Extras import *
    from game.images.Riri import *
    from game.images.Beckham import *
    from game.images.Joe import *
    from game.images.Jt import *
    from game.images.Kyle import *
    from game.images.Maryam import *
    from game.images.Sophia import *
    from game.images.Backgrounds import *

# --------------------------------------------------------
init:
    define pjmc = Character("[mcname]", color = "#ffffff", ctc="ctc_blink", image="gwyn_pajamas", window_background="gui/textbox2.png")
    define pmc = Character("[mcname]", color = "#ffffff", ctc="ctc_blink", image="gwyn_party", window_background="gui/textbox2.png")
    define smc = Character("[mcname]", color = "#ffffff", ctc="ctc_blink", image="gwyn_suit", window_background="gui/textbox2.png")
    define mc = Character("[mcname]", color = "#ffffff", ctc="ctc_blink", image="gwyn_uniform", window_background="gui/textbox2.png")

    define na = Character(name=None, ctc="ctc_blink")
    define mom = Character("Mom", ctc="ctc_blink")
    define teacher_e = Character("先生", ctc="ctc_blink")

    define beckham = Character("マリオ", color = "#ff8b06",  ctc="ctc_blink")
    define joe = Character("[joename]", color = "#bd44d6", ctc="ctc_blink") # define joe = Character("ジョ~")
    define kyle = Character("千葉、昭光", color = "#43BC47", ctc="ctc_blink") # define kyle = Character("千葉、昭光 (Chiba, Akimitsu)")
    define jt = Character("[jtname]", color = "#fff700", ctc="ctc_blink") # define jt = Character("柳井、富 (Yanai, Yutaka)")
    define sophia = Character("[sophianame]", color = "#0051ff", ctc="ctc_blink") # define sophia = Character("高尾、勇 (Takao, Isamu)")
    define maryam = Character("[maryamname]", color = "#00eeff", ctc="ctc_blink") # define maryam = Character("木山、遥花 (Kiyama, Haruka)")
    # define zev = Character("...") # define zev = Character("ゼブ")
    define kadie = Character("Kadie!1!11!", color = "#00eeff", ctc="ctc_blink")

    define mi1 = Character("Magical Ikemen 1", ctc="ctc_blink")
    define mi2 = Character("Meowgical Ikemen 2", ctc="ctc_blink")
    define pp = Character("PyunPyun", ctc="ctc_blink")
    define takeshi = Character("Takeshi", ctc="ctc_blink")
    define dr = Character("Dr.", ctc="ctc_blink")

    define riri = Character("[ririname]", ctc="ctc_blink") # define riri = Character("リリ")
    define mv = Character("Mysterious Voice", ctc="ctc_blink")
    define mi = Character("Mysterious ikemens", ctc="ctc_blink")

    define d1 = Character("Deliquent 1", ctc="ctc_blink")
    define d2 = Character("Deliquent 2", ctc="ctc_blink")
    define d3 = Character("Deliquent 3", ctc="ctc_blink")



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
    play music bgSong
    pause 0.2
    scene gym with Pixellate(0.5,3)

    queue music basketballSong
    "During gym..."
    show zeil normal at char_left with vpunch
    mc "{b}Hi!{/b} I'm {u}mc!{/u} {size=+10}This{/size} is my \"Project\"!"
    mc "Man, is it just me, or am I... {color=#b0b0b0}getting... {size=-6}a {nw}"
    mc "little sleepy...{/size}{/color}"
    return

label DefaultQuestion:
    mc "What?!"
    menu:
        "Nothing!":
            jump Questions_mc.Answer_Nothing
        "Hi.":
            jump Questions_mc.Answer_Hi
        "Play a game with me!":
            $ renpy.dynamic("randumNum","answer") #To make variables local
            $ randomNum = renpy.random.randint(1,4)
            mc "Anyways... OMG! It's a [randomNum]!"
            if randomNum >= 1 or randomNum <= 2:
                $ answer = "What?"
            elif randomNum == 3:
                $ answer = "Say that again?"
            else:
                $ answer = "Huh?"
            mc "[answer]"
            # $ repeatQuestion = renpy.random.choice(["What?", "Say that again?", "Huh?"])
            return
    
label Questions_mc:
    label .Question_What:
        label .Answer_Nothing:
            mc "Oh."
            return
        label .Answer_Hi:
            mc "Hi!"
            return


# --------------------------------------------------------
# p = placeholder label
# s = scene
label p:
    na "PLACEHOLDER"
    return

label riri:
    if riris[10]:

        riri "Yay! You did it! I'm so proud of you Naninani. Okay... let's see your options..."

        riri "Your teacher is really mad right now. If you went to class you'd definitely receive that anger."#Joe19

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

        na " [[Riri shakes her head. It looks like she doesn't want to talk to you right now.]"
        $ riris[27] = False
    if riris[28]:

        riri "The drama! As the main character, you {i}must{/i} pick at least one of them!"

        riri "Don't let the temptation of the forbidden fruit fool you!"

        $ riris[28] = False
    if riris[43]:

        riri "It's me, Riri. Don't worry Naninani, I'm just making some minor adjustments to the fabric of time."

        riri "You may have failed this time at romance, but I won't let you give up!"

        $ riris[43] = False
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
        $ mcname = "何とか、何々"

    #stop music
    
    scene bedroom
    

    #show side gwyn pajamas tired
    pjmc normal "I'm so tired... I stayed up all night playing otome games."#Gwyn1
    
    pjmc "It`s hard not to when you`re given so many choices, especially when you can punch the male leads. Hehehe!"#Gwyn2

    pjmc ecstatic "Oh wait! I forgot to introduce myself. My name is {u}[mcname]{/u}!"#Gwyn3

    pjmc "I'm sixteen. Today is my first day of my second year at Gwetome Academy."#Gwyn4

    pjmc "Ever since my family moved back to Shizuoka, I've been living my high-school life to the fullest."#Gwyn5

    pjmc "During my time here, I've come to learn that love isn't the only important thing in life. 
        I'm my own person, with my own goals and dreams, and I'm proud of that. I am independent and strong!"#Gwyn6

    #show gwyn pajamas embarrassed at right
    pjmc "...and I'm late for school."#Gwyn7

    menu:
        "Go downstairs and get ready for school":
            jump s2
        "Sleep in just a liiitle longer":
            jump s3
    return

label s2:

    na "You put on your uniform and go downstairs."#JT3

    scene kitchen
    mom "Good morning! I made you breakfast since I knew you'd wake up late."#

    mom "Dad's already left to go work on his new Food Network episode and I'm heading out now. Have fun at school! I'm off!"#

    # Door closing noise
    mc "Thanks, have a good day!"#Gwyn8

    na "You happily munch on the breakfast your mother made and pat your belly in satisfaction. 
        Suddenly, the TV turns on, as if it's beckoning you to watch it."#JT4

    na "Wait! Is that... the new season of Magical Ikemen?!? It's been a whole year since the last episode!"#JT5

    na "But... you have school. If you leave now, you still might be able to make it in time."#JT6

    menu:
        "Head off to school":
            jump s4
        "Watch Magical Ikemen":
            jump s5

label s3:

    na "You crawl into your covers again and begin to sleep blissfully; everything is cozy, warm, and peaceful. You begin to dream."#JT7

    na "It's your first day of school at Gwetome Academy. Everyone is calling you Naninani Nantoka. 
        But why? You've always been [mcname] haven't you? How strange."#JT8

    na "Just as you are about to investigate this, you feel a sudden shake."#JT9

    mom "Hey!...Hey! Get up! How did I end up with such a lazy child?"#

    mom "[mcname], school's already started so you need to hurry! I'm off to work now, so I can't help you. I'm off!"#

    menu:
        "Wake up and go go go!":
            jump s6
        "Nahh, I'm sleeping more":
            jump s7

label s4:

    na "Wow, look at you all responsible! You discard the temptation of Magical Ikemen and start your trek to school."#JT10

    scene neighborhood
    na "You check your phone and see you have more time than you realized. Maybe you'll just quickly look up the information about 
        Magical Ikemen's new season while you walk... you have the time after all."#JT11

    na "Plus, you need to know whether or not Takeshi finally leaves his office job to pursue his dream
        of becoming a full-time magical girl in the Kiss Kiss Love Power Team."#JT12

    na "As you scroll through the wonderland that is the Magical Ikemen online forum, you bump into a pole. Ouch."#JT13

    na "Wow, that's a strangely attractive pole. And it's wearing a... Gwetome Academy uniform!? The pole turns around."#JT14

    show joe normal
    joe "Ah sorry, I was walking kind of slow. Are you ok?"#Joe1

    joe "A lot of people bump into me so my back muscles have become hard like metal. My doctor said it's because I tend to draw people in... I'm magnetic."#Joe2

    show joe embarrassed
    joe "Heh. Sorry, I'm rambling. Anyways, I'll just uh... keep walking."#Joe3

    na "The mysterious ikemen runs his hand through his hair cooly and starts to saunter away."#JT15

    na "Your heart is beating fast; you don't know if it's because of his dazzling looks or possible metal poisoning."#JT16

    na "Either way, you should probably get to school. The question is: How?"#JT17

    menu:
        "I'll take the journey alone!":
            jump s8
        "Try to talk to the ikemen":
            jump s9

label s5:

    na "The TV has summoned you and you must answer its call. As you sit down on the couch, you see the familiar face of the main character, Kimura Takeshi."#JT18

    na "It looks like he's having a serious talk with the Kiss Kiss Love Power Team, a magical-girl group that saves the world from evil monsters."#JT19
    
    na "During the last episode, Takeshi was deciding whether or not to keep his office job or pursue his dream of becoming a full-time magical girl. 
        He must be discussing this with them now."#JT20

    mi1 "Takeshi... you must make a choice. If we wait any longer, the Dr. will find out your true identity. Either join us or leave us."#Kyle1

    pp "Pyun!"#Gwyn9

    takeshi "But--{nw}"#Beckham1

    mi2 "Takeshi, we {i}meow{/i} it's a hard decision, but it's one that must be {i}mwade.{/i} {color=#b0b0b0}{size=-6}nya~{/size}{/color}"#Joe4

    takeshi "But... but... what if I'm not cut out to be on the Kiss Kiss Love Power Team? 
        What if I'm not a real magical-girl? If I fail... I can't ever return. Please, give me more--"#Beckham2

    #explosion/crash + helicopter sounds
    #PyunPyun falls

    pp "Pyuuuuuuuuuuun~"#Gwyn10

    mi1 "NO! PYUNPYUN!"#Kyle2

    #Through a megaphone:

    dr "HUEHUEHUEHUEHUE! I will defeat you all one by one!"#JT21

    na "Man, they kept the annoying mascot from season 1."#JT22

    na "Just as the Dr. begins to shoot his sadness missiles at the Kiss Kiss Love Power team, your phone buzzes."#JT23

    mc "Huh?"#Gwyn11

    na "Suddenly, a tiny sexy witch emerges out of your phone."#JT24

    mc "Mark Zuckerberg?!"#Gwyn12

    $ metRiri = True
    $ ririname = "リリ"
    riri "Wrong! I'm Riri. My boss told me there was a weeb here so I came to help."#Joe5

    riri "Wait! Are you Naninani Nantoka!?!?"#Joe6

    mc "Uh. No. I'm [mcname]."#Gwyn13

    riri "Oh how the great have fallen. {i}{color=#b0b0b0}{size=-6}{cps=10}*sigh*{/cps}{/size}{/color}{/i} I used to always hear about you at work--"#Joe7

    riri "you were determined to get a lover by the end of the school day. On your first day of school! You were my hero... But now... {i}*cries*{/i}"#Joe7

    mc "Ummm..."#Gwyn14

    riri "Well no matter Naninani! I'll help you get back on your feet and into the world of romance once again. Let's go!"#Joe8

    mc "Ummmmmmmmm..."#Gwyn15

    menu:
        "Go to school... late":
            $ riris[10] = True
            jump s10

label s6:

    mc "Ah! I've done it now!"#Gwyn16

    na "You quickly throw on your uniform, grab a piece of toast, and run out the door."#JT25

    mc "I'm gonna be late!"#Gwyn17

    na "It isn't long before you find yourself turning a sharp corner... with toast... hmm..."#JT26

    mc "Ah! It hurts!"#Gwyn18

    #Background bird caw noises
    mc "...?"#Gwyn19

    mc "Is no one... here?"#Gwyn20

    na "Wow, you must be really off your game today *name*. You look around yourself, stunned... this has never happened before."#JT27

    na "How could you not bump into a hot ikemen while turning a corner with toast in your mouth?!?! Maybe you should try again."#JT28

    na "You pick up the toast and start walking back to where you started, when you hear a strange noise."#JT29

    joe "Kyaa~! I'm gonna be late!"#Joe9

    na "Ah, there it is. You look up and see a hot... pole? No wait! You shake your head to clear your vision."#JT30

    joe "Sorry, are you ok? I don't know what came over me. I just felt a sudden need to run around that corner."#Joe10

    mc "Yeah, I'm alright."#Gwyn21

    na "The boy's eyes sparkle as you take his hand and he smoothly pulls you to your feet. Nice."#JT31

    na "After you both apologize you quickly continue on your way."#JT32

    menu:
        "Go to school... late":
            jump s10

label s7:

    na "Heh... school. Who needs it? You're about to discover the answer to the greatest mystery yet: who is Naninani Nantoka?!"#JT33

    na "You rustle back under your blankets, close your eyes, and start to dream again... but this time you are not at school."#JT34

    na "You are floating through an endless void. You can't move. You can't breathe. All is silent."#JT35

    na "Is this what it's like to be in a world with no love? No romance? No {i}ikemens?{/i}"#JT36

    na "Your mind succumbs to the darkness."#JT37

    mv "You have failed your purpose, [mcname]."#Gwyn22

    na "By the time you wake up, the school year has already ended. You now know your true duty but it is too late, and there is no one left to love you."#JT38

    na "Weeping, you succumb to the darkness of sleep once more."#JT39

    jump e0 #Eternal Power Nap

label s8:

    na "You keep walking to school alone and eventually end up at the front of the school."

    na "You notice a poster near the entrance, offering students to join the Student Council"

    na "Hmmm... It'd look pretty good on college applications. How hard could it be?"

    menu:
        "Go to class":
            jump s51
        "Sign up and go to the Student Council room":
            jump s52

label s9:

    na "His looks are too much to resist... you must talk to him now that you have the chance and time."

    na "Looks like being responsible pays off."

    mc "Oh.. kay, sorry! I didn't see you there."

    joe "Really? I'm quite hard to miss, you know..."
    
    mc "Is that so? Anyways, what is your name?"

    $ joename = "ジョー"

    joe "Oh right! The name's Joe-kun, but you can just call me Joe."

    na "Is that even a name?"

    mc "Well, nice to meet you! My name is [mcname]"

    joe "Wow, what a cool name! I'm jealous."

    show joe normal
    joe "I'm just an average Joe, you know? Hahaha!"

    na "Seriously, laughing at your own jokes? This guy..."

    mc "Ha... well, which way are you heading?"

    joe "Oh, I've got class this way. It was nice talking to you, see you around!"

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

        #riri goes into the corner and you can click on him

        riri "Hehe... hehehehehe..."

        $ metRiri = True
        call riri

    menu:
        "Go to class late":
            jump s11
        "Skip!":
            jump s12

label s11:

    na "Skipping class? It looks like you value your education..."

    na "You walk to class and fling open the door."

    na "You're here in order to learn! You must study! You have your whole life ahead of you and you're not backing down!"

    mc "Excuse me!"

    sensei "Detention!"

    
    if metRiri:
        $ riris[11] = True
        call riri

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
        call riri
    
    menu:
        "Make a scene!":
            jump s15
        "Wait for detention to end and leave":
            jump s16

label s14:

    na "You agree to go and watch Akimitsu's basketball game after school."

    na "How could you not? You've known Akimitsu since you were tiny and basketball has always been really important to him."

    na "Maybe one day you'll be important to him too."

    na "After a short walk out of school the two of you arrive at a small run-down gym."

    scene gym
    show kyle jersey normal
    mc "The final is{cps=4}...{/cps} here?"

    show kyle jersey flirty
    kyle "Yeah! It's just a small local tournament. Nothing to get too excited about."

    mc "Oh, got it."

    na "The two of you slowly open the door to the gym."

    na "Immediately you are blinded by colorful spotlights and music blasts throughout a ginormous stadium."

    na "The stands are packed with cheering onlookers, their voices roaring like thunder."

    na "There must be hundreds, no-- thousands of people here!"

    na "A basketball court stands in the center."

    mc "Is this... THE B. LEAGUE FINALS?"

    kyle "Mhm! That's why I didn't want to miss it."

    kyle "Why don't you grab a seat? I need to get warmed up."

    mc "Uhuh..."

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

    mc "Oh, hey."

    sophia "You dropped this."

    na "Isamu hands you a small handkerchief with a small cute cat print on it."

    mc "Oh, that's not mi--"

    sophia "Keep it."

    na "Isamu coolly grabs their jacket and leaves the room. You can't help but notice a slight blush on their face."

    mc "Huh..."

    na "You unfold the handkerchief to find a piece of paper with a message:"

    #Sophia's voice / piece of paper with words on it
    na "{i}You. Me. Rager party. Tonight? Yes? No? Plz yes. :3 Thank you.{color=#b0b0b0} - The Panther{/i}{/color}"

    na "Despite \"The Panther\"'s horrible grammar, your heart skips a beat. Are they asking you... on a date?"

    if metRiri:
        $ riris[15] = True
        call riri

    menu:
        "I'm going to that party!":
            jump s26
        "Absolutely not":
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

    mc "I refuse! {i}You{/i} shouldn't be able to send me back to class!"

    mc "What are you doing out of class, huh? I'll make {i}you{/i} go back!"

    na "Yukata stares at you for a moment, then a small grin appears on his face."

    jt "Ah, people like you are my favorite!"

    jt "What {i}I{/i} do while at school does not matter to you, understand me? I am the president of the student council!"

    jt "{i}You{/i} have to listen to me, and {i}I{/i} am in charge. That is how it works, and how it always will."

    na "Who does this guy think he is?"

    mc "That's just not fair!"

    jt "Oh, but my dear girl, {i}life{/i} is not fair. I am simply getting you ready for reality."

    na "I want to punch \"reality\" into his face! It would have been better if you chose to fight him."

    jt "Anyways, I like you, so I will let you off easy this time."

    jt "Just detention. Consider yourself lucky."

    mc "Hey!"

    jt "Don't make me angrier now. Welp, See you around!"

    na "Yukata turns and walks away confidently. Man, what a prick!"

    na "You pick up the detention slip that he slid in your pocket and reluctantly read it."

    mc "Right after school? This is the worst! Whatever, I better go..."

label s18:

    na "As you're wandering the halls, you notice a student walking your way. He seems to be dressed very nicely, even for the prestigious Gwetome Academy."

    na "Wait, that's the student council president! You're in trouble if he finds you out here."

    menu:
        "Hide behind a corner!":
            jump sub1
        "Pshh, what is he gonna do?":
            jump sub2
    label s18_1:

        na "As you tip-toe over to the corner of the hallway, you accidentally step on a very conveniently placed stick."

        jt "How'd a stick get in here?"

        na "Busted..."

    label s18_2:

        na "You stand confidently in the center of the hallway as he walks towards you."

        

    label s18_3:

        $ metJT = True

        jt "What's a pretty looking girl such as yourself doing around these parts?"

        jt "Wait, what's a student doing in the halls? ...I'm terribly sorry, but you're gonna have to go back to class."

        mc "Nonono, I just--{nw}"

        jt "--Needed to go to the bathroom and got lost in the halls, I've been there."

        jt "Well, you're not going anywhere without a hall pass. How about we bring you back to class to get one?"

        menu:
            "Sure, I should probably head back":
                jump s21
            "This guy deserves a punch!":
                jump s18_4
    label s18_4:

        na "As you start to turn around to walk back to class, you swiftly turn back and drive your fist into the student's face. Nice."

        na "Uh oh, he got back up? Looks like it's time for a fight!"

label s19:

    na "You throw a powerful punch, flying him across the room. He won't be bringing you back to class again anytime soon."

    na "You hear a feeble voice as you walk away."

    jt "Wait-- please... You don't need to do this!"

    mc "Heh... I knew that CrossFit membership would pay off."

    jump s20

label s20:

    na "Word quickly spreads about how you punched the student council president and skipped class as you proudly walk out the front gates."

    mc "Man, that fight really took a lot out of me. I could really go for a Caramel Ribbon Crunch Frappe right about now."

    jump s24

label s21:

    mc "{i}Oh shoot, I forgot to grab one{/i}! Sure, let's head back."

    na "You walk back to class to get a hall pass, even though you never needed one. But right as you grab it, the bell rings."

    jt "Awww, well that's a shame. Well hey, at least we have the same class next period!"

    mc "Oh, nice! Wait, how did you know that we had the same class?"

    jt "I just checked the Google Classroom! It's the job of the student council president to know their fellow students' names, after all."

    jt "C'mon, we have English class next. Let's go!"

label s22:

    na "You release a powerful punch aimed right at Yukata!"

    na "...and miss. Well, that's embarrassing."

    mc "Oh... oops."

    jt "Ahahha, how cute! You really think you stand a chance against me? I am the one and only student council president, Yukata!"

    mc "Uhm... okay?"

    jt "You've been naughty now, haven't you?"

    jt "You think you can walk free after trying to hurt the most important student in the school?"

    jt "No! I will not let this stand! Off to counseling with you!"

    na "How dramatic can this kid get..."

    mc "Alright fine, I'll go to counseling. Sorry for trying to punch you, but it was too hard to resist."

    jt "Hey! Wait, don't say that about me!"

    na "You turn and go to counseling. You can feel Yukata fuming behind you, but you keep walking without a care in the world."

    jump s25

label s23:

label s24:

    #In starbucks

    mc "I'll take your finest Caramel Ribbon Crunch Frappe, please."

    na "You felt like you've seen this kid before. Maybe from school?"

    beckham "that'll be 2,210¥."

    mc "Wh-{nw}"

    na "-Wait, 2,210¥?? What has this world come to..."

    na "Failing to hold back spending one fourth of your monthly allowance on a single Frappe, you swipe your card and watch as the barista skillfully crafts your drink."

    na "You imagine what the flavor will be as you grab the cup and walk away from the front counter."

    mc "It looks so good! I'll worry about the cost later, because this is gonna be so worth i-"

    #Drink spill noise, crash

    mc "NO! MY CARAMEL RIBBON CRUNCH FRAPPE!!"

    na "Well, that's rough. After you witness-- with pure agony--  the drink spill, you then look up to see… a pole? And an attractive one at that."

    na "Wait, who would put a pole in the middle of a Hoshibucks{size=-12}©{/size}? The pole reaches out a hand to you."

    # Shot with joe and his hand out towards camera in hoshibucks

    joe "Are you okay?! I'm so sorry, I didn't see where I was going."

    if metJoe == True:
        joe "Hey, I remember you! We met at the [metJoeLocation]."
    
    joe "Drinks from Hoshibucks{size=-12}©{/size} are expensive nowadays."

    joe "Here, let me pay for it. It was my fault anyways."

    mc "No, it's okay! Don't even worry about it, It didn't cost {i}that{/i} much."

    na "You're still a bit irritated due to the fact that it {i}did{/i} in fact cost that much."

    joe "No no no, please, let me! I'd feel bad if I didn't."

    mc "No no no no, I wasn't looking where I was going."

    joe "No no n-"

    na "{b}Enough with the “no no no” talk!{/b}"

    $ joename = "ジョ～"
    joe "Well, anyways, my name's Joe. Nice to meet you! I'm gonna buy a drink for myself anyways, so I'll get us both one."

    mc "I'm [mcname], nice to meet you!"

    na "You let him buy you another Caramel Ribbon Crunch Frappe and have a nice chat at one of the tables."

    joe "Hahaha, you're so funny!"

    joe "Well, anyways, It's getting kind of late. Mind if I take you home?"

    mc "Hmmm... It {i}is{/i} getting kind of dark out..."

    if metRiri:
        $ riris[24] = True
        call riri

    menu:
        "No, leave me alone!":
            jump s41
        "Sure, why not?":
            jump s42

label s25:

    beckham "If you don't go to school, you won't find success. You need to try your best everyday. Now go to detention please."

    mc "Okay..."

    jump s13

label s26:

    na "Actually... does it even matter if it's a date? It's a party! Of course you're going!"

    na "You carefully put the handkerchief and note in your bag and begin to daydream."

    mc "I wonder who's going to be there... I'll have to make lots of friends! Maybe I should try something new to make a good impression..."

    # Door sounds

    mc "Eh? Akimitsu?!"

    na "Chiba Akimitsu, your childhood friend since third grade appears at the desk next to yours."

    kyle "Hey [mcname]! Ahaha, did I surprise you?"

    mc "Mhm! Why are you also in detention?"

    kyle "I knew you'd be here on the first day so I came to keep you company."

    kyle "What were you thinking about before I interrupted you?"

    mc "Nothing much... just this party..."

    na "You take out the handkerchief and note and show Akimitsu."

    na "His eyebrows furrow into a look of concern."

    kyle "A party with... the {i}PANTHER{/i}??? TAKAO ISAMU???"

    kyle "There's no way I'm letting you go alone, [mcname]. A party with yakuza attending? Absolutely not."

    mc "What are you... my dad?"

    kyle "I'm just worried about you! Who knows what those people are like?"

    kyle "Please, let me go with you. Or better yet, don't go at all and we can just hang out."

    if metRiri:
        $ riris[26] = True
        call riri

    menu:
        "Go to the party with Akimitsu":
            jump s28
        "Ditch the party and hang out":
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
        call riri

label s28:
    na "Soon, night falls. You arrive at the party with Akimitsu and head inside."

    na "The party is surprisingly classy. Everyone is dressed nicely, there's a live jazz band, and even an open apple juice bar. You make a mental note of the apple juice bar."

    na "You quickly see Takao Isamu spot you and even slightly move their lips upward."

    na "You can't tell if they're grimacing in pain or perhaps attempting a smile, but either way it's directed towards you."

    na "Akimitsu tenses up and steps closer to you."

    $ sophianame = "高尾、勇"

    sophia "Hey. I've heard a lot about you, [mcname]. I'm Takao Isamu."

    sophia "When I first saw you I wasn't sure the rumors were true, but now I know. You're incredible. What dojo did--"

    kyle "Youseikan. We trained at Youseikan."

    sophia "Ah... Who's this?"

    mc "This is my childhood friend, Chiba Akimitsu."

    sophia "Is that so? Interesting."

    sophia "Anyways, how is the party?"

    na "You start to get the feeling that these two aren't getting along."

    na "So, you must do what any reasonable person would do: ignore one of them."

    if metRiri:
        $ riris[28] = True
        call riri
    
    menu:
        "Ignore Isamu":
            jump s30
        "Ignore Akimitsu":
            jump s32
        "Ditch both for apple juice":
            jump s31

label s29:

    mc "Actually, hanging out sounds fun."

    na "Akimitsu flashes a smile."

    kyle "That's a relief. After school let's go to my pla--{nw}"

    # *phone buzz sounds*

    kyle "Actually... wait..."

    mc "Huh?"

    kyle "Ahhh, sorry. I have a basketball game after school."

    kyle "He says, \"Hey, turns out we're in the finals now because some person with bleached blonde hair just showed up and beat up the team that we lost to. He was saying something about [mcname], you, and a party. Weird, huh?"

    mc "I wonder who that could be..."

    kyle "Right? Well now I can't miss my basketball game... would you mind coming to watch instead?"

    if metRiri:
        $ riris[29] = True
        call riri

    menu:
        "Sure, I'll watch":
            jump s14
        "I'd rather party":
            jump s33

label s30:

    mc "The party's good.{nw}"

    na "You say, proceeding to turn and face Akimitsu."

    mc "Hey... should we get going?"

    sophia "Wait. Would you like to get drinks with me?"

    na "{i}{color=#b0b0b0}{size=-6}{cps=10}*Narrator gasps*{/cps}{/size}{/color}{/i}"

    menu:
        "You know what? Sure.":
            jump s35
        "No, I have plans with Akimitsu":
            jump s36

label s31:

    mc "The party's good.{nw}"

    na "You say. And then you run and escape to the apple juice bar."

    #Bar scene

    mc "Apple juice please~"

    beckham "May I ask what type of apple you prefer? Honeycrisp? Fuji?"

    mc "Umm... Gala please."

    beckham "Coming right up."

    na "Never before have you tasted such a sweet, succulent drink."

    na "You down glass after glass until your tummy can take it no longer. Delicious."

    na "Then you go home."

    if metRiri:
        $ riris[27] = True
        call riri

    jump s43

label s32:

    mc "The party's good."

    mc "I just wish I was being escorted by someone since I've been so lonely by myself."

    sophia "Want me to help you?"

    kyle "Hey, hey... wait. [mcname], please."

    kyle "Don't do this... let's just get drinks. Just the two of us."

    na "{i}{color=#b0b0b0}{size=-6}{cps=10}*Narrator gasps*{/cps}{/size}{/color}{/i}"

    menu:
        "Sounds good to me!":
            jump s34
        "No thanks, I'm going with Isamu":
            jump s37

label s33:

    na "You shake your head solemnly"

    mc "Sorry, Akimitsu. I changed my mind. The party never stops."

    kyle "But you just said we would han--{nw}"

    # Door closes

    na "You leave."

    kyle "Wait! Wait! If you're that determined to go to the party I'll go with you. I'll skip my game."

    kyle "Let's just go together, okay?"

    if metRiri:
        $ riris[33] = True
        call riri

    jump s28

label s34:

    mc "Ah, okay! Sounds good to me."

    na "Akimitsu lets out a deep breath as Isamu silently slips away into the crowd."

    kyle "Whew... I thought you were going to ditch me for a second."

    kyle "Wanna go find that open apple juice bar again?"

    na "After finding the bar and getting your apple juice, the two of you begin to reminisce."

    na "You think about the dojo and your childhood."

    na "How Akimitsu has always been there for you, even writing letters to you after you moved away."

    na "He hasn't changed a bit has he? It's almost like this whole time he's been waiting for you..."

    kyle "Hey... it's getting a little stuffy in here. Wanna go somewhere else?"

    jump s40

label s35:

    mc "Sure!"

    kyle "What?? Wait... what?!?!"

    sophia "Heh. Let's go then."

    if metRiri:
        $ riris[35] = True
        call riri

    jump s38

label s36:

    mc "I'm good. I was planning to spend time with Akimitsu tonight."

    na "Isamu glares coldly at you both."

    sophia "Hmph."

    kyle "I actually... was also thinking of getting drinks with you, [mcname]."

    menu:
        "Sounds good to me!":
            jump s34

label s37:

    mc "Sorry~ I've already got plans."

    mc "I'll see you later Akimitsu!"

    kyle "But..."

    kyle "Actually, fine. Do what you want. I don't care."

    na "Akimitsu storms off. His hot fury combined with his blazing looks briefly set another guest on fire, but the flames are doused quickly with some apple juice."

    sophia "Heh. Let's drink something ourselves too."

    if metRiri:
        $ riris[37] = True
        call riri

    menu:
        "Go get drinks with Isamu":
            jump s38
        "Actually... no thanks":
            jump s39

label s38:

    na "As you and Isamu start to go towards the bar you hear a brief shattering sound."

    # Shattering noise

    mc "Ah. I think Akimitsu may have accidentally kicked the door down."

    mc "That's a bad habit of his. He tends to do it when he leaves houses."

    sophia "Don't we all?"

    mc "Hey! Bartender! Get me your most appley apple juice."

    beckham "Of course."

    na "After hours of discussing fighting techniques and the best way to throw someone out a window, you run out of apple juice."

    beckham "I'm sorry, we don't have any more apples to juice. It's a true tragedy for which I am very sorry Takao-sama."

    sophia "Eh, whatever. Hey, [mcname], wanna take break outside? It stinks of granny apples here anyway."

    mc "Sure."

    na "The two of you step outside."

    #Scene change

    na "You find yourself on a balcony overlooking Shizuoka."

    na "The wind softly blows through your hair and the lights of the city sparkle in the distance."

    sophia "To be honest... I didn't think you'd come with me."

    mc "Huh? Why?"

    sophia "My family is yakuza. Ordinary people are usually too afraid of getting hurt. But you're... different."

    sophia "When you threw those three delinquents out the window you reminded me of my cat, Skull Crusher."

    sophia "And I love cats... and I love... you."

    mc "I... I like you too."

    na "Soon after Takao Isamu's confession the two of you start dating."

    na "It's a surprisingly healthy and loving relationship-- you meet {i}The Family{/i}|, go on lots of dates, and work through conflicts together."

    na "Eventually you decide to open a cat cafe together... but... it is no ordinary cat cafe."

    na "Through years of discipline and training, blood and tears, your cat cafe becomes the base for a new group of cat yakuza: {i}Nyanken{/i}."

    na "It is through Nyanken that you wage the Great Cat War, rise through the ranks, and become the most powerful yakuza couple in the nation."

    na "No one can stop your bulging muscles or your untouchable love!...  Nya~"

    jump e5

    # not done

label s39:

    na "Romance? {i}{color=#b0b0b0}{size=-6}{cps=10}*scoff*{/cps}{/size}{/color}{/i} That's for weaklings."

    na "You don't need any of these weirdos, you just came for the party."

    na "But the party sucks so..."

    mc "Actually... I'm good."

    sophia "...Huh?"

    na "You flip your hair and strut out the door."

    scene city night
    na "As you walk you radiate power and confidence. Is this the power of self-worth?"

    na "In fact, the aura from your strut is so strong that it catches the attention of a modeling agent."

    show beckham agent normal at jumper
    beckham "Wait! I'm a modeling agent who also likes attending high school parties hosted by yakuza. You should join my agency! You're incredible!"

    mc "Okay."

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

    mc "Okay!"

    # Switch to bench

    kyle "..."

    mc "..."

    kyle "..."

    mc "It's really cold out here."

    kyle "Maybe we shouldn't have sat down."

    mc "Yeah, that was kind of stupid."

    kyle "Do you want my jacket?"

    mc "No it's okay, you can keep it."

    kyle "Oh. Uh, okay."

    mc "..."

    kyle "..."

    mc "..."

    kyle "Have you ever wondered what the stars would say if they could talk?"

    mc "Haha, n--{nw}"

    kyle "I think they'd tell us the world's secrets. Why we're here, what we're meant to become, and how we might get there."

    kyle "Sometimes I feel lost. Like I'm just falling through time with no real purpose."

    kyle "But there are moments when this light reaches out to me."

    kyle "It tells me that I have something to give. That I have something to offer to this cold world."

    kyle "This light tells me to keep going, keep trying, and keep living."

    kyle "And I've found [mcname], that it's when I'm with you that this light is most prevalent."

    kyle "You're like my star, [mcname]. And that's why… I love you."

    mc "I..."

    jump e4

label s41:

    mc "No thanks, I can make it by myself. Nice meeting you though!"

    joe "Oh okay... I guess I'll see you later then."

    na "You had to get home quick anyways. You haven't been catching up on this season's anime!"

    na "You dart out of the Hoshibucks, not even thanking him for buying your drink before leaving. Bold."

    jump s43
 
label s42:

    mc "Sure, why not? I live just 10 minutes down the road."

    joe "Perfect! I'm going the same direction. Come on, let's get moving!"

    na "You leave the Hoshibucks with Joe."

    na "It almost looks like you two are going on a date, hehe!"

    na "Alright now, what will you talk about for maximum romance?"

    menu:
        "Talk about Hoshibucks":
            jump s44
        "Talk about hobbies":
            jump s45
 
label s43:

    # At home

    na "You sit down in front of your television to watch anime."

    na "For some strange reason you feel empty and alone, like there is a dark hole in your heart."

    na "Maybe it's because Fanana Bish is on? You change the channel."

    mc "Ahh... that's better. Now I can go on with my day and never have to worry about romance agai- {i}{color=#b0b0b0}{size=-6}{cps=10}*yawn*{/cps}{/size}{/color}{/i}"

    mc "Suddenly... {color=#b0b0b0}I feel... {cps=15}{size=-6}very... {size=-8}{cps=5}sleepy.{/cps}"

    na "In the corner of your eye you see a tiny magic wand waving at you from behind the couch. Is that..."

    if metRiri:
        $ riris[43] = True
        call riri
    
    mc "Eh?! What's going on?"

    #Reset with loading screen or something

    jump start
 
label s44:

    mc "So, do you go to Hoshibucks often?"

    joe "Yes! In fact, I go almost every day after school! I live for Hoshibucks, haha!"

    mc "Wow, that's cool! I like Hoshibucks, but I don't go very often because it's so expensive."

    joe "True..."

    joe "Well, if you don't go to hoshibucks often, what do you do in your free time?"

    mc "Well, other than studying and extracurriculars, I like going to to the beach."

    joe "Really? Me too! It's such a nice way to unwind after a long day."

    na "I think this guy just wants something to do with you… he probably spends all day in Hoshibucks."

    joe "Well, if you're ever free, we should go to the beach together."

    mc "Okay, sure! How does tomorrow sound?"

    joe "{color=#b0b0b0}{size=-5}I guess I can go one day without my caramel frappe... for [mcname]...{/size}{/color}"

    joe "Sounds good! I'll be looking forward to it! {i}{color=#b0b0b0}{size=-6}{cps=10}*wink*{/cps}{/size}{/color}{/i}"

    if metRiri:
        $ riris[44] = True
        call riri
    
    jump s46
 
label s45:

    mc "So, what do you like to do in your free time?"

    joe "Well, other than going to hoshibucks, I guess I go to the beach sometimes."

    mc "Really? Me too! I love the beach."

    joe "Is that so? It's such a nice way to unwind after a long day, right?"

    mc "Right? The water feels so nice, especially in the summer."

    joe "Well, if you're ever free, we should go to the beach together."

    na "Wow, I didn't see that coming! What a slick way to ask you out..."

    gwyn "Okay, sure! How does tomorrow sound?"

    joe "{color=#b0b0b0}{size=-5}I guess I can go one day without my caramel frappe... for [mcname]...{/size}{/color}"

    joe "Sounds good! I'll be looking forward to it! {i}{color=#b0b0b0}{size=-6}{cps=10}*wink*{/cps}{/size}{/color}{/i}"

    if metRiri:
        $ riris[44] = True
        call riri
    
label s46:

    na "The next day, you and Joe make plans to go to the beach together."

    na "The way he talks to you... I think he likes you, ya know!"

    na "Anyways... After school, you meet up with Joe at the beach."

    joe "Hey, [mcname]! It's nice to see you again. You look good!"

    na "Well, that was fast."

    mc "Oh, thanks! Nice to see you too!"

    beckham "Ehem, lovebirds!"

    joe "Excuse me?"

    beckham "Sorry to interrupt, but the currents are very strong today."

    na "This guy {i}again?{/i}"

    beckham "I recommend staying out of the water, for your own safety."

    beckham "Rest assured, I can save you, of course, but please be careful. Have a good day at the beach!"

    joe "Oh, okay. What do you think, [mcname]? Should we still swim?"

    if metRiri:
        $ riris[46] = True
        call riri
    
    menu:
        "Go swimming! That lifeguard can't stop you!":
            jump s47
        "Walk on the beach instead":
            jump s48
 
label s47:

    mc "Let's go swimming! That's what I came here for."

    joe "Alright, as long as you're careful. I don't want you to get hurt."

    mc "Oh, I'll be fine! I'm more worried about you, hehe!"

    joe "Hey! I'm a great swimmer, I promise!"

    mc "If you say so!"

    na "Enough flirting! I'm skipping to the part where you actually swim."

    # Switch to water

    na "Ahh, finally... but wait, is Joe okay?"

    joe "Hey, I can't touch the ground here! I'm getting pulled out! Someone save me!!!"

    joe "I'll admit it, I don't go to the beach very often! I prefer caramel frappes, okay!? {i}{color=#b0b0b0}{size=-6}{cps=10}*crying*{/cps}{/size}{/color}{/i}"
 
    if metRiri:
        $ riris[47] = True
        call riri
    
    menu:
        "The lifeguard can deal with it":
            jump s49
        "Oh no, my love! Save him!!!":
            jump s50

label s48:

    mc "Maybe we should just take a walk on the beach for today."

    joe "Okay, sounds good. I'd love to take a walk together."

    # MC Blushes
    mc "We'll have other opportunities to go swimming together anyways..."

    na "Aww, look at you two!"

    na "You take a nice walk and talk about various things, from hoshibucks, to school, to more hoshibucks, and eventually..."

    joe "You know, name, there's something I should tell you..."

    mc "Yes?"

    joe "Ever since I saw you in hoshibucks, I've thought you are the most beautiful person I've ever seen."

    # Whispering:
    joe "Maybe even more beautiful than a caramel frappe..."

    joe "But, anyways, I want you to know that..."

    joe "I think... I love you."

    na "How adorable."

    mc "Joe... I think I love you too."

    joe "You've lightened up my life since we met..."

    na "As in yesterday?"

    joe "And I want you to be the light in my life forever."

    # Gwyn giggles
    mc "I can do that..."

    na "Aww, what a cute couple you make. Good job [mcname]!"

    jump e2

label s49:

    na "You wave your arms until the lifeguard notices Joe struggling."

    na "He rushes out to save Joe!"

    na "He doesn't seem to be paying attention to you though..."

    na "You manage to make it to shore safely, and see the lifeguard performing CPR on an unconscious Joe."

    mc "I've never seen someone perform CPR, but doesn't that seem a little... much?"

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

    mc "Is this what I get for not saving you, Joe?"

    joe "I'm sorry, [mcname]..."

    na "Well, that's that, I suppose..."

    jump e1
 
label s50:

    smc "Don't worry Joe, I'll save you!"

    na "Despite your best efforts, you end up both getting swept away by the current."

    joe "I'm so sorry, [mcname]. This is all my fault..."

    smc "It's okay... I don't want to live if it's without you."

    na "How romantic."

    joe "[mcname]"

    smc "...?"

    joe "I... love you."

    joe "I need you. You are the light in my darkness, the sand on my beach, and..."

    joe "The caramel crunch whipped cream on my caramel frappe."

    joe "You are everything to me, [mcname]."

    na "Wow, this guy really has a way with words."

    na "But, before, you can respond, you are knocked unconscious by a huge wave."

    na "Is this how you die?"

    na "{cps=1.5}...{/cps}"

    na "Just kidding. You wake up on a deserted island with Joe laying by your side."

    # Opens eyes

    joe "[mcname]! You're awake! I got this coconut for you. Please, drink from it!"

    joe "Apparently, Hoshibuck's pink drinks are made with coconut milk, so I thought it must help."

    na "You can feel your burnt skin and pain all over your body, but the coconut does help."

    smc "Thank you, I feel much better. Where are we?"

    joe "It's been a few hours since we washed up on this island. I don't know if anyone will ever come for us."

    smc "Oh... well, we have each other, don't we?"

    na "You take Joe's hand and look into his eyes."

    joe "Maybe, if I have you by my side everyday, I can live without hoshibucks."

    smc "Aw, Joe..."

    na "{i}{color=#b0b0b0}{size=-6}{cps=10}*sigh*{/cps}{/size}{/color}{/i} There he goes again."

    na "You live the rest of your lives together, surviving on the island and its natural resources."

    na "What a happy ending..."
    
    jump e3
 
label s51:

    # English class scene

    na "You arrive at your English class. You could have had something fun, like Japanese. But {i}English?{/i}"

    na "You take a seat and get ready to listen to the teacher's lecture."

    na "Right when they start talking, you start feeling very tired. Perhaps a nap wouldn't be too bad..."

    na "You fall into a deep slumber, and dream of a high school life where {i}you{/i} are the main character."

    # Dream scene

    na "As you walk to the front gates of the school in your dreams, you notice four ikemens waving at you from one of the classrooms. They seem to be trying to say something."

    mi "{i}Heeeeey...{/i}"

    teacher_e "Hey, [mcname]!"

    # Back to classroom scene

    na "Suddenly, you feel a sharp pain on your forehead. A piece of chalk then drops onto your desk."

    teacher_e "Would you like to come up to the board and answer the question?"

    mc "Uhhh... What question?"

    teacher_e "{i}{color=#b0b0b0}{size=-6}{cps=10}*sigh*...{/cps}{/size}{/color}{/i} I have it written right here. What is [quizWord] in Japanese?"


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

    mc "He must be the leader of the student council! I should ask him about signing up!"

    mc "Excuse me, sir?"

    na "The student looks up with a puzzled expression on his face."

    jt "Me? Wow, sir is a new one... Do I really look that good?"

    mc "Oh, you're just well dressed is all..."

    jt "Anyways, what do you need?"

    mc "Well, I saw the poster looking for people to join the student council, and I decided to check it out. Can I sign up?"

    $ jtname = "Yutaka Yanai"
    jt "Of course! I'd be delighted to have you on our student council team. My name is Yutaka Yanai, nice to meet you!"

    na "Yutaka pulls out a book's worth off papers from his cabinet."

    jt "All you have to do is sign all these documents, and then you can get started."

    mc "Oh wow, alright."

    na "It takes the whole school day, but you eventually finish filling out all the documents."

    na "Besides some documents mentioning that the student council will have complete ownership of your loved ones, prized possessions, free time, and soul, you aren't worried about what you are signing up for."

    na "When you are finally done, you hand them all back to Yutaka."

    jt "Congratulations! You are now an official member of the student council. I'm excited to work together~"

    mc "Thank you! I'll do my best!"

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
        call riri
    
    menu:
        "Go to the address":
            jump s58
        "Study alone in the library":
            jump s59
 
label s54:

    na "You swiftly write the answer up on the chalkboard."

    teacher_e "That's correct [mcname], good job. It wouldn't look good if you got that wrong, that was one of the easier ones."

    na "What a downer... You proudly walk back to your seat and listen to the rest of the lesson."

    teacher_e "Alright everyone, we are going to be starting an English project using the vocabulary we learned. Please get with a partner and make a video by this Friday."

    na "You instantly realize that getting with a partner brings up a big issue..."

    na "...you have no friends."

    na "You notice someone sitting in the back of the classroom. Wanna try grouping with them?"

    menu:
        "Ask to group with them":
            jump s56
        "Nah, I'm good":
            jump s55
 
label s55:

    na "You're gonna have to group with somebody..."

    na "Hey, look, someone's walking up to you!"

    jt "Hey, I'm Yukata! You seem pretty cool, want to work together?"

    mc "Oh, sure! What should we do?"

    jt "I was thinking a love story could be pretty fun..."

    na "Something is fishy here..."

    mc "Oh, uh, sure, that could be fun!"

    jt "Alright, it's settled then! Meet me at my house after school to work on it."

    # At Yutaka's house

    na "That night, you head over to Yukata's house."

    na "Well, more like Yukata's castle. This thing is massive!"

    na "Anyways, you spend hours with Yukata, and eventually finish the project."

    jt "Whew! That's the last scene!"

    mc "Yes! We did it!"

    jt "Well, I guess you should start heading back soon..."

    jt "It was... really fun to work together."

    mc "Yeah! I had a lot of fun too. Well, see you tomorrow!"

    na "Well, although Yuata presents as snobby, he really is nice on the inside."

    na "And it seems like he really cares about you... hehe!"

    na "Ahem, anyways, the next day in class..."

    # In class the next day

    teacher_e "Next we have... Yukata and [mcname]'s project."

    jt "Ah yes, our masterpiece is finally being shown!"

    mc "Here we go..."

    na "As the teacher shows your project, you can here your classmates murmuring."

    na "As you thought, they're suspicious. Your project seems a little too romantic..."

    teacher_e "Comments?"

    # Unfinished

label s56:

    na "You walk up to the student's desk."

    mc "Hey, do you have anyone to group with?"

    maryam "N-no!"

    mc "Would you like to work together on this project?"

    maryam "S-Sure!"

    na "You realize that your room is a mess, you probably wouldn't want them seeing that."

    mc "can I come over to your house tomorrow to work on it?"

    maryam "Okay, that works for me!"

    na "You knock on the door, and Haruka answers."

    maryam "Welcome. Make yourself at home. Let's go to my room."

    na "You both go upstairs and enter their room."

 
label s57:

    maryam "I'm going to go get my English work from downstairs... stay here for a little."

    na "You sit down and get under the kotatsu positioned in the middle of the room."

    mc "Aaa~ It's so warm~"

    na "As you look around the room, you can see many pieces of hanging tape on the walls surrounding their bed. Did they take those down recently?"

    na "Looking a bit more, you notice a small shiny object on the floor near the other side of the kotatsu."

    # Gwyn talking to herself

    mc "Ooo~ shiny! Hmmm... Isn't this my ring that I lost? I thought it was gone forever!"

    mc "They found it and never gave it back?! So rude!"

    mc "Hold on a minute..."

    if metRiri:
        $ riris[57] = True
        call riri
    
    menu:
        "Maybe they were planning to give it back":
            jump s61
        "Something's fishy around here...":
            jump s60
 
label s58:

    na "You walk up to the door of the address posted on the flier with no worries in your mind."

    scene door
    na "You then hear some noises coming from the house, like someone is frantically trying to clean up."

    show maryam normal
    maryam "H- Hello... Are you here for the English lessons?"

    mc "Yep! I saw your flier next to the library!"

    maryam "A- Alright... Come on in..."

    na "As you walk inside, you see Haruka running up the stairs ahead of you. You reach the second floor and see a door slam shut down the hallway."

    # Knock knock

    mc "Hey, is everything alright?"

    maryam "Just one minute...!"

    na "You give they a minute, and they eventually opens the door, silently signaling you to enter the room."

    jump s57
 
label s59:

    na "Yeah, it sounds a little too risky."

    mc "I think I'll just study alone in the library today..."

    na "You spend all day studying English in the library, until you are fully satisfied that you have memorized that word."

    mc "Finally! Ahh, I'm exhausted. Time to head home and watch some anime..."

    jump s43
 
label s60:

    mc "Hey, I noticed the ring in your room looks familiar, where did you get it?"

    na "You notice that Haruka starts looking a little nervous."

    maryam "...From a shop."

    mc "Oh, haha! I must be wrong."

    na "You put the ring back on the kotatsu. You start feeling a little uneasy. Maybe working in the safety of your home would be a better idea."

    mc "Do you think we could go to my house to work tomorrow?"

    maryam "Yeah, sure..."

    # New day, at MC house

    na "Haruka arrives at your house, ready to work on the English project."

    mc "Alright, let's get to work!"

    na "Haruka takes their computer out and starts typing right away."

    na "Hmmm... Maybe they're using a Hotspot? You've never given them your Wi-Fi."

    mc "Hey, do you need my Wi-Fi password? You don't have to use data."

    maryam "No-- I mean yes! Yes please!"

    mc "Right... Could I have the computer to put it in?"

    maryam "No! ...I can put it in it myself."

    na "they're acting like they already have your Wi-Fi password. With this and the ring that you found, things are getting awfully suspicious..."

    if metRiri:
        $ riris[60] = True
        call riri

    menu:
        "Test them to see if they know the password":
            jump s63
        "Pshh, it's probably fine!":
            jump s64
 
label s61:

    na "You decide not to think too much of it and start to take out your English work."

    # Door noise

    maryam "Hey, I'm back. Do you have everything?"

    mc "Yep! But why is nobody else here? I even arrived thirty minutes late."

    na "You notice their eyes starting to drift away from you as they respond."

    maryam "Yeah uh... The English problem was pretty specific. Maybe there was j-just nobody else that needed help."

    maryam "Anyways... do you want to-{nw}"

    na "Haruka glances to the floor next to you."

    na "They quickly walk over to the other side of the kotatsu and sit down, grabbing the ring."

    maryam "Would you like to start?"

    mc "Okay!"

    na "You and Haruka work through your English for hours until you finally feel confident about your skills."

    # MC stomach rumbles

    maryam "You want to finish up? We could go eat something after."

    mc "Sounds good!"

    na "You and Haruka clean up and start to walk out the door to go eat."

    jump s62
 
label s62:

    mc "Where would you like to go?"

    maryam "Have you been to Hoshibucks before?"

    mc "Yes! I love Hoshibucks!"

    # In Hoshibucks

    na "In the Hoshibucks line, Haruka notices that they forgot their wallet."

    maryam "Oh no! I forgot my wallet!"

    mc "It's alright, I'll buy you a sweet treat because you helped me so much with the English project!"

    na "Haruka's eyes widen, they are entranced by your generosity and kindness."

    maryam "Thank you so much, [mcname]!"

    na "As you both order the sweet treats and sit down, Haruka seems nervous as if they something important to tell you."

    maryam "uhm... [mcname]... I have something to tell you..."

    mc "Yes, Haruka?"

    maryam "I've liked you ever since we had art together freshman year of highschool!"

    na "You guys went to the same freshman class? How do they even--{nw}"

    maryam "When you gave me your extra pencil right before the final test, I knew you were the one for me! Would you like to go on a date with me?"

    mc "I would love to!"

    jump e8
 
label s63:

    na "You decide to test Haruka."

    mc "Alright then, the password is 123456."

    na "the real password is actually 1234567..."

    maryam "Perfect! I connected! L-let's get to work shall we?"

    na "You go silent, how could they possibly know your wifi password?!"

    maryam "[mcname], are you a-alright? You're awfully quiet."

    na "Your heart starts to race, Haruka has noticed your changed demeanor."

    mc "Ahaha actually, I don't feel very well at the moment, maybe we could continue another day?"

    maryam "Oh, alright, I see."

    na "Haruka hastily grabs their stuff and goes home. Anxiety is rushing through your veins, how could they have known your wifi password?!"

    # New day at school

    na "You and Haruka plan on finishing the project later that day, but then you notice a handsome figure approaching..."

    kyle "Hey naninani, I was wondering if you would like to come hang out with me after school...if you're not busy of course."

    na "Haruka's demeanor suddenly changes."

    na "Hmm, you were originally going to wrap up that project with Haruka though..."

    if metRiri:
        $ riris[63] = True
        call riri
    
    menu:
        "That project can wait! Hang out with Akimitsu instead":
            jump s65
        "Nah, we have to finish this project.":
            jump s66
 
label s64:

    mc "Alright then, the password is 1234567."

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
        call riri

    menu:
        "Call the cops!":
            jump s69
        "Don't call the cops":
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

label e13:
        

        





        










return