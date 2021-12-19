---
layout: page
title: linux/pacman (português (Brasil))
description: "Utilitário de Arch Linux para gerenciamento de pacotes."
content_hash: 0632a2fd623f5f677ff43a92709877c4b4a71649
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
  - title: Türkçe version
    url: /tr/linux/pacman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
---
# pacman

Utilitário de Arch Linux para gerenciamento de pacotes.
Alguns subcomandos como `pacman sync` possuem sua própria documentação de uso.
Mais informações: <https://man.archlinux.org/man/pacman.8>

- Sincroniza e atualiza todos os pacotes:

`sudo pacman --sync --refresh --sysupgrade`

- Instala um novo pacote:

`sudo pacman --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Remove um pacote e suas dependências:

`sudo pacman --remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Procura no banco de dados de pacotes por uma expressão regular ou palavra-chave:

`pacman --sync --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrao_buscado</span>`"`

- Lista pacotes instalados e versões:

`pacman --query`

- Lista apenas os pacotes explicitamente instalados e versões:

`pacman --query --explicit`

- Lista pacotes órfãos (instalado como dependência mas não requerido por qualquer pacote):

`pacman --query --unrequired --deps --quiet`

- Esvazia completamente o cache do pacman:

`sudo pacman --sync --clean --clean`
