import pygame
import random
pygame.init()
surf_color="pink" 
color="blue" 

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(surf_color)
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect=self.image.get_rect()
    def moveRight(self,pixels):
       self.rect.x+=pixels
    def moveLeft(self,pixels):
       self.rect.x-=pixels
    def moveForward(self,speed):
       self.rect.y-=speed*speed/10
    def moveBackward(self,speed):
       self.rect.y+=speed*speed/10 
bg=pygame.image.load("nature.jpeg")   
bg=pygame.transform.scale(bg,(600,600))  
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Add Sprite" )
all_sprites_list=pygame.sprite.Group()

sp1=Sprite(color,20,30)
sp1.rect.x=random.randint(10,580)
sp1.rect.y=random.randint(10,580)
all_sprites_list.add(sp1)

sp2=Sprite("brown",20,30)
sp2.rect.x=random.randint(10,580)
sp2.rect.y=random.randint(10,580)
all_sprites_list.add(sp2)
   
exit=True
clock=pygame.time.Clock()
while exit:
    for event in pygame.event.get():
     if event .type==pygame.QUIT:
       exit=False
     elif event.type==pygame.KEYDOWN:
       if event.key==pygame.K_x:
          exit=False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
     sp1.moveLeft(5)
    
    if keys[pygame.K_RIGHT]:
     sp1.moveRight(5)
    
    if keys[pygame.K_DOWN]:
     sp1.moveBackward(5)

    if keys[pygame.K_UP]:
     sp1.moveForward(5)




    all_sprites_list.update()
    screen.fill(surf_color)
    screen.blit(bg,(0,0))   
    all_sprites_list.draw(screen)
    pygame.display.flip()

    if sp1.rect.colliderect(sp2.rect):
     all_sprites_list.remove(sp2)
     text="Great job!"
     font=pygame.font.SysFont("Times new Roman",50)
     text=font.render(text,True,(158,16,16))
     screen.blit(text,(200-text.get_width()//2,140-text. get_height()//2))

    pygame.display.update()
    clock.tick(60)
pygame.quit()

