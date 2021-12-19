---
layout: page
title: common/nmap (español)
description: "Herramienta de exploración de redes y escáner de seguridad / puertos."
content_hash: cdb070df3b39fdff3fe77bbefee0dd55cf546b43
related_topics:
  - title: English version
    url: /en/common/nmap.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/nmap.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/nmap.html
    icon: bi bi-globe
---
# nmap

Herramienta de exploración de redes y escáner de seguridad / puertos.
Algunas características solo funcionan si ejecutamos Nmap con privilegios.
Más información: <https://nmap.org>.

- Comprueba si una dirección IP está activa, e intenta averiguar el sistema operativo del servidor correspondiente:

`nmap -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_hostname</span>

- Intenta determinar si los hosts están activos y cuáles son sus nombres:

`nmap -sn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_hostname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opcional_otra_direccion</span>

- Como el anterior, pero también ejecuta un escaneo de 1000 puertos TCP por defecto, si el host está activo:

`nmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_hostname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opcional_otra_direccion</span>

- Detecta también scripts, servicios, sistema operativo y traceroute:

`nmap -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">direccion_o_direcciones</span>

- Asume una buena conexión y acelera la ejecución:

`nmap -T4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">direccion_o_direcciones</span>

- Escanea una lista específica de puertos (para todos los puertos `1-65535` usar `-p-`):

`nmap -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto1,puerto2,…,puertoN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">direccion_o_direcciones</span>

- Realiza un escaneo TCP y UDP (usar `-sU` para solo UDP, `-sZ` para SCTP, `-sO` para IP):

`nmap -sSU `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">direccion_o_direcciones</span>

- Realiza un escaneo total de puertos, servicios, detección de versiones con todos los scripts NSE por defecto contra un host para determinar debilidades e información:

`nmap -sC -sV `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">direccion_o_direcciones</span>
