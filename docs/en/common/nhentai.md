---
layout: page
title: common/nhentai (English)
description: "Download doujinshis from nhentai."
content_hash: b333963964a6dc0ecab98c5060347560e551d1e7
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/nhentai.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nhentai

Download doujinshis from nhentai.
More information: <https://github.com/RicterZ/nhentai>.

- Set cookies:

`nhentai --cookie "csrftoken=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TOKEN</span>`; sessionid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ID</span>`"`

- Download a specific doujin:

`nhentai --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- Download the first page of your favorites:

`nhentai --favorites --download --delay 1`

- Download specific pages of your favorites:

`nhentai --favorites --pages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start_page</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end_page</span>` --download --delay 1`
