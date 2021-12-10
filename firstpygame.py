import pygame
pygame.init()

from pygame import mixer
mixer.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First PyGame")
font = pygame.font.SysFont("arial", 16)
text = font.render("Use the ←↑→↓ keys to move the sun, space bar changes its color!", True, (244, 246, 240))
#icon source: https://pngtree.com/freepng/vector-flower-icon_4102412.html
icon=pygame.image.load("flower.jpg")
pygame.display.set_icon(icon) 
done = False
x=60
y=120
#img source: https://www.imgbase.info/images/safe-wallpapers/miscellaneous/8_bit/57676_8_bit_8_bit_art.jpg
image=pygame.image.load("wallpaper.jpg")
image = pygame.transform.scale(image, (500, 500))
#music source: https://www.chosic.com/download-audio/29440/
pygame.mixer.music.load("lofi.mp3")
pygame.mixer.music.play(-1)
#music source2: https://www.chosic.com/download-audio/26756/
pygame.mixer.music.queue("lofi2.mp3")
screen.blit(image, (0, 0))
issun = True
clock = pygame.time.Clock()

while not done:
        clock.tick(60)
        pressed = pygame.key.get_pressed()
        if x<=0:
                x=0
        elif x>=400:
                x=400
        if y>=400:
                 y=400
        elif y<=0:
                 y=0
        screen.blit(image, (0, 0))
        screen.blit(text, (10,0))
        if pressed[pygame.K_UP]: y -= 1
        if pressed[pygame.K_DOWN]: y += 1
        if pressed[pygame.K_LEFT]: x -= 1
        if pressed[pygame.K_RIGHT]: x += 1
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                                issun = not issun
                if issun: color = (227,187,28)
                else: color = (244, 246, 240)
        pygame.draw.circle(screen, color, (x,y),50)
        pygame.display.flip()
        
