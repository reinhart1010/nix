---
layout: page
title: linux/csplit (English)
description: "Split a file into pieces."
content_hash: 436dc59203fcc56f89991a22c9b1644983bdf92e
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/linux/csplit.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/csplit.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/csplit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csplit

Split a file into pieces.
This generates files named "xx00", "xx01", and so on.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/csplit-invocation.html>.

- Split a file at lines 5 and 23:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` 5 23`

- Split a file every 5 lines (this will fail if the total number of lines is not divisible by 5):

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` 5 {*}`

- Split a file every 5 lines, ignoring exact-division error:

`csplit -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` 5 {*}`

- Split a file at line 5 and use a custom prefix for the output files:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` 5 -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>

- Split a file at a line matching a regular expression:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`/`
