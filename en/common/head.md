---
layout: page
title: common/head (English)
description: "Output the first part of files."
content_hash: 2b8962bfc67d7b0fd2981485e52aee29f0d1913d
related_topics:
  - title: Deutsch version
    url: /de/common/head.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/head.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/head.html
    icon: bi bi-globe
---
# head

Output the first part of files.
More information: <https://www.gnu.org/software/coreutils/head>.

- Output the first few lines of a file:

`head --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Output the first few bytes of a file:

`head --bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Output everything but the last few lines of a file:

`head --lines -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Output everything but the last few bytes of a file:

`head --bytes -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
