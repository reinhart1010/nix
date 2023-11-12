---
layout: page
title: common/aria2c (español)
description: "Utilidad de descarga rápida."
content_hash: 9f419a3356c79488664381464b7c69c7108feb26
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/aria2c.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aria2c.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/aria2c.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/aria2c.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aria2c.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aria2c.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aria2c

Utilidad de descarga rápida.
Soporta HTTP(S), FTP, SFTP, BitTorrent y Metalink.
Más información: <https://aria2.github.io>.

- Descarga un URI específico a un archivo:

`aria2c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`"`

- Descarga un archivo de una URI con un nombre de salida específico:

`aria2c --out=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`"`

- Descarga varios archivos diferentes en paralelo:

`aria2c --force-sequential `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">false</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url1 url2 ...</span>`"`

- Descarga desde múltiples fuentes con cada URI apuntando al mismo archivo:

`aria2c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url1 url2 ...</span>`"`

- Descarga las URI enumeradas en un archivo con un número determinado de descargas paralelas:

`aria2c --input-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` --max-concurrent-downloads=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_de_descargas</span>

- Descarga con varias conexiones:

`aria2c --split=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_de_conexiones</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`"`

- Descarga FTP con nombre de usuario y contraseña:

`aria2c --ftp-user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_usuario</span>` --ftp-passwd=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contrasena</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`"`

- Limita la velocidad de descarga en bytes por segundo:

`aria2c --max-download-limit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">velocidad</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`"`
