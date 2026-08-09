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
laser=pygame.transform.scale(pygame.image.load("laser.png"),(100,100))
thunder=pygame.transform.scale(pygame.image.load("thunder.png"),(100,100))

def draw(ir,th,lasers,thunders):
    techwars.blit(bg,(0,0))
    techwars.blit(Ironman,(ir.x-60,ir.y-10))
    techwars.blit(Thor,(th.x-40,th.y-20))
    techwars.blit(Tower,(border.x, border.y))
    for i in lasers:
        techwars.blit(laser,(i.x,i.y))
    for i in thunders:
        techwars.blit(thunder,(i.x,i.y))

def handlemovement(ir,th,keys):
    if keys [pygame.K_w] and ir.y > 10:
        ir.y-=6
    if keys [pygame.K_s] and ir.y + ir.height < H:
        ir.y+=6
    if keys [pygame.K_d] and ir.x + ir.width < border.x:
        ir.x+=6
    if keys [pygame.K_a] and ir.x > 0:
        ir.x-=6
    if keys [pygame.K_UP] and th.y > 10:
        th.y-=6
    if keys [pygame.K_DOWN] and th.y + th.height < H:
        th.y+=6
    if keys [pygame.K_RIGHT] and th.x + th.width < W:
        th.x+=6
    if keys [pygame.K_LEFT] and th.x > border.x + border.width:
        th.x-=6
    

def handlebullets(ir,th,lasers,thunders):
    pass


def main():
    ir=pygame.Rect(100,H/2,180,280)
    th=pygame.Rect(W-400,H/2,220,260)
    lasers=[]
    thunders=[]



    while True:
        draw(ir,th,lasers,thunders)
        keys=pygame.key.get_pressed()
        handlemovement(ir,th,keys)
        for i in pygame.event.get():
            print(i)
            if i.type==pygame.QUIT:
                pygame.quit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_LSHIFT:
                    bullet=pygame.Rect(ir.x + ir.width/1.3, ir.y + 50, 100,100)
                    lasers.append(bullet)
                if i.key==pygame.K_RSHIFT:
                    bullet=pygame.Rect(th.x + th.width/-2.1, th.y + 50, 100,100)
                    thunders.append(bullet)
        handlebullets(ir,th,lasers,thunders)
        pygame.display.update()

main()