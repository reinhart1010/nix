---
layout: page
title: linux/kill (español)
description: "Envía una señal a un proceso, generalmente relacionada con detener el proceso."
content_hash: 0f9a65f205b1d15514ef71e65d1e3db5ce6b9ce5
last_modified_at: 2024-12-21
related_topics:
  - title: English version
    url: /en/linux/kill.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/kill.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/kill.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/kill.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kill

Envía una señal a un proceso, generalmente relacionada con detener el proceso.
Todas las señales excepto SIGKILL y SIGSTOP pueden ser interceptadas por el proceso para realizar una salida limpia.
Más información: <https://manned.org/kill>.

- Termina un programa usando la señal SIGTERM (terminar) predeterminada:

`kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_del_proceso</span>

- Lista valores de señal y sus nombres correspondientes (para ser utilizados sin el prefijo `SIG`):

`kill -L`

- Termina un trabajo en segundo plano:

`kill %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_del_trabajo</span>

- Termina un programa usando la señal SIGHUP (hang up). Muchos servicios se recargarán en lugar de terminar:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|HUP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_del_proceso</span>

- Termina un programa usando la señal SIGINT (interrupción). Esto es normalmente iniciado por el usuario pulsando `Ctrl + C`:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|INT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_del_proceso</span>

- Indica al sistema operativo terminar inmediatamente un programa (que no tiene oportunidad de capturar la señal):

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9|KILL</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_del_proceso</span>

- Indica al sistema operativo detener un programa hasta que se reciba una señal SIGCONT ("continúa"):

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17|STOP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_del_proceso</span>

- Envía una señal `SIGUSR1` a todos los procesos con el GID dado (id del grupo):

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGUSR1</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_del_grupo</span>
