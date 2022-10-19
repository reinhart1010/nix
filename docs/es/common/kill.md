---
layout: page
title: common/kill (español)
description: "Envía una señal a un proceso, usualmente relacionado a detener el proceso."
content_hash: 6892457a6168e62d09e7a48d133a4bf8da56b2ba
related_topics:
  - title: English version
    url: /en/common/kill.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/kill.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/kill.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># kill

Envía una señal a un proceso, usualmente relacionado a detener el proceso.
kill envia una señal para terminar uno o un grupo de procesos.
Más información: <https://manned.org/kill>.

- Termina un programa usando la señal SIGTERM (terminar) por defecto:

`kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_del_proceso</span>

- Lista todas las señales disponibles (para ser utilizadas sin el prefijo `SIG`):

`kill -l`

- Termina una tarea en segundo plano:

`kill %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_de_tarea</span>

- Termina un programa usando la señal SIGHUP (hang up/colgar). Muchos programas residentes se recargarán en lugar de terminar:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|HUP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_del_proceso</span>

- Termina un programa usando la señal SIGINT (interrumpir). Esto es normalmente iniciado por el usuario presionando `Ctrl + C`:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|INT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_del_proceso</span>

- Señala al sistema operativo para terminar inmediatamente un programa (el cual no tiene oportunidad de capturar la señal):

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9|KILL</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_del_proceso</span>

- Señala al sistema operativo para pausar un programa hasta que la señal SIGCONT ("continuar") es recibida:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17|STOP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_del_proceso</span>

- Envia una señal `SIGUSR1` a todos los procesos con un GID (id de grupo) dado:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGUSR1</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_de_grupo</span>
