# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port 8000
EXPOSE 8000

# Default command to run Django server (no --reload)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
