---
layout: page
title: common/strings (English)
description: "Find printable strings in an object file or binary."
content_hash: a78edec2e1c037f5b07116f820d62e03d31550b5
last_modified_at: 2023-12-19
related_topics:
  - title: Nederlands version
    url: /nl/common/strings.html
    icon: bi bi-globe
tldri18n_status: 2
---
# strings

Find printable strings in an object file or binary.
More information: <https://manned.org/strings>.

- Print all strings in a binary:

`strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Limit results to strings at least n characters long:

`strings -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Prefix each result with its offset within the file:

`strings -t d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Prefix each result with its offset within the file in hexadecimal:

`strings -t x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
