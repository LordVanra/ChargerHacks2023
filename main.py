import pygame
import asyncio
import sys
import math
from pygame.locals import *
from pygame.sprite import *
from random import randint
from time import sleep

#init pygame
pygame.init()
windowSurface = pygame.display.set_mode((1000, 600), 0, 32);
pygame.display.set_caption("Pollution game");
windowRect = windowSurface.get_rect()

#colors and fonts
BLACK = (0, 0, 0)
RED = (255, 0, 0)
basicFont = pygame.font.SysFont(None, 72)
smallFont = pygame.font.SysFont(None, 32)

#header
text = basicFont.render("Catch the plastic", False, BLACK)
textRect = text.get_rect()
textRect.centerx = windowRect.centerx
textRect.midtop = windowRect.midtop

#backdrop
image = pygame.image.load("img/bg.png")
bgRect = image.get_rect()
bgRect.centerx = windowRect.centerx
bgRect.centery = windowRect.centery

#player
plr = pygame.image.load("img/player.png")
plrRect = plr.get_rect()
plrRect.midbottom = windowRect.midbottom
plrRect.y -= 75

#draw items
windowSurface.blit(image, bgRect)
windowSurface.blit(text, textRect)
windowSurface.blit(plr, plrRect)

#draw everything
pygame.display.update()

class Trash(Sprite):
	def __init__(this, images):
		super().__init__()
		this.screen = windowSurface
		
		this.trash = pygame.image.load("img/trash/bottle.png")
		this.rect = this.trash.get_rect()
		this.rect.x = randint(30, 900)
		this.rect.y -= 50
		#rn = randint(0, len(images))
		
		#print(rn)
		
	def update(this):	
		this.rect.y += 5

async def main():

	#constants and variable
	IMAGES = ["src/trash/bottle.png", "src/trash/bag.png", "src/trash/fork.png", "src/trash/milk.png", "src/trash/trash.png"]
	SPEED = 7.5
	MAXRIGHT = 919
	diff = 250
	lives = 9
	score = 0
	alive = True
	left = False;
	right = False;
	trashes = pygame.sprite.Group()
	
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
		
		if alive:
		
			#move
			if left:
				plrRect.x -= SPEED
			if right:
				plrRect.x += SPEED
			
			if plrRect.x < 0 :
				plrRect.x = 0
			if plrRect.x > MAXRIGHT:
				plrRect.x = MAXRIGHT
				
			#create trash
			if randint(0,diff) == 1:
				newTrash = Trash(IMAGES)
				trashes.add(newTrash)
				
			#redraw screen
			windowSurface.blit(image, bgRect)
			windowSurface.blit(text, textRect)
			windowSurface.blit(plr, plrRect)
			for trash in trashes.sprites():
				trash.update()
				windowSurface.blit(trash.trash, trash.rect)
			
			#check for collisions
			for trash in trashes.sprites():
				if trash.rect.y>300:
					if abs(trash.rect.x-plrRect.x)<100:
						trash.kill()
						score += 1
					else:
						trash.kill()
						lives -= 1
					diff -= 15
			if diff < 15:
				diff = 50
			print(diff)
			
			text1 = smallFont.render("Lives left: " + str(lives), False, BLACK)
			textRect1 = text1.get_rect()
			textRect1.topleft = windowRect.topleft
			
			text2 = smallFont.render("Score: " + str(score), False, BLACK)
			textRect2 = text2.get_rect()
			textRect2.topleft = windowRect.topleft
			textRect2.y += 20
			
			windowSurface.blit(text1, textRect1)
			windowSurface.blit(text2, textRect2)
			
			pygame.display.update()
			
		if lives<=0:
			alive = False
			
			windowSurface.fill(BLACK)
			text3 = smallFont.render("Game over! Score: " + str(score), False, RED)
			textRect3 = text3.get_rect()
			textRect3.centerx = windowRect.centerx
			textRect3.centery = windowRect.centery
			windowSurface.blit(text3, textRect3)
		
			pygame.display.update()
		await asyncio.sleep(0)
		
asyncio.run(main())
