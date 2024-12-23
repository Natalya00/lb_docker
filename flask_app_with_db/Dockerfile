FROM python:3.9-alpine

RUN adduser -D flaskuser
RUN apk add --no-cache gcc musl-dev postgresql-dev
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chown -R flaskuser /app
USER flaskuser

CMD ["python", "app.py"]

