---
layout: page
title: common/xz (português (Brasil))
description: "Compactar ou descompactar arquivos com a extensão .xz ou .lzma."
content_hash: 67c072505ce5e067518084835369f47a74c3fa39
related_topics:
  - title: English version
    url: /en/common/xz.html
    icon: bi bi-globe
---
# xz

Compactar ou descompactar arquivos com a extensão .xz ou .lzma.
Mais informações: <https://tukaani.org/xz/format.html>.

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
