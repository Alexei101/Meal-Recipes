# Используем базовый образ с Python 3.9
FROM python:3.9-slim

# Устанавливаем зависимости, необходимые для Tkinter
RUN apt-get update && apt-get install -y \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем все файлы в рабочую директорию контейнера
COPY . .

# Устанавливаем зависимости, указанные в requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Запускаем приложение
CMD ["python", "your_script_name.py"]
