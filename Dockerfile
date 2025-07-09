FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget unzip curl xvfb libxi6 libgconf-2-4 libnss3 libxss1 libappindicator1 \
    fonts-liberation libasound2 libatk1.0-0 libcups2 libgtk-3-0 libdbus-glib-1-2 \
    chromium wkhtmltopdf && \
    mkdir -p /tmp/chromedriver && \
    wget --no-check-certificate -O /tmp/chromedriver/chromedriver.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/114.0.5735.90/linux64/chromedriver-linux64.zip && \
    unzip /tmp/chromedriver/chromedriver.zip -d /tmp/chromedriver && \
    mv /tmp/chromedriver/chromedriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN="/usr/bin/chromium"
ENV PATH="${PATH}:/usr/local/bin"

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
