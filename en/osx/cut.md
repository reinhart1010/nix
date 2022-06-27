---
layout: page
title: osx/cut (English)
description: "Cut out fields from stdin or files."
content_hash: fb840f3144339d2b3628389a69a9338fa879acc7
related_topics:
  - title: русский version
    url: /ru/osx/cut.html
    icon: bi bi-globe
---
# cut

Cut out fields from stdin or files.
More information: <https://manned.org/man/freebsd-13.0/cut.1>.

- Print a specific character/field range of each line:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | cut -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c|f</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|1,10|1-10|1-|-10</span>

- Print a range of each line with a specific delimiter:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | cut -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>`" -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Print a range of each line of a specific file:

`cut -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
