FROM python:3.8

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install -U pip && pip install -e .

# creating a directory that will contain nltk_data
RUN mkdir /data

ENV DATA_FOLDER '/data'

EXPOSE 8007
