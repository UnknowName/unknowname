FROM django:1.10-python2
RUN pip install django_admin_bootstrapped
ADD ./  /usr/src/app
WORKDIR /usr/src/app
EXPOSE 8000
RUN echo "yes" > yes.txt && python manage.py collectstatic <yes.txt
VOLUME ["/usr/src/app/uploads","/usr/src/app/static"]
RUN rm -rf .git  yest.txt Dockerfile requirements.txt Deploy
CMD ["/usr/local/bin/python","manage.py","runserver","0.0.0.0:8000"]
