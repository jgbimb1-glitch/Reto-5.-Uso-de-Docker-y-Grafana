# Reto 5 - Observabilidad QA con Docker y Grafana

## Objetivo
Implementar un flujo mínimo de observabilidad para métricas de calidad de pruebas utilizando Docker, Prometheus y Grafana.

## Arquitectura

Metrics Service → Prometheus → Grafana

## Métrica simulada
flake_rate = 0.08

## Ejecución

### Construir servicio
docker build -t test-metrics .

### Ejecutar métricas
docker run -d -p 8080:8080 --name test-metrics test-metrics

### Ejecutar Prometheus
docker run -d -p 9090:9090 --name prometheus -v "%cd%/prometheus.yml:/etc/prometheus/prometheus.yml" prom/prometheus

### Ejecutar Grafana
docker run -d -p 3000:3000 --name grafana grafana/grafana-oss

## URLs
- Metrics: http://localhost:8080/metrics
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000