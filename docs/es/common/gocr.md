---
layout: page
title: common/gocr (español)
description: "Herramienta de reconocimiento óptico de caracteres."
content_hash: b7efffded1a5ee1ecd66311899a32ef51d2c75c6
last_modified_at: 2024-02-26
related_topics:
  - title: English version
    url: /en/common/gocr.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gocr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gocr

Herramienta de reconocimiento óptico de caracteres.
Reconoce caracteres utilizando su motor y solicita al usuario patrones desconocidos para almacenarlos en una base de datos.
Más información: <https://manned.org/gocr.1>.

- Reconoce caracteres en una [i]magen y los escribe en un archiv[o]. Coloca la base de datos en una carpeta existente para que no se omita su uso. [m]odo 130 significa crear, usar y extender la base de datos:

`gocr -m 130 -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_db</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen_entrada.png</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_salida.txt</span>

- Reconoce caracteres y asume que todos son números:

`gocr -m 130 -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_db</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen_entrada.png</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_salida.txt</span>` -C "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..9</span>`"`

- Reconoce caracteres con certez[a] del 100% (los caracteres tienen una mayor probabilidad de ser tratados como desconocidos):

`gocr -m 130 -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_db</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen_entrada.png</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_salida.txt</span>` -a 100`
