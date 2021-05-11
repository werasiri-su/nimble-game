import os, sys , random
import pygame , time
from pygame.locals import *
pygame.init()

# Pic Hero
C_PLAY_UP = pygame.image.load('PYUP2.png')
C_PLAY_DOWN = pygame.image.load('PYDOWN2.png')
C_PLAY_LEFT = pygame.image.load('PYLEFT2.png')
C_PLAY_RIGHT = pygame.image.load('PYRIGHT2.png')

ICON = pygame.image.load('icon.png')

#Pic fire's hero
FIRE_DOWN = pygame.image.load('Fire_down.png')
FIRE_UP = pygame.image.load('Fire_up.png')
FIRE_LEFT = pygame.image.load('Fire_left.png')
FIRE_RIGHT = pygame.image.load('Fire_right.png')

#Pic enemy
ENEMY_DOWN = pygame.image.load('monster_down.png')
ENEMY_UP = pygame.image.load('monster_up.png')
ENEMY_LEFT = pygame.image.load('monster_left.png')
ENEMY_RIGHT = pygame.image.load('monster_right.png')

#Pic friend
F_CRY = pygame.image.load('ghost_cry3.png')
F_SMILE = pygame.image.load('Ghost_smile.png')

#Background
END_BG = pygame.image.load('end_bg.png')
LEVEL1_BG = pygame.image.load('BG3.png')
LEVEL2_BG = pygame.image.load('BG2.png')
LEVEL3_BG = pygame.image.load('BG5.png')
DEAD_BG = pygame.image.load('DEAD_BG.png')


blood = pygame.image.load('blood.png')

HOLE = pygame.image.load('hole.jpg')

screen_start = pygame.image.load('pic_start3.png')
HOW_TO = pygame.image.load('HOWTOPLAY.png')

#botton 
start_botton = pygame.image.load('start.png')
start_botton2 = pygame.image.load('start2.png')
howto_botton2 = pygame.image.load('howto.png')
howto_botton = pygame.image.load('howto3.png')
quit_botton = pygame.image.load('quit.png')
quit_botton2 = pygame.image.load('quit2.png')

smallfont = pygame.font.SysFont('comicsansms', 25)
medfont = pygame.font.SysFont('comicsansms', 50)
largefont = pygame.font.SysFont('comicsansms', 75)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.x = round(random.randrange(0,100))
        self.y = round(random.randrange(0, height - block_size))
    def char_p(self, block_size, your_friends, direction):
        head = C_PLAY_DOWN
        if direction == "DOwN":
            head = C_PLAY_DOWN
        elif direction == "UP":
            head = C_PLAY_UP
        elif direction == "LEFT":
            head = C_PLAY_LEFT 
        elif direction == "RIGHT":
            head = C_PLAY_RIGHT  
        for i in your_friends[:-1]:
            space.screen.blit(F_SMILE, (i[0], i[1]))
        space.screen.blit(head, (your_friends[-1][0], your_friends[-1][1]))  
            
