---
layout: page
title: common/ctags (English)
description: "Generate an index (or tag) file of language objects found in source files for many popular programming languages."
content_hash: 61efdc7478eeea3f8b15f988c1d16480cf4b7d66
last_modified_at: 2024-04-26
tldri18n_status: 2
---
# ctags

Generate an index (or tag) file of language objects found in source files for many popular programming languages.
More information: <https://ctags.io/>.

- Generate tags for a single file, and output them to a file named "tags" in the current directory, overwriting the file if it exists:

`ctags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Generate tags for all files in the current directory, and output them to a specific file, overwriting the file if it exists:

`ctags -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` *`

- Generate tags for all files in the current directory and all subdirectories:

`ctags --recurse`

- Generate tags for a single file, and output them with start line number and end line number in JSON format:

`ctags --fields=+ne --output-format=json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
