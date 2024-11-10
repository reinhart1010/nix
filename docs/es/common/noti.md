---
layout: page
title: common/noti (español)
description: "Monitorea un proceso y activa una notificación gráfica de voz o servicio."
content_hash: 420f8fdd36bb9c2066ec3931595b644365f4f2d7
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/noti.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/noti.html
    icon: bi bi-globe
tldri18n_status: 2
---
# noti

Monitorea un proceso y activa una notificación gráfica de voz o servicio.
Más información: <https://github.com/variadico/noti>.

- Muestra una notificación cuando `tar` termina de comprimir archivos:

`noti `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tar -cjf ejemplo.tar.bz2 ejemplo/</span>

- Muestra una notificación incluso cuando se pone después del comando a vigilar:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando_a_vigilar</span>`; noti`

- Monitorea un proceso por PID y activa una notificación cuando el PID desaparece:

`noti -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_del_proceso</span>
