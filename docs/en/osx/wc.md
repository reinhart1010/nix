---
layout: page
title: osx/wc (English)
description: "Count lines, words, or bytes."
content_hash: 4f830487c30965fab30a03ec4d2a997de4a6c6b4
last_modified_at: 2023-08-09
related_topics:
  - title: polski version
    url: /pl/osx/wc.html
    icon: bi bi-globe
---
# wc

Count lines, words, or bytes.
More information: <https://ss64.com/osx/wc.html>.

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
