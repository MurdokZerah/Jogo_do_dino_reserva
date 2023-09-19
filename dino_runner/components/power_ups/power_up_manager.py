import random
import pygame
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.shield_active = False
        self.primal_rage_active = False  # Variável para rastrear o estado do Primal Rage

    def generate_power_up(self, score):
        if not self.power_ups and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            # Escolha aleatoriamente entre o "Shield", o "Hammer" e o "Primal Rage"
            choice = random.choice(["Shield", "Hammer", "Primal Rage"])
            if choice == "Shield":
                self.power_ups.append(Shield())
            elif choice == "Hammer":
                self.power_ups.append(Hammer())
            elif choice == "Primal Rage":
                self.power_ups.append(PrimalRage())

    def update(self, game):
        self.generate_power_up(game.score)
        
        if self.power_ups:
            power_up = self.power_ups[0]
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.type = power_up.type
                game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)

        if game.player.has_power_up and game.player.type == "Shield":
            self.shield_active = True
            game.player.can_pass_obstacles = True
        else:
            self.shield_active = False
            game.player.can_pass_obstacles = False

        if game.player.has_power_up and game.player.type == "Primal Rage":
            self.primal_rage_active = True
            # Aqui você pode adicionar a lógica para ativar o "Primal Rage" quando a tecla "J" for pressionada.
            keys = pygame.key.get_pressed()
            if keys[pygame.K_j]:
                # Ative o Primal Rage
                game.player.primal_rage_start_time = pygame.time.get_ticks()
                game.player.primal_rage_active = True
                game.player.can_break_obstacles = True
        else:
            self.primal_rage_active = False
            game.player.primal_rage_active = False

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.when_appears = random.randint(50, 80)