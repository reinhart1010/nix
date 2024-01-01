---
layout: page
title: linux/shutdown (español)
description: "Apaga y reinicia el sistema."
content_hash: f189670c9a565c83e9b95289d9a7ef8ea71034f9
last_modified_at: 2024-01-01
related_topics:
  - title: català version
    url: /ca/linux/shutdown.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/shutdown.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/shutdown.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/shutdown.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/shutdown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shutdown

Apaga y reinicia el sistema.
Más información: <https://manned.org/shutdown.8>.

- Apaga ([h]alt) inmediatamente:

`shutdown -h now`

- [r]einicia inmediatamente:

`shutdown -r now`

- [r]einicia en 5 minutos:

`shutdown -r +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` &`

- Apaga a las 01:00 pm (Usa el reloj de 24[h]):

`shutdown -h 13:00`

- [c]ancela una operación pendiente de apagado/reinicio:

`shutdown -c`
