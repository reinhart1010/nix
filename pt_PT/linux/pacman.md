---
layout: page
title: linux/pacman (português (Portugal))
description: "Utilitário para gerir pacotes Arch Linux."
content_hash: 82e905c1be0f112787fe35a0855f7649b45ce1f6
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pacman

Utilitário para gerir pacotes Arch Linux.
Sub comandos como `pacman sync` tem a sua própria documentação.
Mais informações: <https://man.archlinux.org/man/pacman.8>.

- Sincronizar e actualizar todos os pacotes:

`sudo pacman --sync --refresh --sysupgrade`

- Instalar um novo pacote:

`sudo pacman --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remover um pacote e todas as dependencias:

`sudo pacman --remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Procurar um pacote na base de dados por palavra chave ou expressão regular (regex):

`pacman --sync --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- Listar versão dos pactotes instalados:

`pacman --query`

- Listar versão dos pactotes instalados explicitamente:

`pacman --query --explicit`

- Listar pacotes órfãos (instalados como dependencia mas não exigidos por nenhum pacote):

`pacman --query --unrequired --deps --quiet`

- Remover memória armazenada (cache) do `pacman`:

`sudo pacman --sync --clean --clean`
