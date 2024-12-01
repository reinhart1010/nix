---
layout: page
title: common/pamstretch (español)
description: "Escala una imagen PAM interpolando entre píxeles."
content_hash: 6b1a661ef42664232d37f6dd0e8ff8af8c3be43b
last_modified_at: 2024-12-01
related_topics:
  - title: English version
    url: /en/common/pamstretch.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pamstretch.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamstretch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamstretch

Escala una imagen PAM interpolando entre píxeles.
Vea también: `pamstretch-gen`, `pamenlarge`, `pamscale`.
Más información: <https://netpbm.sourceforge.net/doc/pamstretch.html>.

- Escala una imagen PAM por un factor entero:

`pamstretch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pam</span>

- Escala una imagen PAM por los factores especificados en las direcciones horizontales y verticales:

`pamstretch -xscale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XN</span>` -yscale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pam</span>
