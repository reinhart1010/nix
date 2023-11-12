---
layout: page
title: common/df (español)
description: "Entrega información general del uso de espacio en disco del sistema de archivos."
content_hash: 7c45a635b1f7f45e3e7984b052158b334cca49fd
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/df.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/df.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/df.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/df.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/df.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/df.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/df.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

Entrega información general del uso de espacio en disco del sistema de archivos.
Más información: <https://www.gnu.org/software/coreutils/df>.

- Muestra todos los sistemas de archivos y sus usos de disco:

`df`

- Muestra todos los sistemas de archivos y sus usos de disco en formato legible para humanos:

`df -h`

- Muestra el sistema de archivos que contiene determinado archivo o directorio y su uso de disco:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio</span>

- Muestra estadísticas sobre el número de inodos libres:

`df -i`

- Muestra sistemas de archivos excluyendo los tipos especificados:

`df -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">squashfs</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>
