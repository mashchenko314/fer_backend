# Backend-часть системы анализа рекламных кампаний с помощью распознавания эмоций человека

## 📋 Требования

- Python 3.8+
- Django 3.2+
- База данных (PostgreSQL)

## ⚙️ Установка и настройка

### 1. Клонирование репозитория

```bash
git https://github.com/mashchenko314/fer_backend
cd fer_backend
```
### 2. Создание виртуального окружения

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# или
venv\Scripts\activate     # Windows
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка переменных окружения

Создайте файл local_settings.py в директории /ademotions/application и заполните необходимые переменные:
```bash
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.postgresql_psycopg2',
 'NAME': '',
 'USER': '',
 'PASSWORD': '',
 'HOST': '127.0.0.1',
 'PORT': '5432',
 }
}

SECRET_KEY = ''

DROPBOX_OAUTH2_TOKEN=''
```

### 5. Применение миграций
```bash
python manage.py migrate
```

### 6. Создание суперпользователя
```bash
python manage.py createsuperuser
```

### 7. Запуск сервера разработки
```bash
python manage.py runserver
```

Приложение будет доступно по адресу: http://127.0.0.1:8000