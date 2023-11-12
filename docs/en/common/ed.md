---
layout: page
title: common/ed (English)
description: "The original Unix text editor."
content_hash: 8b25fe6a4a1ccfe8058b01d847bb116f8a6ddf77
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/ed.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ed.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ed

The original Unix text editor.
See also: `awk`, `sed`.
More information: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Start an interactive editor session with an empty document:

`ed`

- Start an interactive editor session with an empty document and a specific prompt:

`ed --prompt='> '`

- Start an interactive editor session with user-friendly errors:

`ed --verbose`

- Start an interactive editor session with an empty document and without diagnostics, byte counts and '!' prompt:

`ed --quiet`

- Start an interactive editor session without exit status change when command fails:

`ed --loose-exit-status`

- Edit a specific file (this shows the byte count of the loaded file):

`ed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Replace a string with a specific replacement for all lines:

`,s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replacement</span>`/g`
