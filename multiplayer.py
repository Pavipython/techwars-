import pygame,pyautogui,random
pygame.init()
W,H=pyautogui.size()
techwars=pygame.display.set_mode((W,H))
bg=pygame.image.load("darkcity.jpg")
bg=pygame.transform.scale(bg,(W,H))
cyborg=pygame.transform.scale(pygame.image.load("Cyborg.png"),(300,300))
cyborg=pygame.transform.flip(cyborg,True,False)
golem=pygame.transform.scale(pygame.image.load("golem.png"),(300,300))
border=pygame.Rect(W/2-25,0,50,H)
fence=pygame.transform.scale(pygame.image.load("Fence.png"),(50,H))
laser=pygame.transform.scale(pygame.image.load("laser.png"),(100,20))
boulder=pygame.transform.scale(pygame.image.load("meteor1.png"),(80,60))
def draw(cr,gr,lasers,boulders):
    techwars.blit(bg,(0,0))
    # pygame.draw.rect(techwars,"cyan",cr)
    # pygame.draw.rect(techwars,"cyan",gr)
    techwars.blit(cyborg,(cr.x-60,cr.y-10))
    techwars.blit(golem,(gr.x-40,gr.y-20))
    techwars.blit(fence,(border.x, border.y))
    for i in lasers:
        # pygame.draw.rect(techwars,"white", i)
        techwars.blit(laser,(i.x, i.y))
    for i in boulders:
            # pygame.draw.rect(techwars,"brown", i)
            techwars.blit(boulder,(i.x, i.y))    

def handlemovement(cr,gr,keys):
    if keys [pygame.K_UP] and cr.y > 10:
        cr.y-=10
    if keys [pygame.K_DOWN] and cr.y + cr.height < H:
        cr.y+=10
    if keys [pygame.K_RIGHT] and cr.x + cr.width < border.x:
        cr.x+=10
    if keys [pygame.K_LEFT] and cr.x > 0:
        cr.x-=10
    if (random.randint(1,90)<4):
        # gr.x=random.randint(border.x+border.width,W-gr.width)
        if gr.x > border.x+border.width and gr.x < W-gr.width-100 and gr.y > 10 and gr.y < H-gr.height:
            gr.x +=random.randint(-50,50)
            gr.y +=random.randint(-150,150)


def handlebullets(cr,gr,lasers,boulders):
    pass


def main():
    cr=pygame.Rect(100,H/2,180,280)
    gr=pygame.Rect(W-400,H/2,220,260)
    lasers=[]
    boulders=[]


    while True:
        draw(cr,gr,lasers,boulders)
        keys=pygame.key.get_pressed()
        handlemovement(cr,gr,keys)
        for i in pygame.event.get():
            print(i)
            if i.type==pygame.QUIT:
                pygame.quit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_SPACE:
                    bullet=pygame.Rect(cr.x + cr.width/2, cr.y + 50, 100,20)
                    lasers.append(bullet)
        if random.randint(1,100) < 5:
            bullet=pygame.Rect(gr.x , gr.y + gr.height -100, 80,60)
            boulders.append(bullet)
        handlebullets(cr,gr,lasers,boulders)
        pygame.display.update()

main()
