---
layout: page
title: common/tee (English)
description: "Read from `stdin` and write to `stdout` and files (or commands)."
content_hash: b37d62c01aa951fdbd3ffb8acfd3016f1269a127
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/tee.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/tee.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tee.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tee.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tee

Read from `stdin` and write to `stdout` and files (or commands).
More information: <https://www.gnu.org/software/coreutils/manual/html_node/tee-invocation.html>.

- Copy `stdin` to each file, and also to `stdout`:

`echo "example" | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Append to the given files, do not overwrite:

`echo "example" | tee -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print `stdin` to the terminal, and also pipe it into another program for further processing:

`echo "example" | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/tty</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xargs printf "[%s]"</span>

- Create a directory called "example", count the number of characters in "example" and write "example" to the terminal:

`echo "example" | tee >(xargs mkdir) >(wc -c)`
