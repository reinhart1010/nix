---
layout: page
title: linux/genisoimage (português (Brasil))
description: "Programa de pré-masterização para gerar sistemas de arquivos híbridos ISO9660/Joliet/HFS."
content_hash: ac8d551e73e5c90f107f40dacdab56195ca6dfde
last_modified_at: 2023-04-23
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># genisoimage

Programa de pré-masterização para gerar sistemas de arquivos híbridos ISO9660/Joliet/HFS.
Mais informações: <https://manpages.debian.org/latest/genisoimage/genisoimage.1.en.html>.

- Criar uma imagem ISO a partir do diretório de origem fornecido:

`genisoimage -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minhaimagem.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório_origem}`

- Criar uma imagem ISO com arquivos maiores que 2GiB, relatando um tamanho aparente menor para o sistema de arquivos ISO9660:

`genisoimage -o -allow-limited-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minhaimagem.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório_origem</span>
