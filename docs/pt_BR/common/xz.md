---
layout: page
title: common/xz (português (Brasil))
description: "Compactar ou descompactar arquivos XZ ou LZMA."
content_hash: d225e15f52c6ea89e11babc4e18c77a99763964f
last_modified_at: 2024-03-14
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

Compactar ou descompactar arquivos XZ ou LZMA.
Mais informações: <https://manned.org/xz>.

- Compacta um arquivo no formato xz:

`xz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Descompacta um arquivo no formato xz:

`xz --decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.xz</span>

- Compacta um arquivo no formato LZMA:

`xz --format=lzma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Descompacta um arquivo no formato LZMA:

`xz --decompress --format=lzma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.lzma</span>

- Descompacta um arquivo e escrever a saída no terminal (implica `--keep`):

`xz --decompress --stdout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.xz</span>

- Compacta um arquivo sem apagar o arquivo original:

`xz --keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Compacta um arquivo utilizando a compactação mais rápida:

`xz -0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Compacta um arquivo utilizando a compactação mais eficiente:

`xz -9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
