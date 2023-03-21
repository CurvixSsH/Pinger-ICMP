import sys
import signal
import time 
from colorama import init, Fore, Style
import pyfiglet
from pythonping import ping


init()

"""
este fragmento de código crea un banner de texto personalizado 
con un estilo y color específicos utilizando dos módulos externos.
"pyfiglet" y "colorama"
"""
banner = pyfiglet.figlet_format("Pinger", font="standard")
banner += Style.BRIGHT + Fore.MAGENTA + "\nMade by CurvixSsH & Hassan-Evil" + Style.RESET_ALL

print(Fore.CYAN + banner + Fore.RESET)


# Solicita el host si no se proporciona en los argumentos asi se evita que entre en un bucle de arror al no insertar un host
if len(sys.argv) < 2:
    host = input("Por favor, introduce el host para hacer ping: ")
else:
    host = sys.argv[1]

print(f"Pinging {host}...")

""""
Función para detener la ejecucion con ctrl+c ya que sin esta funcion al detener el pinger se mostraban errores en la consola
la otra opcion era importar la libreria keyboard pero asi es mas practico
"""
successful_pings = 0
failed_pings = 0

def signal_handler(sig, frame):
    print(f"\nDeteniendo...\n")
    if failed_pings == 0:
        print(f"Estadísticas:\n  Pings exitosos: {Fore.GREEN}{successful_pings}{Fore.RESET}\n  Pings fallidos: {failed_pings}")
    else:
        print(f"Estadísticas:\n  Pings exitosos: {Fore.GREEN}{successful_pings}{Fore.RESET}\n  Pings fallidos: {Fore.RED}{failed_pings}{Fore.RESET}")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

# codigo del ping a un host especifico y mostrar los tiempos de respuesta
""""
Aca Se le añadieron varias funciones, 
1)- Se le agrego un bucle infinito basado en la funcion ping -t de windows CMD
2)- La biblioteca utilizada para hacer ping era la biblioteca "ping3 pero no daba los ms correctamente
    asi que se actualizo a usar from pythonping import ping para solucionar el problema
3)- El código luego verifica si la respuesta del ping fue exitosa y la imprime como online y si la latencia promedi es inferior o igual a 1200ms
    pero si sobrepasa este parametro EJ: 1300 ms se imprimira como offline 
"""

while True:
    response_list = ping(host, count=1)
    if response_list.rtt_avg_ms is not None:
        if response_list.rtt_avg_ms <= 1200:
            successful_pings += 1
            print(f"{Fore.WHITE}CurvixSsH - {Fore.GREEN}Online{Fore.RESET} {Fore.WHITE}from{Fore.RESET} {Fore.WHITE}{host}{Fore.RESET}: {Fore.WHITE}time={Fore.BLUE}{response_list.rtt_avg_ms:.2f}ms{Fore.RESET}")
        else:
            failed_pings += 1
            print(f"{Fore.WHITE}CurvixSsH - {Fore.RED}Offline{Fore.WHITE} - {Fore.WHITE}{host}: {Fore.WHITE}time={Fore.BLUE}{response_list.rtt_avg_ms:.2f}ms{Fore.RESET}")
    else:
        failed_pings += 1
        print(f"{Fore.WHITE}CurvixSsH - {Fore.RED}Offline{Fore.WHITE} - {Fore.WHITE}{host}: {Fore.WHITE}time={Fore.BLUE}{Fore.RED}fly{Fore.RESET}")
    time.sleep(1)