---
layout: page
title: linux/prime-run (español)
description: "Ejecuta un programa utilizando una tarjeta gráfica Nvidia alternativa."
content_hash: 8fd75bd541e0696d1aba09af38c0084d194ca890
last_modified_at: 2024-09-15
related_topics:
  - title: English version
    url: /en/linux/prime-run.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/prime-run.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># prime-run

Ejecuta un programa utilizando una tarjeta gráfica Nvidia alternativa.
Más información: <https://wiki.archlinux.org/title/PRIME#PRIME_render_offload>.

- Ejecuta un programa utilizando una GPU Nvidia dedicada:

`prime-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Valida si se está utilizando la tarjeta Nvidia:

`prime-run glxinfo | grep "OpenGL renderer"`
