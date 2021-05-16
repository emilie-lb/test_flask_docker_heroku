FROM ubuntu:16.04
# RUN apt-get update &&  apt-get upgrade -y
# RUN python -m pip install --upgrade pip
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev


COPY requirements.txt /app/back/requirements.txt
COPY run.py /app/run.py
COPY ./back /app/back
WORKDIR /app/back
RUN pip install -r requirements.txt 


EXPOSE 5000
WORKDIR /app
ENTRYPOINT [ "python" ]

CMD [ "run.py" ]
# CMD ["app.py"]

# FROM python:3.8.1

# ENV APP_HOME /app
# WORKDIR $APP_HOME

# COPY ./back /app

# RUN pip install -r requirements.txt

# ENTRYPOINT ["python run.py"]