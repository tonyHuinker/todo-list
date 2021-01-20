# Use an official Python runtime as a parent image
FROM ubuntu:20.10
# Set the working directory to /todo

WORKDIR /todo

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install git python3-pip python3-setuptools -y

# Copy the current directory contents into the container at /todo
ADD . /todo

RUN pip3 install pytz
RUN pip3 install oauth2
WORKDIR /todo/evernote 
RUN python3 setup.py install


# Define environment variable
WORKDIR /todo

