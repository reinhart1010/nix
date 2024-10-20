---
layout: page
title: linux/btrfs-balance (español)
description: "Equilibra grupos de bloques en un sistema de archivos btrf."
content_hash: 7b5047bc87f63b6c85ff1567990dd67ea2b5d86a
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/linux/btrfs-balance.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/btrfs-balance.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-balance.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs balance

Equilibra grupos de bloques en un sistema de archivos btrf.
Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-balance.html>.

- Muestra el estado de una operación de equilibrio en curso o pausada:

`sudo btrfs balance status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/sistema_de_archivos_btrfs</span>

- Equilibra todos los grupos de bloques (lento; reescribe todos los bloques en el sistema de archivos):

`sudo btrfs balance start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/sistema_de_archivos_btrfs</span>

- Equilibra grupos de bloques de datos que están menos del 15% utilizados, ejecutando la operación en segundo plano:

`sudo btrfs balance start --bg -dusage=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/sistema_de_archivos_btrfs</span>

- Equilibra un máximo de 10 bloques de metadatos con menos del 20% de utilización y al menos 1 bloque en un dispositivo dado `devid` (vea `btrfs filesystem show`):

`sudo btrfs balance start -musage=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>`,limit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`,devid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">devid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/sistema_de_archivos_btrfs</span>

- Convierte bloques de datos a raid6 y metadatos a raid1c3 (vea mkfs.btrfs(8) para perfiles):

`sudo btrfs balance start -dconvert=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raid6</span>` -mconvert=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raid1c3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/sistema_de_archivos_btrfs</span>

- Convierte bloques de datos a raid1, omitiendo bloques ya convertidos (por ejemplo, después de una operación de conversión cancelada previamente):

`sudo btrfs balance start -dconvert=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raid1</span>`,soft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/sistema_de_archivos_btrfs</span>

- Cancela, pausa o reanuda una operación de equilibrio en curso o pausada:

`sudo btrfs balance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cancelar|pausar|reanudar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/sistema_de_archivos_btrfs</span>
