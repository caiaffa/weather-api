FROM python:3.7

WORKDIR /app/

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENV C_FORCE_ROOT=1

COPY . /app

ENV PYTHONPATH=/app

RUN chmod +x /app/start.sh

CMD ["bash", "/app/start.sh"]