---
layout: page
title: common/cmp (English)
description: "Compare two files byte by byte."
content_hash: 07b1a53b6ed89a778160b0864daf754f3aaf67fc
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

- Find the byte and line number of the first difference between two files:

`cmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Find the byte number and differing bytes of every difference:

`cmp -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>
