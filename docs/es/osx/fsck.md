---
layout: page
title: osx/fsck (español)
description: "Comprueba la integridad de un sistema de archivos o los repara. El sistema de ficheros debe estar desmontado en el momento de ejecutar el comando."
content_hash: af4eeea23703445cfce1c33b5efc89297d02b13c
last_modified_at: 2023-07-26
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
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># fsck

Comprueba la integridad de un sistema de archivos o los repara. El sistema de ficheros debe estar desmontado en el momento de ejecutar el comando.
Es una envoltura que llama a `fsck_hfs`, `fsck_apfs`, `fsck_msdos`, `fsck_exfat`, y `fsck_udf` según sea necesario.
Más información: <https://ss64.com/osx/fsck.html>.

- Comprueba el sistema de ficheros `/dev/sdX`, informando de cualquier bloque dañado:

`fsck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Comprueba el sistema de ficheros `/dev/sdX` sólo si está limpio, informando de los bloques dañados y dejando que el usuario elija interactivamente si repara cada uno de ellos:

`fsck -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Comprueba el sistema de archivos `/dev/sdX` sólo si está limpio, informando de los bloques dañados y reparándolos automáticamente:

`fsck -fy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Comprueba el sistema de archivos `/dev/sdX`, informando si se ha desmontado correctamente:

`fsck -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
