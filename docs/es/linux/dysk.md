---
layout: page
title: linux/dysk (español)
description: "Muestra información del sistema de archivos en una tabla."
content_hash: b105e82df20c55ae1fefd5927cde854d0925bdb0
last_modified_at: 2024-08-19
related_topics:
  - title: English version
    url: /en/linux/dysk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dysk

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
