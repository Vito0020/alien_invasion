
class Settings:
    """Клас для збереження всіх налаштувань гри"""

    def __init__(self):
        """Ініціалізувати постійні налаштування гри"""

        #Налаштування екрану
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Налаштування корабля
        self.ship_limit = 3
        
        #Налаштування кулі
        self.bullet_width = 3
        self.bullet_heigth = 15
        self.bullet_color = (175, 238, 238)
        self.bullets_allowed = 3

        #Налаштування прибульця
        self.fleet_drop_speed = 10

        #Як швидко гра має прискорюватися
        self.speedup_scale = 1.1

        #Як швидко збільшується вартість прибульців
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Ініціалізувати динамічні налаштування гри"""

        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        #1 -- рух праворуч, -1 -- рух ліворуч
        self.fleet_direction = 1

        #Вартість одного приульця
        self.alien_points = 50

    def increase_speed(self):
        """Збільшення налаштувань швидкості та вартості прибульця"""

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
