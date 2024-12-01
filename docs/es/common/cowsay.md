---
layout: page
title: common/cowsay (español)
description: "Imprime arte ASCII (por defecto una vaca) diciendo o pensando algo."
content_hash: 54d3099675a336f16b807d1a0d3ab9451cd918e1
last_modified_at: 2024-12-01
related_topics:
  - title: English version
    url: /en/common/cowsay.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/cowsay.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cowsay.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cowsay.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cowsay

Imprime arte ASCII (por defecto una vaca) diciendo o pensando algo.
Más información: <https://github.com/tnalpgge/rank-amateur-cowsay>.

- Imprime una vaca ASCII diciendo "hola, mundo":

`cowsay "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hola, mundo</span>`"`

- Imprime una vaca ASCII diciendo texto de `stdin`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hola, mundo</span>`" | cowsay`

- Lista todos los tipos de arte disponibles:

`cowsay -l`

- Imprime el arte ASCII especificado diciendo "hola, mundo":

`cowsay -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arte</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hola, mundo</span>`"`

- Imprime un pensamiento triste de una vaca ASCII:

`cowthink -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Solo soy una vaca, no una gran pensadora...</span>`"`

- Imprime una vaca ASCII con ojos personalizados diciendo "hola, mundo":

`cowsay -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caracteres</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hola, mundo</span>`"`
