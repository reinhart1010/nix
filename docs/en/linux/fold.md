---
layout: page
title: linux/fold (English)
description: "Folds long lines for fixed-width output devices."
content_hash: 709ad29914b0b1f1e844b3a6090de7d250e4c68b
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/linux/fold.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/fold.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fold

Folds long lines for fixed-width output devices.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/fold-invocation.html>.

- Fold lines in a fixed width:

`fold --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Count width in bytes (the default is to count in columns):

`fold --bytes --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width_in_bytes</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Break the line after the rightmost blank within the width limit:

`fold --spaces --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
