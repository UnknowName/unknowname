FROM django:1.8-python2
RUN pip install django_admin_bootstrapped gunicorn
ADD ./  /usr/src/app
WORKDIR /usr/src/app
RUN echo "yes" > yes.txt && python manage.py collectstatic <yes.txt
VOLUME ["/usr/src/app/uploads","/usr/src/app/static"]
RUN rm -rf .git  yest.txt Dockerfile requirements.txt Deploy
#CMD ["/usr/local/bin/python","manage.py","runserver","0.0.0.0:8000"]
CMD ["gunicorn", "unknowname.wsgi", "-w", "2", "-b", "0.0.0.0:8000"]  
EXPOSE 8000
