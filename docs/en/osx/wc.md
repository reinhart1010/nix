---
layout: page
title: osx/wc (English)
description: "Count lines, words, or bytes."
content_hash: 87f07430f0c701dad876408997ecb61814ff28d0
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/wc.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/wc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wc

Count lines, words, or bytes.
More information: <https://keith.github.io/xcode-man-pages/wc.1.html>.

- Count lines in file:

`wc -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Count words in file:

`wc -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Count characters (bytes) in file:

`wc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Count characters in file (taking multi-byte character sets into account):

`wc -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Use `stdin` to count lines, words and characters (bytes) in that order:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find .</span>` | wc`
