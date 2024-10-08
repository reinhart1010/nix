---
layout: page
title: linux/pacdiff (português (Brasil))
description: "Utilitário de manutenção para arquivos `.pacorig`, `.pacnew` e `.pacsave` criados pelo `pacman`."
content_hash: 78ed4c41d23931958f64b01e2c5c875db763ee29
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/linux/pacdiff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacdiff

Utilitário de manutenção para arquivos `.pacorig`, `.pacnew` e `.pacsave` criados pelo `pacman`.
Mais informações: <https://manned.org/pacdiff>.

- Reveja arquivos que precisam manutenção em modo interativo:

`pacdiff`

- Usa sudo e sudoedit para remover e mesclar arquivos:

`pacdiff --sudo`

- Reveja arquivos precisando de manutenção, criando `.bak`ups do original se você `s(O)brescrever`:

`pacdiff --sudo --backup`

- Usa um editor específico para ver e mesclar arquivos de configuração (o padrão é `vim -d`):

`DIFFPROG=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">editor</span>` pacdiff`

- Procura arquivos de configuração com `locate` ao invés de usar o banco de dados do `pacman`:

`pacdiff --locate`

- Exibe ajuda:

`pacdiff --help`
