---
layout: page
title: common/transmission-cli (português (Brasil))
description: "Um cliente BitTorrent leve e de linha de comando."
content_hash: 33a61971909f5e5dbc3132d62e4543bc2cde6add
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/transmission-cli.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/transmission-cli.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/transmission-cli.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># transmission-cli

Um cliente BitTorrent leve e de linha de comando.
Esta ferramenta foi descontinuada. Por favor, veja `transmission-remote`.
Mais informações: <https://transmissionbt.com>.

- Baixa um torrent específico:

`transmission-cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|caminho/para/arquivo</span>

- Baixa um torrent para um diretório específico:

`transmission-cli --download-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório_download</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|caminho/para/arquivo</span>

- Cria um arquivo torrent de um arquivo ou diretório específico:

`transmission-cli --new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório_origem</span>

- Especifica o limite de velocidade de download (em KB/s):

`transmission-cli --downlimit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|caminho/para/arquivo</span>

- Especifica o limite de velocidade de upload (em KB/s):

`transmission-cli --uplimit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|caminho/para/arquivo</span>

- Usa uma porta específica para conexões:

`transmission-cli --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_porta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|caminho/para/arquivo</span>

- Força criptografia para conexões com pares:

`transmission-cli --encryption-required `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|caminho/para/arquivo</span>

- Usa uma lista de bloqueio de pares formatados em Bluetack:

`transmission-cli --blocklist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_lista_bloqueio|caminho/para/lista_bloqueio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|caminho/para/arquivo</span>
