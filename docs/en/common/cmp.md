---
layout: page
title: common/cmp (English)
description: "Compare two files byte by byte."
content_hash: b97a0c19f0b77894f4d3f10968b55c0eabce4c62
related_topics:
  - title: italiano version
    url: /it/common/cmp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cmp.html
    icon: bi bi-globe
---
# cmp

Compare two files byte by byte.
More information: <https://www.gnu.org/software/diffutils/manual/html_node/Invoking-cmp.html>.

- Output char and line number of the first difference between two files:

`cmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Output info of the first difference: char, line number, bytes, and values:

`cmp --print-bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Output the byte numbers and values of every difference:

`cmp --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Compare files but output nothing, yield only the exit status:

`cmp --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>
