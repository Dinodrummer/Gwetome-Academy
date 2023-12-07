# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image vid = Movie(play="audio/5-6.webm", size=(1920,1080),loop=False, xalign=0.10, yalign=0.10)
#--------------
image zeil normal:
    "images/zeil normal.png"
    zoom 0.8
# --------------------------------------------------------
init:
    define mc = Character("[mcname]", color = "#43BC47")
    define na = Character("")
    define mom = Character("Mom")
    define sensei = Character("先生 (Sensei)")
    define beckham = Character("マリオ")
    define joe = Character("[joename]") # define joe = Character("ジョ~")
    define kyle = Character("[kylename]") # define kyle = Character("千葉、昭光 (Chiba, Akimitsu)")
    define jt = Character("[jtname]") # define jt = Character("柳井、富 (Yanai, Yutaka)")
    define sophia = Character("[sophianame]") # define sophia = Character("高尾、勇 (Takao, Isamu)")
    define maryam = Character("[maryamname]") # define maryam = Character("木山、遥花 (Kiyama, Haruka)")
    # define zev = Character("...") # define zev = Character("ゼブ")

    define mi1 = Character("Magical Ikemen 1")
    define mi2 = Character("Meowgical Ikemen 2")
    define pp = Character("PyunPyun")
    define takeshi = Character("Takeshi")
    define dr = Character("Dr.")

    define riri = Character("リリ")
    define mv = Character("{i}Mysterious Voice")

    define d1 = Character("Deliquent 1")
    define d2 = Character("Deliquent 2")
    define d3 = Character("Deliquent 3")

    # image beckham agent normal = "/images/Zeil/ph.png"
    # image beckham agent ecstatic = "/images/Zeil/ph.png"
    # image beckham bartender normal = "/images/Zeil/ph.png"
    # image beckham bartender angry = "/images/Zeil/ph.png"
    # image beckham bartender sad = "/images/Zeil/ph.png"
    # image beckham fan normal = "/images/Zeil/ph.png"
    # image beckham fan ecstatic = "/images/Zeil/ph.png"
init python:

    riris = []
    for i in range(100):
        riris.append(False)

    char_left = Position(xpos=0.18, ypos=0.75)
    basketballSong = "bgm_basketball.mp3"
    sfxBell = "sfx_bell.mp3"
    bgSong = "bgm_skipABeat.mp3"
    config.auto_voice = "voice/{id}.mp3"

    metRiri = False

    mcname = "..."
    joename = "..."
    kylename = "..."
    jtname = "..."
    sophianame = "..."
    maryamname = "..."

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
    mc "Man, is it just me, or am I... {color=#808080}getting... {size=-6}a {nw}"
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
    return
# -------------------------------------------------------------------------------------------------------------------
# s1 = start
# voice voice.mp3
label start:
    show beckham agent ecstatic
    $ mcname = renpy.input("What is your name?")
    $ mcname = mcname.strip()
    $ mcname = mcname[0:13]
    
    jump s28

    if mcname == "":
        $ mcname = "Naninani Nantoka"

    mc "I'm so tired... I stayed up all night playing otome games."#Gwyn1
    
    mc "It`s hard not to when you`re given so many choices, especially when you can punch the male leads. Hehehe!"#Gwyn2

    mc "Oh wait! I forgot to introduce myself. My name is {u}[mcname]{/u}!"#Gwyn3

    mc "I'm sixteen. Today is my first day of my second year at Gwetome Academy."#Gwyn4

    mc "Ever since my family moved back to Shizuoka, I've been living my high-school life to the fullest."#Gwyn5

    mc "During my time here, I've come to learn that love isn't the only important thing in life. 
        I'm my own person, with my own goals and dreams, and I'm proud of that. I am independent and strong!"#Gwyn6

    mc "...and I'm late for school."#Gwyn7

    menu:
        "Go downstairs and get ready for school":
            jump s2
        "Sleep in just a liiitle longer":
            jump s3
    return

