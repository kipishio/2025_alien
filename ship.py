import pygame


class Ship:
    """Класс для управления кораблем."""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        # Сохраняет экран игры в атрибут self.screen.
        # Кораблю нужен доступ к экрану, чтобы на нём рисовать (в методе
        # blitme()). Без этой строки корабль не сможет отображаться,
        # так как не будет знать, где рисовать.
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # загружаем размер экрана
        self.screen_rect = ai_game.screen.get_rect()
        # Загружает изображение корабля
        self.image = pygame.image.load('images/ship.bmp')
        # Получает прямоугольник изображения корабля (pygame.Rect) и
        # сохраняет его в self.rect. Этот прямоугольник содержит
        # координаты и размеры картинки (например, ширина и высота
        # ship.bmp).
        self.rect = self.image.get_rect()
        # Устанавливает начальную позицию корабля, выравнивая его
        # середину нижней части (midbottom) по середине нижней части экрана
        self.rect.midbottom = self.screen_rect.midbottom
        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)
        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        # Обновляется атрибут x, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Обновление атрибута rect на основании self.x.
        self.rect.x = int(self.x)

    def blitme(self):
        """Рисует корабль в текущей позиции."""

        # устанавливаем картинку в позицию как у прямоугольника rect
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
