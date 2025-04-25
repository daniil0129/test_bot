FROM python:3.9-slim

# Установка системных зависимостей (Nginx, Certbot)
RUN apt-get update && apt-get install -y \
    nginx \
    certbot \
    python3-certbot-nginx \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы
COPY . .

# Копируем конфиг Nginx
COPY nginx/nginx.conf /etc/nginx/nginx.conf

# Получаем SSL-сертификат (замените на свои данные)
RUN certbot certonly --nginx --non-interactive --agree-tos \
    -d example.com \
    -m your@email.com \
    --no-eff-email

# Скрипт запуска
COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 80 443
CMD ["/start.sh"]