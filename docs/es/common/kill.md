---
layout: page
title: common/kill (español)
description: "Envía una señal a un proceso, usualmente relacionada con detener el proceso."
content_hash: 3658c6038b8261fe26a6caf946f7f79d9532b845
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/kill.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/kill.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/kill.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/kill.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/kill.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kill

Envía una señal a un proceso, usualmente relacionada con detener el proceso.
Todas las señales a excepción de SIGKILL y SIGSTOP pueden ser interceptadas por el proceso para efectuar una salida limpia.
Más información: <https://manned.org/kill.1posix>.

- Termina un programa usando la señal SIGTERM (terminar) predeterminada:

`kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_del_proceso</span>

- Lista todas las señales disponibles (para utilizarlas sin el prefijo `SIG`):

`kill -l`

- Termina un programa usando la señal SIGHUP (hang up/colgar). Muchos programas residentes (daemons) se recargarán en lugar de terminar:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|HUP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_del_proceso</span>

- Termina un programa usando la señal SIGINT (interrumpir). Esto es normalmente iniciado por el usuario al presionar `Ctrl + C`:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|INT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_del_proceso</span>

- Señala al sistema operativo terminar inmediatamente un programa (el cual no tiene oportunidad de capturar la señal):

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9|KILL</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_del_proceso</span>

- Señala al sistema operativo pausar un programa hasta que la señal SIGCONT (continuar) sea recibida:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17|STOP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_del_proceso</span>

- Envía una señal `SIGUSR1` a todos los procesos con un GID (id de grupo) dado:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGUSR1</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_grupo</span>
