from genBoard2 import *

import Image
import time
import console
console.hide_output()

lastS = 0 
lastB = 0


def settings(sender):
	x,y = ui.get_screen_size()
	settings = ui.View(frame = (0,0,x/2,y/2), name='setView')
	w = settings.width
	l = settings.height
	settings.background_color = 'white'
	
	playB = ui.Button(frame = (w/4,3*l/4,w/8,50), action = newStart, name = 'play', title = 'New Game',font = ('<system>', 45), alignment = ui.ALIGN_CENTER)
	playB.background_color = '0e61b4'
	playB.width = playB.width + 50
	playB.tint_color = '#57c4ff'
	shadow = ui.View()
	playB.border_color = '#0e61b4'
	playB.border_width = 5
	playB.alpha = 1
	playB.corner_radius = 5
	
	shadow = ui.View(frame = (w/4 + 10, 3*l/4 - 10, playB.width,playB.height))
	shadow.background_color = 'black'
	shadow.alpha = 0.3
	shadow.corner_radius = 5
	
	size = ui.Slider(frame=(w/4,l/4,w/2,34),continuous = True, name = 'size')
	num = ui.Slider(frame=(w/4,3 * l/4 - 120,w/2,34), continuous = True, name = 'num')
	num.action = slider
	size.action = slider
	num.value = lastB
	size.value = lastS
	
	sizeT = ui.Label(frame=(w/4 - 60, l/4, 50,34), text = 'Size', font=('<system>', 15), alignment = ui.ALIGN_RIGHT, action = slider, name = 'sizeT')
	numT = ui.Label(frame=(w/4 - 60,3 * l/4 - 120, 50,34), text = 'Bombs', font=('<system>', 15), alignment = ui.ALIGN_RIGHT, action = slider, name = 'numT')
	sizeV = ui.Label(frame=(3 * w/4 -60 + 60, l/4, 100,34), text = '3', font=('<system>', 15), alignment = ui.ALIGN_LEFT, action = slider, name = 'sizeV')
	numV = ui.Label(frame=(3 * w/4 -60 + 60,3 * l/4 - 120, 100,34), text = '3', font=('<system>', 15), alignment = ui.ALIGN_LEFT, action = slider, name = 'numV')
	
	sizeV.text = str(int((size.value * 12) + 3))
	numV.text = str(int((((2 * (int(sizeV.text) ** 2))/3)-3) * num.value) + 4)  
	
	#settings.add_subview(shadow)
	settings.add_subview(playB)
	settings.add_subview(sizeV)
	settings.add_subview(numV)
	settings.add_subview(sizeT)
	settings.add_subview(numT)
	settings.add_subview(num)
	settings.add_subview(size)
	settings.present('sheet')
	
def slider(sender):
	global lastS
	global lastB
	
	l = sender.superview 
	v1 = int((l['size'].value * 12) + 3)
	v2 = int((((2 * (int(l["sizeV"].text) ** 2))/3)-3) * l['num'].value) + 4  
	
	lastS = l['size'].value
	lastB = l['num'].value
	
	
	l["numV"].text = str(v2)
	l["sizeV"].text = str(v1)
	

def newStart(sender):
	l = sender.superview
	x = int(l["sizeV"].text)
	y = int(l["numV"].text)
	nName = ''
	print("")
	print("")
	print("Retart")
	print("")
	print(x)
	print(y)
	
	v.close()
	l.close()
	v.wait_modal()
	

	print("starting with")
	print(x)
	print(y)
	start(x,y,nName)
	
	print("both closed")
	
	

	
	
def start(x,y,name):
	print("Started")
	global v
	global size
	size = x
	sett = ui.ButtonItem()
	v = init(x,y,name)
	sett = ui.ButtonItem()
	sett.image = ui.Image.named('Gear.PNG').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
	sett.action = settings
	v.left_button_items = [sett]

start(5,7, '')
