# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY app.py .

# Install Flask
RUN pip install flask

# Expose port
EXPOSE 8000

# Run the app
CMD ["python", "app.py"]
