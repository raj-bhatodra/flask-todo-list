# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Set environment variable for database
ENV DATABASE_URL=postgresql://postgres:postgres@database/mydb

# Expose port 5000 for the Flask application
EXPOSE 6000

# Start the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
