---
layout: page
title: osx/automountd (español)
description: "Un daemon de montaje/desmontaje automático para `autofs`. Iniciado bajo demanda por `launchd`."
content_hash: c649bda04fa7e6584728dc9cbdd5c398bf380260
last_modified_at: 2023-11-28
related_topics:
  - title: English version
    url: /en/osx/automountd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/automountd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/automountd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># automountd

Un daemon de montaje/desmontaje automático para `autofs`. Iniciado bajo demanda por `launchd`.
No debe ser invocado manualmente.
Más información: <https://www.manpagez.com/man/8/automountd/>.

- Inicia el daemon:

`automountd`

- Registra más detalles en `syslog`:

`automountd -v`
