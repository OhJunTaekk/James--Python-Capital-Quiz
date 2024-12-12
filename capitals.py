import random
import time

startGame = "go" 
Instructions = "I" 


countries = {"India":"New Dheli","Burkina Faso":"Ouagadougou","Cape Verde":"Praia","Comoros":"Moroni",
             "Algeria":"Algiers","England":"London","France":"Paris","Germany":"Berlin","Greece":"Athens",
             "Ireland":"Dublin","Netherlands":"Amsterdam","Norway":"Oslo","Russia":"Moscow","Spain":"Madrid",
             "Ecuador":"Quito","Colombia":"Bogota","New Zealand":"Wellington","Finland":"Helsinki",
             "Belgium":"Brussels","Denmark":"Copenhagen","Belarus":"Minsk"} 

def choice(): 
     print("Enter GO to play or I to display instructions")
     choice = input("Please Enter GO or I:  ") 

     if choice == "go": 
         startGame() 
     else:
        Instructions() 

def Instructions(): 
    print("")
    print("Help:")
    print("In this game you must guess the correct capital of the country given \n guessing right will allow you to proceed to the next question.")
    print("Try to answer as quick as possible.")
    print("") 
    choice() 

# 추가된 코드 설명
# Insert_User()을 만들어 게임 시작 전에 이름을 입력받는 함수를 만든다.
def Insert_Username():
     username = input("Insert your name : ")
     # 입력한 이름을 리턴한다.
     return username

def startGame(): 
    # 게임 시작 전 이름을 입력받는다다
    username = Insert_Username()

    score = 0 
    
    continuegame = "y" 
     
    startTime = time.time() 

    while continuegame == "y": 
        for x in range(0,10): 
             
          country = random.choice(list(countries.keys())) 

          answer_correct = countries.get(country) 

          question = print("What is the capital of " + country + "?") 
          answer = input(" ")

          if answer.lower() == answer_correct.lower(): 
               print("correct")
               score += 1 
          else:
               print("incorrect")
          print("") 

        endTime = time.time() 
        testTime = int(endTime - startTime) 
        print("")
        
        # 게임 후 이름을 출력하는 코드드
        print("{}'s Game".format(username))

        if score == 0:
             print("You'd better get the map out! you was unable to guess any capitals correctly 0/10")
        elif score == 1:
             print("You need to work on your geography,you guessed 1/10 answered correctly ")
        elif score == 2:
             print("Not so good, you guessed 2/10 answered correctly")
        elif score == 3:
             print("Nope, you guessed 3/10 answered correctly")
        elif score == 4:
             print("Di you listen at school? you guessed 4/10 answered correctly")
        elif score == 5:
             print("The glass is half full, you guessed 5/10 answered correctly")
        elif score == 6:
             print("You're a little rusty, you guessed 6/10 answered correctly")
        elif score == 7:
             print("Nice, you guessed 7/10 answered correctly")
        elif score == 8:
             print("Well played, you guessed 8/10 answered correctly")
        elif score == 9:
             print("Wow, you guessed 9/10 answered correctly")
        else:
             print("Amazing! you really know your stuff! you guessed 10/10 answered correctly")

        print("You completed the test in", testTime, "seconds")
        print("")
        continuegame = input("Enter y to restart:  ")
          
choice()

