# django-lab1-opt7
Django| The first laboratory. News. 7-th option

Реалізувати веб-сайт з наступними сторінками: адміністративна сторінка для додавання / видалення / коригування повідомлень на сайті; призначена для користувача сторінка для пошуку на сайті повідомлень за ключовими словами.

# Start Instruction in russian:
После копирования проекта, создай python виртуальное окружение. Активируй его, и в корне проекта выполни команду pip install -r requirements.txt. Так же, по заданию нужно было делать все на mysql, создай у себя локально бд с названием "django_lab1_opt7" , логином "root" и паролем "root". (Если что, можешь назвать как угодно и потом заменить в файле Lab1_eng/Lab1_eng/settings.py под свои данные). Далее в корне проекта выполни команду './manage.py makemigrations Lab1'  и после нее './manage.py migrate'. После - './manage.py createsuperuser'. Вводи какие хочешь данные. Они тебе будут нужны для перехода на администрирование сайта по адресу 'localhost:8000/admin.py'

# [ Если появились проблемы с установкой и подключением данной лабораторной работы к mysql]
Перейди в Lab1_engine/Lab1_engine/settings. Найти вот такие строчки: #' DATABASES = { #' 'default': { #' 'ENGINE': 'django.db.backends.sqlite3', #' 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), #' } #' } DATABASES = { 'default': { 'ENGINE': 'django.db.backends.mysql', 'NAME': 'django_lab1_var7', 'USER': 'root', 'PASSWORD': 'root', } } Выдели их и вставь вместо них это: DATABASES = { 'default': { 'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), } } #' DATABASES = { #' 'default': { #' 'ENGINE': 'django.db.backends.mysql', #' 'NAME': 'django_lab1_var7', #' 'USER': 'root', #' 'PASSWORD': 'root', #' } #' } Выполни команду из инструкции по установке " manage.py makemigrations Lab1Files " и следуй дальнейшим инструкциям из установки. Это создаст Sqlite базу данных. Это, конечно, не подходит по заданию лабораторной работы, но может тебе повезет и этого не обнаружат :)
# P.S. Так же, в папке Screens лежат скрины для отчета
