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
    all_sprites_list.update()
    screen.fill(surf_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
