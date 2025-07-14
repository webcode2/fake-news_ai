# Use official Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies (optional but recommended)
RUN apt-get update && \
    apt-get install -y build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app source code
COPY ./src ./src

# Copy root-level files if needed
COPY ./.env ./

# Command to run the app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
