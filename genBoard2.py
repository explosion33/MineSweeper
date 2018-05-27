import ui
from random import randint

bombs = []
isFlag = False
fSize = 0

def init(size,numBombs,name):
	global v
	global bombs
	global isFlag
	
	bombs = []
	v = ui.View(name = name)
	v.background_color = '#D3D3D3'
	x,y = ui.get_screen_size()
	v.frame =(0,0,x,y-60)			
	p = creategrid(size,numBombs,x,y)
	flag_button.action = flag			
	v.right_button_items = [flag_button]							
	v.present('fullscreen')
	return v




def addText(size):
	for i in range(0, size):
		for l in range(0,size):
			global fSize
			label = ui.Label(frame = (v.width/size * i,v.height/size * l,v.width/size,v.height/size))
			label.name = str(i) + "/" + str(l) + "L"
			label.text_color = 'black'
			label.alignment = ui.ALIGN_CENTER
			if size == 3:
				label.font = ('Verdana-Bold', 105 + 45)
				fSize = 105 + 45
			elif size == 4:
				label.font = ('Verdana-Bold', 80 + 45)
				fSize = 80 + 45
			elif size == 5:	
				label.font = ('Verdana-Bold', 60 + 45)
				fSize = 60 + 45
			elif size == 6:	
				label.font = ('Verdana-Bold', 40 + 45)
				fSize = 40 + 45
			elif size == 5:	
				label.font = ('Verdana-Bold', 25 + 45)
				fSize = 25 + 45
			elif size >= 6 and size <= 8:	
				label.font = ('Verdana-Bold', 30 + 45)
				fSize = 30 + 45
			elif size >= 9 and size <= 11:	
				label.font = ('Verdana-Bold', 25 + 30)
				fSize = 25 + 30
			else:	
				label.font = ('Verdana-Bold', 20 + 15)
				fSize = 20 + 15
				
				
				
							
										
													
																
																			
																									
					
			v.add_subview(label)
			

def addButton(size):
	for i in range(0,size):
		for l in range(0,size):
			button = ui.Button(frame = (v.width/size * i,v.height/size * l,v.width/size,v.height/size))
			button.name = str(i) + "/" + str(l)
			button.action = butt
			v.add_subview(button)


def creategrid(gSize, num_Bombs,x,y):
	global bombs
	bombs = createBombs(num_Bombs,gSize)
	bombs = createNums(bombs,gSize)
	print(bombs)
	if gSize >= 3:
		addText(gSize)
		addButton(gSize)
		for i in range(1, gSize):
			lineh = ui.View(frame=((v.width/gSize) * i,0,3,y))
			linev = ui.View(frame=(0, (v.height/gSize) * i,x,3))
			linev.background_color = 'black'
			lineh.background_color = 'black'
			v.add_subview(linev)
			v.add_subview(lineh)
	return bombs

def createBombs(num, size):
	bombx = []
	bomby = []
	f = 0
	l = 0
	for i in range(0,num):

		num1 = randint(0,size-1)
		num2 = randint(0,size-1)
		
		bombx.append(num1)
		bomby.append(num2)
		l=0
		f+=1	
		chh = 0	
	for i in (0, len(bombx)):
		for x in range(0, len(bombx)):
			if i <= num-1 and x <= num-1:
				if bombx[i] == bombx[x] and bomby[i] == bomby[x]:
					chh += 1
					if chh == 2:
						
						print("change")
						chh = 0
						bombx[i] = randint(0,size-1)
						bomby[i] = randint(0,size-1)
			 
	bombs = []
	for i in range(0,size):
		subbombs = list(range(0,size))
		bombs.append(subbombs)
	
	for i in range(0,len(bombx)):
		print(i)
		print(i)
		bombs[bomby[i]][bombx[i]] = "B"
	return bombs					


