---
layout: page
title: linux/adig (español)
description: "Muestra la información recibida de los servidores del Sistema de Nombres de Dominio (DNS)."
content_hash: 2f27fb70ea0b9091b5582e607e61f5cfd8a8c4ff
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/adig.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/adig.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/adig.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/adig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adig

Muestra la información recibida de los servidores del Sistema de Nombres de Dominio (DNS).
Más información: <https://manned.org/adig>.

- Muestra el registro A (predeterminado) desde DNS para el(los) nombre(s) de host:

`adig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Muestra salida adicional de [d]epuración:

`adig -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Conecta a un [s]ervidor DNS especificado:

`adig -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Usa un puerto TCP específico para conectarse a un servidor DNS:

`adig -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Usa un puerto UDP específico para conectarse a un servidor DNS:

`adig -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
