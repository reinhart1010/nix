---
layout: page
title: common/kate (English)
description: "KDE's advanced text editor."
content_hash: ce939998fbab2e5ae1b6698132630f4d64d88c20
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# kate

KDE's advanced text editor.
More information: <https://kate-editor.org/>.

- Open specific files:

`kate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Open specific remote files:

`kate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/path/to/file1 https://example.com/path/to/file2 ...</span>

- Create a new editor instance even if one is already open:

`kate --new`

- Open a file with the cursor at the specific line:

`kate --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">line_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a file with the cursor at the specific line and column:

`kate --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">line_number</span>` --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Create a file from `stdin`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | kate --stdin`

- Display help:

`kate --help`
