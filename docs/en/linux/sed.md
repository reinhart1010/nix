---
layout: page
title: linux/sed (English)
description: "Edit text in a scriptable manner."
content_hash: 0e1574e27d43248516428870f023dad26f56d453
last_modified_at: 2024-01-25
related_topics:
  - title: Nederlands version
    url: /nl/linux/sed.html
    icon: bi bi-globe
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

- Replace all `apple` (extended regex) occurrences with `APPLE` (extended regex) in all input lines and print the result to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -E 's/(apple)/\U\1/g'`

- Replace all `apple` (basic regex) occurrences with `mango` (basic regex) in a specific file and overwrite the original file in place:

`sed -i 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Execute a specific script [f]ile and print the result to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sed</span>

- Print just the first line to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -n '1p'`

- [d]elete the first line of a file:

`sed -i 1d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file</span>

- [i]nsert a new line at the first line of a file:

`sed -i '1i\your new line text\' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file</span>
