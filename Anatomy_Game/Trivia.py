### TRIAGE QUIZ GAME ###

## QUESTIONS (this is the list of questions separated by category (colors, long answer, etc.)
# questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9]
#Actually am not sure if how many questions we add will affect the code, will have to test later

questions = [
    ## 1 - COLOR TRIAGE CATEGORY QUESTIONS ##
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
    ["Which of the following patients would be considered a delayed patient?\n A.a patient with a broken finger\n B.a patient who has an uncontrolled arterial bleed and is pale\n C.patient who is laying supine complaining they cannot feel or move extremities\n D.a patient who is pulseless and apneic\n",
    "Which of the following is true about START triage?\n A.it utilizes three basic steps for brief assessment\n B.it was developed in the military\n C.is only performed on decreased patients\n D.can only be done in a hospital lobby\n ",
    "Which of the following patients would be considered immediate?\n A.a patient with burns to the whole lower half of their body\n B.16-year-old with a Femur fracture\n C.52-year-old with heart burn and a minor abrasion to the left elbow\n D.patient with an open pneumothorax\n" ,
    "Which of the following patients would be considered immediate?.\n A.a patient who is siting on the curb with a broken ankle and cannot walk\n B.a patient with a minor laceration to the left thigh\n C.a patient who has a femur fracture\n D.52-year-old patient who is running and screaming 'we are going to die'\n" ,
    "Which of the following patients would be considered immediate?\n A.28 yo with a back injury\n B.bystander w/ circumferential burn to forearm\n C.74 yo w/ both legs amputated\n D.first responder w/ femur fracture\n" ,
    "Which of the following patients would be considered minor?\n A. 44 yo patient who is cool, pale, diaphoretic\n B.23 yo who has an abrasion on the whole posterior side of left leg\n C.patient who is unconscious and breathing 40 times a min\n D.32 yo w/ bilateral femur fractures\n F.23 yo who has an abrasion on the whole posterior side of left leg\n" ,
    "What is the main goal of triage?\n A.to assess each patient thoroughly and transport to the closest facility\n B.to transport all immediate patients as soon as the hospitals are open\n C.to be rapid and brief w/ the assessment in order to spread patients to treatment units\n D.to be rapid in the transportation and treatment of the expectant patients\n"],
    
    ## 4 - DELEGATION QUESTIONS ##
    ["Which is true about nursing delegation?\n A.the nurse can transfer accountability\n B.the nurse is no longer responsible\n C.the nurse can assume all UAPs are qualified\n D.the nurse retains accountability\n", 
    "The nurse taught a patient's caregiver how to administer Lovenox(enoxaparin sodium)injections to a patient. How should the RN evaluate if the teaching was effective prior to discharge?\n A. arrange for the follow up with home care nurse\n B. ask the caregiver to 'demeonstrate back' her ability to administer it\n C. moitioring patients lab work before discharge\n D.asking the caregiver what she found helpful about the teaching\n", 
    "With the delegated task, who is accountable?\n A.Delegator\n B.Delegator\n C.Nurse manager\n D.None\n",
    "In the process of delegation, the nurse understands that the primary person who maintains accountability for the accuracy, safety, and completion of the task delegated remains with whom? A.The delegator of the task\n B.The delegatee of the task\n C.Those who assisted with task completion\n D.The person who documented task completion\n",
    "Which health care team member is responsible for the coordination and assignments of client care?\n A.charge nurse\n B.nurse manager\n C.cheif nursing officer\n D.unlicensed assistive personnel\n ", 
    "What is the primary purpose of delegation in nursing practice?\n A.To transfer full responsibility of patient care to another individual\n B.To allow the nurse to focus solely on administrative tasks\n C.To enable the nurse to assign specific tasks to others while retaining accountability\n D.To eliminate the need for communication among healthcare team members\n",
    "After a surgical procedure, which assessment finding should the nurse prioritize obtaining directly from the client to ensure accurate care planning?\n A.Level of consciousness\n B.Post-operative incision appearance\n C.Nausea and vomiting\n D.Current medication regimen\n", 
    "A nurse delegator assigns work to a delegatee who has the ability and willingness to do the work but the relationship between the delegator and delegatee is relatively new. How is the delegator's behavior described according to Hersey's Model?\n A.Selling\n B.Telling\n C.Delegating\n D.Participating\n",
    "The nurse is having an exceptionally busy shift on an obstetrical unit. Which task is the nurse justified in delegating to an unlicensed care provider?\n A.Assessing the size and quantity of clots that are in a client's bedpan and informing the nurse\n B.Giving an anti-inflammatory medication to a client who is eight hours postdelivery\n C.Emptying a client's Foley catheter bag and reporting the volume to the nurse\n D.Helping a first-time mother achieve a good latch when breastfeeding the infant\n",
    "A nurse and an unlicensed assistive personnel (UAP) are caring for clients in a labor and birth unit. Which task should the nurse assign to the UAP?\n A.preform a funddal check on a 2-day postpartum client.\n B.Remove a fetal monitor and assist patient to bathroom.\n C.Teach a new mother how to bottle feed her infant.\n"],

    ##5 SCENARIO QUESTIONS
    ["A 40yo woman currently on chemotherapy with a temperature of 102F. What level of triage is this?\n",
    "A 5yo has sudden onset of left foot pain. They have a history of diabetes requiring insulin and their left foot cold to touch- no pulses. What level triage would you place this?\n",
    "A 19yo male brought in by police, with ETOH on breath, an unsteady gait, large head lac, and slurred speech but oriented. What level triage would you place this?\n",
    "A 24yo patient is brought in with severe respiratory distress. Their SPo2 is 80%. What level triage would you place this?\n",
    "A woman brings in her 3yo child who fell down the steps. THey are unresponsive to a sternal rub. What level of triage is this\n?",
    "A healthy 52yo man is brought into the ED. He ran out of BP medication and his blood pressure is 150/92. What level triage would you place this\n?",
    "A 12yo girl is brought into the ED with poison ivy. What level triage would you place this?\n",
    "A 19yo boy is brought in with a sore throat and fever. What level triage would you place this?\n",
    "A 29yo woman is brought into the ED with a UTI. What level triage would you place this?\n",
    "A 22-year-old is brought into the ED with right LLQ pain since early am and nausea. They have no appetite. What level triage would you place this?\n",
    "A 45-yr old obese female comes to the ED with complaints of LLE pain/swelling. IT started 2 days ago after driving for 12 hrs What level triage would you place this?\n"],

    ##6 CONDITIONS
    ["What triage color would 'Asphyxia' be considered?\n",
     "What triage color would 'Stable abdominal wounds' be considered?\n",
     "What triage color would '2nd/3rd degree burns' be considered?\n",
     "What triage color would 'Unresponsive patients' be considered?\n",
     "What triage color would 'Upper extremity fractures' be considered?\n",
     "What triage color would 'Soft tissue injury' be considered?\n",
     "What triage color would 'High spinal cord injury' be considered?\n",
     "What triage color would 'Unstable chest and abdominal wounds' be considered?\n",
     "What triage color would 'Fractures requiring open reduction' be considered?\n",
     "What triage color would 'Extensive burns over 60% of body' be considered?\n"],


    ##7 START 
    ["What does START stand for?\n",
     "What Triage System does the United States use Emergency Department?\n",
     "Which one of these parameters is not one of the three physiological parameters that are assessed according to START triage?\n A.Apperence\n B.Pulse\n C.Respiration\n D.Mental Status\n",
     "How long should START triage take per patient?\n",
     "What is STEP TWO of START triage?\n",
     "What priority is a patient that's not breathing, even after attempting to open airway?\n",
     "What are the characteristics of a priority 0 (black tag) patient?\n",],
    

   ##8 RANDOM
     ["The nurse knows that common mechanisms of injury involved in penetrating trauma include all of the following except which of the following?\n A.Stabbings\n B.Gunshot wounds\n C.Motor vehicle collisions\n D.Impalements\n",
      "True or False: psycological capabilities is a large challange for triage nurses?\n",
      "Which of the following are ethcical concerns for Triaging?(type all that apply)\n Resource Allication\n Undertriage\n Discrimination\n All of the above\n",
      "True or False: Human resource managements and structural preformance create a large amount of challanges for triaging?\n",
      "Is it more common for patients to be triaged as under severe or over severe?\n",
      "What is the Acronym for the exam nurses must take?\n",
      "What scale are patients asked to rate their pain on?\n",
      "Type out the five stages of triaging.(place a common between each level)\n",],

     

]

