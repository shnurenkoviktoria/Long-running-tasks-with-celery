# Homework_9
## How to run
1. Після завантаження всіх Python files пропишіть такі команди :

* ``python manage.py makemigrations``

* ``python manage.py migrate``

2. Виповніть  команду для встановлення необхідних пакетів:

* ``pip install -r .\requirements.txt``

3. Пропишіть в терміналі :

* ``set TWILIO_TOKEN={your token}``, де {your token}- Ваш твіліо токен 

* ``python manage.py runserver``

4. Пропишіть в іншому терміналі :

* ``celery -A homework_9  worker -l INFO``

