FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/pet_project

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .

RUN useradd -m dev1
RUN chown -R dev1:dev1 /app/pet_project
USER dev1

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]