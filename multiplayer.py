import pygame,pyautogui
pygame.init()
W,H=pyautogui.size()
techwars=pygame.display.set_mode((W,H))
bg=pygame.image.load("darkcity.jpg")
bg=pygame.transform.scale(bg,(W,H))
cyborg=pygame.transform.scale(pygame.image.load("Cyborg.png"),(300,300))
golem=pygame.transform.scale(pygame.image.load("golem.png"),(300,300))

def draw():
    techwars.blit(bg,(0,0))
    techwars.blit(cyborg,(100,H/2))
    techwars.blit(golem,(W-400,H/2))

def main():

    while True:
        draw()
        for i in pygame.event.get():
            print(i)
            if i.type==pygame.QUIT:
                pygame.quit()
        pygame.display.update()

main()
