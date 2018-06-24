# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /todo

# Copy the current directory contents into the container at /app
ADD . /todo

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Define environment variable

# Run app.py when the container launches
CMD ["python", "main.py"]
