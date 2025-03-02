---
layout: page
title: linux/head (English)
description: "Output the first part of files."
content_hash: 3ef6589252d0bfbf2b48cf638b7c2b0d3849c3a7
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/head.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/head.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/head.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/head.html
    icon: bi bi-globe
tldri18n_status: 2
---
# head

Output the first part of files.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html>.

- Output the first few lines of a file:

`head --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Output the first few bytes of a file:

`head --bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Output everything but the last few lines of a file:

`head --lines -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Output everything but the last few bytes of a file:

`head --bytes -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
