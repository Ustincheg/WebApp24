FROM python:3.12
WORKDIR /app
RUN apt-get update -y
RUN apt-get upgrade -y
COPY ./requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPE ./src ./src
CMD gunicorn -w 3 --chdir ./src online_streaming.wsgi --bind 0.0.0.0:8000
