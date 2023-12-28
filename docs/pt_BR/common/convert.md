---
layout: page
title: common/convert (português (Brasil))
description: "Ferramenta de conversão de imagens da ImageMagick."
content_hash: 4c17ac483f0f9b6c374bdc528813a27da4677fdd
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/common/convert.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/convert.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/convert.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/convert.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/convert.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># convert

Ferramenta de conversão de imagens da ImageMagick.
Mais informações: <https://imagemagick.org/script/convert.php>.

- Converte uma imagem do formato JPG para o formato PNG:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem.png</span>

- Escala uma imagem para 50% do seu tamanho original:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem.png</span>` -resize 50% `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nova_imagem.png</span>

- Escala uma imagem, mantendo as suas proporções originais, para uma dimensão máxima de 640x480:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem.png</span>` -resize 640x480 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nova_imagem.png</span>

- Junta várias imagens horizontalmente:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem3.png</span>` +append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nova_imagem.png</span>

- Cria um GIF a partir de uma série de imagens, com um intervalo de 100ms entre elas:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem3.png</span>` -delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nova_imagem.gif</span>

- Cria uma nova imagem de tamanho 800x600 com apenas um fundo sólido vermelho:

`convert -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">800x600</span>` "xc:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#ff0000</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem.png</span>
