---
layout: page
title: linux/modinfo (español)
description: "Extrae información sobre un módulo del núcleo Linux."
content_hash: 72617f545f79df785da336f19039f43a8ac55747
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/modinfo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/modinfo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/modinfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# modinfo

Extrae información sobre un módulo del núcleo Linux.
Vea también: `kmod`, para otros comandos de gestión de módulos.
Más información: <https://manned.org/modinfo>.

- Lista todos los atributos de un módulo del núcleo:

`modinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">módulo_del_núcleo</span>

- Lista solo el atributo especificado:

`modinfo -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">author|description|license|parm|filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">módulo_del_núcleo</span>
