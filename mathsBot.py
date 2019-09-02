import pyautogui, sys, time
from pyscreeze import ImageNotFoundException
level = 0

input('Press enter when the game screen is visible.')
botWindow = pyautogui.position()


# locate the game window
window = pyautogui.locateOnScreen('pivot.png')
if window is None:
    sys.exit('Game not found!')

winLeft = window[0]
winTop = window[1]
numbers = ['0.png', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', 'neg.png']

start_game = [250 + winLeft, 430 + winTop]
plus   = [50 + winLeft, 750 + winTop]
minus = [180 + winLeft, 750 + winTop]
times   = [310 + winLeft, 750 + winTop]
divide    = [410 + winLeft, 750 + winTop]

def solve(term1, term2, term3, term4, level):
	if (level < 34):	
		if (term1 + term2 - term3 == term4):
			pyautogui.click(plus)
			pyautogui.click(minus)
			print(term1, '+', term2, '-', term3, '=', term4)
		elif (term1 + term2 * term3 == term4):	
			pyautogui.click(plus)
			pyautogui.click(times)	
			print(term1, '+', term2, 'x', term3, '=', term4)
		elif (term1 + term2 / term3 == term4):	
			pyautogui.click(plus)
			pyautogui.click(divide)	
			print(term1, '+', term2, '/', term3, '=', term4)
		elif (term1 + term2 + term3 == term4):	
			pyautogui.click(plus)
			pyautogui.click(plus)		
			print(term1, '+', term2, '+', term3, '=', term4)
		elif (term1 - term2 + term3 == term4):	
			pyautogui.click(minus)
			pyautogui.click(plus)		
			print(term1, '-', term2, '+', term3, '=', term4)
		elif (term1 - term2 * term3 == term4):	
			pyautogui.click(minus)
			pyautogui.click(times)		
			print(term1, '-', term2, 'x', term3, '=', term4)
		elif (term1 - term2 / term3 == term4):	
			pyautogui.click(minus)
			pyautogui.click(divide)	
			print(term1, '-', term2, '/', term3, '=', term4)	
		elif (term1 - term2 - term3 == term4):
			pyautogui.click(minus)
			pyautogui.click(minus)	
			print(term1, '-', term2, '-', term3, '=', term4)		
		elif (term1 * term2 + term3 == term4):	
			pyautogui.click(times)
			pyautogui.click(plus)	
			print(term1, 'x', term2, '+', term3, '=', term4)	
		elif (term1 * term2 - term3 == term4):	
			pyautogui.click(times)
			pyautogui.click(minus)		
			print(term1, 'x', term2, '-', term3, '=', term4)
		elif (term1 * term2 / term3 == term4):	
			pyautogui.click(times)
			pyautogui.click(divide)		
			print(term1, 'x', term2, '/', term3, '=', term4)
		elif (term1 * term2 * term3 == term4):
			pyautogui.click(times)
			pyautogui.click(times)		
			print(term1, 'x', term2, 'x', term3, '=', term4)	
		elif (term1 / term2 + term3 == term4):	
			pyautogui.click(divide)
			pyautogui.click(plus)	
			print(term1, '/', term2, '+', term3, '=', term4)	
		elif (term1 / term2 - term3 == term4):	
			pyautogui.click(divide)
			pyautogui.click(minus)	
			print(term1, '/', term2, '-', term3, '=', term4)	
		elif (term1 / term2 * term3 == term4):
			pyautogui.click(divide)
			pyautogui.click(times)	
			print(term1, '/', term2, 'x', term3, '=', term4)		
		elif (term1 / term2 / term3 == term4):	
			pyautogui.click(divide)
			pyautogui.click(divide)	
			print(term1, '/', term2, '/', term3, '=', term4)
		else:
			print("NO SOLUTION")	
	else:
		print("REACHED END FOR NOW")
		
pyautogui.click(start_game)
time.sleep(4)

while True:
	term1, term2, term3, term4, first_dig, second_dig, space, dif = 0,0,0,0,-1,-1, 0, 0
	neg = False
	for y in range(11):
		for x in pyautogui.locateAllOnScreen(numbers[y], grayscale=True, region=(300,500, 500, 150), confidence=0.85):
			#print('found ', y)
			#print(x[0])
			if x[0] < 390:
				term1 = y
			elif x[0] < 500 and x[0] > 390:
				term2 = y
			elif x[0] < 590 and x[0] > 500:
				term3 = y
			elif x[0] < 700 and x[0] > 590:
				if y == 10:
					neg = True
					break
				dif = x[0] - space			
				space = x[0]
				if dif > 5 and dif != x[0]:
					second_dig = y
					break
				elif dif < -5 and dif != x[0]:
					second_dig = y
					#print('first = ', first_dig, 'second = ', second_dig)
					first_dig, second_dig = second_dig, first_dig
					#print("SWAP")
					#print("first = ", first_dig, "second = ", second_dig)
					break
				else:
					first_dig = y
	if second_dig == -1:
		term4 = first_dig
	elif first_dig == -1:
		term4 = second_dig
	else:
		term4 = 10 * first_dig + second_dig
	if neg == True:
		term4 = term4 * -1
	#print(first_dig, '  ', second_dig, '     /     ')
	#print(term1, ' ', term2, ' ', term3, ' ', term4)
	
	solve(term1, term2, term3, term4, level)
	level = level + 1
	if level == 34
		break
	time.sleep(2)


