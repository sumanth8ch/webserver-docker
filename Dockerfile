FROM centos:latest

RUN yum -y install python3
RUN pip3 install flask
RUN yum -y install git


WORKDIR /puts2

COPY . /puts
EXPOSE 4080

ENTRYPOINT ["python3"]
CMD ["main.py"]
