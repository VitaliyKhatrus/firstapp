FROM python:2.7
MAINTAINER Vitaliy Khatrus <vitaliy.khatrus@gmail.com>
ADD . /project
ENV DJANGO_SETTINGS_MODULE firstapp.settings
RUN pip install -r /project/requirements.txt
RUN python /project/manage.py validate
RUN python /project/manage.py collectstatic --noinput
CMD python /project/manage.py runserver 0.0.0.0:8080
