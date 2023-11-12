---
layout: page
title: linux/pacman (português (Portugal))
description: "Utilitário para gerir pacotes Arch Linux."
content_hash: 918c58ab687815c2f55bab1e3f4e9cb578b90c68
last_modified_at: 2023-11-12
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
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/pacman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman

Utilitário para gerir pacotes Arch Linux.
Veja também: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
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
