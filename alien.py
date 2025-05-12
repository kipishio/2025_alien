import pygame


class Alien:
    """Класс для управления кораблем."""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        # Сохраняет экран игры в атрибут self.screen.
        self.screen = ai_game.screen
        # загружаем размер экрана
        self.screen_rect = ai_game.screen.get_rect()
        # Загружает изображение корабля
        self.image = pygame.image.load('images/alien.bmp')
        # Получает прямоугольник изображения корабля и
        # содержит координаты и размеры картинки
        self.rect = self.image.get_rect()
        # Устанавливает начальную позицию корабля, выравнивая его
        # верх середина (midtop)
        self.rect.midtop = self.screen_rect.midtop

    def blitme(self):
        """Рисует корабль в текущей позиции."""

        self.screen.blit(self.image, self.rect)
