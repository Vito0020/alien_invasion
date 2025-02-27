import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats

class AlienInvasion:
    """Загальний клас програми що керує ресурсами та поведінкою гри"""

    def __init__(self):
        """Ініціалізувати гру, створити ресурси гри"""

        pygame.init()
        self.settings = Settings()

        """
        #Повноекранний режим гри
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        """

        #Віконний режим гри
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #Задати колір фону
        self.bg_image = pygame.image.load("images/space.bmp")

        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Запуск головного циклу гри"""

        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._update_screen()

    def _check_events(self):
        # Відстеження руху клавіатури та мишки
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        """Відслідковувати натиснуті клавіші"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_event(self, event):
        """Відслідковувати відтиснуті клавіші"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Створити нову кулю та додати до групи"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Створити флот прибульців"""
        #Створити прибульців та визначити кількість прибульців у ряду
        #Відстань між прибульцями буде дорівнювати одному прибульцю
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_of_aliens_x = available_space_x // (2 * alien_width)

        #Визначити яка кількість рядів прибульців поміщається на екрані
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_of_rows = available_space_y // (2 * alien_height)

        #Створити весь флот прибульців
        for row_number in range(number_of_rows):
            for aline_number in range(number_of_aliens_x):
                self._create_alien(aline_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Створити прибульця та поставити його в ряд"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Реагує чи досяг якийсь з прибульців краю екрану"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Спуск всього флоту та зміна напрямку"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_bullets(self):
        """Оновлення пуль як були випущені та зниклі"""
        #Оновлення позиції куль
        self.bullets.update()

        #Видалення пуль які зникли
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """Взаємодія кулі та прибульця"""
        #Якщо влучила видалити і кулю і прибульця
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        #Якщо всі прибульці збиті, видалити всі полі та створити новий флот
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Перевірити чи флот знаходиться на краю, тоді
        оновити позицію всіх прибульців у флоті"""
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _ship_hit(self):
        """Реагувати на зіткнення прибульця з кораблем"""
        if self.stats.ship_left > 0:
            #Відняти одне життя
            self.stats.ship_left -= 1

            #Позбутися лишніх елементів на екрані
            self.aliens.empty()
            self.bullets.empty()

            #Створити новий флот та поставити корабель по центру
            self._create_fleet()
            self.ship.center_ship()

            #Пауза
            sleep(1.0)
        else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        """Перевіряє чи не досягли прибульці до низу екрану"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_screen(self):
        #Наново перемалювати екран
        #self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.bg_image, (0,0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #Показати останній намальований екран
        pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()