FROM python:3

RUN pip install --upgrade pip
RUN apt-get install tar -y

RUN mkdir /script
WORKDIR /script

COPY docker/backup_daemon/backup.py /script/backup.py

CMD ["python", "backup.py"]