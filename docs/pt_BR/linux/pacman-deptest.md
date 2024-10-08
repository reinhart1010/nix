---
layout: page
title: linux/pacman-deptest (português (Brasil))
description: "Verifica cada dependência especificada e retorna uma lista de dependências que não estão satisfeitas atualmente no sistema."
content_hash: 519c954c96ad091dab220a9f087ca4d9d92a9a93
last_modified_at: 2024-10-08
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-deptest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --deptest

Verifica cada dependência especificada e retorna uma lista de dependências que não estão satisfeitas atualmente no sistema.
Veja também: `pacman`.
Mais informações: <https://manned.org/pacman.8>.

- Imprime os nomes de pacotes das dependências que não estão instaladas:

`pacman --deptest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote1 pacote2 ...</span>

- Verifica se o pacote instalado satisfaz a versão mínima dada:

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>=5</span>`"`

- Verifica se uma versão posterior de um pacote está instalado:

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>5</span>`"`

- Exibe ajuda:

`pacman --deptest --help`
