# Pinger-ICMP
Este proyecto es un script de Python que para hacer pings a un host. El script permite hacer pings a un host y especificar un proxy opcional para hacer la conexión mas segura y anónima. 

La herramienta es útil para comprobar la conectividad con un host y determinar si esta en linea o no (cave destacar que no a todos los host se les puede hacer un ping correctamente ya que algunos tendran medidas de seguridad que bloquearan el íng atraves del protocolo ICMP.
Este proyecto está construido con Python 3.7 y utiliza los módulos 'argparse', 'pythonping', 'colorama' y 'pyfiglet'.

Siéntete libre de contribuir a este proyecto agregando nuevas funciones o mejorando las existentes.


![prueba icmp](https://user-images.githubusercontent.com/127477293/227630649-117684c8-7281-4be1-b129-d7efe180193d.png)


![1111222111](https://user-images.githubusercontent.com/127477293/235280185-e6843645-368f-4c7a-8ced-c8c23a32459b.png)


# INSTALACION
pip install colorama pyfiglet pythonping

git clone https://github.com/CurvixSsH/Pinger-ICMP.git

cd Pinger-ICMP

python pinger.py

# EJEMPLO
python pinger.py (host)

O si deas especificar un proxy

python pinger.py (host) -p (proxy) Ping a host con opción de proxy

python pinger.py -h (help) 

#FORMATO DE PROXY
http://IP:PUERTO, https://IP:PUERTO, socks4://IP:PUERTO, socks5://IP:PUERTO
