---
layout: page
title: common/rev (English)
description: "Reverse a line of text or a file."
content_hash: 29ec3d17c2cae362909cee89eabfef142a831f5d
last_modified_at: 2024-10-10
related_topics:
  - title: Deutsch version
    url: /de/common/rev.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/rev.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rev

Reverse a line of text or a file.
More information: <https://manned.org/rev>.

- Reverse text typed into terminal:

`rev`

- Reverse the text string "hello":

`echo "hello" | rev`

- Reverse an entire file and print to `stdout`:

`rev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Use '\0' as a line separator (zero termination):

`rev -0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display help:

`rev -h`

- Display version:

`rev -V`
