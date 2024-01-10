---
layout: page
title: linux/genisoimage (português (Brasil))
description: "Programa de pré-masterização para gerar sistemas de arquivos híbridos ISO9660/Joliet/HFS."
content_hash: e26e5dae0267e6bfc81f17102d8e8971a4b7c370
last_modified_at: 2024-01-10
related_topics:
  - title: English version
    url: /en/linux/genisoimage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# genisoimage

Programa de pré-masterização para gerar sistemas de arquivos híbridos ISO9660/Joliet/HFS.
Mais informações: <https://manpages.debian.org/latest/genisoimage/genisoimage.1.en.html>.

- Cria uma imagem ISO a partir do diretório de origem fornecido:

`genisoimage -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minha_imagem.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório_origem</span>

- Cria uma imagem ISO com arquivos maiores que 2GiB, relatando um tamanho aparente menor para o sistema de arquivos ISO9660:

`genisoimage -o -allow-limited-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minha_imagem.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório_origem</span>
