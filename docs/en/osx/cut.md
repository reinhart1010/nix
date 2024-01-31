---
layout: page
title: osx/cut (English)
description: "Cut out fields from `stdin` or files."
content_hash: 53db2f42051811ba17a1386c402d0ceaa6f8551d
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/cut.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/cut.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/cut.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/osx/cut.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cut

Cut out fields from `stdin` or files.
More information: <https://keith.github.io/xcode-man-pages/cut.1.html>.

- Print a specific character/field range of each line:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | cut -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c|f</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|1,10|1-10|1-|-10</span>

- Print a field range of each line with a specific delimiter:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | cut -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>`" -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Print a character range of each line of a specific file:

`cut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
