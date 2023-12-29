---
layout: page
title: linux/fold (English)
description: "Folds long lines for fixed-width output devices."
content_hash: ef67959370bd121c02931b7990311c5e12ea8610
last_modified_at: 2023-12-29
tldri18n_status: 2
---
# fold

Folds long lines for fixed-width output devices.
More information: <https://www.gnu.org/software/coreutils/fold>.

- Fold lines in a fixed width:

`fold --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Count width in bytes (the default is to count in columns):

`fold --bytes --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width_in_bytes</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Break the line after the rightmost blank within the width limit:

`fold --spaces --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
