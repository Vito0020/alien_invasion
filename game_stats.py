class GameStats:
    """Відстеження статистики гри"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        #Рекорд не анульовується
        self.high_score = 0

        #Розпочати гру в неактивному стані
        self.game_active = False

    def reset_stats(self):
        """Ініціалізація статистики що може змінюватися впродовж гри"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.game_level = 1