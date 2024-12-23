# Этап 1: Сборка зависимостей
FROM python:3.9-alpine as builder
RUN apk add --no-cache gcc musl-dev postgresql-dev
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Этап 2: Финальный образ
FROM python:3.9-alpine
RUN adduser -D flaskuser
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN chown -R flaskuser /app
USER flaskuser

CMD ["./entrypoint.sh"]
