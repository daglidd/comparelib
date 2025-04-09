# Use an official Python runtime as a parent image.
FROM python:3.9-slim

# Install required apt packages for Chromium and Playwright.
RUN apt-get update && apt-get install -y \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    fonts-liberation \
    libappindicator3-1 \
    lsb-release \
    xdg-utils \
 && rm -rf /var/lib/apt/lists/*

# Set working directory.
WORKDIR /app

# Copy requirements file and install Python dependencies.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright and download all browsers.
RUN pip install playwright && python -m playwright install

# Copy the application code.
COPY . .

# Expose port 5000.
EXPOSE 5000

# Run the Flask app.
CMD ["python", "app.py"]