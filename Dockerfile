FROM python:3.9.7-slim-buster
WORKDIR /usr/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt update && apt upgrade -y && apt install wkhtmltopdf -y
COPY . .
# CMD [ "python3", "server.py"]
# CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "wsgi:app"]