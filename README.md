# bboard
проект доски объявлений на Django

#### Инструкция по деплою приложения на вашей машине

1. Убедитесь, что запущен Docker.
2. Клонируйте в любое удобное место этот репозиторий:

`git clone https://github.com/stasyao/bboard`

3. Перейдите через CLI в папку с клонированным репозиторием и выполните следующие команды:
- `docker-compose up -d --build` &ndash; собрать приложение и сделать его первоначальный запуск
- `docker-compose down` &ndash; остановить работу приложения
- `docker-compose run web python manage.py migrate` &ndash; сделать необходимые миграции
- `docker-compose up` &ndash; окончательно запустить приложение.
