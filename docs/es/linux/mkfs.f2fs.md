---
layout: page
title: linux/mkfs.f2fs (español)
description: "Crea un sistema de archivos F2FS en una partición."
content_hash: e6caf2b24188fbfb6f65b07ccacd498dc0fe1383
last_modified_at: 2024-04-04
related_topics:
  - title: English version
    url: /en/linux/mkfs.f2fs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs.f2fs

Crea un sistema de archivos F2FS en una partición.
Más información: <https://manned.org/mkfs.f2fs>.

- Crea un sistema de archivos F2FS en la primera partición del dispositivo b (`sdb1`):

`sudo mkfs.f2fs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Crea un sistema de archivos F2FS con una etiqueta de volumen:

`sudo mkfs.f2fs -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiqueta_volumen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
