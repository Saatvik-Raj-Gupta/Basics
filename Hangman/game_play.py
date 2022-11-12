import pygame
import math
import random
import mysql.connector


##*****___________*****##


##SQL connection##
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="root",
                             database="hangman")

##cursor object##
cursor=mydb.cursor()


##*****___________*****##


##Getting the word and hint##

def word_hint(x):
    sql="select Word from words where W_ID like(%s)"
    cursor.execute(sql,(x,))
    word=cursor.fetchall()
    
    ##fetchall() gets a list and the word will be a tuple inside that list##
    z=word
    y=z[0]
    W=y[0]
    sql="select Hint from words where W_ID like(%s)"
    cursor.execute(sql,(x,))
    hint=cursor.fetchall()
    
    ##fetchall() gets a list and the hint will be a tuple inside that list##
    a=hint
    b=a[0]
    H=b[0]
    return([W,H])


##*****___________*****##


##This thing runs the GAME##

##putting everything in a function to reduce error##

def game():
    pygame.init()
    
    ##basic variables##
    WIDTH=1000
    HEIGHT=600
    WHITE=(255,255,255)
    BLACK=(0,0,0)
    HEADER=pygame.font.SysFont("comicsans",60)
    FONT=pygame.font.SysFont("comicsans",40)
    win=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("HANGMAN")
    
    ##making a list to hold images##
    images=[]

    ##using for loop to load images##
    for i in range(0,7):
        img=pygame.image.load("hangman"+str(i)+".png")#loading images
        images.append(img)
       
    hangman_status=0
    x=random.randint(0,11)
    W=word_hint(x)
    
    ##return() gives a list##
    word=W[0]
    hint=W[1]
    guessed=[]

    ##variables for buttons##
    RADIUS=25
    GAP=20
    letters=[]
    
    ##value from where buttons will appear##
    startx=round((WIDTH-(RADIUS*2+GAP)*13)/2)
    starty=400
    
    ##using IISC codes to get letters##
    A=65

    ##getting the possition of buttons and letters##
    for i in range(26):
        x=startx+GAP*2+((RADIUS*2+GAP)*(i%13))
        y=starty+((i//13)*(GAP+RADIUS*2))
        letters.append([x,y,chr(A+i),True])
        ##making a list inside a list to hold different variables coressponding to a letter##

    ##making a function to display the win/lost message##
    def message(t):
        pygame.time.delay(1000)
        win.fill(WHITE)
        text=FONT.render(t,1,BLACK)
        win.blit(text,(WIDTH/2-text.get_width()/2,HEIGHT/2-text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(2000)

    ##drawing everything to the screen##
    def draw():
        win.fill(WHITE)

        ##header##
        text=HEADER.render("HANGMAN",1,BLACK)
        win.blit(text,(WIDTH/2-text.get_width()/2,50))

        ##hint button##
        pygame.draw.rect(win,BLACK,(900,5,70,40),3)
        text=FONT.render("HINT",1,BLACK)
        win.blit(text,(905,10))

        ##back button##
        pygame.draw.rect(win,WHITE,(5,5,75,25),1)
        text=FONT.render("BACK",1,BLACK)
        win.blit(text,(5,5))

        ##displaying the blanks for the word##
        display_word=""
        for letter in word:
            if letter in guessed:
                display_word+=letter+ " "
            else:
                display_word+="_ "
        text=FONT.render(display_word,1,BLACK)
        win.blit(text,(400,200))

        ##drawing buttons for letters##
        for letter in letters:
            x,y,ltr,visible=letter
            if visible:
                pygame.draw.circle(win,BLACK,(x,y),RADIUS,3)
                text=FONT.render(ltr,1,BLACK)
                win.blit(text,(x-text.get_width()/2,y-text.get_height()/2))

        ##displaying hangman image and adding note##
        win.blit(images[hangman_status],(100,100))
        text=FONT.render("GO TO THE MAIN MENU TO QUIT",1,BLACK)
        win.blit(text,(200,560))
        pygame.display.update()

    ##main loop in game function##
    run=True

    ##getting a clock for game##
    FPS=60
    clock=pygame.time.Clock()

    ##while loop##
    while run:
        global hangman_satatus
        draw()
        clock.tick(FPS)
        for event in pygame.event.get():

            ##closing on clicking cross##
            if event.type== pygame.QUIT:
                run=False

            ##getting the input of mouse clicks##
            if event.type==pygame.MOUSEBUTTONDOWN:
                m_x,m_y=pygame.mouse.get_pos()

                ##giving the hint##
                if 900<m_x <970 and 5<m_y<45:
                    print(hint)

                ##getting back to the menu##
                elif 5<m_x<75 and 5<m_y<25:
                    menu()

                ##checking for the clicks on button or not##
                for letter in letters:
                    x,y,ltr,visible=letter
                    dis=math.sqrt((x-m_x)**2+(y-m_y)**2)
                    if visible:
                        if dis<RADIUS:
                            letter[3]=False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status+=1
        draw()
        
        ##deciding the winner or looser##
        won=True
        for letter in word:
            if letter not in guessed:
                won=False
                break
        if won:        
             message("WON")
             break
        if hangman_status==6:
            message("LOST")
            break
    pygame.quit()


##*****___________*****##


##Rules for the game##
def rules():
    pygame.init()

    ##basic variables##
    WIDTH=1000
    HEIGHT=600
    WHITE=(255,255,255)
    BLACK=(0,0,0)
    HEADER=pygame.font.SysFont("comicsans",60)
    FONT=pygame.font.SysFont("comicsans",40)
    win=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("HANGMAN")

    ##displaying the image and header##
    image=pygame.image.load("hangman6.png")
    win.fill(WHITE)
    text=HEADER.render("HANGMAN",1,BLACK)
    win.blit(text,(WIDTH/2-text.get_width()/2,50))
    win.blit(image,(100,200))

    ##writing the rules##
    rules="The motive of the game is to guess the word before"
    rules1="the diagram of the hangman is complete.The"
    rules2="blank spaces give exact lenght of the word. There"
    rules3="is an option of hint on the top left corner of the"
    rules4="screen where the meaning of the word or a picture"
    rules5="realted to it will be shown.The word has to be"
    rules6="gueessed in the alloted time Each player will"
    rules7="get 4 life. For each correct guessed word"
    rules8="player will get 10 points.ENJOY!!"

    ##displaying the rules##
    text=FONT.render(rules,1,BLACK)
    win.blit(text,(300,190))
    text=FONT.render(rules1,1,BLACK)
    win.blit(text,(300,220))
    text=FONT.render(rules2,1,BLACK)
    win.blit(text,(300,250))
    text=FONT.render(rules3,1,BLACK)
    win.blit(text,(300,280))
    text=FONT.render(rules4,1,BLACK)
    win.blit(text,(300,310))
    text=FONT.render(rules5,1,BLACK)
    win.blit(text,(300,340))
    text=FONT.render(rules6,1,BLACK)
    win.blit(text,(300,370))
    text=FONT.render(rules7,1,BLACK)
    win.blit(text,(300,400))
    text=FONT.render(rules8,1,BLACK)
    win.blit(text,(300,430))

    ##back button##
    pygame.draw.rect(win,WHITE,(5,5,75,25),1)
    text=FONT.render("BACK",1,BLACK)
    win.blit(text,(5,5))

    ##updating the screen##
    pygame.display.update()

    ##main loop of the rules() function##
    run=True
    while run:
        for event in pygame.event.get():
            
            ##checking if user wants to quit##
            if event.type== pygame.QUIT:
                run=False

            ##checking the mouse inputs##
            if event.type== pygame.MOUSEBUTTONDOWN:
                m_x,m_y=pygame.mouse.get_pos()

                ##checking if they click on back button##
                if 5<m_x<75 and 5<m_y<25:
                    menu()
    pygame.quit()


##*****___________*****##


##Credits##

def credit():
    pygame.init()

    ##basic variables##
    WIDTH=1000
    HEIGHT=600
    WHITE=(255,255,255)
    BLACK=(0,0,0)
    HEADER=pygame.font.SysFont("comicsans",60)
    FONT=pygame.font.SysFont("comicsans",40)
    win=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("HANGMAN")

    ##displaying the image and header##
    image=pygame.image.load("hangman6.png")
    win.fill(WHITE)
    text=HEADER.render("HANGMAN",1,BLACK)
    win.blit(text,(WIDTH/2-text.get_width()/2,50))
    win.blit(image,(100,200))

    ##back button##
    pygame.draw.rect(win,WHITE,(5,5,75,25),1)
    text=FONT.render("BACK",1,BLACK)
    win.blit(text,(5,5))

    ##creating a rectangle for scrolling text##
    pygame.draw.rect(win,BLACK,(350,200,550,300),1)
    pygame.display.update()

    ##variables for scrolling text##
    centerx=400
    centery=250
    centery1=300
    centery2=350
    deltaY=0

    ##main loop for the credit() function##
    run=True
    while run:
        for event in pygame.event.get():

            ##checking if the user wants to quit##
            if event.type== pygame.QUIT:
                run=False

            ##getting the mouse possition##
            if event.type== pygame.MOUSEBUTTONDOWN:
                m_x,m_y=pygame.mouse.get_pos()

                ##checking if they click on back button##
                if 5<m_x<75 and 5<m_y<25:
                    menu()

        '''displaying the image and header as the
           screen will be updated every second for
           scrolling texrt'''
        image=pygame.image.load("hangman6.png")
        win.fill(WHITE)
        text=HEADER.render("HANGMAN",1,BLACK)
        win.blit(text,(WIDTH/2-text.get_width()/2,50))
        win.blit(image,(100,200))
        pygame.draw.rect(win,WHITE,(5,5,75,25),1)
        text=FONT.render("BACK",1,BLACK)
        win.blit(text,(5,5))

        ##scrolling text##
        msg=FONT.render("created by:",1,BLACK)
        pos=(centerx,centery+deltaY)
        msg1=FONT.render("Saatvik Gupta",1,BLACK)
        pos1=(centerx,centery1+deltaY)
        msg2=FONT.render("XII-A",1,BLACK)
        pos2=(centerx,centery2+deltaY)
        deltaY -= 1

        ##repeating the scrolling text##
        if(centery+deltaY<200):
            deltaY=220
        win.blit(msg,pos)
        win.blit(msg1,pos1)
        win.blit(msg2,pos2)
        pygame.display.update()
    pygame.quit()


##*****___________*****##


##Menu##
def menu():
    pygame.init()

    ##basic variables##
    WIDTH=1000
    HEIGHT=600
    WHITE=(255,255,255)
    BLACK=(0,0,0)
    HEADER=pygame.font.SysFont("comicsans",60)
    FONT=pygame.font.SysFont("comicsans",40)
    win=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("HANGMAN")

    ##displaying the image and header##
    image=pygame.image.load("hangman6.png")
    win.fill(WHITE)
    text=HEADER.render("HANGMAN",1,BLACK)
    win.blit(text,(WIDTH/2-text.get_width()/2,50))
    win.blit(image,(100,200))

    ##drwaing the button for various optins##
    pygame.draw.rect(win,BLACK,(450,200,150,50),3)

    pygame.draw.rect(win,BLACK,(450,300,150,50),3)

    pygame.draw.rect(win,BLACK,(450,400,150,50),3)

    ##adding the text in those buttons##
    text=FONT.render("START",1,BLACK)
    win.blit(text,(475,205))

    text=FONT.render("RULES",1,BLACK)
    win.blit(text,(475,305))


    text=FONT.render("CREDITS",1,BLACK)
    win.blit(text,(470,405))
    pygame.display.update()

    ##main loop for the menu() finction##
    run=True
    while run:
        for event in pygame.event.get():

            ##checking if the user wants to quit##
            if event.type== pygame.QUIT:
                run=False

            ##getting the mouse click possition##
            if event.type==pygame.MOUSEBUTTONDOWN:
                m_x,m_y=pygame.mouse.get_pos()

                ##checking if they want to start the game##
                if 450<m_x<600 and 200<m_y<250:
                    while True:
                        game()

                ##checking if they want to see the rules##
                elif 450<m_x<600 and 300<m_y<350:
                    rules()

                ##checking if they want to see the credits##
                elif 450<m_x<600 and 400<m_y<450:
                    credit()
    pygame.quit()


##*****___________*****##


##Main loop##
def main():
    
    ##main loop of the main() function##
    while True:
        menu()

##*****___________*****##


##Calling main function##

main()



