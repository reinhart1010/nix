---
layout: page
title: common/transmission-create (português (Brasil))
description: "Cria arquivos BitTorrent `.torrent`."
content_hash: a2a4c813fc116cbd23b74db1f5e655289472e35d
last_modified_at: 2024-10-05
related_topics:
  - title: English version
    url: /en/common/transmission-create.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/transmission-create.html
    icon: bi bi-globe
tldri18n_status: 2
---
# transmission-create

Cria arquivos BitTorrent `.torrent`.
Veja também: `transmission`.
Mais informações: <https://manned.org/transmission-create>.

- Cria um torrent com 2048 KB como o tamanho da parte:

`transmission-create -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/exemplo.torrent</span>` --tracker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_anuncio_tracker</span>` --piecesize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2048</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório</span>

- Cria um torrent privado com um tamanho de parte de 2048 KB:

`transmission-create -p -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/exemplo.torrent</span>` --tracker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_anuncio_tracker</span>` --piecesize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2048</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório</span>

- Cria um torrent com um comentário:

`transmission-create -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/exemplo.torrent</span>` --tracker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_rastreador1</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comentário</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório</span>

- Cria um torrent com vários rastreadores:

`transmission-create -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/exemplo.torrent</span>` --tracker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_rastreador1</span>` --tracker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_rastreador2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório</span>

- Exibe a página de ajuda:

`transmission-create --help`
