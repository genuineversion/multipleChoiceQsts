 # This is a multiple choice collection of statements
 # 
 #  These are questions and the answers
Qst1={"Q1":"What is the capital of Nigeria","Q1optionA":"Lagos","Q1optionB":"Oyo","Q1optionC":"Abuja","Q1Ans":"C" }
Qst2={"Q2":"What is the capital of England","Q2optionA":"Manchester","Q2optionB":"London","Q2optionC":"Liverpool","Q2Ans":"B" }
Qst3={"Q3":"who won the 2020/2021 Premier league","Q3optionA":"ManUtd","Q3optionB":"ManCity","Q3optionC":"Chelsea","Q3Ans":"B" }

#  These are the three options that the user will select from.
options = ["A", "B", "C"]


#The "question" functions display each question and also accept and stores the user input
#The "functionQ" functions determines if the user input is correct and stores the value whether True or False
#Question 1
def question1():
    print("Question1: "+ Qst1["Q1"])
    print("a: "+Qst1["Q1optionA"])
    print("b: "+Qst1["Q1optionB"])
    print("c: "+Qst1["Q1optionC"])
    global userAnsQ1

    userAnsQ1=input("Answer by entering a, b or c \n").upper()
    return userAnsQ1

def functionQ1():
    if userAnsQ1 not in options:
       print ("Input is out of range")
       question1()
    elif userAnsQ1.upper()==Qst1["Q1Ans"].upper():
        Result1 = True
    else: 
        Result1= False
    return Result1
    
#Question 2
def question2():
    print("Question2: "+ Qst2["Q2"])
    print("a: "+Qst2["Q2optionA"])
    print("b: "+Qst2["Q2optionB"])
    print("c: "+Qst2["Q2optionC"])
    global userAnsQ2

    userAnsQ2=input("Answer by entering a, b or c \n").upper()
    return userAnsQ2

def functionQ2():
    if userAnsQ2 not in options:
       print ("Input is out of range")
       question2()
    elif userAnsQ2.upper()==Qst2["Q2Ans"].upper():
        Result2 = True
    else: 
        Result2= False
    return Result2

#Question 3
def question3():
    print("Question3: "+ Qst3["Q3"])
    print("a: "+Qst3["Q3optionA"])
    print("b: "+Qst3["Q3optionB"])
    print("c: "+Qst3["Q3optionC"])
    global userAnsQ3

    userAnsQ3=input("Answer by entering a, b or c \n").upper()
    return userAnsQ3

def functionQ3():
    if userAnsQ3 not in options:
       print ("Input is out of range")
       question3()
    elif userAnsQ3.upper()==Qst3["Q3Ans"].upper():
        Result3 = True
    else: 
        Result3= False
    
    return Result3


#The score is to be displayed in %, so this function converts the float into % (string)
def convertToPercent (decimal):
    convertedValue=decimal*100
    convertedValue=str(convertedValue)+"%"
    return convertedValue

#Functions call, to dsiplay the questions, obtain the user input and confirm if correct or not. 
question1()
answer1=functionQ1()
question2()
answer2=functionQ2()
question3()
answer3=functionQ3()

#This stores the answers in a list
listOfAnswers=[answer1, answer2, answer3]

numberOfCorrectAns=listOfAnswers.count(True)

totalQsts=len(listOfAnswers)

#THis calculates the score in decimals
percentScore=round(numberOfCorrectAns/totalQsts,2)
#THis displays the score to the user and also use the function convertToPercentage to convert the float to percentage. 
print("Your score is "+ convertToPercent(percentScore))

#This returns the answer to the user to see how they did, whether True or False
print ("See how correct your choices are:")
x=0
for i in listOfAnswers:
    x+=1
    print("Question {}".format(x))
    print(i)