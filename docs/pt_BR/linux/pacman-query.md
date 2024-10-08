---
layout: page
title: linux/pacman-query (português (Brasil))
description: "Utilitário de Arch Linux para gerenciamento de pacotes."
content_hash: 696f064c04d37bb47cb5d500233d100c1d748f27
last_modified_at: 2024-10-08
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-query.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-query.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-query.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-query.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-query.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-query.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --query

Utilitário de Arch Linux para gerenciamento de pacotes.
Veja também: `pacman`.
Mais informações: <https://manned.org/pacman.8>.

- Lista pacotes instalados e suas versões:

`pacman --query`

- Lista apenas pacotes e versões que foram instalados explicitamente:

`pacman --query --explicit`

- Procura qual pacote possui um arquivo:

`pacman --query --owns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Exibe informações sobre um pacote instalado:

`pacman --query --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Lista arquivos fornecidos por um pacote:

`pacman --query --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Lista pacotes órfãos (instalados como dependências, mas que nenhum pacote instalado necessita):

`pacman --query --unrequired --deps --quiet`

- Lista pacotes instalados não encontrados nos repositórios:

`pacman --query --foreign`

- Lista pacotes desatualizados:

`pacman --query --upgrades`
