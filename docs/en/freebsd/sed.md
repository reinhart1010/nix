---
layout: page
title: freebsd/sed (English)
description: "Edit text in a scriptable manner."
content_hash: 23a4862305eedcd60c977912438ba3a5b6ffff67
last_modified_at: 2024-01-01
tldri18n_status: 2
---
# sed

Edit text in a scriptable manner.
See also: `awk`, `ed`.
More information: <https://www.freebsd.org/cgi/man.cgi?sed>.

- Replace all `apple` (basic regex) occurrences with `mango` (basic regex) in all input lines and print the result to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed 's/apple/mango/g'`

- Execute a specific script [f]ile and print the result to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sed</span>

- Delay opening each file until a command containing the related `w` function or flag is applied to a line of input:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -fa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sed</span>

- Replace all `apple` (extended regex) occurrences with `APPLE` (extended regex) in all input lines and print the result to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -E 's/(apple)/\U\1/g'`

- Print just a first line to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -n '1p'`

- Replace all `apple` (basic regex) occurrences with `mango` (basic regex) in a specific file and overwrite the original file in place:

`sed -i 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
