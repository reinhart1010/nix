---
layout: page
title: linux/asciiart (português (Brasil))
description: "Converte imagens para ASCII."
content_hash: 081f7ea1313475e4948c85afb1e5c865f389e596
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/linux/asciiart.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/asciiart.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/asciiart.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/asciiart.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/asciiart.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asciiart

Converte imagens para ASCII.
Mais informações: <https://github.com/nodanaonlyzuul/asciiart>.

- Lê uma imagem de um arquivo e imprime em ASCII:

`asciiart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/imagem.jpg</span>

- Lê uma imagem de uma URL e imprime em ASCII:

`asciiart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.exemplo.com/imagem.jpg</span>

- Escolha a largura da saída (o padrão é 100):

`asciiart --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/imagem.jpg</span>

- Imprime com cor:

`asciiart --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/imagem.jpg</span>

- Escolha o formato de saída (o padrão é text):

`asciiart --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text|html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/imagem.jpg</span>

- Inverte o mapeamento dos caracteres:

`asciiart --invert-chars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/imagem.jpg</span>
