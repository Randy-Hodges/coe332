FROM python:3.9

RUN mkdir /app
WORKDIR /app
RUN pip install flask
RUN pip install redis
COPY redis_app.py /app
COPY ML_Data_Sample.json /app

ENTRYPOINT ["python"]
CMD ["redis_app.py"]