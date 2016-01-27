# use base python image with python 2.7
FROM python:2.7

# add requirements.txt to the image
ADD requirements.txt /app/requirements.txt

# set working directory to /app/
WORKDIR /app/

# install python dependencies
RUN pip install -r requirements.txt

# Add user
RUN adduser --disabled-password --gecos '' celery

# mount ip-172-31-9-250.us-west-2.compute.internal:/public /public

# docker build -t worker /public && \
# docker run \
#   -e BROKER_URL=amqp://guest:guest@ip-172-31-9-250.us-west-2.compute.internal/ \
#   -v /public:/app worker \
#   su -m celery -c "celery -A kwcontributes worker -l info"
