import pygame, random, sys, time, button
from pygame.locals import *
from datetime import datetime



print("BIENVENIDO, DISPONES DE 3 VIDAS")
BLACK = (0,0,0)
WHITE= (255,255,255)
RED = (255,0,0)
#Creamos las clases necesarias(Meteoritos y Nave)

class Meteorito(pygame.sprite.Sprite):


	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("imagenes/meteorito.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()#Guardar posición
        

	def update(self,choque):
		if choque==True:
			self.kill()	  
		self.rect.y +=1        
		if self.rect.y > 600 :
			self.rect.y = -5
			self.rect.x = random.randrange(1000)
    

		   


class Nave(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("imagenes/playerN.png").convert()
		self.imageC = pygame.image.load("imagenes/corazon.png").convert()
		self.imageC.set_colorkey(BLACK)
		#self.rectC = self.image.get_rect()        
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
    

 
pygame.init()

size = (1000, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock() #Tener control de los frames
background = pygame.image.load("imagenes/backgala.webp").convert()
background_menuInicio = pygame.image.load("imagenes/galaxy.webp").convert()
play_img= pygame.image.load("imagenes/play.webp").convert_alpha()
width = play_img.get_rect().width
height = play_img.get_rect().height
play_img = pygame.transform.scale(play_img, (width-500, height-100))


#bo
#screen.blit(play_img,(300,500) )

fin_juego=False
VIDA=3


#Coordenadas de la nave al inicio
coord_x = 500
coord_y = 500
#Velocidad teclado
x_speed = 0
y_speed = 0

ListaMeteoritos = pygame.sprite.Group()
TodosSprite = pygame.sprite.Group()

#Creamos todos los meteoritos

def crear_meteoritos(aviso):
    if aviso == True:
        meteorito=Meteorito()
        meteorito.rect.x = random.randrange(1000)
        meteorito.rect.y = random.randrange(100)
        ListaMeteoritos.add(meteorito)
        TodosSprite.add(meteorito)
    else:
       # ListaMeteoritos= []
        time.sleep(0.5)
        for i in range(5):
            
            meteorito = Meteorito()
            meteorito.rect.x = random.randrange(1000)
            meteorito.rect.y = random.randrange(100)
            ListaMeteoritos.add(meteorito)
            TodosSprite.add(meteorito)
    

nave = Nave()
TodosSprite.add(nave)


#Control de las distinas pantallas
juego_en_pausa = False
estado_menu = "menuInicial"



fuente=pygame.font.SysFont("arialblack",100)
fuente2=pygame.font.SysFont("arialblack",50)




def movimiento_teclado(event,x_speed,y_speed):

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_a:
            x_speed = -3
        if event.key == pygame.K_d:
            x_speed = 3
        if event.key == pygame.K_w:
            y_speed = -3
        if event.key == pygame.K_s:
            y_speed = 3
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            x_speed = 0
        if event.key == pygame.K_d:
            x_speed = 0
        if event.key == pygame.K_w:
            y_speed = 0
        if event.key == pygame.K_s:
            y_speed = 0
    

    return [x_speed,y_speed]

def click_en_play(coord):
    rdo= True
    return rdo



Choque=False
tiempoSinChoque=0
avisoTiempoSinChoque=False
crear_meteoritos(avisoTiempoSinChoque)


#load button images
start_img = pygame.image.load('imagenes/play.webp').convert_alpha()
controles_img = pygame.image.load('imagenes/ajustes.webp').convert_alpha()
return_img = pygame.image.load('imagenes/return.webp').convert_alpha()
exit_img = pygame.image.load('imagenes/x.webp').convert_alpha()
tick_img = pygame.image.load('imagenes/tick.webp').convert_alpha()


#create button instances
start_button = button.Button(480, 200, start_img, 0.05)
ajustes_button = button.Button(475, 275, controles_img, 0.05)
return_button = button.Button(930, 526, return_img, 0.05)
exit_button = button.Button(475, 526, exit_img, 0.05)
tick_button = button.Button(600, 526, tick_img, 0.05)


##CORAZONES


corazones_añadidos=False

game_mode= "menuInicio"
click=False

#Sitema de puntuacion
puntos=0
fuentec=pygame.font.match_font("consolas")
def texto_pantalla(pantalla, fuente, texto, color, dimensiones):
    font= pygame.font.Font(fuente, dimensiones)
    superficie= font.render(texto, True, color)
    rectangulo= superficie.get_rect()
    #rectangulo.center(cords)
    pantalla.blit(superficie, rectangulo)
    


#### COSAS NECESARIAS TEXTBOX
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()
input_box = pygame.Rect(425, 150, 140, 32)
color_inactive = pygame.Color(BLACK)
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
done = False

while not fin_juego:
    if game_mode== "controles":
        screen.blit(background_menuInicio, [0, 0])
        screen.blit(fuente.render("CONTROLES ", True,WHITE ), (300, 50))
        screen.blit(fuente2.render("Desplazamiento Derecha: d", True,WHITE ), (5, 130))
        screen.blit(fuente2.render("Desplazamiento Izquierda: a ", True,WHITE ), (5, 200))
        screen.blit(fuente2.render("Desplazamiento Frontal: w ", True,WHITE ), (5, 270))
        screen.blit(fuente2.render("Desplazamiento Trasero: s ", True,WHITE ), (5, 330))
        screen.blit(fuente2.render("Menu de Pausa: p ", True,WHITE ), (5, 400))


        if return_button.draw(screen):
            game_mode="menuInicio"

        for evento in pygame.event.get():
            if evento.type== pygame.QUIT:
                sys.exit()
        pygame.display.update()


    if game_mode == "menuInicio":


        screen.blit(background_menuInicio, [0, 0])
        screen.blit(fuente.render("CHOQUE ESPACIAL", True,WHITE ), (150, 50))
        screen.blit(fuente2.render("Nombre: ", True,BLACK ), (275, 150))
        if start_button.draw(screen):
            game_mode="jugando"
        if ajustes_button.draw(screen):
            game_mode="controles"
        for evento in pygame.event.get():
            if evento.type== pygame.QUIT:
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(evento.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if evento.type == pygame.KEYDOWN:
                if active:
                    if evento.key == pygame.K_RETURN:
                        #print(text)
                        text = ''
                        pass
                    elif evento.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                        pass
                    else:
                        text += evento.unicode
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)


        pygame.display.update()


    elif game_mode == "partida_pausada": 
        reactivar = False
        while reactivar == False:
            screen.blit(fuente.render("JUEGO EN PAUSA", True,WHITE ), (160, 250))
            pygame.display.flip()
            for evento in pygame.event.get():
                if evento.type== pygame.QUIT:
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_p:
                        game_mode = "jugando"
                        reactivar=True
                        pygame.display.flip()
                        
    elif game_mode == "jugando":
        

        if tiempoSinChoque == 1000:#subir de dificultad periodicamente
            screen.blit(fuente.render("Puntuacion", True,WHITE ), (275, 50))
            puntos+=1
            avisoTiempoSinChoque=True
            crear_meteoritos(avisoTiempoSinChoque)
            tiempoSinChoque=0
            avisoTiempoSinChoque=False

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
            elif evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_p:
                    
                    game_mode = "partida_pausada"

            x_speed=movimiento_teclado(evento,x_speed,y_speed)[0]
            y_speed=movimiento_teclado(evento,x_speed,y_speed)[1]
            
        screen.blit(background, [0, 0])#añadir imagen
        if VIDA==3:
            screen.blit(pygame.transform.scale(nave.imageC,(25,25)),(510,15))
            screen.blit(pygame.transform.scale(nave.imageC,(25,25)),(550,15))
            screen.blit(pygame.transform.scale(nave.imageC,(25,25)),(470,15))
        elif VIDA==2:
            screen.blit(pygame.transform.scale(nave.imageC,(25,25)),(510,15))            
            screen.blit(pygame.transform.scale(nave.imageC,(25,25)),(550,15))
        elif VIDA==1:           
            screen.blit(pygame.transform.scale(nave.imageC,(25,25)),(550,15))
            
        TodosSprite.update(Choque) 
        coord_x += x_speed
        coord_y += y_speed
        nave.rect.x = coord_x
        nave.rect.y = coord_y
        numcolisiones=pygame.sprite.spritecollide(nave, ListaMeteoritos, True)
        for colisiones in numcolisiones:
            VIDA -=1 
            Choque =True
            avisoTiempoSinChoque=False
            TodosSprite.update(Choque)
            crear_meteoritos(avisoTiempoSinChoque)
            coord_x = 500
            coord_y = 500
            time.sleep(0.10)#Nose si añadirlo
            
            #print("LE QUEDAN " + str(VIDA)+" VIDAS")    
            if VIDA == 0:
                #puntuacion= tiempoIni-tiempoFin
                #print(tiempoFin)
                ranking=[]
                game_mode="menu_fin"
                #fin_juego=True
        Choque=False
        TodosSprite.draw(screen)

        ###DELIMITAMOS BORDES###
        if coord_x > 904 :#limites del cubo con los bordes laterales
            coord_x=904
        elif coord_x <= 0:
            coord_x=0           
        if coord_y > 526 :#limites del cubo con los bordes laterales
            coord_y=526
        elif coord_y <= 0:
            coord_y=0        
        ###DELIMITAMOS BORDES### 
        texto_pantalla(screen, fuentec, str(puntos),RED,40)  
        pygame.display.flip()
        tiempoSinChoque+=1
        #print(tiempoSinChoque)
        

        clock.tick(170) #Frames por segundo  
    elif game_mode == "menu_fin":
        ranking.append(str(text)+ " ha conseguido " + str(puntos))
        screen.blit(background_menuInicio, [0, 0])
        screen.blit(fuente.render("GAME OVER", True,WHITE ), (275, 50))


        screen.blit(fuente.render("¿JUGAR OTRA VEZ?", True,WHITE ), (275, 400))
        if exit_button.draw(screen):
            sys.exit()
        if tick_button.draw(screen):
            VIDA=3
            coord_x = 500
            coord_y = 500
            x_speed=0
            y_speed=0
            puntos=0
            game_mode="jugando"
        for evento in pygame.event.get():
            if evento.type== pygame.QUIT:
                sys.exit()

       # pygame.display.update()


    pygame.display.update()




#MEJORAS NECESARIAS

#INCREMENTAR EL NIVEL EN FUNCION DEL TIEMPO

#NUEVA FUNCIONALIDAD MENU FINAL

 #AÑADIR PARA PONER USUARIO
 #RANKING --BBDD?
 #MENUS