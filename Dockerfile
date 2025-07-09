FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget unzip curl xvfb libxi6 libgconf-2-4 libnss3-dev libxss1 libappindicator1 libindicator7 \
    fonts-liberation libasound2 libatk1.0-0 libcups2 libgtk-3-0 libxss1 libdbus-glib-1-2 \
    chromium chromium-driver wkhtmltopdf && \
    apt-get clean

# Set environment for headless Chrome
ENV CHROME_BIN="/usr/bin/chromium"
ENV PATH="${PATH}:/usr/bin/chromedriver"

# Set working directory
WORKDIR /app

# Copy everything into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
