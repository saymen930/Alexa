# Use the official Python 3.9 slim image
FROM python:3.9-slim-buster

# Install necessary dependencies including Git and ffmpeg, then clean up
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory and copy the application files
WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Set the default command
CMD ["bash", "start"]