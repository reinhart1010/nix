---
layout: page
title: common/ect (português (Brasil))
description: "Efficient Compression Tool."
content_hash: 4840a3656ee68228867a2c76433c5b7c6cf5a249
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ect.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ect.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ect

Efficient Compression Tool.
Otimizador de arquivos escrito em C++. Suporta arquivos do tipo `.png`, `.jpg`, `.gzip` and `.zip`.
Mais informações: <https://github.com/fhanau/Efficient-Compression-Tool>.

- Comprime um arquivo:

`ect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.png</span>

- Comprime um arquivo com level de compressão específico e multithreading (1=Mais rápido (pior), 9=Mais lento (Melhor). O padrão é 3):

`ect -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9</span>` --mt-deflate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.zip</span>

- Comprime todos os arquivos em um diretório recursivamente:

`ect -recurse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Comprime um arquivo, mantendo o tempo de modificação original:

`ect -keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.png</span>

- Comprime um arquivo, removendo metadados:

`ect -strip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.png</span>
