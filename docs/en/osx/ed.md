---
layout: page
title: osx/ed (English)
description: "The original Unix text editor."
content_hash: 041d3ece8549d5034ed5f4cec21f02213d018bd9
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ed

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