class Firing(pygame.sprite.Sprite):
    def __init__(self, direction):
        super().__init__()
        self.direction = direction
        if direction == 'DOWN':
            self.image = FIRE_DOWN
        elif self.direction == 'UP':
            self.image = FIRE_UP
        elif self.direction == 'LEFT':    
            self.image = FIRE_LEFT
        elif self.direction == 'RIGHT':    
            self.image = FIRE_RIGHT
        self.rect = self.image.get_rect()
    def update(self):
        if self.direction == 'DOWN':
            fire_y = 45 #move fire
            fire_x = 0
        elif self.direction == 'UP':
            fire_y = -45
            fire_x = 0
        elif self.direction == 'LEFT':
            fire_x = -45
            fire_y = 0
        elif self.direction == 'RIGHT':
            fire_x = 45
            fire_y = 0        
        self.rect.y += fire_y
        self.rect.x += fire_x
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self, typ):
        super().__init__()
        self.image = typ
        self.rect = self.image.get_rect()
        self.way = 'GO' 
        self.shoot_time = 0
        self.laser = False
        self.laser_x = 0
        self.laser_y = 0
        if self.image == ENEMY_DOWN:
            self.enemy_fire = 'down'
        elif self.image == ENEMY_UP:
            self.enemy_fire = 'up'    
        elif self.image == ENEMY_RIGHT:
            self.enemy_fire = 'right'
        elif self.image == ENEMY_LEFT:
            self.enemy_fire = 'left'
            
    def update(self):
        change_x = 0
        change_y = 0
        change_fire_x = 0
        change_fire_y = 0
        if self.enemy_fire == 'left':
            if self.way == 'GO':
                change_y = 10 #enemy move 10 block
                change_x = 0
                if self.laser == True:
                    change_fire_x = -10 #laser's enemy move 10 block
                    change_fire_y = 0
                self.shoot_time += 1
            elif self.way == 'BACK':
                change_y = -10
                change_x = 0
                if self.laser == True:
                    change_fire_x = -10
                    change_fire_y = 0 
                self.shoot_time += 2
            
        elif self.enemy_fire == 'right' :
            if self.way == 'GO':
                change_y = -10
                change_x = 0  
                if self.laser == True:
                    change_fire_x = 10
                    change_fire_y = 0                
                self.shoot_time += 2
            elif self.way == 'BACK':
                change_y = 10
                change_x = 0 
                if self.laser == True:
                    change_fire_x = 10
                    change_fire_y = 0                    
                self.shoot_time += 1
        elif self.enemy_fire == 'up' :
            if self.way == 'GO':
                change_y = 0
                change_x = 10
                if self.laser == True:
                    change_fire_x = 0
                    change_fire_y = -10
                self.shoot_time += 1
            elif self.way == 'BACK':
                change_y = 0
                change_x = -10
                if self.laser == True:
                    change_fire_x = 0
                    change_fire_y = -10
                self.shoot_time += 2
            
        elif self.enemy_fire == 'down' :
            if self.way == 'GO':
                change_y = 0
                change_x = -10 
                if self.laser == True:
                    change_fire_x = 0
                    change_fire_y = 10
                self.shoot_time += 2
            elif self.way == 'BACK':
                change_y = 0
                change_x = 10  
                if self.laser == True:
                    change_fire_x = 0
                    change_fire_y = 10
                self.shoot_time += 1
        self.rect.y += change_y
        self.rect.x += change_x 
        if self.shoot_time % 5 == 0 and self.laser == False : #time to shoot by enemy
            self.laser = True   
            self.laser_x = self.rect.x
            self.laser_y = self.rect.y
        elif self.laser_x > space.width or self.laser_x < 0 or self.laser_y > space.height or self.laser_y < 0 and self.laser == True :
            self.laser = False
        if self.laser == True:
            self.laser_x += change_fire_x
            self.laser_y += change_fire_y
            pygame.draw.circle(space.screen, (255,0,0), (self.laser_x,self.laser_y), 10, 0)
        pygame.display.update()
        
        if self.rect.y >= space.height-20 or self.rect.y <= 20 or self.rect.x >= space.width-20 or self.rect.x <= 20:
            if self.way == 'BACK':
                self.way = 'GO'
            elif self.way == 'GO':
                self.way = 'BACK' 
    def kill_hero(self, players_x, players_y):
        if (players_x < self.laser_x and self.laser_x < players_x + block_size) or (players_x < self.laser_x + 10 and self.laser_x + 10 < players_x + 50):
            if self.laser_y > players_y and self.laser_y < players_y + block_size or self.laser_y + 10 > players_y and self.laser_y + 10 < players_y + block_size:
                return True

class Friend:
    def __init__(self):
        self.x = round(random.randrange(0, width - block_size))
        self.y = round(random.randrange(0, height - block_size))    
    def char_f(self,block_size):
        return space.screen.blit(F_CRY, [self.x,self.y,block_size, block_size])
    
class Hole:
    def __init__(self):
        self.x = round(random.randrange(200, width - 200))
        self.y = round(random.randrange(200, height - 200))        
        
