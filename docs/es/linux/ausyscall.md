---
layout: page
title: linux/ausyscall (español)
description: "Mapea los nombres y números de las llamadas al sistema (syscalls)."
content_hash: 9cd62baf83c3cc21e75783f30692b43a863528a3
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/ausyscall.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/ausyscall.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ausyscall

Mapea los nombres y números de las llamadas al sistema (syscalls).
Más información: <https://manned.org/ausyscall>.

- Muestra el número de llamada al sistema de una llamada específica:

`ausyscall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>

- Muestra el nombre de una llamada al sistema específico a partir de su número:

`ausyscall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_llamada_al_sistema</span>

- Muestra todas las llamadas al sistema para una arquitectura específica:

`ausyscall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquitectura</span>` --dump`
