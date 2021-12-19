---
layout: page
title: common/head (English)
description: "Output the first part of files."
content_hash: 84cce4929fc1b9f8d1f558fa8b7c0df8f63656dd
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

`head -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count_of_lines</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Output the first few bytes of a file:

`head -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size_in_bytes</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Output everything but the last few lines of a file:

`head -n -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count_of_lines</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Output everything but the last few bytes of a file:

`head -c -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size_in_bytes</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>
