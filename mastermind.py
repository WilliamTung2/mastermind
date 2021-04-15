import random
from random import randint

def main():
    number_list = [1,2,3,4,5,6]

    answer = []
    count = 0
    while(count < 4):
        one = random.choice(number_list)
        number_list.remove(one)
        answer.append(one)
        count+=1

    real_answer = list(answer)
    print(real_answer)
    user_input = [0,0,0,0]
    def mastermind(real_answer, user_input):
        guesses = 0
        while (user_input != real_answer):
            i=0
            user_guess = input("guess the number: ")
            user_input = list(user_guess)
            while i < 4:
                user_input[i] = int(user_input[i])
                i +=1
                #print(user_input)
            retstring = ""
            j=0
            for x in user_input:
                if x not in real_answer: #prints C when the number is not in the game
                    retstring += "C"
                else:
                    if real_answer[j] == x:
                        retstring += "A" #prints A when the number is in the array and the right spot
                    else:
                        retstring += "B" #prints B when the number is in the array but not the right number
                j+=1
            guesses += 1
            print(real_answer)
            print(retstring)
        print("you guess it right")
        print("Number of Guesses: " + str(guesses))
    mastermind(real_answer, user_input)
main()
