FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update
RUN apt-get install -y binutils libproj-dev gdal-bin

COPY . /app/

RUN chmod +x entrypoint.sh

EXPOSE 1111

CMD ["python", "manage.py", "runserver", "0.0.0.0:1111"]
