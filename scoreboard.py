import pygame.font
from pygame.sprite import Group

from ship import Ship

class ScoreBoard:
    """Клас що виводить рахунок"""

    def __init__(self, ai_game):
        """Ініціалізація атрибутів рахунку гри"""

        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #Налаштування шрифту для відображення рахунку
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #Підготувати зображення з початковим рахунком
        self.prep_score()
        self.prep_high_score()
        self.prep_game_level()
        self.prep_ship()

    def prep_score(self):
        """Перетворити рахунок на зображення"""

        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_img = self.font.render(score_str, True,
                                          self.text_color)

        #Показати рахунок у верхньому правому куті екрана
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Згенерувати рекорд у зображенні"""

        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_img = self.font.render(high_score_str, True,
                                               self.text_color)

        #Відцентрувати рекорд по центру
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.midtop = self.screen_rect.midtop
        self.high_score_rect.top = 20

    def prep_game_level(self):
        """Перетворити рівень в зображення"""

        game_level = self.stats.game_level
        game_level_str = str(game_level)
        self.game_level_img = self.font.render(game_level_str, True,
                                               self.text_color)

        #Розмістити рівень під рахунком
        self.game_level_rect = self.game_level_img.get_rect()
        self.game_level_rect.right = self.screen_rect.right - 20
        self.game_level_rect.top = self.score_rect.bottom + 20

    def prep_ship(self):
        """Показує скільки лишилося кораблів"""

        self.ships = Group()
        image = pygame.image.load("images/new_ship.png")
        image = pygame.transform.scale(image, (50, 50))
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_game)
            ship.image = image
            ship.rect.x = 10 + (10 * ship_number) + ship_number * ship.rect.width
            ship.rect.y = 5
            self.ships.add(ship)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Показати рахунок на екрані"""

        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.game_level_img, self.game_level_rect)
        self.ships.draw(self.screen)