---
layout: page
title: linux/genisoimage (português (Brasil))
description: "Programa de pré-masterização para gerar sistemas de arquivos híbridos ISO9660/Joliet/HFS."
content_hash: f8cd33eec1dd64e111b4180ea297462923fe4271
last_modified_at: 2024-09-18
related_topics:
  - title: English version
    url: /en/linux/genisoimage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# genisoimage

Programa de pré-masterização para gerar sistemas de arquivos híbridos ISO9660/Joliet/HFS.
Mais informações: <https://manned.org/genisoimage.1>.

- Cria uma imagem ISO a partir do diretório de origem fornecido:

`genisoimage -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minha_imagem.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório_origem</span>

- Cria uma imagem ISO com arquivos maiores que 2GiB, relatando um tamanho aparente menor para o sistema de arquivos ISO9660:

`genisoimage -o -allow-limited-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minha_imagem.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório_origem</span>
