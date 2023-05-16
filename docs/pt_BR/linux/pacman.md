---
layout: page
title: linux/pacman (português (Brasil))
description: "Utilitário de Arch Linux para gerenciamento de pacotes."
content_hash: 2c5317657c42be2c615fccf052f7623edf4bac7b
last_modified_at: 2023-05-16
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
  - title: Indonesia version
    url: /id/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/pacman.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman.html
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
Veja também: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`,  `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
Mais informações: <https://man.archlinux.org/man/pacman.8>.

- Sincroniza e atualiza todos os pacotes:

`sudo pacman -Syu`

- Instala um novo pacote:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Remove um pacote e suas dependências:

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Procura no banco de dados de pacotes por uma expressão regular ou palavra-chave:

`pacman -Ss "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrao_buscado</span>`"`

- Lista pacotes instalados e versões:

`pacman -Q`

- Lista apenas os pacotes explicitamente instalados e versões:

`pacman -Qe`

- Lista pacotes órfãos (instalado como dependência mas não requerido por qualquer pacote):

`pacman -Qtdq`

- Esvazia completamente o cache do pacman:

`sudo pacman -Scc`
