---
layout: page
title: common/keep-header (English)
description: "Keep first line untouched by a command, passing it directly to `stdout`."
content_hash: d025cd42bff29f9777edfdf77fa5b3bf81fc91c4
last_modified_at: 2022-12-04
---
# keep-header

Keep first line untouched by a command, passing it directly to `stdout`.
More information: <https://github.com/eBay/tsv-utils#keep-header>.

- Sort a file and keep the first line at the top:

`keep-header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -- sort`

- Output first line directly to `stdout`, passing the remainder of the file through the specified command:

`keep-header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Read from `stdin`, sorting all except the first line:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | keep-header -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Grep a file, keeping the first line regardless of the search pattern:

`keep-header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -- grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>
