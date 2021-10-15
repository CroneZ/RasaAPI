 
FROM rasa/rasa-sdk:1.8.0
USER root
ENV BOT_ENV=development
COPY . /var/www
WORKDIR /var/www
RUN pip3 install rasa==1.8.0
RUN rasa train

ENTRYPOINT ["rasa", "run", "-p", "8080", "--debug", "-vv", "--enable-api", "-m", "models","--log-file", "out.log", "--cors", "*", "actions"]
