---
layout: page
title: common/json5 (English)
description: "Convert JSON5 files to JSON."
content_hash: 2adebb84c790b919698230223111760f80a71a50
last_modified_at: 2024-02-25
tldri18n_status: 2
---
# json5

Convert JSON5 files to JSON.
More information: <https://json5.org>.

- Convert JSON5 `stdin` to JSON `stdout`:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input</span>` | json5`

- Convert a JSON5 file to JSON and output to `stdout`:

`json5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.json5</span>

- Convert a JSON5 file to the specified JSON file:

`json5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.json5</span>` --out-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.json</span>

- Validate a JSON5 file:

`json5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.json5</span>` --validate`

- Specify the number of spaces to indent by (or "t" for tabs):

`json5 --space `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indent_amount</span>

- Display help:

`json5 --help`
