FROM python:3.8-slim-buster

# Install app
COPY . /app
WORKDIR /app

# Install dependencies
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Run Battlesnake
CMD [ "python", "app.py" ]
