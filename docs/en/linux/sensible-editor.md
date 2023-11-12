---
layout: page
title: linux/sensible-editor (English)
description: "Open the default editor."
content_hash: ab085685ef3a5121775eab605b64b82ce893094b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# sensible-editor

Open the default editor.
More information: <https://manned.org/sensible-editor>.

- Open a file in the default editor:

`sensible-editor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a file in the default editor, with the cursor at the end of the file:

`sensible-editor + `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a file in the default editor, with the cursor at the beginning of line 10:

`sensible-editor +10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open 3 files in vertically split editor windows at the same time:

`sensible-editor -O3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 path/to/file3</span>
