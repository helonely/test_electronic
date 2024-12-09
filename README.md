##  Технологии:
python 3.12
django 5.1
DRF 3.15.2
PostgreSQL
## Установка и запуск проекта:
## Клонируйте репозиторий:
https://github.com/helonely/test_electronic.git
## Установите зависимости:
pip install -r requirements.txt
## Настройте переменные окружения в файле .env по примеру из .env.sample
## Выполните миграции:
python manage.py migrate
## Загрузите фикстуры с данными:
python manage.py loaddata имя_фикстуры.json
## Создайте суперпользователя:
python manage.py csu
## Запустите сервер разработки:
python manage.py runserver
## Приложение доступно по адресу http://127.0.0.1:8000/.
## Автор проекта: https://github.com/helonely
