---
layout: page
title: osx/bless (português (Brasil))
description: "Define a capacidade de inicialização por volume e as opções de disco de inicialização. Set volume boot capability and startup disk options."
content_hash: bf83470b08b20f907ae3093faf58a3b4ff44c94b
last_modified_at: 2023-11-12
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
Mais informações: <https://ss64.com/osx/bless.html>.

- Definir um volume somente com Mac OS X ou Darwin, e criar os arquivos BootX e `boot.efi` se necessário:

`bless --folder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/Volumes/Mac OS X/System/Library/CoreServices</span>` --bootinfo --bootefi`

- Definir um volume contendo Mac OS 9 ou Mac OS X como o volume ativo:

`bless --mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/Volumes/Mac OS</span>` --setBoot`

- Definir o sistema para NetBoot e transmitir para um servidor disponível:

`bless --netboot --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bsdp://255.255.255.255</span>

- Coletar informações sobre o volume atualmente selecionado (conforme determinado pelo firmware), adequado para piping para um programa capaz de analisar listas de propriedades:

`bless --info --plist`
