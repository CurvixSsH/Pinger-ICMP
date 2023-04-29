import argparse
import signal
import time
from colorama import init, Fore, Style
import pyfiglet
from pythonping import ping
import sys

init()

banner = pyfiglet.figlet_format("Pinger", font="standard")
banner += Style.BRIGHT + Fore.MAGENTA + "\nMade by CurvixSsH & Hassan-Evil" + Style.RESET_ALL

print(Fore.CYAN + banner + Fore.RESET) 

parser = argparse.ArgumentParser(
    description='IGNORAR EL RESTO',
    usage='Ejemplos\nusa: python pinger.py (host) Ping a host\nusa: python pinger.py (host) -p (proxy) Ping a host con opción de proxy\n\nOPCIONES:\n  -h [ayuda]\n  -p [proxy_url]\n\nFORMATO:\n(formato: http://IP:PUERTO, https://IP:PUERTO, socks4://IP:PUERTO, socks5://IP:PUERTO)\n\nLISTA DE PROXY\nhttps://hidemy.name/es/proxy-list/',
    add_help=False
)
parser.add_argument('host', metavar='host', type=str, nargs='?',
                    help='Host a hacer ping')
parser.add_argument('-p', '--proxy', metavar='proxy_url', type=str, nargs='?',
                    help='URL del proxy a usar')
args = parser.parse_args()

# Solicitar el host si no se proporciona en los argumentos
if args.host is None:
    host = input("Por favor, introduce el host para hacer ping: ")
else:
    host = args.host

# Imprimir información sobre el host y el proxy si se especifica
if args.proxy is not None:
    print(f"Pinging {host} a través del proxy {args.proxy}...")
else:
    print(f"Pinging {host}...")

# Función para detener la ejecución con ctrl+c
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

while True:
    # Ping al host sin proxy
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





      