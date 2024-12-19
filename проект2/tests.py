import pygame
import unittest
from unittest import mock
from main import Button
from unittest.mock import patch


class TestButton(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.image = pygame.Surface((100, 50))  # Создаем временное изображение для кнопки
        self.button = Button(100, 100, self.image, 1)

    def tearDown(self):
        pygame.quit()

    # Тестирование конструктора __init__
    def test_button_initialization(self):
        # Положительный тест 1
        self.assertEqual(self.button.rect.topleft, (100, 100))  # Проверка позиции кнопки
        self.assertFalse(self.button.clicked)

        # Положительный тест 2
        self.assertEqual(self.button.image.get_size(), (100, 50))  # Проверка размера кнопки

    # Тестирование метода draw
    def test_button_draw(self):
        # Положительный тест 1
        with mock.patch('pygame.mouse.get_pos', return_value=(150, 120)), \
                mock.patch('pygame.mouse.get_pressed', return_value=(1, 0, 0)), \
                mock.patch('pygame.display.update') as mock_update:
            result = self.button.draw(self.screen)
            self.assertTrue(result)
            self.assertTrue(self.button.clicked)  # Проверяем, что кнопка теперь считается нажатой

        # Положительный тест 2
        with mock.patch('pygame.mouse.get_pos', return_value=(150, 120)), \
                mock.patch('pygame.mouse.get_pressed', return_value=(0, 0, 0)):
            result = self.button.draw(self.screen)
            self.assertFalse(result)  # Проверяем, что кнопка не была нажата

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