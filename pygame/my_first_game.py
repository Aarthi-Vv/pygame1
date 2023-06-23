import pygame
import random

from  pygame. locals import*
pygame.init()

blck=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)

w=650
h=700
#Image size in pixel
p=64

screen=pygame.display.set_mode((w,h))

#Game Name

pygame.display.set_caption("Hit Hit")

#Game symbol

icon=pygame.image.load("thunder.png ")
pygame.display.set_icon(icon)

#Background image

bg=pygame.image.load("background.jpg ")

#Boy Image
boy=pygame.image.load("boy.png")

#Boy's position in x axis and y axis

boyposx=(w/2)-(p/2)
boyposy= h-p-10

boyposchange=0

def boy(x,y):
    
    screen.blit(boy,(x,y))

#obstacle
obs=pygame.image.load(" ")

#obstcle position

obsposx=random.randint(0,(width-pixel))
obsposy=0-pixel

#speed
obsposxchange=0
obsposychange=2


#Function

def obs(x,y):

    screen.blit(obs,(x,y))
    
def crash():

    global obsposy
    if  boyposy<(obsposy + p):
        
        if ((boyposx > obsposx and boyposx <(obsposy+p))or((boyposx+p)> obsposx  and (boyposx+p)<(obsposx+p))):


                     obsposy = h +1000

running=True
while running:
    screen.blit(bg,(0,0))

    for event in pygame.event.get():

          if event. type == pygame . Quit :

               pygame. quit()

          if event. type == pygame.KEYDOWN:

               if event.key == pygame.K_RIGHT:

                     boyposxchange = 3

               if event.key == pygame.K_LEFT:

                     boyposxchange = -3
                     
          if event.type == pygme.KEYUP:

                 if event.key == pygame.K_RIGHT or K_LEFT:

                         boyposxchange=0
                         
if boyposx >=(w-p):
    boyposx = (w-p)

if boyposx <= 0:
    boyposx=0

if (obsposy >= h-0 and obsposy <= (h+200)):

      obsposy = 0-p
      
      obsposx = random.randint(0,(w-p))

boyposy += boyposxchange
obsxpos += obsposychnge

#Function call
boy(boyposx,boyposy)

obs(obsposx,obsposy)

crash()

pygame.display.update()










    








                     


































    


