FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3", "tg-bot.py" ]