---
layout: page
title: osx/fsck (español)
description: "Comprueba la integridad de un sistema de archivos o los repara. El sistema de ficheros debe estar desmontado en el momento de ejecutar el comando."
content_hash: 137d0a3cd98c4d3bf5a279f3aaf7c79027a6305b
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/fsck.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/fsck.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/fsck.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fsck

Comprueba la integridad de un sistema de archivos o los repara. El sistema de ficheros debe estar desmontado en el momento de ejecutar el comando.
Es una envoltura que llama a `fsck_hfs`, `fsck_apfs`, `fsck_msdos`, `fsck_exfat`, y `fsck_udf` según sea necesario.
Más información: <https://keith.github.io/xcode-man-pages/fsck.8.html>.

- Comprueba el sistema de ficheros `/dev/sdX`, informando de cualquier bloque dañado:

`fsck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Comprueba el sistema de ficheros `/dev/sdX` sólo si está limpio, informando de los bloques dañados y dejando que el usuario elija interactivamente si repara cada uno de ellos:

`fsck -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Comprueba el sistema de archivos `/dev/sdX` sólo si está limpio, informando de los bloques dañados y reparándolos automáticamente:

`fsck -fy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Comprueba el sistema de archivos `/dev/sdX`, informando si se ha desmontado correctamente:

`fsck -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
