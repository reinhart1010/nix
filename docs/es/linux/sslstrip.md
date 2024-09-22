---
layout: page
title: linux/sslstrip (español)
description: "Realiza ataques de stripping de Secure Sockets Layer (SSL) basados en el trabajo de Moxie Marlinspike."
content_hash: a6eab37f03760d3503ad1e92b354348110d96335
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/linux/sslstrip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sslstrip

Realiza ataques de stripping de Secure Sockets Layer (SSL) basados en el trabajo de Moxie Marlinspike.
Realiza un ataque de suplantación de ARP en conjunto.
Más información: <https://www.kali.org/tools/sslstrip/>.

- Registra sólo el tráfico HTTPS POST en el puerto 10000 por defecto:

`sslstrip`

- Registra sólo el tráfico HTTPS POST en el puerto 8080:

`sslstrip --listen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>

- Registra todo el tráfico SSL hacia y desde el servidor en el puerto 8080:

`sslstrip --ssl --listen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>

- Registra todo el tráfico SSL y HTTP hacia y desde el servidor en el puerto 8080:

`sslstrip --listen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>` --all`

- Especifica la ruta del archivo para almacenar los registros:

`sslstrip --listen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>` --write=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo</span>

- Muestra la ayuda:

`sslstrip --help`
