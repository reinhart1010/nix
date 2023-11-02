---
layout: page
title: common/xz (português (Brasil))
description: "Compactar ou descompactar arquivos com a extensão .xz ou .lzma."
content_hash: 9438ff7704e88ffa93cf2c55ee04c94dde51f1c0
last_modified_at: 2023-11-02
related_topics:
  - title: English version
    url: /en/common/xz.html
    icon: bi bi-globe
---
# xz

Compactar ou descompactar arquivos com a extensão .xz ou .lzma.
Mais informações: <https://manned.org/xz>.

- Compactar um arquivo no formato xz:

`xz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Descompactar um arquivo no formato xz:

`xz -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.xz</span>

- Compactar um arquivo no formato lzma:

`xz --format=lzma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Descompactar um arquivo no formato lzma:

`xz -d --format=lzma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.lzma</span>

- Descompactar um arquivo e escrever a saída no terminal:

`xz -dc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.xz</span>

- Compactar um arquivo sem apagar o arquivo original:

`xz -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Compactar um arquivo utilizando a compactação mais rápida:

`xz -0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Compactar um arquivo utilizando a compactação mais eficiente:

`xz -9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>
