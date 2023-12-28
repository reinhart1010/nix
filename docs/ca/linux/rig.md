---
layout: page
title: linux/rig (català)
description: "Utilitat per generar un nom, cognom, carrer i número, en conjunt d'una ubicació geogràfica consistent (un conjunt vàlid de ciutat, estat i codi postal)."
content_hash: d4ff7e9e2ad8069b459f0b8083a29d9175c57dd0
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/rig.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/rig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rig

Utilitat per generar un nom, cognom, carrer i número, en conjunt d'una ubicació geogràfica consistent (un conjunt vàlid de ciutat, estat i codi postal).
Més informació: <https://manned.org/rig>.

- Mostra un nom aleatori (masculí o femení) i una direcció:

`rig`

- Mostra un nom [m]asculí o [f]emení aleatori i una direcció:

`rig -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">m|f</span>

- Fa servir arxius de dades d'un directori específic (per defecte és `/usr/share/rig`):

`rig -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directori</span>

- Especifica el número d'identitats a generar:

`rig -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero</span>

- Especifica el número d'identitats femininas a generar:

`rig -f -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero</span>
