---
layout: page
title: common/fc-list (español)
description: "Lista las fuentes disponibles instaladas en el sistema."
content_hash: aeee7a295f09eefc2869675c1e229421a8f83d68
last_modified_at: 2025-01-05
related_topics:
  - title: English version
    url: /en/common/fc-list.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/fc-list.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fc-list.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/fc-list.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fc-list

Lista las fuentes disponibles instaladas en el sistema.
Más información: <https://manned.org/fc-list>.

- Devuelve una lista de las fuentes instaladas en su sistema:

`fc-list`

- Devuelve una lista de las fuentes instaladas con el nombre dado:

`fc-list | grep '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DejaVu Serif</span>`'`

- Devuelve el número de fuentes instaladas con el nombre dado:

`fc-list | wc -l`

- Devuelve una lista de las fuentes instaladas que soportan el idioma basado en su código de idioma:

`fc-list :lang=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jp</span>

- Devuelve una lista de las fuentes instaladas que contienen el glifo especificado por su código Unicode:

`fc-list :charset=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f303</span>
