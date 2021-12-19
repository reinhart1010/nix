---
layout: page
title: osx/wc (English)
description: "Count lines, words, or bytes."
content_hash: c9303e4dad6ae51ed5ef91991b0c16e46761d26c
related_topics:
  - title: polski version
    url: /pl/osx/wc.html
    icon: bi bi-globe
---
# wc

Count lines, words, or bytes.
More information: <https://www.gnu.org/software/coreutils/wc>.

- Count lines in file:

`wc -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Count words in file:

`wc -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Count characters (bytes) in file:

`wc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Count characters in file (taking multi-byte character sets into account):

`wc -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Use standard input to count lines, words and characters (bytes) in that order:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find .</span>` | wc`
