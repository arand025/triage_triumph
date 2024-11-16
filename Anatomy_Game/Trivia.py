### TRIAGE QUIZ GAME ###

## QUESTIONS (this is the list of questions separated by category (colors, long answer, etc.)
# questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9]
#Actually am not sure if how many questions we add will affect the code, will have to test later

questions = [
    ## 1 - TRIAGE CATEGORY QUESTIONS ##
    [ "An unresponsive male patient has snoring respirations. His breathing improves when you open his airway. What triage color would this patient be considered?\n" ,
    "A 66yo male patient is sitting on the ground. His eyes are open, but he cannot answer or follow directions. What triage color would this patient be considered?\n" ,
    "A 50yo man has bilateral fractured femurs. He has a faint radial pulse and a RR of 24. What triage color would this patient be considered?\n" ,
    "A 16yo female who is ambulatory (walking) and says she is O.K. What triage color would this patient be considered?\n" ,
    "A 19yo male with 2nd and 3rd degree burns over 80% of his body. Respirations 24 and pulse about 120. What triage color would this patient be considered?\n" ,
    "A 42yo woman with no obvious injuries and without a carotid pulse. What triage color would this patient be considered?\n" ,
    "A 57yo female has a deformed tibia and fibula. She is oriented with respirations of 20 and a pulse of about 100. What triage color would this patient be considered?\n" ,
    "A 14yo male with a broken arm walking around the scene. What triage color would this patient be considered?\n" ,
    "A responsive 34yo female has pale, moist skin and respirations of 32/minute. What triage color would this patient be considered?\n"
    "A 34yo man is unresponsive with brain matter showing. What triage color would this patient be considered?\n"],
    
    ## 2 - TRIAGE THESE PATIENTS ## *****
    ["Triage the following patients:\n 43yo- dislocated shoulder\n 54yo- pulseless\n 64yo- open femur fracture that is bleeding profusely\n 90yo- not breathing until airway is opened\n 78yo- screaming 'you are killing us'\n 32yo- intestines protruding out of abdomen\n 27yo- open skull fracture and exposed brain matter\n" , #double check this one
    "Triage the following patients:\n 23yo- house voice and audible wheezing after being in engine room during fire\n 24yo- unconscious but breathing normally\n 43yo- open head injury w/no brian exposed and is unconscious\n 32yo- massive uncontrolled bleed coming from chest\n 33yo- pneumothroax\n 31yo- partial thickness burn on left leg\n" ,
    "You arrive on scene for an auto vs pedestrian call. Triage the following patients:\n 12yo- femur fracture\n 32yo- unconscious and not breathing\n 42yo- broken left leg\n 44yo- laceration to the upper arm that has been controlled by a tourniquet\n 32yo- crushed head\n 89yo- severe respiratory distress and wheezing\n 21yo- broken hand\n"],
    
    ## 3 - GENERAL QUESTIONS## 
    ["Which of the following patients would be considered a delayed patient?\n",
    "Which of the following is true about START triage?\n",
    "Which of the following patients would be considered immediate?\n" ,
    "Which of the following patients would be considered immediate?.\n" ,
    "Which of the following patients would be considered immediate?\n" ,
    "Which of the following patients would be considered minor?\n" ,
    "What is the main goal of triage?\n"],
    
    ## 4 - DELEGATION QUESTIONS ##
    ["Which is true about nursing delegation?\n", 
    "The nurse taught a patient's caregiver how to administer Lovenox(enoxaparin sodium)injections to a patient. How should the RN evaluate if the teaching was effective prior to discharge?\n"
,



    ## 5 - INTEGUMENTARY SYQUESTIONS ##
    ["Skin accounts for what percentage of total body weight?\n",
    "True or False: Skin is the body's largest organ.\n",
    "What are the three main layers of skin tissue?\n",
    "What cells within the epidermis produce melanin giving skin its color?\n",
    "What is the protein found in the epidermis that gives skin its toughness and strength?\n",
    "Hair follicles can be found on Which layer of the skin?\n",
    "Which layer of the skin is mostly fatty tissue?\n",
    "True or False: The epidermis is constantly being renewed by shedding dead skin cells on a daily basis.\n",
    "True or False: The lymphatic vessels, which drain fluid from the tissues, are housed in the hypodermis.\n",
    "Physicians who specialize in treating disesases, disorders, and injuries of the skin, hair, and nails are called?\n"],   
    
    ## 6 - LYMPHATIC SYSTEM QUESTIONS ##
    ["True or False: The lymphatic system is a network of tissues and organs that help rid the body of toxins, waste, and other unwanted materials. \n",
    "What is the name of the clear, colorless fluid transported by the lymphatic system that contains infection-fighting white blood cells?\n",
    "Located on the left side of the body just above the kidney, what organ acts as a blood filter?\n",
    "Which white blood cell produced by the spleen acts as defenders against germs?\n",
    "What part of the lymphatic system,found in the back of the throat, is one of the immune system's first lines of defense against outside invaders?\n",
    "What small organ located in the chest just above the heart stores immature lymphocytes and prepares them to become active T cells?\n",
    "Which of the following organs is NOT part of the lymphatic system: spleen, thymus, bone marrow, gallbladder?\n",
    "True or False: Like blood, lymph flows throughout the body in a continue loop.\n",
    "Which medical specialists typically treat disesase and disorders of the lymphatic system?\n",
    "How many drainage areas does the lymphatic system have in which to clear different parts of the body?\n"],

    ## 7 - MUSCULAR SYSTEM QUESTIONS ##
    ["How many muscles are there in the adult human muscular system?\n",
    "What are the 3 types of muscles?\n",
    "Which of the 3 muscle types consist of the only voluntary muscle tissue, controlling every action that a person consciously performs?\n",
    "Known as involuntary muscle, which muscle type is controlled by the unconscious part of the brain?\n",
    "Which muscle type is found only in the heart and reponsible for pumping blood throughout the body?\n",
    "Where in your body is the deltoid muscle situated?\n",
    "Where is the smallest skeletal muscle, the stapedius, found in the body?\n",
    "What is the largest muscle in the human body?\n",
    "What is the hardest working muscle, pumping at least 2,500 gallons of blood per day?\n",
    "True or False: There is no single type of doctor that treats muscular disesases and disorders.\n"],

    ## 8 - NERVOUS SYSTEM QUESTIONS ##
    ["What are the specialists who study the nervous system are called?\n",
    "True or False: the nervous system consists of the primary nervous system and the peripheral nervous system.\n",
    "The central nervous system consists of the nerves, the brain, and what else?\n",
    "True or False: the peripheral nervous system has sensory neurons, ganglia, and nerves that connect to the central nervous system.\n",
    "What type of neurons transmit signals to activate the muscles or glands?\n",
    "True or False: the somatic component and the automotive component are the two main subdivisions of the nervous system.\n",
    "What is the name of specialized cells that support, protect, or nourish nerve cells?\n",
    "True or False: the average human brain as about 100 neural connections.\n",
    "Neurons send signals to other cells through thin fibers called what?\n",
    "True or False: sensory neurons react to emotional stimuli.\n"],
    
    ## 9 - REPRODUCTIVE SYSTEM QUESTIONS ##
    ["When fertilization occurs, sperm must enter through what part of the female reproductive system, in order to burrow into the egg?\n",
    "True or False: Bartholin's gland is a part of the female reproductive structure.\n",
    "Which part of the male reproductive system is responsible for sperm production?\n",
    "True or False: the fetus begins to take shape during a process called embryogenesis.\n",
    "In male infertility, what is it called when no sperm cells are produced?\n",
    "True or False: cystic fibrosis can cause male infertility.\n",
    "What is the term for people with both male and female reproductive parts?\n",
    "True or False: the vagina is attached to the uterus through the fallopian tubes.\n",
    "Which specialists typically oversee disorders in the male reproductive system?\n",
    "True or False: the only way to screen for cervical cancer is through Pap tests/smears.\n"],

    ## 10 - RESPIRATORY SYSTEM QUESTIONS ##
    ["What are the primary organs of the respiratory system, responsible for carrying out the exchange of gases as we breathe?\n",
    "The human respiratory system is a series of organs responsible for taking in oxygen and expelling what other gas?\n",
    "True or False: Brain cells being dying after about 4 minutes without oxygen.\n",
    "What is a newborn's normal breathing rate per minute?\n",
    "Also known as the windpipe, what filters the air that is inhaled?\n",
    "True or False: The left lung has 3 lobes, while the right lung has 2.\n", ### The left lung has 2 to accommodate the heart ###
    "Where does the exhange of oxygen and carbon dioxide occur?\n",
    "What is the name of the dome-shaped muscle at the bottom of the lungs that controls breathing?\n",
    "What condition causes coughing, wheezing, and shortness of breath due to inflammation of the lung airways?\n",
    "What medical specialists treat conditions of the respiratory system?\n"],

    ## 11 - SKELETAL SYSTEM QUESTIONS ##
    ["How many bones are there in the adult human skeletal system?\n",
    "True or False: Human infants are born with about 400 bones.\n",
    "What are considered part of the skeletal system, although not counted as bones?\n",
    "True or False:  The male pelvis is proportionately larger than the female pelvis.\n",
    "What can be found in the middle of some bones where new cells are constantly being produced for blood?\n",
    "What are the two distinctive parts of the skeletal system?\n",
    "What prevalent disease, particularly among the elderly, results in the loss of bone tissue?\n",
    "True or False: It takes about 10-16 pounds of pressure to break an average bone.\n",
    "What is the longest and strongest bone with the most powerful muscles attached to it?\n",
    "What are the medical specialists responsible for treating the entire skeletal system?\n"],
    
    ## 12 - URINARY SYSTEM QUESTIONS ###
    ["What are the primary organ(s) of the urinary system?\n",
    "True or False: The urinary system is also known as the renal system.\n",
    "The kidneys remove urea from the blook through small filtering units called?\n",
    "True or False: A normal, healthy bladder can hold up to 1 liter of urine comfortably for 2-5 hours.\n",
    "Which of the following are part of the renal system?\n(a) The urethra\n(b) The bladder\n(c) The kidneys\n(d) All of the above\n",
    "True or False: Small amounts of urine are emptied into the bladder from the ureters about every 10-15 seconds.\n",
    "What organ stores urine until the brain signals that it is ready to empty it?\n",
    "True or False: Circular muscles called sphincters close tightly around the opening of the bladder to prevent leakage into the urethra.\n",
    "Which of the following is NOT a disease of the urinary system?\n(a) Interstitial cystitis\n(b) Arteriosclerosis\n(c)Kidney Stones\n(d) Urinary tract infections\n",
    "True or False: Nephrologists treat problems of the urinary tract.\n"],
]

## ANSWERS ##
# VIP: if you make changes in the question zone, don't forget to synchronise this zone (the variable and the list)!

answers = [
    ## 1 - TRIAGE CATEGORY ANSWERS ##
    ["Red",
     "Red",
    "Yellow",
    "Green", 
    "Yellow" ,
    "Black", #expected to pass
    "Yellow",
    "Green",
    "Green",
    "Red", #cardiogenic shock possible
    "Black"], #already dead
    
    ## 2 - TRIAGE THESE PATIENTS ANSWERS ##
    ["5 immediate (64,90,78,32 patients), 0 delayed, 1 minor (43), 2 expectant (54,27)", #stopped here to go to work
    "5 immediate (23,24,43,32,33), 1 delayed (31), 0 minor, 0 expectant",
    "2 expectant, 1 minor, 2 delayed, 2 immediate"], # only three questions 

    ## 3 - ENDOCRINE SYSTEM ANSWERS ##
    ["Patient who is laying supine complaining they cannot feel or move extremities",
    "It utilizes basic steps for brief assessment", 
    "A patient with an open pneumothorax",
    "A 52yo patient who is running around screaming 'We are going to die", 
    "First responder with femur fracture",
    "23yo who has an abrasion on the whole posterior side of left leg",
    "To be rapid and brief with the assessment in order to spread patients to treatment units"],

    ## 4 - IMMUNE SYSTEM ANSWERS ##
    ["lymph nodes",
    "false", # white blood cells #
    "blood tests",
    "false", # autoimmune diseases #
    "corticosteroids",
    "true",
    "monoclonal",
    "true",
    "lymphatic",
    "false"], # it remembers threats #

    ## 5 - INTEGUMENTARY SYSTEM ANSWERS ##
    ["16",
    "true",
    "epidermis, dermis, and hypodermis",
    "melanocytes",
    "keratin",
    "dermis",
    "hypodermis",
    "true",
    "false", # dermis #
    "dermatologists"],

    ## 6 - LYMPHATIC SYSTEM ANSWERS ##
    ["true",
    "lymph",
    "spleen",
    "lymphocytes",
    "tonsils",
    "thymus",
    "gallbladder",
    "false", # lymph flows in only one direction-upward toward the neck #
    "immunologists",
    "2"],

    ## 7 - MUSCULAR SYSTEM ANSWERS ##
    ["650",
    "skeletal, smooth, and cardiac",
    "skeletal",
    "smooth",
    "cardiac",
    "arm",
    "ear",
    "gluteus maximus",
    "heart",
    "true"],

    ## 8 - NERVOUS SYSTEM ANSWERS ##
    ["neurologists",
    "false", # central nervous system and peripheral nervous system #
    "spinal cord",
    "true",
    "motor neurons",
    "false", # somatic and autonomic #
    "glial cells",
    "false", # 100 trillion #
    "axons",
    "false"], # physical stimuli #
    
    ## 9 - REPRODUCTIVE SYSTEM ANSWERS ##
    ["fallopian tube",
    "true",
    "testes",
    "false", # morphogenesis #
    "azoospermia",
    "true",
    "intersex",
    "false", # cervix #
    "urologists",
    "false"], # pap tests/smears and HPV tests #

    ## 10 - RESPIRATORY SYSTEM ANSWERS ##
    ["lungs",
    "carbon dioxide",
    "true",
    "40",
    "trachea",
    "false",
    "alveoli",
    "diaphragm",
    "asthma",
    "pulmonologists"],

    ## 11 - SKELETAL SYSTEM ANSWERS ##
    ["206",
    "false", # 300 bones #
    "teeth",
    "false",
    "bone marrow",
    "axial, skeleton, and appendicular skeleton",
    "osteoporosis",
    "true",
    "femur",
    "orthopedics"],

    ## 12 - URINARY SYSTEM ANSWERS ##
    ["kidneys",
    "true",
    "nephrons",
    "false", # 1/2 liter #
    "d",
    "true",
    "b",
    "true",
    "b",
    "false"] # answer = urologists...nephrologists treat diseases of the kidney #
]  

### CATEGORIES ######


categories =["circulatory" ,  "digestive" , "endocrine" , "immune" , "integumentary" , "lymphatic" , "muscular" , "nervous" ,  "reproductive" , "respiratory" ,  "skeletal" ,  "urinary"]
greetings = [
            "Let's get to the heart of the matter...the circulatory system!" , 
            "All about the gut...on to the digestive system!",
            "This gland is your gland....on to the endocrine system!" , 
            "Our hidden heroes...the immune system." , 
            "The body's shield...the integumentary system!",
            "The invisible system...the lymphatic system!" , 
            "You think you're tough eh?...let's try the muscular system." ,
            "Okay, brainiac...on to the nervous system." ,  
            "Let's give the reproductive system a try." ,
            "Take a deep breath, as we proceed to the respiratory system." ,
            "You won't find these humerus...but on to the skeletal system." , 
            "Gotta go right now...to the urinary system."
            ]
## GLOBAL GAME SETTINGS ##

points = 0
name = None
yes = ['Yes', 'yes', 'YES']
no = ['No', 'no', 'NO']
category = 0

## RESET ZONE ##

def game_reset():
    '''
    Reset all variables of the whole game for a new play
    '''

    global points
    global name

    points = 0
    name = None
# end-function #

## GAME INTRO ZONE ##

def game_intro():
    '''
    Welcome the player and ask him for his name as long as he thinks is correct.
    '''

    print("\n       ------ !! Welcome to the Human Anatomy Trivia Game !! ------\n")
    
    global name
    global category

    while name == None:
        name = input("What's your name? ")
        print("Welcome, "+name+", to the Human Anatomy Trivia Game!")
        correct = input("Did we get your name right? ")
        if yes.count(correct) == True: ##"Yes" or ok == "yes" or ok == "YES":
            print("Perfect, let's move on!\n")
        else:
            print("Eh?? Try again and confirm with Yes!")
            name = None

        list_categories() 
        start_system()

# end-function #
            
## GAME PLAY ZONE ##

def print_play_status(x):
    '''
    just print out the current score and the current challenge number.
    '''

    global points
    print("At the moment your total points are", points)
    print("Challenge", x+1, "\n")

# end-function #

def start_system() : 
    
    system = int(input("Pick a category by typing a number (0 to exit) : 1-12\n"))
    if system == 0 : 
        game_end()
    else :
        print(greetings[system - 1])
        start_category(system)
   
def start_category(cat) : 
    global category
    category = cat
    
    game_play()
    
def list_categories() : 
    
  # loop through categories array and print categories #
  for c in categories : 
      print(categories.index(c) + 1 , " : " , c)

def play_quest(x):
    '''int -> int
    this functions asks the player question X, checks if player's answer is right and eventually changes the variable points.
    no examples needed
    '''
    global points
    global questions
    global answers
    answerPlayer = input(questions[category - 1][x])
    if answerPlayer.lower() == answers[category - 1][x]:
        print("Well done,", name + ", 10 points gained! Let's move to the next question.\n")
        points +=10
    else:
        print("Wrong! 0 points gained, the correct answer was:", answers[category - 1][x], ". Next question...\n")
    last_cat = len(questions[category - 1])
    if x == last_cat -1 : 
        global categories
        
        global greetings
        
        categories.pop(category - 1)
        greetings.pop(category - 1)
        questions.pop(category - 1)
        answers.pop(category - 1)
        if len(categories) == 0 : 
            game_end()
        else:
            list_categories() 
            start_system()

# end-function #

def game_play():
    '''
    first : tell the player his current score and the current challenge number
    second: tell the play_quest-function how many and which questions it must asks the player.
    '''
   
    for x in range(len(questions[category - 1])):
        print_play_status(x)
        play_quest(x)

# end-function #

## GAME END ZONE ##

def game_end():
    '''
    first : tell the player his finish score.
    second: ask the player if wants to play again and fullfil his wish.
    '''

    print("\nYou finished the game with a total of", points, "points! \n")

    again = None
    
    while again == None:
        again = input("Play again? ")
        if yes.count(again) == True:
            print("\nEnjoy :)\n")
            game_control()
        elif no.count(again) == True:
            print("        Congratulations!  You've completed the game."      )
            print("            https://github.com/ksu-hmi/Anatomy-Game"       )
            print("  Questions generated from information gathered from livescience.com   ")
            print("  at the following address:  https://www.livescience.com/health        ")
            print("                                                         ")
            print("                   Thanks for playing!"                    )
            print("                ------ !! B Y E !! ------                  ")
            
        else:
            print("oh, just yes or no!")
            again = None

# end-function #
    
## GAME CONTROL ZONE ##

def game_control():
    '''
    Control the whole game with these single steps.
    '''
    game_reset()
    game_intro()
    
    #start_system()
   
    #game_play()
    #game_end()
# end-function #

## FIRST GAME START ZONE ##

game_control()
