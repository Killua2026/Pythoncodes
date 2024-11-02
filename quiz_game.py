print("Welcome to my Computer Quiz!")

playing = input("Do you want to play?(yes/no) ")

if playing.lower() != "yes":
    quit() #to terminate the program
print("Okay! Let's play :)")
score = 0


answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")    

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does LLM stand for? ").lower()
if answer == "large language model":git
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 
    
print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + "%.")

       