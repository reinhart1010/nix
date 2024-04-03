---
layout: page
title: linux/showkey (español)
description: "Muestra el código de las teclas pulsadas en el teclado, útil para depurar problemas relacionados con el teclado y la reasignación de teclas."
content_hash: 1de1ace1c85c451495b1f076f09f0df40e3a279a
last_modified_at: 2024-04-03
related_topics:
  - title: English version
    url: /en/linux/showkey.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/showkey.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># showkey

Muestra el código de las teclas pulsadas en el teclado, útil para depurar problemas relacionados con el teclado y la reasignación de teclas.
Más información: <https://manned.org/showkey>.

- Visualiza códigos de teclas en decimal:

`sudo showkey`

- Visualiza códigos de ra[s]treo en hexadecimal:

`sudo showkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--scancodes</span>

- Muestra códigos de teclas en decimal (por defecto):

`sudo showkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-k|--keycodes</span>

- Muestra los códigos en [a]SCII, decimal y hexadecimal:

`sudo showkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--ascii</span>

- Sal del programa:

`Ctrl + d`
