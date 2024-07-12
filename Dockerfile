# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
#COPY requirements.txt .

# Install any needed packages specified in requirements.txt

# Copy the rest of the application code into the container
COPY . .
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

# Expose the port the app runs on
EXPOSE 8000

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]












