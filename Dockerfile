
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 5000
EXPOSE 8501