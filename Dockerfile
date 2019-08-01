FROM ubuntu:latest
MAINTAINER Atul Abhishek "atul.abhishek@mayadata.io"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

