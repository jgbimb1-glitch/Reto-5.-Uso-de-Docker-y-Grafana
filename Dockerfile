FROM python:3.11-slim

WORKDIR /app

COPY metrics_server.py .

RUN pip install prometheus_client

EXPOSE 8080

CMD ["python", "metrics_server.py"]