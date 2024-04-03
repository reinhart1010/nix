---
layout: page
title: osx/diskutil-partitiondisk (español)
description: "Utilidad para gestionar particiones en discos y volúmenes."
content_hash: fcf02f383327c132cd185343e44fe1d818ab6ea3
last_modified_at: 2024-04-03
related_topics:
  - title: English version
    url: /en/osx/diskutil-partitiondisk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/diskutil-partitiondisk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># diskutil partitionDisk

Utilidad para gestionar particiones en discos y volúmenes.
Parte de `diskutil`.
APM solo es compatible con macOS, MBR está optimizado para DOS, mientras que GPT es compatible con la mayoría de los sistemas operativos modernos.
Más información: <https://keith.github.io/xcode-man-pages/diskutil.8.html>.

- Reformatea un volumen usando el esquema de particionado APM/MBR/GPT, sin dejar particiones en su interior (esto borrará todos los datos del volumen):

`diskutil partitionDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_de_disco</span>` 0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">APM|MBR|GPT</span>

- Reformatea un volumen, luego crea una única partición usando un sistema de archivos específico llenando todo el espacio libre:

`diskutil partitionDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_de_disco</span>` 1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">APM|MBR|GPT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">partición_con_sistema_de_archivos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_partición</span>

- Reformatea un volumen, luego crea una única partición con un sistema de archivos y tamaño específico (ej. `16G` para 16GB o `50%` para llenar la mitad del tamaño total del volumen):

`diskutil partitionDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_de_disco</span>` 1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">APM|MBR|GPT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">partición_con_sistema_de_archivos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_partición</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tamaño_de_partición</span>

- Reformatea un volumen y crea múltiples particiones:

`diskutil partitionDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_disco</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_particiones</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">APM|MBR|GPT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">partición_sistema_archivos1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_partición1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tamaño_partición1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">partición_sistema_archivos2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_partición2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tamaño_partición2</span>` ...`

- Lista todos los sistemas de ficheros soportados para particionar:

`diskutil listFilesystems`
