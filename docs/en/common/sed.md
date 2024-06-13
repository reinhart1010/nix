---
layout: page
title: common/sed (English)
description: "Edit text in a scriptable manner."
content_hash: 3af77c9c61c243c612aae8d30be8439675183c4f
last_modified_at: 2024-06-13
related_topics:
  - title: dansk version
    url: /da/common/sed.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/sed.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/sed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

Edit text in a scriptable manner.
See also: `awk`, `ed`.
More information: <https://manned.org/sed.1posix>.

- Replace all `apple` (basic regex) occurrences with `mango` (basic regex) in all input lines and print the result to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed 's/apple/mango/g'`

- Execute a specific script [f]ile and print the result to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sed</span>

- Print just a first line to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -n '1p'`
