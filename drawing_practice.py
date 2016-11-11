#MODIFIED SAMPLE4 CODE

#required 
import pygame
pygame.init();

#create colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

#create a surface
gameDisplay = pygame.display.set_mode((400,400)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Nov 11 Discussion")

pygame.display.update()		#only updates portion specified




gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	gameDisplay.fill(blue)
	#look up draw.rect()
	pygame.draw.rect(gameDisplay, black, [400,300, 10, 100])


	gameDisplay.fill(blue, rect=[200,200, 20,20])


	gameDisplay.fill(blue, rect=[50,50, 20,20])
	pygame.draw.lines(gameDisplay, yellow, False, [(100,100), (200,200), (300,100)], 50)
	pygame.draw.lines(gameDisplay, yellow, False, [(100,100), (100,300)], 50)
	pygame.draw.lines(gameDisplay, yellow, False, [(300,100), (300,300)], 50)
	pygame.display.update()		




#required
pygame.quit()
quit()				#exits python