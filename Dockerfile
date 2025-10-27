FROM python:3.11-slim

# Устанавливаем рабочую директорию на /app
WORKDIR /app

# Копируем требования
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем содержимое папки app в /app/app внутри контейнера
COPY ./app ./app

# Открываем порт
EXPOSE 8000

# Запускаем uvicorn, указывая модуль с приложением - app/server.py, экземпляр FastAPI должен быть `app`
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]
