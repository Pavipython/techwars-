import pygame,pyautogui
pygame.init()
W,H=pyautogui.size()
techwars=pygame.display.set_mode((W,H))
bg=pygame.image.load("Bluesky.jpg")
bg=pygame.transform.scale(bg,(W,H))
Ironman=pygame.transform.scale(pygame.image.load("Ironman.png"),(300,300))
Thor=pygame.transform.scale(pygame.image.load("Thor.png"),(300,300))
border=pygame.Rect(W/2-25,0,50,H)
Tower=pygame.transform.scale(pygame.image.load("Tower.png"),(50,H))


def draw(cr,gr):
    techwars.blit(bg,(0,0))
    techwars.blit(Ironman,(cr.x-60,cr.y-10))
    techwars.blit(Thor,(gr.x-40,gr.y-20))
    techwars.blit(Tower,(border.x, border.y))

def handlemovement(ir,gr,keys):
    if keys [pygame.K_UP] and ir.y > 10:
        cr.y-=6
    if keys [pygame.K_DOWN] and cr.y + cr.height < H:
        cr.y+=6
    if keys [pygame.K_RIGHT] and cr.x + cr.width < border.x:
        cr.x+=6
    if keys [pygame.K_LEFT] and cr.x > 0:
        cr.x-=6
    if keys [pygame.K_w] and gr.y > 10:
        gr.y-=6
    if keys [pygame.K_s] and gr.y + gr.height < H:
        gr.y+=6
    if keys [pygame.K_d]:
        gr.x+=6
    if keys [pygame.K_a]:
        gr.x-=6
    

def main():
    ir=pygame.Rect(100,H/2,180,280)
    th=pygame.Rect(W-400,H/2,220,260)



    while True:
        draw(cr,gr)
        keys=pygame.key.get_pressed()
        handlemovement(cr,gr,keys)
        for i in pygame.event.get():
            print(i)
            if i.type==pygame.QUIT:
                pygame.quit()
        pygame.display.update()

main()