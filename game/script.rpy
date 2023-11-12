# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



image vid = Movie(play="audio/5-6.webm", size=(1920,1080),loop=False, xalign=0.10, yalign=0.10)

image zeil normal:
    "images/zeil normal.png"
    zoom 0.8
image gym:
    "images/bg gym.jpg"
    zoom 1.5
# --------------------------------------------------------
init python:
    char_left = Position(xpos=0.18, ypos=0.75)
    preferences.text_cps = 20
    basketballSong = "bgm_basketball.mp3"
    sfxBell = "sfx_bell.mp3"
    bgSong = "bgm_skipABeat.mp3"
    config.auto_voice = "voice/{id}.mp3"
    mcname = "..."

define mc = Character("[mcname]", color = "#43BC47")
define na = Character("")
define mom = Character("Mom")
define joe = Character("ジョ~")

define mi1 = Character("Magical Ikemen 1")
define mi2 = Character("Meowgical Ikemen 2")
define pp = Character("PyunPyun")
define takeshi = Character("Takeshi")
define dr = Character("Dr.")


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

# -------------------------------------------------------------------------------------------------------------------
# s1 = start
# voice voice.mp3
label start:
    $ mcname = renpy.input("What is your name?")
    $ mcname = mcname.strip()

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
            jump p
        "Watch Magical Ikemen":
            jump p

label s3:

    na "You crawl into your covers again and begin to sleep blissfully; everything is cozy, warm, and peaceful. You begin to dream."#JT7

    na "It's your first day of school at Gwetome Academy. Everyone is calling you Naninani Nantoka. 
        But why? You've always been [mcname] haven't you? How strange."#JT8

    na "Just as you are about to investigate this, you feel a sudden shake."#JT9

    mom "Hey!...Hey! Get up! How did I end up with such a lazy child?"#

    mom "[mcname], school's already started so you need to hurry! I'm off to work now, so I can't help you. I'm off!"#

    menu:
        "Wake up and go go go!":
            jump p
        "Nahh, I'm sleeping more":
            jump p

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
            jump p
        "Try to talk to the ikemen":
            jump p

label s5:

    na "The TV has summoned you and you must answer its call. As you sit down on the couch, you see the familiar face of the main character, Kimura Takeshi."#JT18

    na "It looks like he's having a serious talk with the Kiss Kiss Love Power Team, a magical-girl group that saves the world from evil monsters."#JT19
    
    na "During the last episode, Takeshi was deciding whether or not to keep his office job or pursue his dream of becoming a full-time magical girl. 
        He must be discussing this with them now."#JT20

    mi1 "Takeshi… you must make a choice. If we wait any longer, the Dr. will find out your true identity. Either join us or leave us."#

    pp "Pyun!"#

    takeshi "But--{nw}"#

    mi2 "Takeshi, we {i}meow{/i} it's a hard decision, but it's one that must be {i}mwade.{/i} {color=#808080}{size=-6}nya~{/size}{/color}"#

    takeshi "But… but… what if I'm not cut out to be on the Kiss Kiss Love Power Team? 
        What if I'm not a real magical-girl? If I fail… I can't ever return. Please, give me more--"#

    #explosion/crash + helicopter sounds
    #PyunPyun falls

    pp "Pyuuuuuuuuuuun~"#

    mi1 "NO! PYUNPYUN!"#

    #Through a megaphone:

    dr "HUEHUEHUEHUEHUE! I will defeat you all one by one!"#

    na "Man, they kept the annoying mascot from season 1."#JT21

    na "Jeez"
    










return