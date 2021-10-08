
FROM python:3.6.15
USER root
ENV BOT_ENV=production
COPY . /var/www
WORKDIR /var/www
RUN pip3 install rasa==1.8.0 
RUN rasa train

ENTRYPOINT ["rasa", "run", "-p", "8080"]
#ENTRYPOINT ["rasa", "run", "actions", "-p", "8088"]
