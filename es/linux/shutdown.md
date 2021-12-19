---
layout: page
title: linux/shutdown (español)
description: "Detiene, apaga o reinicia la máquina."
content_hash: afd361133ae5c8fa29e3357d96191821f83f4ac2
related_topics:
  - title: English version
    url: /en/linux/shutdown.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/shutdown.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/shutdown.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/shutdown.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># shutdown

Detiene, apaga o reinicia la máquina.
Más información: <https://manned.org/shutdown.8>.

- Detiene inmediatamente:

`shutdown -H now`

- Apaga inmediatamente:

`shutdown -h now`

- Reinicia inmediatamente:

`shutdown -r now`

- Reinicia dentro de 5 minutos:

`shutdown -r +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` &`

- Apaga a la 1:00 PM (formato 24h):

`shutdown -h 13:00`

- Cancela una operación de apagado/reinicio pendiente:

`shutdown -c`
