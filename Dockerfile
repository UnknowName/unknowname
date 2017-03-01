FROM django:1.10-python2
RUN pip install django_admin_bootstrapped
ADD ./  /usr/src/app
WORKDIR /usr/src/app
RUN rm -rf .git Dockerfile requirements.txt
EXPOSE 8000
CMD ["/usr/local/bin/python","manage.py","runserver","0.0.0.0:8000"]