def createNums(bombs,size):
	print("Create Nums\n")
	print(size)
	for y in range(0, len(bombs)):
		for x in range(0, len(bombs[y])):
			numBombs = 0
			#Check If its in a corner
			if bombs[y][x] != "B":
			
				if x == 0 and y == 0:
					#TL
					if bombs[y+1][x] == "B":
						print("FRICKING FLABERFLIBWJEHR")
						numBombs += 1
					if bombs[y][x+1] == "B":
						print("FRICKING FLABERFLIBWJEHR")
						numBombs += 1
					if bombs[y+1][x+1] == "B":
						print("FRICKING FLABERFLIBWJEHR")
						numBombs += 1
						
				elif x == size-1 and y == 0:
					#TR
					print(size)
					if bombs[y+1][x] == "B":
						numBombs += 1
					if bombs[y][x-1] == "B":
						print("FRICKING FLABERFLIBWJEHR")
						numBombs += 1
					if bombs[y+1][x-1] == "B":
						print("FRICKING FLABERFLIBWJEHR")
						numBombs += 1
				elif y == size-1 and x == 0:
					#BL
					if bombs[y-1][x] == "B":
						print("FRICKING FLABERFLIBWJEHR")
						numBombs += 1
					if bombs[y][x+1] == "B":
						print("FRICKING FLABERFLIBWJEHR")
						numBombs += 1
					if bombs[y-1][x+1] == "B":
						print("FRICKING FLABERFLIBWJEHR")
						numBombs += 1
				elif x == size-1 and y == size-1:
					#BR
					if bombs[y-1][x] == "B":
						print("FRICKING FLABERFLIBWJEHR")
						numBombs += 1
					if bombs[y][x-1] == "B":
						print("FRICKING FLABERFLIBWJEHR")
						numBombs += 1
					if bombs[y-1][x-1] == "B":
						print("FRICKING FLABERFLIBWJEHR")
						numBombs += 1
				elif x == 0 and y > 0 and y < size-1:
					if bombs[y-1][x] == "B":
						numBombs += 1
					if bombs[y+1][x] == "B":
						numBombs += 1
					if bombs[y][x+1] == "B":
						numBombs += 1
					if bombs[y-1][x+1] == "B":
						numBombs += 1
					if bombs[y+1][x+1] == "B":
						numBombs += 1
				
				elif y == 0 and x > 0 and x < size-1:
					if bombs[y+1][x] == "B":
						numBombs += 1
					if bombs[y][x-1] == "B":
						numBombs += 1
					if bombs[y][x+1] == "B":
						numBombs += 1
					if bombs[y+1][x+1] == "B":
						numBombs += 1
					if bombs[y+1][x-1] == "B":
						numBombs += 1		
						
										
				elif x == size-1 and y > 0 and y < size-1:
					if bombs[y-1][x] == "B":
						numBombs += 1
					if bombs[y+1][x] == "B":
						numBombs += 1
					if bombs[y][x-1] == "B":
						numBombs += 1
					if bombs[y-1][x-1] == "B":
						numBombs += 1
					if bombs[y+1][x-1] == "B":
						numBombs += 1			
						
				elif y == size-1 and x > 0 and x < size-1:
					if bombs[y-1][x] == "B":
						numBombs += 1
					if bombs[y][x-1] == "B":
						numBombs += 1
					if bombs[y][x+1] == "B":
						numBombs += 1
					if bombs[y-1][x+1] == "B":
						numBombs += 1
					if bombs[y-1][x-1] == "B":
						numBombs += 1
													
																																																			
				else:
					if bombs[y-1][x] == "B":
						numBombs += 1
					if bombs[y+1][x] == "B":
						numBombs += 1
					if bombs[y][x+1] == "B":
						numBombs += 1
					if bombs[y][x-1] == "B":
						numBombs += 1
					if bombs[y+1][x+1] == "B":
						numBombs += 1
					if bombs[y-1][x+1] == "B":
						numBombs += 1
					if bombs[y+1][x-1] == "B":
						numBombs += 1	
					if bombs[y-1][x-1] == "B":
						numBombs += 1																																																					
										
				bombs[y][x] = numBombs
	print("bombs")
	print(bombs)
	return bombs
			

		
def winLose(sender, bombs):
	l = sender.superview
	t = l[sender.name + "L"]
	canWin = True
	
	
	print(canWin)
	
	if t.text == 'Bomb':
		canWin = False
		v.name = "Lose"
		for y in range(0, len(bombs)):
			for x in range(0, len(bombs)):
				l[str(y) + "/" + str(x)].enabled = False
	else:
		print(t.text)
		if len(t.text) == 1:
			sender.enabled = False 
		
		for y in range(0,len(bombs)):
			for x in range(0,len(bombs)):
				if l[str(y) + "/" + str(x)].enabled == True and bombs[x][y] != 'B':
					print(str(y) + "/" + str(x))
					canWin = False
					break
		
	print('can win?')					
	print(canWin)
	
	if canWin == True:
		for y in range(0, len(bombs)):
			for x in range(0, len(bombs)):
				l[str(y) + "/" + str(x)].enabled = False
		v.name = "WIN"
				
						
										
