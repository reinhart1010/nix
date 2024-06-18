---
layout: page
title: common/nmap (español)
description: "Herramienta de exploración de redes y escáner de seguridad/puertos."
content_hash: b85660864d4ec2034722a31b87b3ac479db273f6
last_modified_at: 2024-06-18
related_topics:
  - title: Deutsch version
    url: /de/common/nmap.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/nmap.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/nmap.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/nmap.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/nmap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmap

Herramienta de exploración de redes y escáner de seguridad/puertos.
Algunas funciones (p. ej. escaneo SYN) se activan solamente cuando `nmap` es ejecutado con los permisos del superusuario.
Más información: <https://nmap.org/book/man.html>.

- Escanea los top 1000 puertos de un host remoto con varios niveles de [v]erbosidad:

`nmap -v`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_nombre_de_host</span>

- Ejecuta un barrido de ping sobre una subred o hosts específicos:

`nmap -T5 -sn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.0/24|ip_o_nombre_de_host1,ip_o_nombre_de_host2,...</span>

- Activa la detección de sistemas operativos, la detección de versión, el escaneo con guiones y traceroute:

`sudo nmap -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_nombre_de_host1,ip_o_nombre_de_host2,...</span>

- Escanea una lista de puertos (invoca `nmap` con `-p-` para escanear todos los puertos desde 1 a 65535):

`nmap -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto1,puerto2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_host1,ip_o_host2,...</span>

- Detecta el servicio y versión de los top 1000 puertos usando los guiones NSE por defecto y escribe los resultados (`-oA`) en archivos de salida:

`nmap -sC -sV -oA `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">top-1000-ports</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_host1,ip_o_host2,...</span>

- Escanea objetivo(s) cuidadosamente usando los guiones NSE `default and safe`:

`nmap --script "default and safe" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_host1,ip_o_host2,...</span>

- Escanea servidores web ejecutándose en los puertos estándares 80 y 443 usando todos los guiones `http-*` NSE disponibles:

`nmap --script "http-*" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_host1,ip_o_host2,...</span>` -p 80,443`

- Intenta evadir los sistemas de detección y prevención de intrusos escaneando extremadamente lento (`-T0`) y usando direcciones de origen de señuelo (`-D`), paquetes [f]ragmentados, datos aleatorios y otros métodos:

`sudo nmap -T0 -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_de_señuelo1,ip_de_señuelo2,...</span>` --source-port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">53</span>` -f --data-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>` -Pn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_host</span>