## ANSWERS ##
# VIP: if you make changes in the question zone, don't forget to synchronise this zone (the variable and the list)!

answers = [
    ## 1 - TRIAGE CATEGORY ANSWERS ##
    ["red",
    "red",
    "yellow",
    "green", 
    "yellow" ,
    "black", #expected to pass
    "yellow",
    "green",
    "red", #cardiogenic shock possible
    "black"], #already dead
    
    ## 2 - TRIAGE THESE PATIENTS ANSWERS ##
    ["5 immediate (64,90,78,32 patients), 0 delayed, 1 minor (43), 2 expectant (54,27)", #stopped here to go to work
    "5 immediate (23,24,43,32,33), 1 delayed (31), 0 minor, 0 expectant",
    "2 expectant, 1 minor, 2 delayed, 2 immediate"], # only three questions 

    ## 3 - GENERAL QUESTIONS ANSWERS ##
    ["C",
    "A", 
    "D",
    "D", 
    "D",
    "E",
    "To be rapid and brief with the assessment in order to spread patients to treatment units"],

    ## 4 - DELAGATION QUESTION ANSWERS ##
    ["D",
    "B", 
    "A",
    "A",
    "A",
    "C",
    "C",
    "D",
    "C",
    "B"],

    ## 5
    ["Level 2", 
    "Level 2", 
    "Level 2",
    "Level 1",
    "Level 1",
    "Level 5", 
    "Level 5",
    "Level 4",
    "Level 4",
    "Level 3",
    "Level 3"],

    ##6 CONDITION ANSWERS
    ["Red",
     "Yellow",
     "Green",
     "Black",
     "Green",
     "Yellow",
     "Black",
     "Red",
     "Yellow",
     "Black"],
   
   ##7 START 
    ["Simple triage and rapid treatment",
    "START",
    "A",
    "30 seconds",
    "Assesing RPM",
    "Priorty 0",
    "Not breathing"],

  ##8 RANDOM
    ["Gunshot wounds",
     "True",
     "All of the above",
     "True",
     "Under severe",
     "NCELX-RN",
     "1 to ten",
     "Resuscitation,Emergency,Urgent,Semi-Urgent,Non-urgent",],
]  

