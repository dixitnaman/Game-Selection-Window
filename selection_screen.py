import pygame

class button():
    def __init__(self,x,y,image):
        self.image=image
        self.rect =self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False

    def drawbutton(self,surface):
        start_action=False
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                start_action=True
        if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False
        surface.blit(self.image,(self.rect.x,self.rect.y))
        return start_action