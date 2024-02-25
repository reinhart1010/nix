---
layout: page
title: netbsd/df (español)
description: "Muestra una visión general del uso del espacio en disco del sistema de archivos."
content_hash: d00a626b211175faff70388dbeba9a899b8014b3
last_modified_at: 2024-02-25
related_topics:
  - title: English version
    url: /en/netbsd/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/df.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/netbsd/df.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># df

Muestra una visión general del uso del espacio en disco del sistema de archivos.
Más información: <https://man.netbsd.org/NetBSD-9.3/df.1>.

- Muestra todos los sistemas de ficheros y su uso de disco usando unidades de 512 bytes:

`df`

- Utiliza palabras [h]umanas para indicar unidades (basadas en potencias de 1024):

`df -h`

- Muestra todos los campos de la(s) estructura(s) devuelta(s) por `statvfs`:

`df -G`

- Muestra el sistema de archivos y su uso del disco que contiene el archivo o directorio dado:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio</span>

- Incluye estadísticas sobre el número de nodos-[i] libres y utilizados:

`df -i`

- Utiliza unidades de 1024 bytes al escribir las cifras de espacio:

`df -k`

- Muestra la información de manera [P]ortable:

`df -P`
