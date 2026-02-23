from prometheus_client import start_http_server, Gauge
import time

flake = Gauge('flake_rate', 'Flaky test rate')

start_http_server(8080)

print("Servidor de métricas activo en puerto 8080")

while True:
    flake.set(0.08)
    time.sleep(5)