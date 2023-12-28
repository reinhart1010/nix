---
layout: page
title: common/xz (português (Brasil))
description: "Compactar ou descompactar arquivos com a extensão .xz ou .lzma."
content_hash: 1535083283d41dcd87ca75502ca5008128407400
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/xz.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/xz.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xz

Compactar ou descompactar arquivos com a extensão .xz ou .lzma.
Mais informações: <https://manned.org/xz>.

- Compacta um arquivo no formato xz:

`xz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Descompacta um arquivo no formato xz:

`xz -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.xz</span>

- Compacta um arquivo no formato lzma:

`xz --format=lzma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Descompacta um arquivo no formato lzma:

`xz -d --format=lzma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.lzma</span>

- Descompacta um arquivo e escrever a saída no terminal:

`xz -dc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.xz</span>

- Compacta um arquivo sem apagar o arquivo original:

`xz -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Compacta um arquivo utilizando a compactação mais rápida:

`xz -0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Compacta um arquivo utilizando a compactação mais eficiente:

`xz -9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>
