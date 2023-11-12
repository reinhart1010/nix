---
layout: page
title: osx/sed (English)
description: "Edit text in a scriptable manner."
content_hash: 32f7a72cab2dd7d5f712cda2fc62f9af48883575
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/sed.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

Edit text in a scriptable manner.
See also: `awk`, `ed`.
More information: <https://keith.github.io/xcode-man-pages/sed.1.html>.

- Replace all `apple` (basic regex) occurrences with `mango` (basic regex) in all input lines and print the result to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed 's/apple/mango/g'`

- Execute a specific script [f]ile and print the result to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script_file.sed</span>

- Replace all `apple` (extended regex) occurrences with `APPLE` (extended regex) in all input lines and print the result to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -E 's/(apple)/\U\1/g'`

- Print just a first line to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -n '1p'`

- Replace all `apple` (basic regex) occurrences with `mango` (basic regex) in a `file` and save a backup of the original to `file.bak`:

`sed -i bak 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
