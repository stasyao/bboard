from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomSignupForm


class SignUp(CreateView):
    """Регистрация с активацией аккаунта через email"""
    form_class = CustomSignupForm
    success_url = reverse_lazy('users:confirmation_page')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        self.object = form.save()
        email = EmailMessage(
            subject='Перейдите по ссылке для окончания регистрации на сайте',
            body=self.request.build_absolute_uri(self.object.uuid),
            to=[self.object.email],
        )
        email.send(fail_silently=True)
        return super().form_valid(form)


def email_confirm(request, uuid):
    new_user = get_object_or_404(get_user_model(), uuid=uuid)
    new_user.is_active = True
    new_user.save()
    messages.success(request, 'Регистрация завершена! Теперь можно войти :)')
    return redirect('users:login')


class CustomLoginView(auth_views.LoginView):
    """Авторизация по email и паролю
    с дополнительной рекапчей после 3-го фэйла"""
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        # проверяем, отмечена ли рекапча
        marked_recaptcha = request.POST.get('g-recaptcha-response')
        if form.is_valid():
            # если рекапча отмечена
            # или ее нет (не было 3 неудачных попыток ввода логина/пароля)
            if marked_recaptcha or not request.session.get('exceeding_limit'):
                # данные из формы сохраняются в базу
                return self.form_valid(form)
        # если данные в форме неверны или не отмечена рекапча
        # форма считается невалидной
        return self.form_invalid(form)

    def form_invalid(self, form):
        # добавляем логику появления рекапчи после 3 фэйлов с логином/паролем
        # берем SessionStore object текущего запроса
        session = self.request.session
        if not session.get('failed_attempt'):
            # включаем в сессию счётчик неудачных попыток входа
            session['failed_attempt'] = 0
            # срок жизни сессии - пока у юзера не закрыт браузер
            session.set_expiry(0)
        # включаем в сессию показатель достижения лимита фэйлов
        session['exceeding_limit'] = False
        # счётчик считает фэйлы
        session['failed_attempt'] += 1
        # если фэйлов сверх лимита его показатель становится True
        if session['failed_attempt'] > 3:
            session['exceeding_limit'] = True
        # показатель достижения лимита передается логин-шаблону
        # если показатель True форма дополнится рекапчей
        return self.render_to_response(
            self.get_context_data(
                form=form,
                exceeding_limit=session['exceeding_limit'],
            )
        )


class CustomPasswordResetView(auth_views.PasswordResetView):
    """Восстановление забытого пароля через ссылку на email"""
    success_url = reverse_lazy('users:password_reset_done')


class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy('users:password_reset_complete')
