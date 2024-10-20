---
layout: page
title: linux/btrfs-rescue (español)
description: "Intenta recuperar un sistema de archivos btrfs dañado."
content_hash: f258a356fb845c406a766f614cb7cd2ff0dd8884
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/linux/btrfs-rescue.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-rescue.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/btrfs-rescue.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-rescue.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs rescue

Intenta recuperar un sistema de archivos btrfs dañado.
Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-rescue.html>.

- Reconstruye el árbol de metadatos del sistema de archivos (muy lento):

`sudo btrfs rescue chunk-recover `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la_partición</span>

- Corrige problemas relacionados con la alineación del tamaño del dispositivo (por ejemplo, incapacidad para montar el sistema de archivos debido a una discrepancia en los bytes totales del superbloque):

`sudo btrfs rescue fix-device-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la_partición</span>

- Recupera un superbloque dañado de copias correctas (recupera la raíz del árbol de archivos del sistema):

`sudo btrfs rescue super-recover `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la_partición</span>

- Recupera de transacciones interrumpidas (corrige problemas de reproducción de registros):

`sudo btrfs rescue zero-log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la_partición</span>

- Crea un dispositivo de control `/dev/btrfs-control` cuando `mknod` no está instalado:

`sudo btrfs rescue create-control-device`
