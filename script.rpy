
init python:
    def m_text(event, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/m_text.mp3")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    def f_text(event, **kwargs):
        if event == "show_done":
                renpy.sound.play("audio/f_text.mp3")
        elif event == "slow_done" or event == "end":
                renpy.sound.stop()


image ctc_blink:
    "ctc.png"
    linear 0.75 alpha 1.0
    linear 0.75 alpha 0.0
    repeat

define y = Character("Yuko", callback = f_text, ctc="ctc_blink", ctc_position="nestled")
define m = Character(" ", callback = m_text, ctc="ctc_blink", ctc_position="nestled")

label start:
    scene black
    with Fade(0.5, 1.0, 0.5)

    play music "audio/piano.mp3"
    centered "Once upon a time, I dreamt I was a
    butterfly,{w=0.5} fluttering hither and thither,{w=0.5} to all intents and
    purposes a butterfly."
    centered "I was conscious only of my happiness as a butterfly,{w=0.5} unaware that I was myself."
    centered "Soon I awaked,{w=0.5} and there I was,{w=0.5} veritably myself again."
    centered "Now I do not know whether I was then a man dreaming I was a
    butterfly,{w=0.5} or whether I am now a butterfly,{w=0.5} dreaming I am a man."
    centered "..."
    centered "..."
    stop music fadeout 2.0
    centered "..."

    play music "audio/alarm.mp3" volume 0.2
    "..."
    "Ngh... {w=0.5} Damn..."

    scene pc_on
    with Dissolve(2)


    m "What time is it?"
    m "6:00 AM?!"
    m "God... I stayed up late night trying to study for my Mid-terms. {w=0.5} I ended up just sleeping on my chair..."
    m "Man, I can already tell my joints are sore."
    m "I'd better turn off the alarm clock, {w=0.5} It's only making my headache worse."

    menu:
        "Turn it Off":
            play sound "audio/button.mp3"
            stop music
            play music "audio/morning_bgs.mp3"
            m "Finally some peace.{w=0.5} I can already tell this is gonna be a long day."
            m "Maybe I could sneak in a few minutes before she comes in... {w=0.5} to... {w=0.5} wake... {w=0.5} me... {nw}"
            play sound "audio/soft_knock.mp3"
            scene pc_on with vpunch
            m "?!!"
            "???" "“I'm comming in, Okay?”"
            show yuko_neutral with dissolve
            y "..."
            y "“Please tell you me you remembered it was going to rain today...”"
            y "“I told you yesterday that we have to take the 6:30 Bullet Train.
            You know... {w=0.5} since the rain is going to make us late. ”"
            show yuko_neutral with dissolve
            y "..."
            show yuko_upset
            y "“Did you play all night? You didn't even turn off your computer...”"
            m "..."
            y "{i}Sigh{/i} “I thought older brothers were supposed to be the
            responsible ones.”"
            show yuko_neutral
            y "“I'll turn it off, just get ready.”"
            play sound "audio/button.mp3" volume 1.5
            scene pc_off with dissolve
            show yuko_neutral with dissolve
            y "I made breakfast so come out when you're done.”"
            hide yuko_neutral with dissolve


        "Leaving it on":
            m "Eh... I'm too lazy... {w=0.5} to.. {w=0.9} turn...{nw} "
            play sound "audio/loud_knock.mp3" volume 2.00
            scene pc_on with vpunch
            m "?!!"
            "???" "Please turn off you're god damn clock!"
            m "Bruh"
            "???" "“Ugh...{w=0.5} I'm coming in”"
            show yuko_upset with dissolve
            y "..."
            play sound "audio/button.mp3"
            stop music
            play music "audio/morning_bgs.mp3" volume 0.3
            y "“Do I seriously have to do everything for you? ”"
            y "{i}Sigh{/i} “I thought older brothers were supposed to be the
            responsible ones.”"
            show yuko_neutral
            y  "Don't tell me you forgot that it was going to rain today...”"
            y "“I told you yesterday that we have to take the 6:30 Bullet Train.
            You know... {w=0.5} since the rain is going to make us late. ”"
            show yuko_upset
            y "“Did you play all night? You didn't even turn off your computer...”"
            m "..."
            show yuko_neutral
            y "“I'll turn it off, just get ready.”"
            play sound "audio/button.mp3"
            scene pc_off with dissolve
            show yuko_neutral with dissolve
            y "I made breakfast so come out when you're done.”"
            hide yuko_neutral with dissolve

    scene night_bedroom with dissolve
    m "{i}As I look up from my desk I can see the cloud filled sky. It almost seems like a gray blanket has covered all of Tokyo.{/i}"
    m "It really does set the mood, doesn't it?"


    m "{i}looking in the closet trying to find clean uniform but to my surprised all of of them are ironed. {/i}"
    m "{i}Yuko must have done this for me. {/i}"
    m "As get dressed I start to notice my phone ring."


label phone_example:
    call screen phone(phone_conv_1)


label downstairs:
    m "That idiot..."
