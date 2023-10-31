# Just a fun computer knowledge quiz have at it :)
# Make sure spelling is exact!!
def computerQuiz():
    """
        This is a fun little test to check your computer knowledge 
        make sure the spelling is exact for your answers Good Luck!!
    """
    score = 0
    question = input("Welcome to our computer quiz would you like to play? ")
    if question.lower() == "no":
        print("okay thanks again!")
    elif question.lower() == "yes":
            print("Okay cool lets get started ")
            question_1 = input("What does cpu stand for?  ")
            if question_1.lower() == "central processing unit":
                print("yes that was correct")
                score += 1
            else:
                print("that was not correct")
            question_2 = input("What does gpu stand for?  ")
            if question_2.lower() == "graphics processing unit":
                print("yes that was correct")
                score += 1
            else:
                print("that was not correct")
            question_3 = input("What does ram stand for?  ")
            if question_3.lower() == "random access memory":
                print("yes that was correct")
                score += 1
            else:
                print("that was not correct")
            question_4 = input("What does sata cable do?  ")
            if question_4.lower() == "transfer data between hardware":
                print("yes that was correct")
                score += 1
            else:
                print("that was not correct")
            question_5 = input("What does html stand for?  ")
            if question_5.lower() == "hyper text markup language":
                print("yes that was correct")
                score += 1
            else:
                print("that was not correct")
            question_6 = input("What does mobo stand for?  ")
            if question_6.lower() == "motherboard":
                print("yes that was correct")
                score += 1
            else:
                print("that was not correct")
            question_7 = input("What does aio stand for ?  ")
            if question_7.lower() == "all in one":
                print("yes that was correct")
                score += 1
            else:
                print("that was not correct")
            question_8 = input("What does ssd stand for?  ")
            if question_8.lower() == "solid state drive":
                print("yes that was correct")
                score += 1
            else:
                print("that was not correct")
            question_9 = input("what does hdd stand for?  ")
            if question_9.lower() == "hard disk drive":
                print("yes that was correct")
                score += 1
            else:
                print("that was not correct")
            question_10 = input("What does psu stand for?  ")
            if question_10.lower() == "power supply":
                print("yes that was correct")
                score += 1
            else:
                print("that was not correct")

            if score <= 4:
                print(f"your score was {score/10*100}% it is okay you tried")
            else:
                print(f'Your score is {score/10*100}% Great Job!')
    else:
        print("try a valid input")
computerQuiz()

