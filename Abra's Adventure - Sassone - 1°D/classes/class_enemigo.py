import pygame
from configuraciones import obtener_rectangulos
from classes.class_personaje import Personaje
import random
from modo import get_modo

class Enemigo(Personaje):
    def __init__(self, x, y, hp, animaciones, width, height, piso_der, velocidad, pantalla):
        self.hp = hp
        self.width = width
        self.height = height
        self.animaciones = animaciones
        self.x = x
        self.pantalla = pantalla
        self.reescalar_animaciones()
        self.contador_pasos = 0
        self.rectangulo = self.animaciones["rocket_fem_camina"][0].get_rect()
        self.rectangulo.x = x
        self.rectangulo.bottom = y
        self.piso_der =  piso_der
        self.lados = obtener_rectangulos(self.rectangulo)
        self.velocidad = velocidad
        self.flag_orientacion = "derecha"
        self.hp = hp
        self.flag_dmg = False
        self.genero = random.randint(0, 1)

    def spawnear_enemigo(self, target):
        if self.rectangulo.x + self.width >= self.piso_der:
            self.flag_orientacion = "izquierda"
        if self.rectangulo.x <= self.x:
            self.flag_orientacion = "derecha"
        if self.flag_orientacion == "derecha":
            self.mover(self.velocidad)
            if self.genero == 1:
                self.animar("rocket_masc_camina")
            elif self.genero == 0:
                self.animar("rocket_fem_camina")
        else:
            self.mover((self.velocidad)*-1)
            if self.genero == 1:
                self.animar("rocket_masc_camina_der")
            elif self.genero == 0:
                self.animar("rocket_fem_camina_der")
        self.realizar_dmg(target)
        if get_modo():
            pygame.draw.rect(self.pantalla, "red", self.rectangulo, 2)
    

    def restar_hp(self):
        if self.hp > -1:
            self.hp -= 1
            self.animar("rocket_fem_hit_izq")
        return True
    
    def realizar_dmg(self, target):
        if self.rectangulo.colliderect(target.rectangulo):
            if target.hp > 0:
                if self.flag == False:
                    target.hp -= 1
                    self.flag = True
        else:
            self.flag = False