class Screen:
    def __init__(self, width = 1000 , height = 600):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
    def botton(self, x, y, width, height, name):
        mouse = pygame.mouse.get_pos()
        if x < mouse[0] < x+width and y < mouse[1]< y+height:
            name +='2'
            self.screen.blit(name,(x,y))
        else:
            self.screen.blit(name,(x,y))

    def how_to(self):
        how = True
        while how:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            self.screen.blit(HOW_TO, (0,0))
            self.menu_start(10, 380, start_botton, start_botton2)
            self.menu_start(300, 380, quit_botton, quit_botton2)

            self.clock.tick(15)
            pygame.display.update()        
            
    def menu_start(self, x, y, before, after,):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x+300 and y < mouse[1]<y+105:
            self.screen.blit(after,(x,y))
            if click[0] == 1 :
                if after == start_botton2:
                    self.GameLoop(1,1, LEVEL1_BG)
                elif after == howto_botton:                   
                    self.how_to()
                elif after == quit_botton2:
                    pygame.quit()
                    quit()
        else:
            self.screen.blit(before,(x,y))        
    def StartScreen(self):
        start = True
        while start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1:
                        start = False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit() 
            self.screen.blit(screen_start,(0,0))
            self.menu_start(10, 230, start_botton, start_botton2)
            self.menu_start(350, 230, howto_botton2, howto_botton)
            self.menu_start(200, 360, quit_botton, quit_botton2)

            self.clock.tick(15)
            pygame.display.update()
    def paused(self):
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if  event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_F1:
                        pause = False
            self.screen.fill((0,0,0))
            space.msg_to_screen('PAUSED',(255,255,255), 0, 'large')
            pygame.display.update()
            self.clock.tick(5)
                        
    def OverScreen(self):
        self.screen.blit(DEAD_BG, (0,0))
        pygame.display.update()
    def text_object(self, msg, color, size ='small'):
        if size == 'small':
            screen_text = smallfont.render(msg, True, color )
        elif size == 'medium':
            screen_text = medfont.render(msg, True, color )
        elif size == 'large':
            screen_text = largefont.render(msg, True, color )
        return screen_text, screen_text.get_rect()
    def msg_to_screen(self, msg, color, y_skip , size='small'):
        textSurf, textRect = self.text_object(msg, color, size)
        textRect.center = (self.width/2), ((self.height/2) + y_skip)
        self.screen.blit(textSurf, textRect)
        
    def make_score(self, score):
        text = smallfont.render('Spirits : {0}'.format(score), True, (255,255,255))
        self.screen.blit(text, [0,0])
        
    def levelup(self, level, num_of_enemy, score):
        level += 1
        num_of_enemy +=2 
        if level == 2:
            self.GameLoop(level, num_of_enemy, LEVEL2_BG , score) 
        elif level == 3:
            self.GameLoop(level, num_of_enemy, LEVEL3_BG , score) 
        elif level ==4:
            self.end_screen(1, 1, LEVEL1_BG, score)
        
        
    def end_screen(self, level, num_of_enemy, BG, score):
        self.screen.blit(END_BG, (0,0))
        self.msg_to_screen('You help {0} spirits.'.format(score), (255,255,255), -100 , size='small')
        self.msg_to_screen('press C to start new game or press Q to quit game.', (255,255,255), -200 , size='small')
        pygame.display.update()
        GameOver = True
        while GameOver == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit() 
                    if event.key == pygame.K_c:
                        self.GameLoop(level, num_of_enemy, BG)        
           
    def GameLoop(self, level, num_of_enemy, BG, score = 0):    
        
        #change x,y hero,friend
        x_change = 0 
        y_change = 0
        
        bf = 40
        FPS = 7
        your_friends = [] #list friends
        long_line = 1 # num of hero + friend
        
        players = Player() 
        
        hole = Hole()
        
        friend = Friend()
        
        direction = '' #direction hero
        
        lst_fire = [] 
        
        GameOver = False
        GameExit = False
        
        my_enemys = [] #all of enemy
        
        all_sprites_list = pygame.sprite.Group()
         
        # List of each block in the game
        lst_enemy = pygame.sprite.Group()
         
        # List of each bullet
        lst_fire = pygame.sprite.Group()   
        
        for i in range(num_of_enemy):
            type_enemy = [ENEMY_DOWN, ENEMY_UP, ENEMY_LEFT, ENEMY_RIGHT]
            # This represents a block
            enemy = Enemy(type_enemy[random.randrange(0,3)])
         
            # Set a random location for the block
            enemy.rect.x = random.randrange(0+100,self.width-100)
            enemy.rect.y = random.randrange(0+200,self.height-200)
         
            # Add the block to the list of objects
            lst_enemy.add(enemy)
            all_sprites_list.add(enemy) 
            my_enemys.append([enemy.rect.x, enemy.rect.y]) #add enemy
        
        while not GameExit:
            
            while GameOver == True:
                space.OverScreen()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            GameExit = True
                            GameOver = False
                        if event.key == pygame.K_c:
                            self.GameLoop(level, num_of_enemy, BG)            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and direction !='RIGHT':
                        x_change = -30
                        y_change = 0
                        direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and direction!='LEFT':
                        x_change = 30
                        y_change = 0
                        direction = 'RIGHT'
                    elif event.key == pygame.K_UP and direction!='DOWN':
                        y_change = -30
                        x_change = 0
                        direction = 'UP'
                    elif event.key == pygame.K_DOWN and direction!='UP':
                        y_change = 30                        
                        x_change = 0
                        direction = 'DOWN'
                    elif event.key == pygame.K_F2:
                        self.paused()
                    elif event.key == pygame.K_SPACE:
                        fire = Firing(direction)
                        fire.rect.x = players.x + 10
                        fire.rect.y = players.y + 10
                        # Add the bullet to the lists
                        #all_sprites_list.add(fire)
                        lst_fire.add(fire)
                        my_enemys = []
            lst_enemy.update()
            lst_fire.update()
            
            for bomb in lst_fire:
                block_hit_list = pygame.sprite.spritecollide(bomb, lst_enemy, True)
                #lst_firee_nemy.add(fire)
                for i in block_hit_list:
                    lst_fire.remove(bomb)
                if bomb.rect.y < 0 or bomb.rect.y > self.height or bomb.rect.x < 0 or bomb.rect.x > self.width: #delete fire when out of screen
                    lst_fire.remove(bomb)
                              
            if  players.x + block_size  > self.width or players.x + block_size < 0 or players.y + block_size> self.height + block_size or players.y + block_size< 0 :
                GameOver = True
            # kill enemy by fire
            for spot in lst_enemy:
                if (spot.rect.x < players.x and players.x < spot.rect.x + 40) or (spot.rect.x < players.x + block_size and players.x + block_size < spot.rect.x + 40):
                    if players.y > spot.rect.y and players.y < spot.rect.y + 32 or players.y + 40 > spot.rect.y and players.y + 40 < spot.rect.y + 32:
                        self.screen.blit(blood, [players.x, players.y, block_size, block_size])
                        pygame.display.flip()
                        GameOver = True
                    
            players.x += x_change
            players.y += y_change
            
            head = []
            head.append(players.x)
            head.append(players.y)
            # overlay 
            if head in your_friends and len(your_friends) != 1:
                GameOver = True
            
            your_friends.append(head)
            # delete friend (your_friends = long_line)
            if len(your_friends) > long_line:
                del your_friends[0]
            
            self.screen.blit(BG, (0,0))
            self.make_score(score) #show score
            lst_enemy.draw(self.screen) # draw enemy
            players.char_p(block_size, your_friends, direction) # draw hero
            lst_fire.draw(self.screen) #draw firing
            if len(lst_enemy) != 0:
                friend.char_f(bf) #draw friend
            
            
            for hunter in lst_enemy:
                if len(your_friends) != 1:
                    for dead in your_friends[:-1]:
                        if (hunter.rect.x < dead[0] and dead[0] < hunter.rect.x + 40) or (hunter.rect.x < dead[0] + block_size and dead[0] + block_size < hunter.rect.x + 40):
                            if dead[1] > hunter.rect.y and dead[1] < hunter.rect.y + 32 or dead[1] + 40 > hunter.rect.y and dead[1] + 40 < hunter.rect.y + 32:
                                long_line -=1
                                score -=1
                                del your_friends[0]
            
            for k in lst_enemy: #Draw Laser
                k.update()
                if k.kill_hero(players.x,players.y): #kill hero by laser's enemy
                    GameOver = True
                    break
            pygame.display.update()
            
            # help friend
            if players.x > friend.x and players.x < friend.x + bf or players.x + block_size > friend.x and players.x + block_size < friend.x + bf:
                if players.y > friend.y and players.y < friend.y + bf or players.y + block_size > friend.y and players.y + block_size < friend.y + bf: 
                    friend = Friend()
                    long_line += 1
                    score += 1 
            # next level 
            if len(lst_enemy) == 0 :
                self.screen.blit(HOLE, (hole.x, hole.y))
                pygame.display.update()
                if players.x > hole.x + 20 and players.x < hole.x + 70 or players.x + block_size > hole.x + 20 and players.x + block_size < hole.x + 70:
                    if players.y > hole.y + 20 and players.y < hole.y + 70 or players.y + block_size > hole.y + 20 and players.y + block_size < hole.y + 70:
                        self.levelup(level, num_of_enemy, score)
                
            self.clock.tick(FPS)
        pygame.quit()
        quit()            
if __name__== '__main__':
    global block_size
    global direction 
    global num_of_enemy
    block_size = 40 #size hero and friend
    width = 700 
    height = 500 
    space = Screen(width,height)
    pygame.display.update() 
    pygame.display.set_caption('Game')
    pygame.display.set_icon(ICON)    
    space.StartScreen() 