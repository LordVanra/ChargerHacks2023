import pygame
import asyncio
import sys
import math
from pygame.locals import *
from random import randint
from time import sleep

#init pygame
pygame.init()
windowSurface = pygame.display.set_mode((1000, 600), 0, 32);
pygame.display.set_caption("Pollution game");
windowRect = windowSurface.get_rect()

#colors and fonts
BLACK = (0, 0, 0)
LIGHT_GREY = (240, 240, 240)
basicFont = pygame.font.SysFont(None, 48)

windowSurface.fill(LIGHT_GREY)

#header
text = basicFont.render("Catch the plastic", False, BLACK)
textRect = text.get_rect()
textRect.centerx = windowRect.centerx
textRect.midtop = windowRect.midtop

#backdrop
image = pygame.image.load("img/bg.bmp")
bgRect = image.get_rect()
bgRect.centerx = windowRect.centerx
bgRect.centery = windowRect.centery

#player
plr = pygame.image.load("img/player.bmp")
plrRect = plr.get_rect()
plrRect.midbottom = windowRect.midbottom

#draw items
windowSurface.blit(image, bgRect)
windowSurface.blit(text, textRect)
windowSurface.blit(plr, plrRect)

#draw everything
pygame.display.update()


async def main():

	SPEED = 1
	left = False;
	right = False;
	
	while True:
		
		#check for events
		for event in pygame.event.get():
		
			#quit application
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
				
			#key pressed
			if event.type == KEYDOWN:
				if event.key == K_RIGHT:
					right = True
				elif event.key == K_LEFT:
					left = True
					
			#key released
			elif event.type == KEYUP:
				if event.key == K_RIGHT:
					right = False
				elif event.key == K_LEFT:
					left = False
		
		#move
		if left:
			plrRect.x -= SPEED
		if right:
			plrRect.x += SPEED
			
		#redraw player
		windowSurface.blit(image, bgRect)
		windowSurface.blit(text, textRect)
		windowSurface.blit(plr, plrRect)
		pygame.display.update()
		await asyncio.sleep(0)
		
asyncio.run(main())
	