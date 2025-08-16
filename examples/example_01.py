import pygame, sys
from pygame_animation_player import Animation, AnimationPlayer

pygame.init()

screen = pygame.display.set_mode((500,500))

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups) -> None:
        super().__init__(*groups)
        
        idle = Animation(0, pygame.image.load("assets/idle.png").convert_alpha())
        jump = Animation(0, pygame.image.load("assets/jump.png").convert_alpha())
        look_down = Animation(0, pygame.image.load("assets/look_down.png").convert_alpha())
        look_up = Animation(0, pygame.image.load("assets/look_up.png").convert_alpha())
        run = Animation(10, pygame.image.load("assets/run.png").convert_alpha(), tilesize=(8, 8), one_shot=False)

        self.image:pygame.Surface
        self.animation_player = AnimationPlayer(self, idle=idle, jump=jump, look_down=look_down, look_up=look_up, run=run)
        if self.image:
            self.rect = self.image.get_rect(center= (250,250))
        else:
            self.rect = pygame.Rect(0,0,0,0)

    def update(self, dt):
        self.animation_player.update(dt)


    def scale_by(self, scale:float):
        return pygame.transform.scale_by(self.image, scale)


clock = pygame.time.Clock()
player = Player()

while True:
    dt = clock.tick() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                player.animation_player.play("jump")
            elif event.key == pygame.K_2:
                player.animation_player.play("look_down")
            elif event.key == pygame.K_3:
                player.animation_player.play("look_up")
            elif event.key == pygame.K_4:
                player.animation_player.play("run")
            elif event.key == pygame.K_5:
                player.animation_player.play("idle")
    # logic:
    player.update(dt)


    # rendering
    screen.fill("black")
    screen.blit(player.scale_by(10), player.rect)
    pygame.display.flip()





