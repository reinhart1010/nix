---
layout: page
title: osx/ed (English)
description: "The original Unix text editor."
content_hash: 041d3ece8549d5034ed5f4cec21f02213d018bd9
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/ed.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/ed.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/osx/ed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ed

The original Unix text editor.
See also: `awk`, `sed`.
More information: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Start an interactive editor session with an empty document:

`ed`

- Start an interactive editor session with an empty document and a specific [p]rompt:

`ed -p '> '`

- Start an interactive editor session with an empty document and without diagnostics, byte counts and '!' prompt:

`ed -s`

- Edit a specific file (this shows the byte count of the loaded file):

`ed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Replace a string with a specific replacement for all lines:

`,s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replacement</span>`/g`
