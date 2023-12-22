FROM python
WORKDIR /webserver
COPY requirements.txt ./webserver
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./webserver /webserver
CMD python app.py