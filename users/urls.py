from django.urls import include, path
from django.views.generic import TemplateView

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/',
         views.SignUp.as_view(),
         name='signup'),  # регистрация новых пользователей
    path('signup/confirm_your_email/',
         TemplateView.as_view(template_name='registration/confirm_page.html'),
         name='confirmation_page'),  # сообщение о ссылке-подтверждении
    path('signup/<uuid:uuid>/',
         views.email_confirm,
         name='email_confirm'),  # переход по ссылке-подтверждению
    path('login/',
         views.CustomLoginView.as_view(),
         name='login'),  # вход зарегистрированных активых пользователей
    path('password_reset/',
         views.CustomPasswordResetView.as_view(),
         name='password_reset'),  # запрос на восстановление пароля
    path('reset/<uidb64>/<token>/',
         views.CustomPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),  # подтверждение восстановления пароля
    path('', include('django.contrib.auth.urls')),
]
