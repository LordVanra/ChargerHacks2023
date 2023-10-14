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

#draw header
windowSurface.blit(text, textRect)

#draw everything
pygame.display.update()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
	        sys.exit()
		await asyncio.sleep(0)
asyncio.run(main())
