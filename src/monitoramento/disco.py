import psutil

def monitorar_uso_disco():
    uso_disco = psutil.disk_usage('/')
print("Uso de disco:")
print("Total:", uso_disco.total)
print("Usado:", uso_disco.used)
print("Livre:", uso_disco.free)

monitorar_uso_disco()