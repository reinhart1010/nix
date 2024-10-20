---
layout: page
title: linux/btrfs-scrub (español)
description: "Realiza un scrub en sistemas de archivos btrfs para verificar la integridad de los datos."
content_hash: d691e44ea19a6aa4cf997b2615bb9b0a2b40236b
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/linux/btrfs-scrub.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-scrub.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/btrfs-scrub.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-scrub.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs-scrub.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs scrub

Realiza un scrub en sistemas de archivos btrfs para verificar la integridad de los datos.
Se recomienda ejecutar un scrub una vez al mes.
Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-scrub.html>.

- Inicia un scrub:

`sudo btrfs scrub start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_montaje_btrfs</span>

- Muestra el estado de un scrub en curso o del último completado:

`sudo btrfs scrub status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_montaje_btrfs</span>

- Cancela un scrub en curso:

`sudo btrfs scrub cancel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_montaje_btrfs</span>

- Reanuda un scrub previamente cancelado:

`sudo btrfs scrub resume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_montaje_btrfs</span>

- Inicia un scrub, pero espera a que termine antes de salir:

`sudo btrfs scrub start -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_montaje_btrfs</span>

- Inicia un scrub en modo silencioso (no imprime errores ni estadísticas):

`sudo btrfs scrub start -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_montaje_btrfs</span>
