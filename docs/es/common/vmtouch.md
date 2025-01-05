---
layout: page
title: common/vmtouch (español)
description: "Gestiona la caché del sistema de archivos."
content_hash: 6f8032effc30c8380347c8ffe94f02793198d849
last_modified_at: 2025-01-05
related_topics:
  - title: English version
    url: /en/common/vmtouch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vmtouch

Gestiona la caché del sistema de archivos.
Más información: <https://manned.org/vmtouch>.

- Imprime el estado de la caché de un archivo:

`vmtouch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Carga un archivo en la caché:

`vmtouch -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Expulsa un archivo de la caché:

`vmtouch -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Bloquea un archivo en la memoria caché para evitar que salga de la memoria:

`vmtouch -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Bloquea un archivo y daemoniza el programa:

`vmtouch -ld `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
