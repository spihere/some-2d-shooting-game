#! /usr/bin/env python3
''' An example of sprites: Mario is a sprite '''
import pygame

def main():
    pygame.init()
    window_size_x = 1200
    window_size_y = 622
    surface = pygame.display.set_mode([window_size_x,window_size_y]) 
    pygame.display.set_caption('Mario as a Sprite')
    background = pygame.image.load('mario_background.png').convert()
    surface.blit(background, (0,0))
    sprites_surf = pygame.image.load('mario_sprites.png').convert()
    
    mario_group = pygame.sprite.GroupSingle()  
    coins_group = pygame.sprite.Group()
            
    clock = pygame.time.Clock()  
    while True:
        clock.tick(60)
        quit, click, click2 = check_events()
        if quit:
            break
        if click:        
            mario = Mario(click, sprites_surf)
            mario_group.add(mario)
        if click2:
            coin = Coin(click2, sprites_surf)
            coins_group.add(coin)

        mario_group.update(window_size_y)
        if len(mario_group) > 0 and len(coins_group) > 0:
            pygame.sprite.spritecollide(mario_group.sprite, coins_group, True, 
                                        collided=pygame.sprite.collide_circle)
        
        surface.blit(background, (0,0))
        mario_group.draw(surface)
        coins_group.draw(surface)
        pygame.display.flip()

class Mario(pygame.sprite.Sprite):

    def __init__(self, pos, sprites_surf):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((29,47))        
        self.image.blit(sprites_surf, (0,0), (4, 13, 29, 47))
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect(center=pos) 
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self, size_y):
        self.rect.move_ip(0,1)
        if self.rect.top > size_y:
            self.kill()

class Coin(pygame.sprite.Sprite):
    
    def  __init__(self, pos, sprites_surf):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((18,18))        
        self.image.blit(sprites_surf, (0,0), (371, 88, 18, 18))
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect(center=pos) 
        self.mask = pygame.mask.from_surface(self.image)
        self.radius = 20
        
    def update(self):
        pass
                   
def check_events():
    ''' A controller of sorts.  Looks for Quit, several simple events.
        Returns: True/False for if a Quit event happened.
    '''
    
    quit = False
    click = click2 = None
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit = True
            if event.key == pygame.K_ESCAPE:
                quit = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                click = event.pos
            if event.button == 3:
                click2 = event.pos
                
    return quit, click, click2

if __name__ == "__main__":
    main()