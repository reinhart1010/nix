---
layout: page
title: linux/pacman (português (Portugal))
description: "Utilitário para gerir pacotes Arch Linux."
content_hash: faa62efb323ad0188d01cce7150d9783f464945b
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
# pacman

Utilitário para gerir pacotes Arch Linux.
Sub comandos como `pacman sync` tem a sua própria documentação.
Mais informações: <https://man.archlinux.org/man/pacman.8>.

- Sincronizar e actualizar todos os pacotes:

`sudo pacman -Syu`

- Instalar um novo pacote:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remover um pacote e todas as dependencias:

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Procurar um pacote na base de dados por palavra chave ou expressão regular (regex):

`pacman -Ss "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- Listar versão dos pactotes instalados:

`pacman -Q`

- Listar versão dos pactotes instalados explicitamente:

`pacman -Qe`

- Listar pacotes órfãos (instalados como dependencia mas não exigidos por nenhum pacote):

`pacman -Qtdq`

- Remover memória armazenada (cache) do `pacman`:

`sudo pacman -Scc`
