---
layout: page
title: linux/eyed3 (português (Brasil))
description: "Lê e manipula os metadados de arquivos MP3."
content_hash: 3ef91c3800d671b7e61e212835916def15759994
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/eyed3.html
    icon: bi bi-globe
tldri18n_status: 2
---
# eyeD3

Lê e manipula os metadados de arquivos MP3.
Mais informações: <https://eyed3.readthedocs.io>.

- Visualiza as informações de um arquivo MP3:

`eyeD3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.mp3</span>

- Define o título de um arquivo MP3:

`eyeD3 --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">titulo</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.mp3</span>

- Define o álbum de todos os arquivos MP3 de um diretório:

`eyeD3 --album "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_album</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.mp3</span>

- Define a capa do álbum para um arquivo MP3:

`eyeD3 --add-image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">capa.jpeg</span>`:FRONT_COVER: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.mp3</span>
