# Use official Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy code and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Expose the port Flask runs on
EXPOSE 8000

# Start the app
CMD ["python", "app.py"]
