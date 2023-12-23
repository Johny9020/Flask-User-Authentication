FROM python:3.11-alpine
WORKDIR /webserver
COPY requirements.txt /webserver
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
COPY ./webserver /webserver
CMD python app.py