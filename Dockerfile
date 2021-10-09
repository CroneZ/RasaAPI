
FROM python:3.6.15
USER root
ENV BOT_ENV=development
COPY . /var/www
WORKDIR /var/www
RUN pip3 install rasa==1.8.0 

ENTRYPOINT ["rasa", "run", "-p", "8080", "--debug", "-vv", "--enable-api", "-m", "models", "--cors", "*", "actions"]
#ENTRYPOINT ["rasa", "run", "actions", "-p", "8088"]
