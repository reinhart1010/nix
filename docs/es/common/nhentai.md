---
layout: page
title: common/nhentai (español)
description: "Descarga doujinshis de nhentai."
content_hash: ca8fa47a209d9acf2ace6f142b479d83a181ee86
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/nhentai.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nhentai

Descarga doujinshis de nhentai.
Más información: <https://github.com/RicterZ/nhentai>.

- Establece cookies:

`nhentai --cookie "csrftoken=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TOKEN</span>`; sessionid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ID</span>`"`

- Descarga un doujin específico:

`nhentai --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número</span>

- Descarga la primera página de tus favoritos:

`nhentai --favorites --download --delay 1`

- Descarga páginas específicas de tus favoritos:

`nhentai --favorites --pages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">página_inicial</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">página_final</span>` --download --delay 1`
