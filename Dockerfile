FROM python:alpine3.10
WORKDIR /app 
COPY . /app
RUN pip install --upgrade pip
RUN pip install requests
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./gig/form.py
#COPY requirements.txt /app/requirements.txt
#ENTRYPOINT ["python", "./gig/form.py"]
