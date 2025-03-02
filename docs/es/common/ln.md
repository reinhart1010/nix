---
layout: page
title: common/ln (español)
description: "Crea enlaces a archivos y directorios."
content_hash: f1604279c506aec789f92da2ca715623505e83e8
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/ln.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/ln.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ln.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ln.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ln.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ln.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ln.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ln.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ln

Crea enlaces a archivos y directorios.
Más información: <https://www.gnu.org/software/coreutils/manual/html_node/ln-invocation.html>.

- Crea un enlace simbólico a un archivo o directorio:

`ln -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/al/archivo_o_directorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/enlace_simbólico</span>

- Sobrescribe un enlace simbólico existente para que apunte a un archivo distinto:

`ln -sf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/al/nuevo_archivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/enlace_simbólico</span>

- Crea un enlace duro a un archivo:

`ln `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/al/archivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/enlace_duro</span>
