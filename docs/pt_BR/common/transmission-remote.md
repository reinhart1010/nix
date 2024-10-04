---
layout: page
title: common/transmission-remote (português (Brasil))
description: "Utilitário de controle remoto para `transmission-daemon` e `transmission`."
content_hash: 8bbbce3cc099953fa231c68b81d51ab2b878b653
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/transmission-remote.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/transmission-remote.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/transmission-remote.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># transmission-remote

Utilitário de controle remoto para `transmission-daemon` e `transmission`.
Mais informações: <https://transmissionbt.com>.

- Adiciona um arquivo torrent ou link magnético para o Transmission e baixa para um diretório específico:

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torrent|url</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/diretorio_download</span>

- Altera o diretório de download padrão:

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/diretorio_download</span>

- Lista todos os torrents:

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` --list`

- Inicia os torrents 1 e 2, interrompe o torrent 3:

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,2</span>`" --start -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` --stop`

- Remove os torrents 1 e 2 e também exclui dados locais do torrent 2:

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --remove -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --remove-and-delete`

- Interrompe todos os torrents:

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all</span>` --stop`

- Move os torrents 1-10 e 15-20 para um novo diretório (que será criado se não existir):

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-10,15-20</span>`" --move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/nodo_diretorio</span>
