# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

COPY requirements.txt .
COPY configs.yaml .
RUN pip install -r requirements.txt



COPY . .

EXPOSE 5000

CMD ["python", "app/main.py"]