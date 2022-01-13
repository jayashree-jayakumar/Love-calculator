# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

low_name1=name1.lower()
low_name2=name2.lower()
couple_name=low_name1 + low_name2
T=couple_name.count("t")
R=couple_name.count("r")
U=couple_name.count("u")
E=couple_name.count("")
L=couple_name.count("l")
O=couple_name.count("o")
V=couple_name.count("v")
E=couple_name.count("e")
sum_of_true=int(T+R+U+E)
sum_of_love=int(L+O+V+E)
score=str(sum_of_true) + str(sum_of_love)
love_score=int(score)
if (love_score<10) or (love_score>90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (love_score>=40) and (love_score<=50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
