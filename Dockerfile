FROM python:3.8.5

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

RUN useradd --create-home appuser
USER appuser

COPY / /home/appuser
WORKDIR /home/appuser

ENV PYTHONPATH "/home/appuser/"

CMD ["python", "-u", "./main.py"]
