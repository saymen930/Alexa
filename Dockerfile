# Use the official Python 3.9 slim image
FROM python:3.9-slim-buster

# Set environment variables to reduce interactive prompts and enable Python optimizations
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install necessary dependencies including Git and ffmpeg, then clean up
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory and copy the application files
WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Set the default command
CMD ["bash", "start"]