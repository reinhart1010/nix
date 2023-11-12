---
layout: page
title: common/wc (English)
description: "Count lines, words, and bytes."
content_hash: 9df9d29cff051e9f8621aea215ad1aaee86d8b89
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/wc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/wc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/wc.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/wc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/wc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wc

Count lines, words, and bytes.
More information: <https://www.gnu.org/software/coreutils/wc>.

- Count all lines in a file:

`wc --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Count all words in a file:

`wc --words `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Count all bytes in a file:

`wc --bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Count all characters in a file (taking multi-byte characters into account):

`wc --chars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Count all lines, words and bytes from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find .</span>` | wc`

- Count the length of the longest line in number of characters:

`wc --max-line-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
