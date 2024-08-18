---
layout: page
title: linux/dysk (español)
description: "Muestra información del sistema de archivos en una tabla."
content_hash: b105e82df20c55ae1fefd5927cde854d0925bdb0
last_modified_at: 2024-08-18
related_topics:
  - title: English version
    url: /en/linux/dysk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dysk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dysk

Muestra información del sistema de archivos en una tabla.
Más información: <https://dystroy.org/dysk>.

- Obtén una visión general estándar de tus discos habituales:

`dysk`

- Ordena por tamaño libre:

`dysk --sort free`

- Incluye solo discos HDD:

`dysk --filter 'disk = HDD'`

- Excluye discos SSD:

`dysk --filter 'disk <> SSD'`

- Muestra discos con alta ocupación o poco espacio libre:

`dysk --filter 'use > 65% | free < 50G'`
