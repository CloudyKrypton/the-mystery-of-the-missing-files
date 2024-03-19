# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character(name="Steve", color="#c8ffc8")
define m = Character(name="Mario", color="#c8ffc8")
define d = Character(name="David", color="#c8ffc8")
define f = Character(name="Francois", color="#c8ffc8")
define t = Character(name="Tom", color="#c8ffc8")
define jo = Character(name="Jonathan", color="#c8ffc8")
define ja = Character(name="Jack", color="#c8ffc8")

label start:

    "Our story begins at the end of a semester, with two CSC258 professors."
    "Steve and Mario have been hard at work, and have finished marking exams and finalizing grades."
    "All that was left to do was to upload the results onto acorn…"
    jump scene1

label scene1:
    scene bg stevesoffice
    show steve computer:
        xpos 1100

    s "Hmm."
    s "Hmmm."

    scene bg stevelaptop
    hide steve

    s "NO FILES FOUND?!"

    scene bg stevesoffice
    show steve horror:
        xpos 900

    s "Mario, come quick, it’s an emergency! All our files have disappeared!"
    show mario normal:
        xpos 400
    m "What?"
    show steve normal:
        xpos 900
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
    scene bg vic
    show jonathan normal:
        xpos 400
    show jack normal:
        xpos 1200
    jo "I must say, that bubble tea looks delicious."
    ja "Thank you, a student gave it to me earlier today."
    "*Steve and Mario enter the room*"
    s "Hello!"
    jo "Why, hello!"
    m "Good evening professors."
    m "We’re here to inquire about a mass deletion of files from the Teaching Machines, specifically E."
    ja "Oh, yes. I had recently written 1000 test cases for a bubble tea competition, and a bug in the code accidentally wrote to 1000 files instead…"
    ja "No matter. That all happened on Teaching Machine B, not E."
    ja "What happened to Teaching Machine E?"
    s "Mayhem! A complete loss of all the CSC258 files."
    jo "Have you checked the security cameras? That might give you a clue."
    m "Right, the cameras! We completely forgot about those."
    s "Of course! Aren’t those password protected, though?"
    ja "Luckily, Jonathan and I each have recorded a part of the password."
    scene bg ja_computer
    hide jonathan
    hide jack

    label scene4apuzzle:
    s "It must be..."
menu:
    "34.":
        scene bg vic
        show jonathan normal:
            xpos 400
        show jack normal:
            xpos 1200
        s "Is it 34?"
        ja "Looks right to me."
        scene bg ja_computer
        hide jonathan
        hide jack
        jump scene4continued
    "7.":
        scene bg vic
        show jonathan normal:
            xpos 400
        show jack normal:
            xpos 1200
        s "Is it 7?"
        ja "Are you sure? Try again."
        scene bg ja_computer
        hide jonathan
        hide jack
        jump scene4apuzzle
    "37.":
        scene bg vic
        show jonathan normal:
            xpos 400
        show jack normal:
            xpos 1200
        s "Is it 37?"
        ja "Are you sure? Try again."
        jump scene4continued
    "43.":
        scene bg vic
        show jonathan normal:
            xpos 400
        show jack normal:
            xpos 1200
        s "Is it 7?"
        ja "Are you sure? Try again."
        scene bg ja_computer
        hide jonathan
        hide jack
        jump scene4apuzzle
label scene4continued:
    jo "Here’s my half."
    jo "(Right as rain./I don’t think it is. Try again.)"
    jo "We got it! Now to enter it into the system…"
# Typing the password into the system. Ding ding ding!
# Footage of David.
    s "*Gasp* David!?"
    m "It couldn’t be…"
    jump catching_david

label catching_david:
    scene bg myhal
    show david normal
    m "Give it up, David. We know you’re guilty."
    d "Wait, you don’t understand! I can explain…"
menu:
    "Give David a chance!":
        jump david_innocent
    "No, he’s definitely guilty.":
        jump david_guilty

label david_guilty:
    s "Not a chance. We’ve been hunting the perpetrator down all day for this, and we won’t give up now."
    d "You won’t find anything."
    m "It’s the end of the line now."
    d "I’ve been framed. Framed!"
    jump guilty_ending

label david_innocent:
    s "Okay, we’ll give you one last chance."
    d "I have been sneaking onto Teaching Machine E. But not for the reason you think."
    d "I’ve been using it… to watch AOT reaction videos during break."
    s "…"
    m "What about the files? The video?"
    s "Wait. There's a burried video here in the system!"
# Zoom back into the video. It's toad or something lol
    m "Why that must be..."
    jump innocent_ending

label guilty_ending:
    "Steve and Mario proceeded to spend the next few weeks hunting down the files on David’s computer, to no avail."
    "Weeks had passed since the marks were due to be released, and piazza complaints were indeed piling up by the dozens." 
    "The instructors had no choice but to let the students self evaluate, and of course, most gave themselves 100s."
    "Perhaps Steve and Mario should have trusted David after all…"
# Flip to end card. Mission unsuccessful
    return

label innocent_ending:
    "Steve and Mario hunted down the one student they knew that fit the description."
    "It turns out that the offending student was a misguided do-gooder, stealing the files in hopes that they would be able to give everyone a high mark on Acorn."
    "The instructors were able to return the marks to their students on time, and only received one or two complaints on piazza, instead of the dreaded dozens." 
    "Success!"
# Flip to end card, Mission successful
    return
