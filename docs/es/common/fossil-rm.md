---
layout: page
title: common/fossil-rm (español)
description: "Elimina archivos o directorios del control de versiones Fossil."
content_hash: c7c6b794ece20db67949054106dfe42a913e554d
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/common/fossil-rm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/fossil-rm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/fossil-rm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fossil-rm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fossil rm

Elimina archivos o directorios del control de versiones Fossil.
Vea también: `fossil forget`.
Más información: <https://fossil-scm.org/home/help/rm>.

- Elimina un archivo o directorio del control de versiones Fossil:

`fossil rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio</span>

- Elimina un archivo o directorio del control de versiones Fossil, y también lo elimina del disco:

`fossil rm --hard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio</span>

- Añade nuevamente todos los archivos previamente eliminados y no comprometidos (uncommitted) al control de versiones Fossil:

`fossil rm --reset`
