FROM python:3.8

WORKDIR /app
COPY /app/requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
