---
layout: page
title: common/wal (català)
description: "Una eina per crear esquemes de colors basats en els colors dominants del fons de pantalla."
content_hash: afa97fd9b6e6d003dec9c2d5978059a75afedad1
related_topics:
  - title: English version
    url: /en/common/wal.html
    icon: bi bi-globe
---
# wal

Una eina per crear esquemes de colors basats en els colors dominants del fons de pantalla.
Més informació: <https://github.com/dylanaraps/pywal>.

- Preveure l'esquema de colors:

`wal --preview `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imatge.png</span>

- Crear esquema de colors:

`wal -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imatge.png</span>

- Crea un esquema de colors clars:

`wal -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imatge.png</span>` -l`

- No canvia el fons de pantalla:

`wal -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imatge.png</span>` -n`

- No canvia els colors de la terminal:

`wal -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imatge.png</span>` -s`

- Restableix l'anterior fonts de pantalla i esquema de colors generat:

`wal -R`