def butt(sender):
	global bombs
	global isFlag
	
	p = ui.Button

	
	l = sender.superview
	
	num1 = 0
	num2 = 0
	numbas = ""
	numbas2 = ""
	check = False
	for item in sender.name:
		if item != "/" and check == False:
			numbas += item
		elif item == "/":
			check = True
		elif check == True:
			numbas2 += item
	num1 = int(numbas)
	num2 = int(numbas2)
	print("error for index out of range check")
	print(num2)
	print(num1)
	print(bombs)
	if l[sender.name + "L"].text == 'flag':
		l[sender.name + "L"].text = ''
		l[sender.name + "L"].font = (('Verdana-Bold', fSize))
		l[sender.name].image = None
		
	elif isFlag == True:
		l[sender.name + "L"].text = 'flag'
		l[sender.name + "L"].font = (('Verdana-Bold', 0))
		l[sender.name].image = ui.Image.named('flag.PNG').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
			

	elif bombs[num2][num1] == "B":
		print("CASE B")
		l[sender.name + "L"].text = "Bomb"
		l[sender.name + "L"].font = ('<system>', 0)
		l[sender.name].image = ui.Image.named('bomb.PNG').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
		l[sender.name].background_color = 'red'
	elif bombs[num2][num1] == 0:
		l[sender.name + "L"].text = "0"
		l[sender.name + "L"].border_width = 100
		l[sender.name + "L"].border_color = '#aeaeae'
		l[sender.name ].enabled = False
		print("First zero found")
		clearZeros(bombs, num2, num1,l)	
	elif bombs[num2][num1] != "B" and bombs[num2][num1] != 0:
		print("CASE NORM")
		print(bombs)	
		print(bombs[num2][num1])
		l[sender.name + "L"].text = str(bombs[num2][num1])
		
		
		if bombs[num2][num1] == 1:
			l[sender.name + "L"].text_color = "blue"
		elif bombs[num2][num1] == 2:
			l[sender.name + "L"].text_color = "green"
		else:
			l[sender.name + "L"].text_color = "red"	
		
	winLose(sender, bombs)

