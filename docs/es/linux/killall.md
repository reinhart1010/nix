---
layout: page
title: linux/killall (español)
description: "Envía señal de finalización a todas las instancias de un proceso por nombre (debe ser el nombre exacto)."
content_hash: 0632361bfd13b4b7d6ea39669edf769f8b8fc061
last_modified_at: 2024-12-26
related_topics:
  - title: English version
    url: /en/linux/killall.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/killall.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/killall.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/killall.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># killall

Envía señal de finalización a todas las instancias de un proceso por nombre (debe ser el nombre exacto).
Todas las señales excepto SIGKILL y SIGSTOP pueden ser interceptadas por el proceso, permitiendo una salida limpia.
Más información: <https://manned.org/killall>.

- Termina un proceso utilizando la señal SIGTERM (terminar), predeterminada:

`killall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_proceso</span>

- Lista los nombres de señal disponibles (para ser utilizados sin el prefijo 'SIG'):

`killall --list`

- Interactivamente pide confirmación antes de la terminación:

`killall -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_proceso</span>

- Termina un proceso utilizando la señal SIGINT (interrupción), que es la misma señal enviada pulsando `Ctrl + C`:

`killall -INT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_proceso</span>

- Finaliza -a la fuerza- un proceso:

`killall -KILL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_proceso</span>
