---
layout: page
title: common/clamdscan (español)
description: "Escaneo de virus con el servicio (daemon) ClamAV."
content_hash: 73166eb7a63e9934553bca1371d8ac68ce5bfc46
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/clamdscan.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/clamdscan.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clamdscan.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/clamdscan.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/clamdscan.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/clamdscan.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/clamdscan.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># clamdscan

Escaneo de virus con el servicio (daemon) ClamAV.
Más información: <https://docs.clamav.net/manual/Usage/Scanning.html#clamdscan>.

- Escanea un archivo o directorio buscando vulnerabilidades:

`clamdscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio</span>

- Escanea desde 'stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | clamdscan -`

- Escanea el directorio actual y muestra solo los archivos infectados:

`clamdscan --infected`

- Imprime el informe de la exploración a un archivo de registro (log):

`clamdscan --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_registro</span>

- Mueve los archivos infectados a un directorio específico:

`clamdscan --move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio_de_cuarentena</span>

- Elimina los archivos infectados:

`clamdscan --remove`

- Utiliza varios hilos para escanear un directorio:

`clamdscan --multiscan`

- Pasa el descriptor de archivo en lugar de transmitir el archivo al daemon:

`clamdscan --fdpass`
