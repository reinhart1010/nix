---
layout: page
title: common/alex (English)
description: "A tool that catches insensitive, inconsiderate writing."
content_hash: 72ed48c30570c481b42b4a9737520089a05d7421
last_modified_at: 2023-12-03
related_topics:
  - title: español version
    url: /es/common/alex.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/alex.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alex.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alex.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/alex.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/alex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alex

A tool that catches insensitive, inconsiderate writing.
It helps you find gender favouring, polarising, race related, religion inconsiderate, or other unequal phrasing in text.
More information: <https://github.com/get-alex/alex>.

- Analyze text from `stdin`:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">His network looks good</span>` | alex --stdin`

- Analyze all files in the current directory:

`alex`

- Analyze a specific file:

`alex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.md</span>

- Analyze all Markdown files except `example.md`:

`alex *.md !`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.md</span>
