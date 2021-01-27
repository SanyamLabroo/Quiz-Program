import random
import time
from itertools import chain, repeat
import stdiomask
import getpass
import os
from tqdm import tqdm


if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()

#For loading screen
print("Making your test ready...")
time.sleep(2)
print("This may take a while...")
for _ in tqdm(range(100),
        desc = "Loading your Test...",
        ascii = False, ncols =75):
    time.sleep(0.1)

print("Here you GO...")
time.sleep(2)

clear()


class Login:
    def __init__(self, id, password):
        self.id = id
        self.password = password
        self.error = "Incorrect ID...\nPlease try again."
    def check(self):
        if (self.id == log_id and self.password == log_pass):
            print("Login successful")
        else:
            print(self.error) 
            exit()
            
log = Login("sanyam", "password")
log_id = input("Enter user name: ")
log_pass = stdiomask.getpass("Enter password: ")
log.check()

time.sleep(1)

print("\nWelcome " + log_id)
Instructions = ["\nThis is a Quiz game in which you will get 5 Questions to answer.", "The Questions will have very short answers.",
                    "If you answer 4 Questions of the 5 Questions then you win else you loose.",
                        "There are 3 sets of paper(SET1,SET2 & SET3) and you can select the set of paper on your own."]

for i in chain.from_iterable(repeat(Instructions, 1)):
    time.sleep(2)
    print(i)
    

def SET1():
    
    marks = 0
    
    print("* SET 1 *")
    time.sleep(1)
    set1 = ["\nQ1. Who is world's Richest Man?", "Q2. Is HTML a programming Language or not?",
                "Q3. Who is the Current Prime Minister of India?", "Q4. Who is the Creator of Whatsapp?",
                        "Q5. What is the name of worlds No.1 University?"]
    
    for i in chain.from_iterable(repeat(set1, 1)):
        time.sleep(2)
        print(i)
    
    Ans1 = input("Enter the Answer of Question 1: ")
    
    if Ans1 == "Elon Musk" or Ans1 == "elon musk" or Ans1 == "ELON MUSK":
        time.sleep(0.3)
        print("Correct answer.")
        marks = marks + 1 
        
    else:
        time.sleep(0.3)
        print("Wrong Answer.")
    
    time.sleep(0.3)
    
    Ans2 = input("Enter the Answer of Question 2: ")
    
    if Ans2 == "NO" or Ans2 == "No" or Ans2 == "no":
        time.sleep(0.3)
        print("Correct answer.")
        marks = marks + 1
        
    else:
        time.sleep(0.3)
        print("Wrong Answer.")
        
    time.sleep(0.3)
    
    Ans3 = input("Enter the Answer of Question 3: ")
    
    if Ans3 == "Narendra Modi" or Ans3 == "NARENDRA MODI" or Ans3 == "narendra modi":
        time.sleep(0.3)
        print("Correct answer.")
        marks = marks + 1
        
    else:
        time.sleep(0.3)
        print("Wrong Answer.")
        
    time.sleep(0.3)
    
    Ans4 = input("Enter the Answer of Question 4: ")
    
    if Ans4 == "Brian Acton" or Ans4 == "brian acton" or Ans4 == "BRIAN ACTON":
        time.sleep(0.3)
        print("Correct answer.")
        marks = marks + 1
        
    else:
        time.sleep(0.3)
        print("Wrong Answer.")

    time.sleep(0.3)
    
    Ans5 = input("Enter the Answer of Question 5: ")
    
    if Ans5 == "Massachusetts Institute of Technology" or Ans5 == "massachusetts institute of technology" or Ans5 == "MASSACHUSETTS INSTITUTE OF TECHNOLOGY" or Ans5 == "MIT" or Ans5 == "mit":
        time.sleep(0.3)
        print("Correct answer.")
        marks = marks + 1
        
    else:
        time.sleep(0.3)
        print("Wrong Answer.")
    
    time.sleep(1)
    print("Your score is {0} out of {1} ".format(marks,5))
    time.sleep(1)
    
    if marks >= 4:
        print("Congractulations you won.")
        
    else:
        print("Sorry You lost.")

