FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY config/requirements.txt config/
RUN pip install --no-cache-dir -r config/requirements.txt

COPY config config
COPY src src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--reload"]