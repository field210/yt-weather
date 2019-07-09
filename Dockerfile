# Dockerfile

# Using the official with Python 3.6 image
FROM python:3.6.8-alpine3.10

RUN apk update && apk add g++ gcc libxslt-dev chromium chromium-chromedriver

# Set the Work Directory
RUN mkdir /app
WORKDIR /app

# Copy the project codes into the Work Directory
COPY . .

# Install the project's dependencies
RUN pip install -r requirements.txt

# Run the image as a non-root user
RUN adduser -D myuser
USER myuser

# Run the Flask application
CMD python app.py
