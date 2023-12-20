import pygame
import sys

pygame.init()

#colous
white = (255, 255, 255)
black = (0,0,0)
red = (255,0,0)

#initialize window 
WIDTH = 1000
HIEGHT = 1000
screen = pygame.display.set_mode((WIDTH, HIEGHT))
title = "bezier curves"
pygame.display.set_caption(title)

clock = pygame.time.Clock()

frameRate = 60


startPos = (200,HIEGHT//2)
endPos = (WIDTH-200,HIEGHT//2)


def lerp(a, b, t):
	x = a[0] + (b[0]-a[0])*t
	y = a[1] + (b[1]-a[1])*t
	pos = (x,y)
	return pos



def Bezier(points,rez):
	for point in range(1,rez):
		t = point * (1/rez)
		lines = points

		while len(lines) > 1:
			temp = []
			for i in range(1,len(lines)):
				temp.append(lerp(lines[i-1],lines[i],t))
			lines = temp

		dot = lines[0]
		pygame.draw.circle(screen,white,dot,3)




points = [startPos,endPos]

mouseDown = False

while True:

#INPUT DETECTION
	for event in pygame.event.get():
		#close window
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and mouseDown == False:
			points.append(pygame.mouse.get_pos())
			points[-1],points[-2] = points[-2],points[-1]
			mouseDown = True

		if event.type == pygame.MOUSEBUTTONUP:
			mouseDown = False
		

#DRAW 
	screen.fill(black)

	
	for i in range(len(points)):
		pygame.draw.circle(screen,red,points[i],5)

	Bezier(points,1000)

	clock.tick(frameRate)
	pygame.display.update()

