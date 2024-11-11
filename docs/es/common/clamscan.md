---
layout: page
title: common/clamscan (español)
description: "Un escáner de virus de línea de comandos."
content_hash: 7541ddbaaf7418000c2341fed555301f16c404e0
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/common/clamscan.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/clamscan.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/clamscan.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clamscan.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/clamscan.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/clamscan.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/clamscan.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/clamscan.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># clamscan

Un escáner de virus de línea de comandos.
Más información: <https://docs.clamav.net/manual/Usage/Scanning.html#clamscan>.

- Escanea un archivo buscando vulnerabilidades:

`clamscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Escanea todos los archivos recursivamente en un directorio específico:

`clamscan -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Escanea datos desde 'stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | clamscan -`

- Escanea usando un archivo de bases de datos de virus o directorio de archivos:

`clamscan --database `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio_con_base_de_datos</span>

- Escanea el directorio actual y muestra solo los archivos infectados:

`clamscan --infected`

- Imprime el informe de la exploración a un archivo de registro (log):

`clamscan --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_registro</span>

- Mueve archivos infectados a un directorio específico:

`clamscan --move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_de_cuarentena</span>

- Elimina los archivos infectados:

`clamscan --remove yes`
