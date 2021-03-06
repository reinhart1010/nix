---
layout: page
title: common/json5 (English)
description: "A command-line tool for converting JSON5 files to JSON."
content_hash: 49340f6e373620d4e03fe89056a204394beb5400
---
# json5

A command-line tool for converting JSON5 files to JSON.
More information: <https://json5.org>.

- Convert JSON5 stdin to JSON stdout:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input</span>` | json5`

- Convert a JSON5 file to JSON and output to stdout:

`json5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.json5</span>

- Convert a JSON5 file to the specified JSON file:

`json5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.json5</span>` --out-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.json</span>

- Validate a JSON5 file:

`json5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.json5</span>` --validate`

- Specify the number of spaces to indent by (or "t" for tabs):

`json5 --space `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indent_amount</span>

- View available options:

`json5 --help`
