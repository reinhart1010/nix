---
layout: page
title: common/stdbuf (English)
description: "Run a command with modified buffering operations for its standard streams."
content_hash: 7e2e8d07d01002a17f0cbcab688affb7b1db695b
last_modified_at: 2025-03-02
related_topics:
  - title: हिन्दी version
    url: /hi/common/stdbuf.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/stdbuf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/stdbuf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stdbuf

Run a command with modified buffering operations for its standard streams.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/stdbuf-invocation.html>.

- Change `stdin` buffer size to 512 KiB:

`stdbuf --input=512K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Change `stdout` buffer to line-buffered:

`stdbuf --output=L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Change `stderr` buffer to unbuffered:

`stdbuf --error=0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
