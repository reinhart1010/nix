---
layout: page
title: common/alex (English)
description: "A tool that catches insensitive, inconsiderate writing."
content_hash: 5a1c2759d0b53faf3617947de17234c5469fb3a0
related_topics:
  - title: italiano version
    url: /it/common/alex.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alex.html
    icon: bi bi-globe
---
# alex

A tool that catches insensitive, inconsiderate writing.
It helps you find gender favouring, polarising, race related, religion inconsiderate, or other unequal phrasing in text.
More information: <https://github.com/get-alex/alex>.

- Analyze text from stdin:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">His network looks good</span>` | alex --stdin`

- Analyze all files in the current directory:

`alex`

- Analyze a specific file:

`alex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">textfile.md</span>

- Analyze all Markdown files except `example.md`:

`alex *.md !`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.md</span>