def SET2():
    
    marks = 0
    
    print("* SET 2 *")
    time.sleep(1)
    set1 = ["\nQ1. What is the name of the most radioactive element on Earth?", "Q2. Give the name of the most famous Crypto Currency?",
                    "Q3. What is the name of the creator of PUBG?", "Q4. What is the real name of Captain America in Avengers?",
                            "Q5. What is the  real name of the Carryminati?"]
    
    for i in chain.from_iterable(repeat(set1, 1)):
        time.sleep(2)
        print(i)

    Ans1 = input("Enter the Answer of Question 1: ")
    
    if Ans1 == "Polonium" or Ans1 == "POLONIUM" or Ans1 == "polonium":
        time.sleep(0.3)
        print("Correct answer.")
        marks = marks + 1
        
    else:
        time.sleep(0.3)
        print("Wrong Answer.")
    
    time.sleep(0.3)
    
    
    Ans2 = input("Enter the Answer of Question 2: ")
    
    if Ans2 == "Bitcoin" or Ans2 == "bitcoin" or Ans2 == "BITCOIN":
        time.sleep(0.3)
        print("Correct answer.")
        marks = marks + 1
        
    else:
        time.sleep(0.3)
        print("Wrong Answer.")
    
    time.sleep(0.3)
    
    
    Ans3 = input("Enter the Answer of Question 3: ")
    
    if Ans3 == "Brendan Greene" or Ans3 == "BRENDAN GREENE" or Ans3 == "brendan greene":
        time.sleep(0.3)
        print("Correct answer.")
        marks = marks + 1
        
    else:
        time.sleep(0.3)
        print("Wrong Answer.")
    
    time.sleep(0.3)
    
    
    Ans4 = input("Enter the Answer of Question 4: ")
    
    if Ans4 == "Chris Evans" or Ans4 == "CHRIS EVANS" or Ans4 == "chris evans":
        time.sleep(0.3)
        print("Correct answer.")
        marks = marks + 1
        
    else:
        time.sleep(0.3)
        print("Wrong Answer.")
    
    time.sleep(0.3)
    
    
    Ans5 = input("Enter the Answer of Question 5: ")
    
    if Ans5 == "Ajay Nagar" or Ans5 == "AJAY NAGAR" or Ans5 == "ajay nagar":
        time.sleep(0.3)
        print("Correct answer.")
        marks = marks + 1
        
    else:
        time.sleep(0.3)
        print("Wrong Answer.")
    
    time.sleep(0.3)
    
    time.sleep(1)
    print("Your score is {0} out of {1} ".format(marks,5))
    time.sleep(1)
    
    if marks >= 4:
        print("Congractulations you won.")
        
    else:
        print("Sorry You lost.")
    
def SET3():
    
    marks = 0
    
    print("* SET 3 *")
    time.sleep(1)
    set1 = ["\nQ1. Who is the founder of Apple?", "Q2. Is Warren Buffet an Investor or not?", 
                    "Q3. Who is the God Father of Artificial Intelligence", "Q4. Who invented Laptop?",
                            "Q5. Who is the father of computer?"]
    
    for i in chain.from_iterable(repeat(set1, 1)):
        time.sleep(2)
        print(i)


    Ans1 = input("Enter the Answer of Question 1: ")
    
    if Ans1 == "steve jobs" or Ans1 == "Steve Jobs" or Ans1 == "STEVE JOBS":
        time.sleep(0.3)
        print("Correct answer.")
        marks = marks + 1
        
    else:
        time.sleep(0.3)
        print("Wrong Answer.")
    
    time.sleep(0.3)
    
    
    Ans2 = input("Enter the Answer of Question 2: ")
    
    if Ans2 == "yes" or Ans2 == "YES" or Ans2 == "Yes":
        time.sleep(0.3)
        print("Correct answer.")
        marks = marks + 1
        
    else:
        time.sleep(0.3)
        print("Wrong Answer.")
    
    time.sleep(0.3)
    
    
    Ans3 = input("Enter the Answer of Question 3: ")
    
    if Ans3 == "GEOFFREY HINTON" or Ans3 == "Geoffrey Hinton" or Ans3 == "geoffrey hinton":
        time.sleep(0.3)
        print("Correct answer.")
        marks = marks + 1
        
    else:
        time.sleep(0.3)
        print("Wrong Answer.")
    
    time.sleep(0.3)
    
    
    Ans4 = input("Enter the Answer of Question 4: ")
    
    if Ans4 == "Adam Osborne" or Ans4 == "ADAM OSBORNE" or Ans4 == "adam osborne":
        time.sleep(0.3)
        print("Correct answer.")
        marks = marks + 1
        
    else:
        time.sleep(0.3)
        print("Wrong Answer.")
    
    time.sleep(0.3)
    
    
    Ans5 = input("Enter the Answer of Question 5: ")
    
    if Ans5 == "charles babbage" or Ans5 == "Charles Babbage" or Ans5 == "CHARLES BABBAGE":
        time.sleep(0.3)
        print("Correct answer.")
        marks = marks + 1
        
    else:
        time.sleep(0.3)
        print("Wrong Answer.")
    
    time.sleep(0.3)
    
    time.sleep(1)
    print("Your score is {0} out of {1} ".format(marks,5))
    time.sleep(1)
    
    if marks >= 4:
        print("Congractulations you won.")
        
    else:
        print("Sorry You lost.")

def SET():
    
    try:
        choice = int(input("Enter the set of paper you want to do: "))
        
        if __name__ == '__main__':
	        clear = lambda: os.system('cls')

	        clear()
    
    except ValueError:
        print("Invalid Input.")
        time.sleep(0.5)
        print("Please try again.")
        SET()
        
        if __name__ == '__main__':
	        clear = lambda: os.system('cls')

	        clear()
    
    if choice == 1:
        SET1()
    
    elif choice == 2:
        SET2()
    
    elif choice == 3:
        SET3()
    
    else:
        print("Invalid Input.\nPlease try again.")
        time.sleep(1)
        SET()
        
SET()
