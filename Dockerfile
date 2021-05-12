FROM python:3.8
RUN pip install flask
RUN pip install flask_restful
RUN pip install flask-cors
COPY *.py /app/
COPY *.txt /app/
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["app.py"]