def clearZeros(bombs, y, x,l,):
	print('clearing zeros')
	size = len(bombs)
	color = '#aeaeae'
	tColor = ['black','blue','green','red','red','red','red','red','red']

	try:																					
		l[str(x) + "/" + str(y +1) + "L"].text = str(bombs[y +1][x]) #Down
		l[str(x) + "/" + str(y +1) + "L"].text_color = tColor[bombs[y +1][x]]
	except:
		pass
	try:			
		l[str(x) + "/" + str(y -1) + "L"].text = str(bombs[y -1][x]) #UP
		l[str(x) + "/" + str(y -1) + "L"].text_color = tColor[bombs[y-1][x]]
	except:
		pass
	try:		
		l[str(x +1) + "/" + str(y) + "L"].text = str(bombs[y][x+1]) #Right
		l[str(x +1) + "/" + str(y) + "L"].text_color = tColor[bombs[y][x +1]]
	except:
		pass
	try:		
		l[str(x -1) + "/" + str(y) + "L"].text = str(bombs[y][x-1]) #Left
		l[str(x -1) + "/" + str(y) + "L"].text_color = tColor[bombs[y][x-1]]
	except:
		pass
	try:		
		l[str(x +1) + "/" + str(y +1) + "L"].text = str(bombs[y +1][x+1]) #BR
		l[str(x +1) + "/" + str(y +1) + "L"].text_color = tColor[bombs[y+1][x+1]]
	except:
		pass
	try:		
		l[str(x -1) + "/" + str(y +1) + "L"].text = str(bombs[y +1][x-1]) #BL
		l[str(x-1) + "/" + str(y +1) + "L"].text_color = tColor[bombs[y+1][x-1]]
	except:
		pass
	try:		
		l[str(x +1) + "/" + str(y -1) + "L"].text = str(bombs[y -1][x+1]) #TR
		l[str(x +1) + "/" + str(y -1) + "L"].text_color = tColor[bombs[y-1][x+1]]
	except:
		pass
	try:		
		l[str(x -1) + "/" + str(y -1) + "L"].text = str(bombs[y -1][x-1]) #TL
		l[str(x -1) + "/" + str(y -1) + "L"].text_color = tColor[bombs[y-1][x-1]]
	except:
		pass
		
	try:					
		if l[str(x) + "/" + str(y +1) + "L"].text == "0" and l[str(x) + "/" + str(y +1)].enabled == True:
			#Down
			l[str(x) + "/" + str(y +1) + "L"].border_width = 1000
			l[str(x) + "/" + str(y +1) + "L"].border_color = color
			l[str(x) + "/" + str(y +1)].enabled = False
			clearZeros(bombs,y +1, x,l)
		else:
			l[str(x) + "/" + str(y +1)].enabled = False
	except:
		pass
	try:			
		if l[str(x) + "/" + str(y -1) + "L"].text == "0" and l[str(x) + "/" + str(y -1)].enabled == True:
			#UP
			l[str(x) + "/" + str(y -1) + "L"].text = ""
			l[str(x) + "/" + str(y -1)].border_width = 1000
			l[str(x) + "/" + str(y -1)].border_color = color
			clearZeros(bombs,y -1, x,l)
		else:
			l[str(x) + "/" + str(y -1)].enabled = False	
	except:
		pass
	try:			
		if l[str(x +1) + "/" + str(y) + "L"].text == "0" and l[str(x+1) + "/" + str(y)].enabled == True:
			#Right
			l[str(x +1) + "/" + str(y) + "L"].border_width = 1000
			l[str(x +1) + "/" + str(y) + "L"].border_color = color
			l[str(x +1) + "/" + str(y)].enabled = False
			clearZeros(bombs,y, x +1,l)
		else:
			l[str(x +1) + "/" + str(y)].enabled = False
	except:
		pass
	try:			
		if l[str(x -1) + "/" + str(y) + "L"].text == "0" and l[str(x-1) + "/" + str(y)].enabled == True:
			#Left
			l[str(x -1) + "/" + str(y) + "L"].border_width = 1000
			l[str(x -1) + "/" + str(y) + "L"].border_color = color
			l[str(x-1) + "/" + str(y)].enabled = False
			clearZeros(bombs,y, x -1,l)
		else:
			l[str(x-1) + "/" + str(y)].enabled = False	
	except:
		pass
	try:			
		if l[str(x +1) + "/" + str(y +1) + "L"].text == "0" and l[str(x+1) + "/" + str(y +1)].enabled == True:
			#BR
			l[str(x +1) + "/" + str(y +1) + "L"].border_width = 1000
			l[str(x +1) + "/" + str(y +1) + "L"].border_color = color
			l[str(x +1) + "/" + str(y +1)].enabled = False
			clearZeros(bombs,y +1, x +1,l)
		else:
			l[str(x +1) + "/" + str(y +1)].enabled = False
	except:
		pass
	try:			
		if l[str(x -1) + "/" + str(y +1) + "L"].text == "0" and l[str(x-1) + "/" + str(y +1)].enabled == True:
			#BL
			l[str(x -1) + "/" + str(y +1) + "L"].border_width = 1000
			l[str(x -1) + "/" + str(y +1) + "L"].border_color = color
			l[str(x -1) + "/" + str(y +1)].enabled = False
			clearZeros(bombs,y +1, x -1,l)
		else:
			l[str(x -1) + "/" + str(y +1)].enabled = False	
	except:
		pass		
	try:		
		if l[str(x +1) + "/" + str(y -1) + "L"].text == "0" and l[str(x+1) + "/" + str(y -1)].enabled == True:
			#TR
			l[str(x +1) + "/" + str(y -1) + "L"].border_width = 1000
			l[str(x +1) + "/" + str(y -1) + "L"].border_color = color
			l[str(x +1) + "/" + str(y -1)].enabled = False
			clearZeros(bombs,y -1, x +1,l)
		else:
			l[str(x +1) + "/" + str(y -1)].enabled = False	
	except:
		pass
	try:			
		if l[str(x -1) + "/" + str(y -1) + "L"].text == "0" and l[str(x-1) + "/" + str(y -1)].enabled == True:
			#TL
			l[str(x -1) + "/" + str(y -1) + "L"].border_width = 1000
			l[str(x -1) + "/" + str(y -1) + "L"].border_color = color
			l[str(x -1) + "/" + str(y -1)].enabled = False
			clearZeros(bombs,y -1, x -1,l)
		else:
			l[str(x -1) + "/" + str(y -1)].enabled = False			
	except:
		pass
		
				
								
def changeMode(sender):
	if sender.title == "Flag":
		sender.title = ""
	
		
flag_button = ui.ButtonItem()
flag_button.title = 'Flag'
flag_button.tint_color = (0.0, 0.0, 1.0, 1.0)

			
						
												
def flag(sender):
	global isFlag
	print(sender.tint_color)
	if sender.tint_color == (0.0, 0.0, 1.0, 1.0):
		sender.tint_color = 'red'
		sender.title = ' Flag'
		isFlag = True
	elif sender.tint_color == (1.0, 0.0, 0.0, 1.0):
		sender.tint_color = 'blue'
		sender.title = 'Flag'
		isFlag = False
