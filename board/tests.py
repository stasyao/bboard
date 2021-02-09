from django.test import TestCase
from django.urls import resolve, reverse

from .views import HomePageView


class HomepageTests(TestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    # Доступность страницы
    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    # Использование правильного шаблона
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    # Наличие правильного контента на странице
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Главная страница')

    # Соответствие контроллера и пути
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )
