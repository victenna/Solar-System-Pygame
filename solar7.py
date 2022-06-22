import pygame,random,math
pygame.init()
screen = pygame.display.set_mode((1200, 900))
clock = pygame.time.Clock()
Sun=pygame.image.load('Sun1.png')
Sun_rect=Sun.get_rect(center=(600,450))
class Planet:
    def __init__(self,image):#,angle):
        super().__init__()
        self.image=pygame.image.load(image)
        self.angle=0#angle
    def update(self,dangle,radius):
        self.angle+=dangle
        x_pos=math.cos(self.angle) * radius + 600
        y_pos=-math.sin(self.angle) * radius + 450
        self.rect=self.image.get_rect(center=(x_pos,y_pos))
    def draw(self):
        screen.blit(self.image,self.rect)
mercury=Planet('Mercury2.png')
venus=Planet('Venus.png')
earth=Planet('Earth.png')
mars=Planet('Mars3.png')
jupiter=Planet('Jupiter.png')
saturn=Planet('Saturn.png')
uranus=Planet('Uranus2.png')
neptune=Planet('Neptune2.png')
stars = [(random.randint(0, 1200), random.randint(0, 900)) for x in range(140)]
while True:
    screen.fill('black')
    for star in stars:
        x, y = star[0], star[1]
        pygame.draw.line(screen, 'white', (x, y), (x, y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(Sun,Sun_rect)
    mercury.update(0.03,80)
    mercury.draw()
    venus.update(0.025,120)
    venus.draw()
    earth.update(0.02,180)
    earth.draw()
    
    mars.update(0.0175,230)
    mars.draw()
    jupiter.update(0.0085,310)
    jupiter.draw()
    saturn.update(0.007,390)
    saturn.draw()
    uranus.update(0.005,450)
    uranus.draw()
    neptune.update(0.0045,510)
    neptune.draw()
    pygame.display.update()
    clock.tick(50)        