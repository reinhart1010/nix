---
layout: page
title: linux/sed (English)
description: "Edit text in a scriptable manner."
content_hash: 468701549d75a3eead13a2b58bdbef3dd95d97d7
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

Edit text in a scriptable manner.
See also: `awk`, `ed`.
More information: <https://www.gnu.org/software/sed/manual/sed.html>.

- Replace all `apple` (basic regex) occurrences with `mango` (basic regex) in all input lines and print the result to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed 's/apple/mango/g'`

- Execute a specific script [f]ile and print the result to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sed</span>

- Replace all `apple` (extended regex) occurrences with `APPLE` (extended regex) in all input lines and print the result to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -E 's/(apple)/\U\1/g'`

- Print just a first line to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -n '1p'`

- Replace all `apple` (basic regex) occurrences with `mango` (basic regex) in a specific file and overwrite the original file in place:

`sed -i 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
