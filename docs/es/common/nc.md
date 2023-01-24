---
layout: page
title: common/nc (español)
description: "Netcat es una utilidad versátil para trabajar con datos TCP o UDP."
content_hash: 77fa58cf9400d35809cc761924726e259ae218a2
last_modified_at: 2023-01-24
related_topics:
  - title: English version
    url: /en/common/nc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/nc.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nc

Netcat es una utilidad versátil para trabajar con datos TCP o UDP.
Más información: <https://nmap.org/ncat>.

- Escuchar en un puerto determinado e imprimir cualquier dato recibido:

`nc -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>

- Conectarse a un puerto determinado:

`nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">direccion_ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>

- Configurar un tiempo máximo de respuesta:

`nc -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tiempo_en_segundos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">direccion_ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>

- Mantener el servidor activo hasta que el cliente se desconecte:

`nc -k -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>

- Mantener el cliente activo durante un tiempo después de recibir EOF:

`nc -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tiempo_en_segundos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">direccion_ip</span>

- Escanear puertos abiertos en un determinado host:

`nc -v -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">direccion_ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto1 puerto2 ...</span>

- Actuar como un proxy y redirigir los datos desde un puerto TCP local a un host remoto específico:

`nc -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto_local</span>` | nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto_remoto</span>
