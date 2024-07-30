# COPY ./requirements.txt /app/requirements.txt
FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/requirements.txt

# Install the required Python packages
RUN pip3 install -r /app/requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app

# Specify the command to run the application
CMD ["python3", "app.py"]