### CATEGORIES ######


categories =["Triage Category" ,  "Triage Patients" , "Scenario" , "General" , "Delegation" , "Condition","START","Random"]
greetings = [
            "Rank it, bag it, and tag it." , 
            "Triage Time – Let’s sort the chaos",
            "Time to put on the triage hat!" , 
            "One problem at a time, like a pro!" , 
            "Taking the triage express – no time to waste!",
            "Into the triage trenches – let's roll!" , 
            "Start simple, finish strong!",
            "Mission Impossible? Not today!" ,
    
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

    print("\n       ------ !! Welcome to Triage Triumph!! ------\n")
    
    global name
    global category

    while name == None:
        name = input("What's your name? ")
        print("Welcome, "+name+", to Triage Triumph!")
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
    
    system = int(input("Pick a category by typing a number (0 to exit) : 1-8\n"))
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
    if answerPlayer.lower() == answers[category - 1][x].lower():
        print("Well done,", name + ", 10 points gained! Let's move to the next question.\n")
        points +=10
    else:
        print("Wrong! 0 points gained, the correct answer was:", answers[category - 1][x],". Next question...\n")
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
            print("         https://github.com/ksu-hmi/triage_triumph        ")
            print("  Questions generated from information gathered from quizlet.com   ")
            print("                                                         ")
            print("                   Thanks for playing!                   ")
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
