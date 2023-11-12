---
layout: page
title: linux/shutdown (català)
description: "Deté, apaga o reinicia la màquina."
content_hash: 031a4a5361067d8c066516b9928e84a0005c90fd
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/shutdown.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/shutdown.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/shutdown.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/shutdown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shutdown

Deté, apaga o reinicia la màquina.
Més informació: <https://manned.org/shutdown.8>.

- Deté inmediatament:

`shutdown -h now`

- Reinicia inmediatament:

`shutdown -r now`

- Reinicia després de 5 minuts:

`shutdown -r +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` &`

- Apaga a la 1:00 PM (format 24h):

`shutdown -h 13:00`

- Cancel·la una operació d'apagat/reinici pendent:

`shutdown -c`
