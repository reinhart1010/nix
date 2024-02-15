---
layout: page
title: osx/bless (português (Brasil))
description: "Define a capacidade de inicialização por volume e as opções de disco de inicialização. Set volume boot capability and startup disk options."
content_hash: 8915ec444d03d6f254392512c61dc8551f858d28
last_modified_at: 2024-02-15
related_topics:
  - title: English version
    url: /en/osx/bless.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/bless.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bless

Define a capacidade de inicialização por volume e as opções de disco de inicialização. Set volume boot capability and startup disk options.
Mais informações: <https://keith.github.io/xcode-man-pages/bless.8.html>.

- Define um volume somente com Mac OS X ou Darwin e cria os arquivos BootX e `boot.efi` se necessário:

`bless --folder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/Volumes/Mac OS X/System/Library/CoreServices</span>` --bootinfo --bootefi`

- Define um volume contendo Mac OS 9 ou Mac OS X como o volume ativo:

`bless --mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/Volumes/Mac OS</span>` --setBoot`

- Define o sistema para NetBoot e transmite para um servidor disponível:

`bless --netboot --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bsdp://255.255.255.255</span>

- Coleta informações sobre o volume atualmente selecionado (conforme determinado pelo firmware), adequado para piping para um programa capaz de analisar listas de propriedades:

`bless --info --plist`
