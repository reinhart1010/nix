---
layout: page
title: linux/pacman-files (português (Brasil))
description: "Utilitário de Arch Linux para gerenciamento de pacotes."
content_hash: be75ad8dc89daf2b366d65fcf77764de189a9191
last_modified_at: 2024-10-08
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-files.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-files.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-files.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-files.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-files.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-files.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --files

Utilitário de Arch Linux para gerenciamento de pacotes.
Veja também: `pacman`, `pkgfile`.
Mais informações: <https://manned.org/pacman.8>.

- Atualiza o banco de dados de pacotes:

`sudo pacman --files --refresh`

- Procura o pacote que possui um arquivo específico:

`pacman --files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_arquivo</span>

- Encontra o pacote que possui um arquivo específico, usando uma expressão regular:

`pacman --files --regex '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressao_regular</span>`'`

- Lista apenas os nomes de pacotes:

`pacman --files --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_arquivo</span>

- Lista os arquivos de um pacote específico:

`pacman --files --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Exibe ajuda:

`pacman --files --help`
