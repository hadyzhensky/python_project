# SQL Trainer (Django Project)

Учебный проект для тренировки SQL-запросов с готовыми заданиями и на тему истории.

---

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone <URL_репозитория>
cd <название_проекта>
```

---

### 2. Создать виртуальное окружение

```bash
python -m venv venv
```

Активировать:

**Windows (cmd):**

```bash
venv\Scripts\activate
```

**Windows (PowerShell):**

```bash
venv\Scripts\Activate.ps1
```

---

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

---

### 4. Применить миграции

```bash
python manage.py migrate
```

---

### 5. Загрузить начальные данные

```bash
python manage.py loaddata initial_data
```

### 6. Запустить сервер

```bash
python manage.py runserver
```

Открыть в браузере:

```
http://127.0.0.1:8000/
```