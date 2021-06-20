q1 = """ What is output for −

raining'. find('z') ?

A - Type error

B - ' '

C - -1

D - Not found"""

q2 = """Which of the following is false statement in python

A - int(144)==144

B - int('144')==144

C - int(144.0)==144

D - None of the above"""

q3 = """When the given code is executed how many times ' 'you are learning python ' ' will be printed.

a = 0
while a<10:
… print(''you are learning python'')
… pass

A - 9

B - 10

C - 11

D - Infinite number of times."""

q4 = """What is output of following code −

s = ''mnopqr ''
i = ''m ''
while i in s:
   print('i', end= '' '')
A - i i i i i i i i……..

B - m m m m m …..

C - m n o p q r

D - no output"""

q5 = """What command is used to shuffle a list ‘L’?

A - L.shuffle()

B - random.shufflelist(L)

C - shuffle(L)

D - random.Shuffle(L)"""

questions = {q1 : "D", q2 : "D", q3 : "D", q4 : "A", q5 : "D"}

print("Welcome to Python Quiz!")
score = 0
for i in questions:
	print(i)
	flag1 = input("Do you want to skip the question (yes/no): ")
	if flag1 == "yes":
		continue
	ans = input("Enter your answer (A/B/C/D): ")
	if ans == questions[i]:
		print("Congrats! Your answer is correct.")	
		score = score + 1
		print("Your Current Score is " + str(score))
	else:
		print("Sorry, that was a wrong answer!")
		score = score - 1
		print("Your current score is " + str(score))	
	flag2 = input("Do you want to skip the quiz (yes/no): ")	
	if flag2 == "yes":
		break
print("Your final score is " + str(score))

if score == 5:
	print("Excellent!")	
elif 3 < score < 5:
	print("Good!")		
else:
	print("Try again!")	