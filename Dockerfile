FROM python:3.8.5

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

WORKDIR /app
ADD /bot/. /app

RUN useradd appuser && chown -R appuser /app
USER appuser

CMD ["python", "-u", "./main.py"]
