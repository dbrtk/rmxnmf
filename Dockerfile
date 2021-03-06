FROM python:latest

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install -U pip && pip install -e .

# creating a directory that will contain nltk_data
RUN mkdir /data
VOLUME /data

ENV BROKER_HOST_NAME 'message_broker'

ENV DATA_FOLDER '/data'

