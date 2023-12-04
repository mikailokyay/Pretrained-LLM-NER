# Use an official Python image as a parent image
FROM python:3.11-slim

WORKDIR /code

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        gcc \
        wget \
        git && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt  /code

RUN pip3 install --no-cache-dir -r /code/requirements.txt 

COPY ./ /code

WORKDIR /code

ENV PYTHONPATH "${PYTHONPATH}:/code"

EXPOSE 5000

# Define the command to start the API
CMD ["python", "planet_app:app", "--host", "0.0.0.0", "--port", "5000"]