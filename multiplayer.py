import pygame,pyautogui,random
pygame.init()
W,H=pyautogui.size()
techwars=pygame.display.set_mode((W,H))
bg=pygame.image.load("darkcity.jpg")
bg=pygame.transform.scale(bg,(W,H))
cyborg=pygame.transform.scale(pygame.image.load("Cyborg.png"),(300,300))
golem=pygame.transform.scale(pygame.image.load("golem.png"),(300,300))
border=pygame.Rect(W/2-25,0,50,H)
fence=pygame.transform.scale(pygame.image.load("Fence.png"),(50,H))
def draw(cr,gr):
    techwars.blit(bg,(0,0))
    # pygame.draw.rect(techwars,"cyan",cr)
    # pygame.draw.rect(techwars,"cyan",gr)
    techwars.blit(cyborg,(cr.x-60,cr.y-10))
    techwars.blit(golem,(gr.x-40,gr.y-20))
    techwars.blit(fence,(border.x, border.y))

def handlemovement(cr,gr,keys):
    if keys [pygame.K_UP] and cr.y > 10:
        cr.y-=10
    if keys [pygame.K_DOWN] and cr.y + cr.height < H:
        cr.y+=10
    if keys [pygame.K_RIGHT] and cr.x + cr.width < border.x:
        cr.x+=10
    if keys [pygame.K_LEFT] and cr.x > 0:
        cr.x-=10
    if (random.randint(1,100)<4):
        # gr.x=random.randint(border.x+border.width,W-gr.width)
        if gr.x > border.x+border.width and gr.x < W-gr.width-100 and gr.y > 10 and gr.y < H-gr.height:
            gr.x +=random.randint(-100,100)
            gr.y +=random.randint(-100,100)





def main():
    cr=pygame.Rect(100,H/2,180,280)
    gr=pygame.Rect(W-400,H/2,220,260)


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
