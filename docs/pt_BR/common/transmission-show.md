---
layout: page
title: common/transmission-show (português (Brasil))
description: "Obtém informações sobre um arquivo torrent."
content_hash: 42c2f04da626c5ef486b05a4c6beb1a9d1b341a9
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/transmission-show.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/transmission-show.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/transmission-show.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># transmission-show

Obtém informações sobre um arquivo torrent.
Veja também: `transmission`.
Mais informações: <https://manned.org/transmission-show>.

- Exibe metadados para um torrent específico:

`transmission-show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.torrent</span>

- Gera um link magnético para um torrent específico:

`transmission-show --magnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.torrent</span>

- Consulta os rastreadores de um torrent e imprime o número atual de pares:

`transmission-show --scrape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.torrent</span>