label s2:

    na "You put on your uniform and go downstairs."#JT3

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

    na "You check your phone and see you have more time than you realized. Maybe you'll just quickly look up the information about 
        Magical Ikemen's new season while you walk... you have the time after all."#JT11

    na "Plus, you need to know whether or not Takeshi finally leaves his office job to pursue his dream
        of becoming a full-time magical girl in the Kiss Kiss Love Power Team."#JT12

    na "As you scroll through the wonderland that is the Magical Ikemen online forum, you bump into a pole. Ouch."#JT13

    na "Wow, that's a strangely attractive pole. And it's wearing a... Gwetome Academy uniform!? The pole turns around."#JT14

    joe "Ah sorry, I was walking kind of slow. Are you ok?"#Joe1

    joe "A lot of people bump into me so my back muscles have become hard like metal. My doctor said it's because I tend to draw people in... I'm magnetic."#Joe2

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

    mi2 "Takeshi, we {i}meow{/i} it's a hard decision, but it's one that must be {i}mwade.{/i} {color=#808080}{size=-6}nya~{/size}{/color}"#Joe4

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

    riri "Wrong! I'm Riri. My boss told me there was a weeb here so I came to help."#Joe5

    riri "Wait! Are you Naninani Nantoka!?!?"#Joe6

    mc "Uh. No. I'm [mcname]."#Gwyn13

    riri "Oh how the great have fallen. {i}{color=#808080}{size=-6}{cps=10}*sigh*{/cps}{/size}{/color}{/i} I used to always hear about you at work--"#Joe7

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

    na "Is this what it's like to be in a world with no love? No romance? No ikemens?"#JT36

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

    joe "Oh right! The name's Joe-kun, but you can just call me Joe."

    na "Is that even a name?"

    mc "Well, nice to meet you! My name is [mcname]"

    joe "Wow, what a cool name! I'm jealous."

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

    mc "The final is... here?"

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
    kyle "In honor of this victory, I would like to sing a song. It's dedicated to my favorite person in the world, [mcname]. I love you. {i}{color=#808080}{size=-6}{cps=10}*ahem*{/cps}{/size}{/color}{/i}"
    
    #kyle song

    jump e12



label s15:

    na "You make a scene. How could you resist after all?"

    na "After throwing a few delinquents out the window with your super muscular muscles...{nw}"

    # Sound effects

    na "...Takao Isamu swaggers up to your desk."
    

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
    na "{i}You. Me. Rager party. Tonight? Yes? No? Plz yes. :3 Thank you.{color=#808080} - The Panther{/i}{/color}"

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

        #define jt = Character("柳井、富 (Yanai, Yutaka)")

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

label s23:

label s24:

    #In starbucks

    mc "I'll take your finest Caramel Ribbon Crunch Frappe, please."

    na "You felt like you've seen this kid before. Maybe from school?"

    beckham "that'll be 2,210¥."

label s25:

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

    d1 "{i}{color=#808080}{size=-6}{cps=10}*gasp*{/cps}{/size}{/color}{/i} No way!"

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

    sophia "When I saw you I wasn't sure the rumors were true, but now I know. You're incredible. What dojo did--"

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

label s30:

    mc "The party's good.{nw}"

    na "You say, proceeding to turn and face Akimitsu."

    mc "Hey... should we get going?"

    sophia "Wait. Would you like to get drinks with me?"

    na "{i}{color=#808080}{size=-6}{cps=10}*Narrator gasps*{/cps}{/size}{/color}{/i}"

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

    na "{i}{color=#808080}{size=-6}{cps=10}*Narrator gasps*{/cps}{/size}{/color}{/i}"

    menu:
        "Sounds good to me!":
            jump s34
        "No thanks, I'm going with Isamu":
            jump s37

label s33:
    # not real

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

    # not done

label s39:

label s40:

label s41:
 
label s42:
 
label s43:

    na "You sit down in front of your television to watch anime."

    na "For some strange reason you feel empty and alone, like there is a dark hole in your heart."

    na "Maybe it's because Fanana Bish is on? You change the channel."

    mc "Ahh... that's better. Now I can go on with my day and never have to worry about romance agai- {i}{color=#808080}{size=-6}{cps=10}*yawns*{/cps}{/size}{/color}{/i}"

    mc "Suddenly... {color=#808080}I feel... {cps=15}{size=-6}very... {size=-8}{cps=5}sleepy.{/cps}"

    na "In the corner of your eye you see a tiny magic wand waving at you from behind the couch. Is that..."

    if metRiri:
        $ riris[43] = True
        call riri
    
    mc "Eh?! What's going on?"

    #Reset with loading screen or something

    jump start
 
label s44:
 
label s45:
 
label s46:
 
label s47:
 
label s48:
 
label s49:
 
label s50:
 
label s51:
 
label s52:
 
label s53:
 
label s54:
 
label s55:
 
label s56:
 
label s57:
 
label s58:
 
label s59:
 
label s60:
 
label s61:
 
label s62:
 
label s63:
 
label s64:
 
label s65:
 
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

label e0:

label e1:
    
label e2:

label e3:

label e4:
    
label e5:

label e6:

label e7:

label e8:

label e9:

label e10:
    
label e11:

label e12: #Love in the Basket

label e13:




        

        





        










return