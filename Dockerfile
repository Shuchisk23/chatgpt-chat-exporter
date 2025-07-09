# Use official Python slim image
FROM python:3.10-slim

# Install system dependencies, Chromium, wkhtmltopdf, and utilities
RUN apt-get update && apt-get install -y \
    wget unzip curl xvfb libxi6 libgconf-2-4 libnss3-dev libxss1 libappindicator1 libindicator7 \
    fonts-liberation libasound2 libatk1.0-0 libcups2 libgtk-3-0 libdbus-glib-1-2 \
    chromium wkhtmltopdf && \
    # Download matching ChromeDriver manually
    wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/114.0.5735.90/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip -d /usr/local/bin/ && \
    rm chromedriver-linux64.zip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set environment variables for headless Chrome
ENV CHROME_BIN="/usr/bin/chromium"
ENV PATH="${PATH}:/usr/local/bin"

# Set working directory
WORKDIR /app

# Copy local code to container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
