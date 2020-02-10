#Use the python3.7.2 container image
FROM python:3.7.2-stretch

#set the working directory to /app
WORKDIR /app

ADD requirements.txt .

# install the dependencies
RUN pip install -r requirements.txt

#copy the current director contents into the container at /app
ADD . /app
EXPOSE 3306

#run the command to start uwsgi
#CMD ["uwsgi", "app.ini"]
