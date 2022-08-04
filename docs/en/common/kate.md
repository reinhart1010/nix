---
layout: page
title: common/kate (English)
description: "KDE Text Editor."
content_hash: 4bf9ebffebe88654796f7348fd3eb5b0be3bc6a6
---
# kate

KDE Text Editor.
More information: <https://kate-editor.org/>.

- Launch Kate and open specific files:

`kate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Open a remote document in Kate:

`kate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/path/to/file</span>

- Launch Kate, creating a new instance even if one is already open:

`kate --new`

- Open a file in Kate with the cursor at the specific line:

`kate --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">line_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a file in Kate with the cursor at the specific line and column:

`kate --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">line_number</span>` --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Launch Kate, creating a new temporary file with contents read from stdin:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | kate --stdin`

- Display help:

`kate --help`
