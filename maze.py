#создай игру "Лабиринт"!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def Reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_width, wall_height, wall_x, wall_y):
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def Draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def Update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > -5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 550:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > -6:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 750:
            self.rect.x += self.speed

class Enemy(GameSprite):
    directon = "left"
    def Update(self):
        if self.rect.y <= 400:
            self.directon = "right"

window = display.set_mode((800, 600))
display.set_caption("Лабиринт")
backgroung = transform.scale(image.load("background.jpg"), (800, 600))

hero = Player("hero.png", 50, 500, 5)
enemy = Enemy("cyborg.png", 400, 180, 0)
money = GameSprite("treasure.png", 420, 500, 0)
w1 = Wall(123, 234, 12, 440, 15, 120, 120)
w2 = Wall(123, 234, 12, 15, 484, 345, 123)
w3 = Wall(123, 234, 12, 342, 15, 500, 280)
w4 = Wall(123, 234, 12, 230, 15, 1, 334)
w5 = Wall(123, 234, 12, 353, 15, 350, 443)

mixer.init()
font.init()

mixer.music.load("jungles.ogg")
mixer.music.play()
lose_sound = mixer.Sound("kick.ogg")
win_sound = mixer.Sound("money.ogg")

font = font.SysFont("Arial", 70)
win = font.render("YOU WIN!", True, (255, 215, 0))
lose = font.render("YOU LOSE!", True, (180, 0, 0))

clock = time.Clock()
FPS = 60

finish = False
game = True
while game:

    hero.Reset()
    hero.Update()

    enemy.Reset()
    enemy.Update()

    money.Reset()

    w1.Reset()
    w2.Reset()
    w3.Reset()
    w4.Reset()
    w5.Reset()

    window.blit(backgroung, (0, 0))
    clock.tick(FPS)

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:

        if sprite.collide_rect(hero, enemy) or sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, w2) or sprite.collide_rect(hero, w3) or sprite.collide_rect(hero, w4) or sprite.collide_rect(hero, w5):
            window.blit(lose, (400, 300))
            lose_sound.play()
            finish = True

        if sprite.collide_rect(hero, money):
            window.blit(win, (400, 300))
            win_sound.play()
            finish = True

    display.update()
