---
layout: page
title: linux/dpigs (English)
description: "Show which installed packages occupy the most space on `apt` based systems."
content_hash: cc620c56688a03f374d7ccbf831faa2711adc657
last_modified_at: 2024-10-28
tldri18n_status: 2
---
# dpigs

Show which installed packages occupy the most space on `apt` based systems.
More information: <https://manned.org/dpigs>.

- Display the N largest packages on the system:

`dpigs --lines=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>

- Use the specified file instead of the default dpkg [s]tatus file:

`dpigs --status=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display the largest [S]ource packages of binary packages installed on the system:

`dpigs --source`

- Display package sizes in [H]uman-readable format:

`dpigs --human-readable`

- Display help:

`dpigs --help`
