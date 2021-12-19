---
layout: page
title: common/apropos (français)
description: "Recherche dans les pages de manuel, par exemple pour trouver une nouvelle commande."
content_hash: 3735fafc21d2df005fda498c3bed55e0e1ff0fdd
related_topics:
  - title: Deutsch version
    url: /de/common/apropos.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/apropos.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/apropos.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/apropos.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/apropos.html
    icon: bi bi-globe
---
# apropos

Recherche dans les pages de manuel, par exemple pour trouver une nouvelle commande.
Plus d'informations : <https://manned.org/apropos>.

- Recherche par mot clé :

`apropos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression_reguliere</span>

- Recherche sans limiter la sortie à la largeur du terminal :

`apropos -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression_reguliere</span>

- Recherche les pages qui contiennent toutes les expressions données (fonction ET) :

`apropos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression_reguliere_1</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression_reguliere_2</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression_reguliere_3</span>
