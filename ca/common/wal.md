---
layout: page
title: common/wal (català)
description: "Una eina per crear esquemes de colors basats en els colors dominants del fons de pantalla."
content_hash: b96b52940e66752ba0287efd8d2245c2fd78f5da
related_topics:
  - title: English version
    url: /en/common/wal.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># wal

Una eina per crear esquemes de colors basats en els colors dominants del fons de pantalla.
Més informació: <https://github.com/dylanaraps/pywal>.

- Preveure l'esquema de colors:

`wal --preview `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imatge.png</span>

- Crear esquema de colors:

`wal -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imatge.png</span>

- Crea un esquema de colors clars:

`wal -il `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imatge.png</span>

- No canvia el fons de pantalla:

`wal -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imatge.png</span>

- No canvia els colors de la terminal:

`wal -is `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imatge.png</span>

- Restableix l'anterior fonts de pantalla i esquema de colors generat:

`wal -R`
