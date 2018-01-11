#mymagic8ball
import random
#answers
ans1="Go for it!"
ans2="Why are you asking me that?!"
ans3="That would be a very bad idea!"
ans4="Hmmm... I'm not too sure about that one."
ans5="Yes"
ans6="No"
ans7="Makes no difference to me, do or don't."
ans8="Why are you asking me so many questions?"

print("Welcome to the Magic 8 Ball \n") #intro
#GET USER NAME
name=input("Please type your name...")
#GET USER QUESTION
question=input("\nThank you, %s! Ask me for adivce then press ENTER to shake me. \n" % name)

print("Shaking... \n\n" *3)

choice=random.randint(1, 8)
if choice==1:
    answer=ans1
elif choice==2:
    answer=ans2
elif choice==3:
    answer=ans3
elif choice==4:
    answer=ans4
elif choice==5:
    answer=ans5
elif choice==6:
    answer=ans6
elif choice==7:
    answer=ans7
else:
    answer=ans8

print("My answer to your question is: " + answer)

input("\n\nPress the ENTER key to finish. Thank you for your time, %s." %name)



