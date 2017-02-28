FROM django:1.10-python2
RUN pip install django_admin_bootstrapped
ADD ./  /usr/src/app
WORKDIR /usr/src/app
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000