FROM python:alpine3.10
WORKDIR /app 
COPY . /app
RUN pip install --upgrade pip
RUN pip install flask
RUN pip3 install flask
RUN pip install requests
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./gig/form.py
#COPY requirements.txt /app/requirements.txt
#ENTRYPOINT ["python", "./gig/form.py"]
