---
layout: page
title: linux/csplit (English)
description: "Split a file into pieces."
content_hash: 97587e35b3059b0a757af932f03529feb6c5018c
last_modified_at: 2022-12-04
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/csplit.html
    icon: bi bi-globe
---
# csplit

Split a file into pieces.
This generates files named "xx00", "xx01", and so on.
More information: <https://www.gnu.org/software/coreutils/csplit>.

- Split a file at lines 5 and 23:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">23</span>

- Split a file every 5 lines (this will fail if the total number of lines is not divisible by 5):

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` {*}`

- Split a file every 5 lines, ignoring exact-division error:

`csplit -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` {*}`

- Split a file at line 5 and use a custom prefix for the output files:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>

- Split a file at a line matching a regular expression:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`/`
