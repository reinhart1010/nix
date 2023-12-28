---
layout: page
title: common/nmap (español)
description: "Herramienta de exploración de redes y escáner de seguridad/puertos."
content_hash: 99ec88278fa9b0c1d094bc5c8b19ed06e9ebfd5b
last_modified_at: 2023-12-28
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
Algunas funciones sólo se activan cuando Nmap se ejecuta con privilegios de root.
Más información: <https://nmap.org>.

- Comprueba si una dirección IP está activa y adivina el sistema operativo del host remoto:

`nmap -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_nombre_del_host</span>

- Intenta determinar si los hosts especificados están activos (exploración ping) y cuáles son sus nombres y direcciones MAC:

`sudo nmap -sn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_nombre_del_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opcional_otra_dirección</span>

- Habilita también los scripts, la detección de servicios, la huella digital del SO y el traceroute:

`nmap -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_o_direcciones</span>

- Escanea una lista específica de puertos (usa '-p-' para todos los puertos desde 1 al 65535):

`nmap -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port1,port2,...,portN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_o_direcciones</span>

- Realiza la detección de servicios y versiones de los 1000 puertos principales utilizando los scripts por defecto de NSE; escribiendo los resultados ('-oN') en el fichero de salida:

`nmap -sC -sV -oN `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">top-1000-puertos.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_o_direcciones</span>

- Escanea objetivo(s) cuidadosamente utilizando los scripts NSE "default and safe":

`nmap --script "default and safe" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_o_direcciones</span>

- Escanea el servidor web que se ejecuta en los puertos estándar 80 y 443 utilizando todos los scripts de NSE 'http-*' disponibles:

`nmap --script "http-*" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_o_direcciones</span>` -p 80,443`

- Realiza un escaneo sigiloso muy lento ('-T0') intentando evitar la detección por parte de IDS/IPS y utiliza direcciones IP de origen con señuelo ('-D'):

`nmap -T0 -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">decoy1_direcciónip,decoy2_direcciónip,...,decoyN_direcciónip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_o_direcciones</span>
