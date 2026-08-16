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
laser=pygame.transform.scale(pygame.image.load("laser.png"),(100,100))
boulder=pygame.transform.scale(pygame.image.load("meteor1.png"),(100,100))
instructorfont=pygame.font.SysFont("Arial",35,True,True)
scorefont=pygame.font.SysFont("Arial",50,True)

gamestate="start"
instructions=["press space to start the game","cyborg vs golem warfare","use w,a,s,d to control the cyborg","golem is an AI character","press space to shoot the golem","defend your self from the boulders","who ever score 50 is the winner"]

def draw(cr,gr,lasers,boulders,cyborgscore,golemscore,winner):
    techwars.blit(bg,(0,0))
    # pygame.draw.rect(techwars,"cyan",cr)
    # pygame.draw.rect(techwars,"cyan",gr)
    techwars.blit(cyborg,(cr.x-60,cr.y-10))
    techwars.blit(golem,(gr.x-40,gr.y-20))
    techwars.blit(fence,(border.x, border.y))

    yp=300
    if gamestate == "start":
        for i in instructions:
            text=instructorfont.render(i,1,"cyan")
            techwars.blit(text,(W/3,yp))
            yp=yp+80

    for i in lasers:
        # pygame.draw.rect(techwars,"white", i)
        techwars.blit(laser,(i.x, i.y))
    for i in boulders:
            # pygame.draw.rect(techwars,"brown", i)
            techwars.blit(boulder,(i.x, i.y))  
    cyborgtext=scorefont.render(f"Score:{cyborgscore}",1,"green")
    golemtext=scorefont.render(f"score:{golemscore}",1,"red")
    techwars.blit(cyborgtext,(50,50))
    techwars.blit(golemtext,(W-300,50)) 
    winnertext=scorefont.render(winner,True,"purple","white")
    techwars.blit(winnertext,(W/3,H/3)) 


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
        # if gr.x > border.x+border.width and gr.x < W-gr.width-100 and gr.y > 10 and gr.y < H-gr.height:
        gr.x +=random.randint(-50,50)
        gr.y +=random.randint(-150,150)
        gr.x = max(border.x+border.width,gr.x)
        gr.x = min(W-gr.width,gr.x)
        gr.y = max(10,gr.y)
        gr.y = min(H-gr.height,gr.y)


def handlebullets(cr,gr,lasers,boulders,cyborgscore,golemscore):

    for i in lasers:
        i.x+=10
        if i.x > W:
            lasers.remove(i)
        if i.colliderect(gr):
            lasers.remove(i)
            cyborgscore+=1
    for i in boulders:
        i.x-=10
        if i.x < 0:
            boulders.remove(i)
        if i.colliderect(cr):
            boulders.remove(i)
            golemscore+=1
            continue
        for l in lasers:
            if l.colliderect(i):
                boulders.remove(i)
                lasers.remove(l)
                break
    return cyborgscore,golemscore    
        

    
    


def main():
    cr=pygame.Rect(100,H/2,180,280)
    gr=pygame.Rect(W-400,H/2,220,260)
    lasers=[]
    boulders=[]
    golemscore=0
    cyborgscore=0
    winner=None



    while True:
        draw(cr,gr,lasers,boulders,cyborgscore,golemscore,winner)
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
        cyborgscore,golemscore = handlebullets(cr,gr,lasers,boulders,cyborgscore,golemscore)
        if cyborgscore == 50:
            winner="cyborg is the winner"
        if golemscore == 50:
            winner="golem is the winner"


        pygame.display.update()

main()
