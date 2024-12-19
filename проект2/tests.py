import pygame
import unittest
from unittest import mock
from main import Button
from unittest.mock import patch


class TestButton(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))

    def tearDown(self):
        pygame.quit()

    # Тестирование конструктора __init__
    def test_button_initialization(self):
        # Положительный тест 1
        self.image = pygame.Surface((100, 50))  # Создаем временное изображение для кнопки
        self.button = Button(100, 100, self.image, 1)
        self.assertEqual(self.button.rect.topleft, (100, 100))  # Проверка позиции кнопки
        self.assertFalse(self.button.clicked)
        self.assertEqual(self.button.image.get_size(), (100, 50))  # Проверка размера кнопки

    @patch("pygame.mouse.get_pos")
    @patch("pygame.mouse.get_pressed")
    def test_draw_button_clicked(self, mock_get_pressed, mock_get_pos):
        image = pygame.Surface((100, 50))
        image.fill((255, 0, 0))
        button = Button(50, 50, image, 1)

        mock_get_pos.return_value = (75, 75)
        mock_get_pressed.return_value = (1, 0, 0)

        surface = pygame.Surface((200, 200))

        action = button.draw(surface)

        self.assertTrue(action)

    @patch("pygame.mouse.get_pos")
    @patch("pygame.mouse.get_pressed")
    def test_draw_button_not_clicked(self, mock_get_pressed, mock_get_pos):
        image = pygame.Surface((100, 50))
        image.fill((0, 255, 0))
        button = Button(50, 50, image, 1)

        mock_get_pos.return_value = (75, 75)
        mock_get_pressed.return_value = (0, 0, 0)

        surface = pygame.Surface((200, 200))

        action = button.draw(surface)

        self.assertFalse(action)


if __name__ == '__main__':
    unittest.main()
