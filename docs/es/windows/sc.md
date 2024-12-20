---
layout: page
title: windows/sc (español)
description: "Comunicación con el Administrador de Control de Servicios y los servicios."
content_hash: e7aac3326110d7ca1459c671da25cc064ea784e6
last_modified_at: 2024-12-20
related_topics:
  - title: English version
    url: /en/windows/sc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/sc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/sc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sc

Comunicación con el Administrador de Control de Servicios y los servicios.
Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/sc-query>.

- Muestra el estado de un servicio (al no nombrar un servicio se listan todos los servicios):

`sc.exe query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_servicio</span>

- Inicia un servicio asincrónicamente:

`sc.exe create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_servicio</span>` binpath= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta\al\binario_del_servicio</span>

- Detiene un servicio asincrónicamente:

`sc.exe delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_servicio</span>

- Establece el tipo de servicio:

`sc.exe config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_servicio</span>` type= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo_de_servicio</span>
