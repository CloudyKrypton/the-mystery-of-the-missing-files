# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character(name="Steve", color="#c8ffc8")
define m = Character(name="Mario", color="#c8ffc8")
define d = Character(name="David", color="#c8ffc8")
define f = Character(name="Francois", color="#c8ffc8")
define t = Character(name="Tom", color="#c8ffc8")


label start:

    "Our story begins at the end of a semester, with two CSC258 professors."
    "Steve and Mario have been hard at work, and have finished marking exams and finalizing grades."
    "All that was left to do was to upload the results onto acorn…"
    jump scene1

label scene1:
    scene bg stevesoffice
    show steve normal:
        xpos 1200

    s "Hmm."
    s "Hmmm."

    scene bg stevelaptop
    hide steve

    s "NO FILES FOUND?!"

    scene bg stevesoffice
    show steve horror:
        xpos 1200

    s "Mario, come quick, it’s an emergency! All our files have disappeared!"
    show mario normal:
        xpos 400
    m "What?"
    s "Marked tests, the spreadsheets of student results, the backup folder and the backup backup folder; they’ve all been wiped from the database."
    m "How is this possible?"
    s "It’s a travesty. What are we going to tell the students? Piazza complaints will pile up by the dozens!"
# Shot of hypothetical piazza complaints. (In the video, a vine boom shot sound follows each one.)
    m "Now now, let’s remain calm. I’m sure we can recover the files somehow."
    m "Is there anyone other than you who has access to these computers?"
    s "The whole Teaching Stream Faculty. But the last person who was in here was David."
    m "Then we have a lead."
    hide steve
    hide mario
    jump scene2

label scene2:
    scene bg myhal
    show david normal
    s "Hi David :)"
    m "Hello, David."
    m "We’re here about a couple of missing files. You wouldn’t happen to have interacted with Teaching Machine E recently, have you?"
    d "Gentlemen, hello! Teaching Machine E… *chuckles* why no, I, uh, er, haven’t been near that device in a while!"
    s "Right…"
    d "Lost files, you say?"
    d "Just the other day I made a note about another professor who was mumbling about removing files on a teaching machine."
# Steve and Mario exchange glances.
    d "Ah yes…"
# David pulls out his computer.
    d "Here we are."
    scene bg davidlaptop
    hide david
    d "It seems that I had a lot on my mind that day!"
    d "I may have mixed up thinking about who I spoke to with the lecture material I taught." 
    d "It should be easy enough for you to decipher..."
menu:
    "Francois looks correct.":
        jump scene2a
    "Tom seems about right.":
        jump scene2b
label scene2a:
    scene bg myhal
    show david normal
    s "I think we’ll speak with Francois. Thanks, David!"
    d "No problem, good luck!"
# Steve and Mario turn to go.
    d "Whew."
    hide david
    jump scene3a
label scene2b:
    scene bg myhal
    show david normal
    s "I think we'll speak with Tom. Thanks, David!"
    d "No problem, good luck!"
    d "Whew."
    hide david
    jump scene3b

label scene3a:
    scene bg uc
    show francois
    f "Ah, Mario and Steve! What can I do for you today?"
    m "Unfortunately, we ran into a terrible mishap — all the 258 files on Teaching Machine E have been lost."
    f "Oh no!" 
    s "We were wondering if you had any information on where they could have gone."
    f "Files, files…"
    f "I was just talking to David about removing files on teaching machines last week."
    m "Yes! He told us to come find you."
    f "I had seen some professors remove a mass amount of files on a lab computer earlier that day."
    f "I wanted to ask them more about it today in fact, but they were headed towards a building and I didn't catch them." 
    f "Which one was it again?"
# Francois pulls out his computer.
    f "That’s right! I made a note about it here."
    scene bg francoiscomputer
    hide francois
    jump scene3puzzle
    f "Oh dear, it looks like I mixed up my thoughts with a lecture I was thinking about earlier."
label scene3puzzle:
    f "Right now, the number (12121212222222…) is coming to my mind for some reason."
menu:
    "Definitely Convocation Hall.":
        scene bg uc
        show francois
        s "We'll head to Convocation Hall."
        f "Are you sure? I have a nasty feeling about that one. Why don’t you choose again?"
        scene bg francoiscomputer
        hide francois
        jump scene3puzzle
    "It's Emmanuel College.":
        scene bg uc
        show francois
        s "We'll head to Emmanuel College."
        f "Excellent choice. I felt that one calling to me, too. Best of luck!"
        jump scene4
    "I like the look of Sanford Flemming.":
        scene bg uc
        show francois
        s "We'll head to Sanford Flemming."
        f "Are you sure? I have a nasty feeling about that one. Why don’t you choose again?"
        scene bg francoiscomputer
        hide francois
        jump scene3puzzle

label scene3b:
    scene bg miningbuilding
    show tom
    t "Ah, Mario and Steve! What can I do for you today?"
    m "Unfortunately, we ran into a terrible mishap — all the 258 files on Teaching Machine E have been lost."
    t "Oh no!" 
    s "We were wondering if you had any information on where they could have gone."
    t "No, I haven’t heard anything about lost files. Where did you get that idea from?"
    m "I thought David said—"
    t "He must have been mistaken. What an odd idea."
    t "At any rate. I may have something to help you out."
    scene bg tomcomputer
    hide tom
    jump scene3bpuzzle
    t "Oh dear, it looks like I mixed up my thoughts with a lecture I was thinking about earlier."
label scene3bpuzzle:
    " "
    t "Excellent choice. I felt that one calling to me, too. Best of luck!"
    jump scene4

label scene4:

    return
