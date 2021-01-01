import pyautogui, sys, time
from itertools import product
from pyscreeze import ImageNotFoundException
level = 0

input('Press enter when the game screen is visible.')
botWindow = pyautogui.position()

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

operations = ['+', '-', 'x', '/']

def read(perm, term, n):
	for x in range(n):
		print(term[x], end =" ")
		try:
			if perm[x] == 'x':
				pyautogui.click(times)
				print("x", end =" ")
			elif perm[x] == '/':
				pyautogui.click(divide)
				print("/", end =" ")
			elif perm[x] == '+':
				pyautogui.click(plus)
				print("+", end =" ")
			elif perm[x] == '-':
				pyautogui.click(minus)
				print("-", end =" ")
		except TypeError:
			print("MISREAD:, ", term)
	
	print(term[len(term) - 2], "=", term[len(term) - 1]) 

def operate(i, term, n):
	sumup = []
	result = 0 
	x = 0
	while x < n:
		if i[x] == '+':
			if i[x-1] == '+' or i[x-1] == '-' or x == 0:
				sumup += [term[x]]
			if x == n -1:
				sumup += [term[x+1]]
		elif i[x] == '-':
			if x == n - 1:
				sumup += [term[x + 1] * -1]	
			else:
				term[x + 1] *= -1
			if i[x-1] == '+' or i[x-1] == '-' or x == 0:
				sumup += [term[x]]
		elif i[x] == 'x' or i[x] == '/':
			c,pqsum = 0, term[x]			
			while  i[x + c] == 'x' or i[x + c] == '/':
				if i[x + c] == 'x':
					pqsum *= term[x + c + 1]
				elif i[x + c] == '/' and term[x + c + 1] != 0:
					pqsum /= term[x + c + 1]
				c += 1
				if x + c == n:
					break
			if c != 1:
				x += c - 1
			sumup += [pqsum]
		x += 1			 
	for x in range(n):
		if i[x] == '-' and x != n - 1:
			term[x + 1] *= -1	
	for x in sumup:
		result += x	
	return result

def solve(perm, term, n): 
	for i in perm: 
		if (operate(list(i), term, n) == term[len(term) - 1]):
			return list(i)
			break
	return

pyautogui.click(start_game)
time.sleep(4)
pyautogui.click(winLeft + 100, winTop + 100)

while True:
	if level < 34:
		first_dig, second_dig, space, dif = -1,-1, 0, 0
		term = [0,0,0,0]
		neg = False
		for y in range(11):
			for x in pyautogui.locateAllOnScreen(numbers[y], grayscale=True, region=(300,500, 500, 150), confidence=0.85):
				if x[0] < 390:
					term[0] = y
				elif x[0] < 500 and x[0] > 390:
					term[1] = y
				elif x[0] < 590 and x[0] > 500:
					term[2] = y
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
						first_dig, second_dig = second_dig, first_dig
						break
					else:
						first_dig = y
		if second_dig == -1:
			term[3] = first_dig
		elif first_dig == -1:
			term[3] = second_dig
		else:
			term[3] = 10 * first_dig + second_dig
		if neg == True:
			term[3] = term[3] * -1
		
		if level == 0:
			perm = list(product(operations, repeat = 2))	
		read(solve(perm, term, 2), term, 2)
	
		level = level + 1
	
	elif level >= 34:
		first_dig, second_dig, space, dif = -1,-1, 0, 0
		term = [0,0,0,0, 0]
		neg = False
		for y in range(11):
			for x in pyautogui.locateAllOnScreen(numbers[y], grayscale=True, region=(200,500, 600, 150), confidence=0.85):
				if x[0] < 350:
					term[0] = y
				elif x[0] < 450 and x[0] > 350:
					term[1] = y
				elif x[0] < 550 and x[0] > 450:
					term[2] = y
				elif x[0] < 640 and x[0] > 550:
					term[3] = y
				elif x[0] < 750 and x[0] > 640:
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
						first_dig, second_dig = second_dig, first_dig
						break
					else:
						first_dig = y
		if second_dig == -1:
			term[4] = first_dig
		elif first_dig == -1:
			term[4] = second_dig
		else:
			term[4] = 10 * first_dig + second_dig
		if neg == True:
			term[4] = term[4] * -1
		if level == 34:
			perm = list(product(operations, repeat = 3))	
		read(solve(perm, term, 3), term, 3)
	
		level = level + 1
		
	time.sleep(2)
