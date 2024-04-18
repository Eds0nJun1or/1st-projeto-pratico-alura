import psutil

    def monitorar_recursos(): # Monitoramento de uso de CPU
    uso_cpu = psutil.cpu_percent(interval=1)
print("Uso de CPU:", uso_cpu, "%")

Monitoramento de uso de memória
uso_memoria = psutil.virtual_memory().percent
print("Uso de memória:", uso_memoria, "%")

monitorar_recursos()