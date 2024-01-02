---
layout: page
title: common/chsh (español)
description: "Cambia el intérprete de comandos de inicio de sesión."
content_hash: 214f7f1a684591a7b53dcbf95a905cb2969c196e
last_modified_at: 2024-01-02
related_topics:
  - title: bosanski version
    url: /bs/common/chsh.html
    icon: bi bi-globe
  - title: dansk version
    url: /da/common/chsh.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/chsh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chsh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chsh.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/chsh.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chsh.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/chsh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chsh.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chsh.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/chsh.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/chsh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chsh

Cambia el intérprete de comandos de inicio de sesión.
Más información: <https://manned.org/chsh>.

- Cambia interactivamente el intérprete del usuario actual:

`chsh`

- Cambia el intérprete del usuario actual por otro específico:

`chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/intérprete</span>

- Cambia el intérprete de otro usuario:

`chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/intérprete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>

- [l]ista los intérpretes disponibles:

`chsh -l`
